#! /usr/bin/env python3
import sys
import urllib3
import argparse
import requests
from requests import RequestException
from bs4 import BeautifulSoup as bs
import sys
import re
import io

urllib3.disable_warnings()
parser = argparse.ArgumentParser()
parser.add_argument('-t', '--target', metavar='target.com', type=str, help='Target domain or IP')
args = parser.parse_args()
ip_target = args.target
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Safari/537.36"

#Target validator
def argscheck():
    if len(sys.argv)==1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    elif ip_target == None:
        parser.print_help(sys.stderr)
        print()
        print(f"Error: Target is mandatory")
        sys.exit(1)
    elif "://" in ip_target:       
        print(f"Input only IP or domain. Example: target.com")
        sys.exit(1)    
def re_addr():
    headers = {
        'Origin': 'https://www.ipaddress.com',
        'User-Agent': ua,
        'Content-Type': 'application/x-www-form-urlencoded'
            }
    payload = {"host" : ip_target}
    ipaddr_host = "https://www.ipaddress.com/reverse-ip-lookup"
    fn = ip_target+".txt"
    try:
        r = requests.post(ipaddr_host, data=payload, headers=headers)
        rd = r.text
        soup = bs(rd, 'html.parser')
        hx = soup.find(string = re.compile("We found no hostnames for"))
        hr = soup.find(string = re.compile("Hostname could not be resolved to an IP address"))  
        hf = soup.find(string = re.compile(r"We found\ (\d+) hostnames for"))
        _mip = soup.find(string = re.compile("resolves to more than one IP address. Please select one from the list below."))
        if _mip:
            try:
                for _aip in soup.find_all("input", {"name": "host"}):
                    _ipv4 = _aip.get('value')
                    if _ipv4:
                        _mtarget = _ipv4
                        payload = {"host" : _mtarget}
                        print(f"Retrieving domain from {_mtarget}")
                        r = requests.post(ipaddr_host, data=payload, headers=headers)
                        rd = r.text
                        soup = bs(rd, 'html.parser')
                        for h in soup.findAll('ol'):
                            dcount = 0
                            par = h.find_all('a', attrs={'href': re.compile("https://www.ipaddress.com/site/")})
                            for link in par:
                                dcount += 1            
                                dl = link.text
                                with io.open(fn, "a") as f:
                                    f.write(dl + '\n')
                                    f.close()
                            print(f"Found {dcount} domain for {_mtarget}")
                    else:
                        pass
            except:
                print("Error!")
            finally:
                print(f"Result saved at {fn}")
        elif hx:
            print(f"Found 0 domain for {ip_target}")
        elif hr:
            print(f"Domain or IP not Resolved")
        elif hf:
            for h in soup.findAll('ol'):
                dcount = 0
                par = h.find_all('a', attrs={'href': re.compile("https://www.ipaddress.com/site/")})
                for link in par:
                    dcount += 1            
                    dl = link.text
                    with io.open(fn, "a") as f:
                        f.write(dl + '\n')
                        f.close()
                print(f"Found {dcount} domain for {ip_target}")
                print(f"Result saved at {fn}")
        else:
            print(f"Error!")
    except RequestException as err:
        print(f"{type(err).__name__} was raised: {err}")
if __name__ == '__main__':
    try:
        argscheck()
        re_addr()
    except Exception as err:
        print(f"{type(err).__name__} was raised: {err}")
