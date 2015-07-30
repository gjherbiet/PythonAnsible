#!/usr/bin/env python
'''
The script should find all of the crypto map entries in the file (lines that
begin with 'crypto map CRYPTO') and print out the children of each crypto map.
'''

from ciscoconfparse import CiscoConfParse

def main(cisco_file='cisco_ipsec.txt'):
    '''
    Find all of the crypto map entries in the file (lines that begin with
    'crypto map CRYPTO') and print out the children of each crypto map.
    '''
    
    cisco_cfg = CiscoConfParse(cisco_file)
    
    for crypto_map in cisco_cfg.find_objects(r'^crypto map CRYPTO'):
        print
        print crypto_map.text
        for child in crypto_map.children:
            print child.text
    print

if __name__ == "__main__":
    main()