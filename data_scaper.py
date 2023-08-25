from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page = requests.get(url)

soup = BeautifulSoup(page.text,"html.parser")

star_table = soup.find("table")
temp_list=[]
table_row=star_table.find_all("tr")
for tr in table_row:
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td] 
    temp_list.append(row)
star_name=[]
distance=[]
mass=[]
radius=[]
for i in range(1,len(temp_list)):
    star_name.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])

df2 = pd.DataFrame(list(zip(star_name,distance,mass,radius)),columns=['Star_name','Distance','Mass','Radius']) 
print(df2) 
df2.to_csv('bright_stars.csv')


