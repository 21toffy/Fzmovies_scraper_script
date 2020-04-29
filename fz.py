import re
import mechanize

#to initialize the browser
br = mechanize.Browser()

#to open fzmovies homepage
br.open("http://www.fzmovies.net/")

#to select the search form
br.select_form("searchname")

form[name] = value


#fillin in the form

br.form['boption'] = 'CLoad'
br.form['hitsPerPage'] = [ '50' ]
    

# Select the form

#br.select_form(nr=0)



# Login
br.submit()
