# step 0 : install all the requirements
# pip install requests
# pip install bs4
# pip install html5lib
import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"

# step 1: Get the html
r = requests.get(url)
htmlContent = r.content
#print(htmlContent)

# Step 2: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
#print(soup.prettify)


#Step 3 HTML tree traversal

# Commonly used types of objects:
# 1. print(type(title)) Tags
# 2. print(type(title.string)) NavigableString
# 3. print(type(soup)) BeautifulSoup
# 4. Comment

#markup = "<p><!-- this is a comment --></p>"
#soup2 =  BeautifulSoup(markup)
#print((soup2.p.string))


# Get the title of the HTML page
title = soup.title

# Get all the paragraphs from page
paras = soup.find_all('p')
#print('paras')


#Get first element in the HTML page
print(soup.find('p'))

#Get classes of any element in the HTML page
#print(soup.find('p')['class'])

# Find all the elements with class lead
print(soup.find_all('p', class_="lead"))

# Get the text from the tags/soup
#print(soup.find('p').get_text())
#print(soup.get_text())

# Get all the Anchor tags from page
anchors = soup.find_all('a')
#print(anchors)

# Get all the link from the page
all_links = set()
#for link in anchors:
    #if(link.get('href') != '#'):
        #linkText = "https://codewithharry.com" +link.get('href')
        #all_links.add(link)
        #print(linkText)

#Get all the images tag from page
headings = soup.find_all('img')

#Get images from the paged
all_images = set()
for html_headings in headings:
    html_headings_view = "http://codewithharry.com" +html_headings.get('src')
    all_images.add(html_headings_view)
    print(all_images)


