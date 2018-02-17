import math as mt
import xml.etree.ElementTree as ET

def loadWorld(path):
    tree = ET.parse(path)
    root = tree.getroot()
    world = root.findall("world")

    models = world[0].findall('model')
    for model in models:
        if model.attrib['name'] == "simpleWorld":
            simpleWorld = model
            break
    links = simpleWorld.findall("link")
    xy=[]
    for link in links:
        pose = link.find('pose')
        xyzRYP =map(float,pose.text.split(' '))
        size = map(float,link.find('visual').findall('geometry')[0].findall('box')[0].findall('size')[0].text.split(' '))
        x0=xyzRYP[0]-size[0]/2*mt.cos(xyzRYP[5])
        y0=xyzRYP[1]-size[0]/2*mt.sin(xyzRYP[5])
        x1=xyzRYP[0]+size[0]/2*mt.cos(xyzRYP[5])
        y1=xyzRYP[1]+size[0]/2*mt.sin(xyzRYP[5])
        xy.append([[x0,x1],[y0,y1]])
    return xy


