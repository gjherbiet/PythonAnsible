#!/usr/bin/env python

import snmp_helper as snmp

devices = [
    ('50.76.53.27', 'galileo', '7961'),
    ('50.76.53.27', 'galileo', '8061')
]

oids = [
    '1.3.6.1.2.1.1.5.0',
    '1.3.6.1.2.1.1.1.0'
]

for device in devices:
    for oid in oids:
        snmp_data = snmp.snmp_get_oid(device, oid=oid, display_errors=True)
        output = snmp.snmp_extract(snmp_data)
        
        print output