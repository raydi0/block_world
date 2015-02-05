#!/usr/bin/env python

import xml.etree.ElementTree as ET


# open xml

    tree = ET.parse('worlddata.xml')
    root = tree.getroot()
    Blocklist = []

    for block in root.findall('BLOCK'):
        x = int(block.get('X'))
        y = int(block.get('Y'))
        z = int(block.get('Z'))
        typE = block.find('TYPE')
        _blocklist = [y,x,z,typE]
        Blocklist.append(_blocklist)
    return Blocklist
