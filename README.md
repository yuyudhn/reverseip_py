# reverseip_py
Domain parser for IPAddress.com Reverse IP Lookup. Writen in Python 3.

## What is Reverse IP?
Reverse IP refers to the process of looking up all the domain names that are hosted on a particular IP address. This can be useful for a variety of reasons, such as identifying all the websites that are hosted on a shared hosting server or finding out which websites are hosted on the same IP address as a particular website.

## Requirements
- beautifulsoup4
- requests
- urllib3

Tested on **Debian** with **Python 3.10.8**

### Install Requirements
```
pip3 install -r requirements.txt
```
## How to Use
Help Menu
```
python3 reverse-ip.py -h
usage: reverse-ip.py [-h] [-t target.com]

options:
  -h, --help            show this help message and exit
  -t target.com, --target target.com
                        Target domain or IP
```
Reverse IP
```
python3 reverse-ip.py -t google.com
```
## Screenshot
![ReverseIP](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhM4Z6zSF5yjADs6toEeqYSJs71tGp-8H-E4t0udDQ5qUBqHXOa5fFaUGowEvVSpKw5vSeuBPaGwRrDOsl3TxYB2P9MYC-5gWw9ued2E4iFWybbJz_yiargjToQpYMnalQtiQja7kVOmc1nQfsHLc7xB2wh_BHZ1NWOUABHOYGh0wdCkApkoEl7GvfH0A/s742/reverse-ip.png "ReverseIP")

## Disclaimer
Any actions and or activities related to the material contained within this tool is solely your responsibility.The misuse of the information in this tool can result in criminal charges brought against the persons in question.

Note: modifications, changes, or changes to this code can be accepted, however, every public release that uses this code must be approved by author of this tool (yuyudhn).