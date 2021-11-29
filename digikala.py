import requests
from bs4 import BeautifulSoup
import pandas
 
url = 'https://www.digikala.com/search/category-mobile-phone/?pageno='
titles = []
stars = []
prices = []

for pages in range(1, 15):
    page = requests.get(url+str(pages))
    soup = BeautifulSoup(page.text, 'html.parser')
    title = soup.select('div.c-product-box__content--row')
    for t in title:
        name = t.text
        titles.append(name)
    star = soup.select('div.c-product-box__engagement-rating')    
    for s in star:
        point = s.text.strip()
        stars.append(point)
    price = soup.select('div.c-price__value-wrapper')
    for p in price:
        pri = p.text.strip()
        prices.append(pri)

product = {"titles": titles, "stars": stars, "prices": prices}

data = pandas.DataFrame.from_dict(product, orient='index')
data = data.transpose()
writer = pandas.ExcelWriter('productmobile.xlsx')
data.to_excel(writer)
writer.save()
