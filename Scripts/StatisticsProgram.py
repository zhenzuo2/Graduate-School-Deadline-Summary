from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
with open("/Users/zz4/Documents/GitHub/Graduate-School-Deadline-Summary/Data/Best Statistics Graduate Programs - Top Science Schools - US News Rankings.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    
df = pd.DataFrame(columns = ['Name', 'Program Link', 'Requirement Link'],
        index = [link.string for link in soup.find_all('h3')])

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
 
# to search
for link in soup.find_all('h3'):
    print(link.string)
    query = link.string + " Statistics PhD application deadline"
    for i in search(query, tld="co.in", start = 0, stop = 1):
        print(i)
    query = link.string + " Statistics PhD application GRE"
    for j in search(query, tld="co.in", start = 0, stop = 1):
        print(j)
    df.loc[link.string] = [link.string, i, j]
    print("=================================================================================")

df.to_csv("/Users/zz4/Documents/GitHub/Graduate-School-Deadline-Summary/Results/Satistics PhD/Statistics.csv",index=False)