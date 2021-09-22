from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request, urllib.error, urllib.parse
import re

url = input('Enter url: ')
if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_42.html' #put your URl for a easier checking
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

#extract all numbers
counts = list()
count = 0
span = soup('span')
#print(span)
for num in span:
    nu = num.decode().rstrip().split()
    #print(nu)
    for k in nu:
        x = re.findall('[0-9]+', k) #look for numbers in the list created by line 17
        if len(x) == 0:
            continue
        #print(x)
        for y in x: #convert str to int
            t = int(y)
            #print(t)
            counts.append(t) #append the integers to the counts list
#print(counts)
Sum = 0
for key in counts: #for every key in the list do the following
    Sum = sum(counts)
    count = count + 1

print('Count: ', count)
print('Sum: ', Sum)
