import xml.etree.ElementTree as ET

#parse xml code from file in same directory
tree = ET.parse('worlddata.xml')

#get the root of the xml tree
root = tree.getroot()

#print the text name of root
print root.tag


#Every element of the tree has tag + dictionary
#of elements

#if the element has children they can be iterated over:
for child in root:
    print(child.tag, child.attrib)

#Do the children have children? no
for block in root:
    for Type in block:
        #using .text prints the text between the headers
        print Type.text
        
        
