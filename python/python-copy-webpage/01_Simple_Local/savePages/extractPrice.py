from bs4 import BeautifulSoup

soup = BeautifulSoup(open("rawData/OhioBarECoat_20210219_015744.html"), "html.parser")
price = soup.find(class_='price-box').find(class_='price').string
print(price)
