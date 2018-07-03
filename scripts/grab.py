import re
import requests

midlist1 = requests.get('http://www.primeshop.com/MIDILibrary/midlist2.htm').content.decode()
midlist2 = requests.get('http://www.primeshop.com/MIDILibrary/midlist3.htm').content.decode()

midis = re.findall(r'\"ragsmid/(.+?)\.mid\"', midlist1) + re.findall(r'\"ragsmid/(.+?)\.mid\"', midlist2)

baseurl = 'http://www.primeshop.com/MIDILibrary/'

for midi in midis:
    current = requests.get(baseurl + 'ragsmid/' + midi + '.mid').content
    with open(midi + '.mid', 'wb') as f:
        f.write(current)
