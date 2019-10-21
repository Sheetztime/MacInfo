import sys
import subprocess
import os
from subprocess import check_output
import re

def is_valid_mac(macaddress):
    """Returns True if MAC address is acceptable format.
       Example formats below :
        - ff:ff:ff:ff:ff:ff
        - ff-ff-ff-ff-ff-ff
        - ffffffffffff
    """
    pattern = r'([a-f0-9]{2}[:|\-]{0,1}){5}[a-f0-9]{2}'
    if re.match(pattern, macaddress, re.IGNORECASE):
        return True
    else:
        print ("invalid MAC address format, please enter a Valid MAC in format ff:ff:ff:ff:ff:ff ,ff-ff-ff-ff-ff-ff,ffffffffffff")
        return False

def get_comp_info(inputMacAddrs,apikey):

    URL="https://api.macaddress.io/v1?apiKey="+apikey+"&output=json&search="+inputMacAddrs
    out = check_output(["curl","--silent",URL])
    data = out.decode().split('",') #split API output into a list
    print ("Company details for the MAC address" + inputMacAddrs)
    #This block parses the returned info to only print Company Name and Address
    for temp in data:
        if "company" in temp:
          Subdata = temp.split(',')
          for Cname in Subdata:
            if not "Private" in Cname:
              print (Cname)

def main():
    usage = """
    macinfo - Retrieves Company information for a given mac address from api.macaddress.io
    Required Params:
        - MAC address to get company details for
        - API keyt, generated from
    Example usage :
    """
#parsing command line argument
if len(sys.argv)!=3:
  print ("pass a MAC address  and API key as as  input to this script Example : /usr/local/bin/python3 Mactest.py <MAC ADDR> <API KEY")
  exit
else:
  inputMacAddrs = str(sys.argv[1])
  apikey=str(sys.argv[2])
  if is_valid_mac(inputMacAddrs):
      get_comp_info(inputMacAddrs,apikey)
