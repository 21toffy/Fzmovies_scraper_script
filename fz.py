
import re
import mechanize
from bs4 import BeautifulSoup
import requests



#to initialize the browser
br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]




#to open fzmovies homepage
br.open("https://www.fzmovies.net/")

#initialize form i think
br.select_form(nr=0)

#taking user input
searchname=input('enter movie name: ')

#fillin in the form

br.form['searchname'] = searchname

#submitting form
br.submit()

#print(br.geturl())

# saves page source
orders_html = br.response().read()

#initializing bs4 for scraping
soup = BeautifulSoup(orders_html,'html.parser')


#picking the closest div to the link we want to pick by class name
divs = soup.find_all("div", {"class": "mainbox"})


links = []
#iterating through all available divs produces by the search
for div in divs:
    
    #reavealing the href property inother get link
    rows = div.find_all('a', href=True)
    for row in rows:
        #print(links.append(row['href']))

        #lists = ('https://fzmovies.net/'+row.get("href"))
        #print(lists)
        
        #mylist = list(dict.fromkeys(lists))
        #print(mylist)
        
        links.append(row['href'])
        #print(row.text)
        #print(row['href'])



mylist = list(dict.fromkeys(links))
perf_list = []
for i in mylist:
    if i=='' or 'movietags' in i:
        del i
    else:
        perf_list.append(i)
print(perf_list)

for i in perf_list:
    print('https://fzmovies.net/'+str(i))

    ####################################DETAIL PAGE#######

detail = input('paste the link here to generate a dowload link: ')
detail = detail.replace(" ", "%20")
print(detail)


#r = requests.get(detail)
r = br.open(detail)
orders_html = br.response().read()
soup = BeautifulSoup(orders_html,'html.parser')
divs = soup.find_all("ul", {"class": "moviesfiles"})

li = []

for d in divs:
	ul = d.find_all('a', href=True)
	for u in ul:
		li.append(u['href'])
#this for loop is to remove the medi.php in the link list


for i in li:
    if 'mediainfo.php' in i:
        del i
    else:
        down_page.append(i)
print(down_page)




		



'''
detail_divs = soup.find_all("ul", {"class": "moviesfiles"})

down_page  = []

for ultag in detail_divs:
    a_tag = ultag.find_all('a', href=True)
    for a_tags in a_tag:
        down_page.append(a_tags['href'])
        print(a_tags)
        print(a_tags.text)
print(down_page)
'''





'''

        if len(mylist)>1:
            print('multiple moies were discovered.')
            print('select the link to the intended movie')
            print(mylist)
'''

        
