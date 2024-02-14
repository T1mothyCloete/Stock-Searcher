import requests
from bs4 import BeautifulSoup

URL = 'https://levelupstore.co.za/products/viticulture-essential-edition?variant=43344257417445&currency=ZAR&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic&gclid=CjwKCAjwgZCoBhBnEiwAz35RwrvzMipDM-I63TBeGhuilANUZb6_Zgbjwcm-Wqf5zn9ThXRxgxxbtRoC_HoQAvD_BwE'

headers = {"User_Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')


