#!/usr/bin/env python

# writes xml data to writer_out.xml

import xml.etree.ElementTree as ET

class builder(object):
    

#    def xmlReader(self):
#        tree = ET.parse('practice.xml')
#        root = tree.getroot()
        

        #o = n - 10
        #for _ in xrange(120):
        #    a = random.randint(-o, o)  # x position of the hill
        #    b = random.randint(-o, o)  # z position of the hill
        #    c = -1  # base of the hill
        #    h = random.randint(1, 6)  # height of the hill
        #    s = random.randint(4, 8)  # 2 * s is the side length of the hill
        #    d = 1  # how quickly to taper off the hills
        #    t = random.choice([GRASS, SAND, BRICK])
        #    for y in xrange(c, c + h):
        #        for x in xrange(a - s, a + s + 1):
        #            for z in xrange(b - s, b + s + 1):
        #                if (x - a) ** 2 + (z - b) ** 2 > (s + 1) ** 2:
        #                    continue
        #                if (x - 0) ** 2 + (z - 0) ** 2 < 5 ** 2:
        #                    continue
        #                self.add_block((x, y, z), t, immediate=False)
        #        s -= d  # decrement side length so hills taper off


'''
.XML TEMPLATE

<?xml version="1.0" encoding="ISO-8859-1"?>

<BLOCKWORLD>
    <BLOCK X="15" Y="25" Z="72">
        <COLOR>red</COLOR>
        <TREASURE>100.0</TREASURE>
    </BLOCK>
    <BLOCK X="6" Y="60" Z="16">
        <COLOR>green</COLOR>
        <TREASURE>0.0</TREASURE>
    </BLOCK>
    <BLOCK X="-2" Y="0" Z="12">
        <COLOR>blue</COLOR>
        <TREASURE>1000000.0</TREASURE>
    </BLOCK>
</BLOCKWORLD>
'''