#from flask            import Flask, jsonify, request
#from flask_restful   import Resource, Api
#from importlib       import import_module
#from importlib.util  import find_spec, LazyLoader, module_from_spec, spec_from_file_location
#from inspect         import getmembers, getmodulename, isclass
#from sys             import modules, path
#from tempfile        import NamedTemporaryFile
from ratelimit        import limits, sleep_and_retry
from requests         import post, put
from teamhack_db.sql  import insert
from teamhack_db.util import get_name, get_record_type
from            .sql  import *
#from             sql  import *
from            .util import diff
#from            util import diff

def import_db(text):
  import_db = 'http://import_db.innovanon.com:65432/upload'
  response  = put(import_db, data=text, timeout=300)
  print(f'reponse: {response.text}, code: {response.status_code}')
  return response.text, response.status_code

def troller(queue, endpoint):
  print(f'troller(endpoint={endpoint})')
  response  = put(endpoint,     data='\n'.join(queue), timeout=1800)
  print(f'reponse: {response.text}, code: {response.status_code}')
  if response.status_code != 200: return response.text, response.status_code
  assert response.text
  return import_db(response.text)

""" masscan -h - -p1-65535 --rate=10000 -oX scan_results.xml """
def masscan (queue): return troller(queue, 'http://masscan.innovanon.com:55433/upload')

def nmap    (queue): return troller(queue, 'http://nmap.innovanon.com:55432/upload')

def portscan(queue): return nmap   (queue), masscan(queue)

""" nikto -h - -o nikto_scan.xml -Format xml """
def nikto   (queue): return troller(queue, 'http://nikto.innovanon.com:55434/upload')

""" wapiti -u - -f xml -o wapiti_scan.xml """
def wapiti  (queue): return troller(queue, 'http://wapiti.innovanon.com:55435/upload')

def webscan (queue): return nikto  (queue), wapiti (queue)

def wpscan  (queue): return troller(queue, 'http://wpscan.innovanon.com:55436/upload')

# TODO sqlmap
# TODO dirb, gobuster, feroxbuster
# TODO ssrfmap

def subdomains(queue):
  #print(f'subdomains({queue})')
  pass
def vhosts(queue):
  #print(f'vhosts({queue})')
  pass
def subdirectories(queue):
  #print(f'subdirectories({queue})')
  pass
def credentials(queue):
  #print(f'credentials({queue})')
  pass
def flags(queue):
  #print(f'flags({queue})')
  pass

@sleep_and_retry
@limits(calls=3, period=300)
def loop(dns=None, msf=None, sdn=None, *args, **kwargs):
  inbound  = select_dns(dns)
  print(f'inbound: {inbound}')
  inbound  = [k[0] for k in inbound]
  print(f'inbound: {inbound}')

  psq      =     portscan_queue(inbound, msf) # msfcli   db_nmap psq
  print(f'psq: {psq}')
  text, code = portscan(psq)
  print(f'text: {text}')
  if code != 200: raise Exception(f'text: {text}, code: {code}')

  wsq      =      webscan_queue()
  print(f'wsq: {wsq}')
  text, code =  webscan(wsq)
  print(f'text: {text}')
  if code != 200: raise Exception(f'text: {text}, code: {code}')

  # TODO
  #wpq      =    wordpress_queue()
  #print(f'wpq: {wpq}')
  #text, code =   wpscan(wpq)
  #print(f'text: {text}')
  #if code != 200: raise Exception(f'text: {text}, code: {code}')

  #svq      =      service_queue(inbound, sdn) # TODO should be populated by db_nmap ?

  sdq      =    subdomain_queue(inbound, sdn) # gobuster dns     sdq
  print(f'sdq: {sdq}')
  #sdq      =    subdomain_queue(psq, sdn) # gobuster dns     sdq
  subdomains(sdq) # sequential process

  vhq      =        vhost_queue(inbound, sdn) # gobuster vhost   shq
  print(f'vhq: {vhq}')
  #vhq      =        vhost_queue(sdq, sdn) # gobuster vhost   shq
  vhosts(vhq) # sequential process

  fpq      = subdirectory_queue(inbound, sdn) # gobuster dir     fpq
  print(f'fpq: {fpq}')
  #fpq      = subdirectory_queue(vhq, sdn) # gobuster dir     fpq
  subdirectories(fpq) # sequential process

  crq      =   credential_queue(inbound, sdn) # hydra
  print(f'crq: {crq}')
  credentials(crq) # sequential process

  fgq      =         flag_queue(inbound, sdn) # ssh linpeas, pspy
  print(f'fgq: {fgq}')
  flags(fgq)

  # TODO
  # - access
  # - services found
  #   - scrape web for CVE re: service versions
  #   - 80, 443
  #     - radamsa
  #     - Sublist3r
  #     - subfinder
  #     - ffuf
  #     - wfuzz
  #     - begin vhost        scan
  #     - begin subdirectory scan
  #     - recursively download website
  #       - static analysis
  #       - bulk_extractor => generate wordlists
  #       - cewl
  #       - cupp
  #     - wpsscan
  #     - sqlmap
  #   - hydra/ncrack/medusa
  # - foothold
  #   - persistence
  #   - netstat? => nested dockerized chisel
  #   - sucrack
  #   - linpeas
  #   - pspy
  # - lateral movement
  # - priv esc
  # - hail mary
  #   - db_autopwn
  #   - router scan
  pass
  # TODO check whether targets have successfully been scanned
  # at least once
  # TODO if so, print this helpful message
  print('Bonsoir, Elliot.')
  # TODO check whether any progress has been made
  #      (ie progression thru access, foothold, lateral, priv-esc)
  print('IMMA FIRIN MA LAZORS!')
  # TODO check whether any pwnage has occured
  print('I am INVINCIBLE!')
  # TODO rebrand machine, including
  # /etc/issue.net and /etc/motd

def start_server(host="0.0.0.0", port=6000, dns=None, msf=None, sdn=None, *args, **kwargs):
  #psd = portscan_daemon()
  #while(True): loop(dns, msf, sdn, psd, **kwargs)
  while(True): loop(dns, msf, sdn, **kwargs)
  #app = create_app(dns=dns, msf=msf, **kwargs)
  #app.run(debug=True, host=host, port=port, *args)

