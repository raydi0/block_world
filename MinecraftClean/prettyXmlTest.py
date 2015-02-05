

import xml.dom.minidom

xml = xml.dom.minidom.parse("outputtree.xml") # or xml.dom.minidom.parseString(xml_string)
pretty_xml_as_string = xml.toprettyxml()
prettyFile = open("outputtree.xml", "w")
prettyFile.write(pretty_xml_as_string)
prettyFile.close()

