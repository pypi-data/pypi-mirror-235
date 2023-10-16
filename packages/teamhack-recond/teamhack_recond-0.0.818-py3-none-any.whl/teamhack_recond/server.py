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

# TODO wpscan cannot be directly db_import'd
def wpscan  (queue): return troller(queue, 'http://wpscan.innovanon.com:55436/upload')

def subdomainscan(queue):
  #print(f'subdomains({queue})')
  pass
def vhostscan(queue):
  #print(f'vhosts({queue})')
  pass
def subdirectoryscan(queue):
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
  # TODO how to determine which subdomains have already been iterated ?
  sdq      =    subdomain_queue(inbound, sdn)
  #sdq      =    subdomain_queue(psq, sdn)
  print(f'sdq: {sdq}')
  subdomainscan(sdq)

  inbound  = select_dns(dns)
  print(f'inbound: {inbound}')
  inbound  = [k[0] for k in inbound]
  print(f'inbound: {inbound}')

  psq      =     portscan_queue(inbound, msf)
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

  vhq      =        vhost_queue(inbound, sdn)
  #vhq      =        vhost_queue(sdq, sdn)
  print(f'vhq: {vhq}')
  vhostscan(vhq)

  fpq      = subdirectory_queue(inbound, sdn)
  #fpq      = subdirectory_queue(vhq, sdn)
  print(f'fpq: {fpq}')
  subdirectoryscan(fpq)

  crq      =   credential_queue(inbound, sdn)
  print(f'crq: {crq}')
  credentials(crq)

  fgq      =         flag_queue(inbound, sdn)
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
  #     - ssrfmap
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

