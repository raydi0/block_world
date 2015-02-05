import xml.etree.ElementTree as ET

def recordBlock(locationDict, Type):
    '''record to an xml object
    a new block
    
    '''
    #add a child to the current element
    #with a tag of location dict
    newElement = ET.Element("BLOCK", locationDict)
    
    #make an element with the tag "type"
    childType = ET.Element("TYPE")
    
    #set the text of the elemnt to the input type
    childType.text = Type
    
    #make the element the child of the root
    newElement.append(childType)
    
    #make an newElement a child of root
    root.append(newElement)

def eraseBlock(locationDict):
    '''find the a block in a global xml object and delete it'''
    for child in root:
        if child.attrib == {'Y': '00', 'X': '00', 'Z': '73'}:
            root.remove(child)


#parse xml code from file in same directory
tree = ET.parse('worlddata.xml')

root = tree.getroot()

#set the tag of an element
root.tag = "BlockWorld"

print root.tag

#add a child to the current element
newElement = ET.Element("BLOCK", {'Y': '00', 'X': '00', 'Z': '73'})

testdict = {'Y': '00', 'X': '00', 'Z': '73'}
print testdict


#make an element with the tag "type"
childType = ET.Element("TYPE")

#set the text of the elemnt to "grass"
childType.text = "GRASS"

#make the element the child of the root
newElement.append(childType)



#make an newElement a child of root
root.append(newElement)

tree.write('outputtree.xml')

for child in root:
    if child.attrib == {'Y': '00', 'X': '00', 'Z': '73'}:
        root.remove(child)
        
for child in root:
    print(child.tag, child.attrib)
    