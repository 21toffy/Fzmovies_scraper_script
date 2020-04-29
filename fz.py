
import re
import mechanize
from bs4 import BeautifulSoup


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

#iterating through all available divs produces by the search
for div in divs:
    row = ''
    #reavealing the href property inother get link
    rows = div.find_all('a', href=True)
    links = []
    for row in rows:
        links.append(row['href'])
        #print(row.text)
        print(row['href'])




'''
br.open("https://www.facebook.com/")

br.select_form(nr=0)

#taking user input
email=input('enter email: ')
password=input('enter email: ')


br.form['email'] = email
br.form['pass'] = password

br.submit()
print(br.title())
if br.title() != 'Facebook':
    print("error")
else:
    print("successfull")


'''
