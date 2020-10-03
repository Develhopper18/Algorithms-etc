import requests
from bs4 import BeautifulSoup
import html5lib


# I don't know
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}


def RealmeC12():
    # The product url
    url_r_c12 = "https://www.amazon.in/Realme-C12-Power-Blue-RAM/dp/B08GKHY681/ref=sr_1_2?dchild=1&keywords=realme+mobile&qid=1601036494&s=electronics&sr=1-2"

    # The page
    page1 = requests.get(url_r_c12, headers=headers)

    # The Soup 🍵
    soup = BeautifulSoup(page1.content, "html.parser")
    # print(soup.prettify())

    # Title
    title = soup.find(id="productTitle").get_text()

    # Price
    price = soup.find(id="olp-upd-new").get_text()

    # Shows the name of the product
    print(title.strip())
    print(price.strip())

RealmeC12()


def Redmi9Prime():
    # The product url
    url_mi_Pr = "https://www.amazon.in/Redmi-Prime-Storage-Display-Camera/dp/B08696XM8J/ref=sr_1_1?dchild=1&keywords=mobile+undar+10000&qid=1601037413&refinements=p_36%3A1318505031%2Cp_n_operating_system_browse-bin%3A1485077031%2Cp_n_feature_eight_browse-bin%3A8561116031&rnid=8561111031&s=electronics&sr=1-1"

    # The page
    page2 = requests.get(url_mi_Pr, headers=headers)

    # The Soup 🍵
    soup2 = BeautifulSoup(page2.content, "html.parser")
    # print(soup.prettify())

    # Title
    title2 = soup2.find(id="productTitle").get_text()

    # Price
    price = soup2.find(id="priceblock_ourprice").get_text()

    # Shows the name of the product
    print(title2.strip())
    print(price.strip())

# Redmi9Prime()