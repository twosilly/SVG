import xml.etree.ElementTree as ET
import re

number_re = r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?'
unit_re = r'em|ex|px|in|cm|mm|pt|pc|%'

# 获取 XML 文档对象 ElementTree
#tree = ET.parse('example.xml')
tree = ET.parse('../examples/cc-by-sa.svg')
# 获取 XML 文档对象的根结点 Element
root = tree.getroot()
print("多少个子项：",root.items())
print("width:",root.get("width"))
print("height:",root.get("height"))
viewBox = re.findall(number_re, root.get('viewBox'))
print("viewBox:",viewBox)
print("tag:",root.tag)
# 递归查找所有的 neighbor 子结点
for neighbor in root.iter('{http://www.w3.org/2000/svg}svg'):
    print ("svg:",neighbor.attrib)

for neighbor in root.iter('{http://www.w3.org/2000/svg}style'):
    print ("style:",neighbor.attrib)

for neighbor in root.iter('{http://www.w3.org/2000/svg}g'):
    print ("g:",neighbor.attrib)

for neighbor in root.iter('{http://www.w3.org/2000/svg}path'):
    print ("path:",neighbor.attrib)

# 打印根结点的名称
#print (root.tag)
print("end")