import requests
from bs4 import BeautifulSoup
import textwrap

url = requests.get('https://www.flipkart.com/').text
soup = BeautifulSoup(url,'html')

def get_a():
  find_a = soup.find_all('a')
  try:
    if type(soup.find('a')) == type(None):
      pass
    else:
      a_list = []
      for a in find_a:
        a = str(a.get_text())
        a = textwrap.fill(a, width=80)
        a_list.append(a)
        # remove all empty lists from a_list
        a_list = list(filter(None, a_list))
        # new list to append text densities
        density= []
      for element in a_list:
        #treat each element as a block, # of words / # of lines 
        density.append(len(element.split()))
      return density
  except:
    print('Error retrieving h2 tag')
    
get_a()
threshold=0.3

block = get_a()

print('Threshold is', threshold)
print('Densities of our simulated block:',block)
slope_test = [round(abs(block[i] - block[i+1]) / max(block[i],block[i+1]),2) for i in range(0,len(block)-1)]

slope = lambda x,y : abs(y-x) / max(y,x)

print('Slope deltas:', slope_test)

result, previous = [[]], None
for current in block:
    if previous is None or slope(previous,current) <= threshold:
        result[-1].append(current)
    else:
        result.append([current])
    previous = current
    
    
print('Final result after implementing Block Fusion algorithm:', result)
