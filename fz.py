


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

details = []
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
        
    for tes in divs:
        
        details.append(tes.find_all(text=True))


        
#This eliminates all double links in the list
mylist = list(dict.fromkeys(links))
perf_list = []

#this deletes the empty strings and any movie tag link in the list of links and appends the remaining to a new list
for i in mylist:
    if i=='' or 'movietags' in i:
        del i
    else:
        perf_list.append(i)
        
print('opps multiple recults came back for your Query...')

print('\n')

print('you would need to pick a movie from the list in other to generate your download link')

print('\n')

for link,ident in zip(perf_list, details):
	print('LINK:::  https://fzmovies.net/{}  :::     TITLE:{}    YEAR:{}    QUALITY:{}'.format(link, ident[1], ident[3], ident[5]))
	print('\n')







####################################DETAIL PAGE#######

detail = input('copy and paste the link here to generate a dowload link::: ')

print('\n')

#this eliminates all the white spaces and replace then with 20% in accordance to fzmovies url pattern
detail = detail.replace(" ", "%20")

print('if you did not coppy this link well this code will break')

print('\n')

print(detail)

print('\n')

#r = requests.get(detail)

#for opening detail page
r = br.open(detail)

#to read and save the page
orders_html = br.response().read()

soup = BeautifulSoup(orders_html,'html.parser')

#filltering ul 
divs = soup.find_all("ul", {"class": "moviesfiles"})

#initializing an empty array
li = []

#  this for loop is for filltering all a tags in the ul tag fillltered before and appending the results to a new array
for d in divs:
	ul = d.find_all('a', href=True)
	for u in ul:
		li.append(u['href'])
		

#initializing a new array
down_page = []


#this for loop is to remove the media.php in the link array and form the download page link
for i in li:
    if 'mediainfo.php' in i:
        del i
    else:
        down_page.append('fzmovies.net/'+str(i))
        

#raw url for download page1
down_conf = down_page[0]
#action to open url for downoad page 1, with http appended to it
r = br.open('https://'+down_conf)



orders_html = br.response().read()

soup = BeautifulSoup(orders_html,'html.parser')

divs = soup.find_all("a", {"id": "downloadlink"})

nexts = []
for d in divs:
        nexts.append(d['href'])
	#ul = d.find_all('a', href=True)
	#ulstr = str(ul[0])
	#loc_index = ulstr.index('window.open', )
	#quo_sem_index = ulstr.index('";', )
	#new_with_loc = ulstr[loc_index:quo_sem_index]
	#new_witout_loc = new_with_loc[16:]
	#click_page = ('fzmovies.net/'+str(new_witout_loc))
	#print(click_page)
        maybe = d['href']
        down_page_2 = 'https://fzmovies.net/'+maybe

        
######Entering the last Download page#####

#opening the page
r = br.open(down_page_2)

#reading the page
orders_html = br.response().read()


soup = BeautifulSoup(orders_html,'html.parser')

down_link = soup.find_all("input", {"name": "download1"})

print('your download links are now ready . . .')
label = ['link 1', 'link 2', 'link 3', 'link 4', 'link 5']

for i in down_link:
        print (i['value'])
        print('\n')


'''







#download page 1 inspect
#https://fzmovies.net/download.php?downloadkey=3-17091-babee4acc6c327d44637b00a4b0a852e

#download page1 real link
#https://fzmovies.net/download.php?downloadkey=3-17091-babee4acc6c327d44637b00a4b0a852e
'''

'''
#generatel inspect link
https://fzmovies.net/downloadkey=3-17090-798cb74fcaa4462f9f3f234605c028b0&amp;pt=jRGarGzOo2


#reallink
https://fzmovies.net/download.php?downloadkey=3-17090-cf6e87130cb511b55186aa3c72b12ec2&pt=jRGarGzOo2
	
	
	
#download page 1 url
https://fzmovies.net/download1.php?downloadoptionskey=3-9166-8c71ce8438c69788c1cbeaddf485363a&pt=jRGarGzOo2
'''












		



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

        
