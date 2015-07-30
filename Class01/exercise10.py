#!/usr/bin/env python
'''
The script should find all of the crypto map entries in the file 
that are not using AES (based-on the transform set name).
Print these entries and their corresponding transform set name.
'''

import re
from ciscoconfparse import CiscoConfParse

def main(cisco_file='cisco_ipsec.txt'):
    '''
    Using ciscoconfparse find the crypto maps that are not using AES (based-on
    the transform set name). Print these entries and their corresponding
    transform set name.
    '''
    
    cisco_cfg = CiscoConfParse(cisco_file)
    
    for crypto_map in cisco_cfg.find_objects_wo_child(parentspec=r'crypto map CRYPTO',
                                                      childspec=r'AES'):
        for child in crypto_map.children:
            if 'transform' in child.text:
                 match = re.search(r"set transform-set (.*)$", child.text)
                 print "{0} : {1}".format(crypto_map.text.strip(), match.group(1))


if __name__ == "__main__":
    main()