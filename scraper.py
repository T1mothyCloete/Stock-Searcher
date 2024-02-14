def getData(symbol):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}
        url = f'https://finance.yahoo.com/quote/{symbol}'
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        stock = {
            'symbol': symbol,
            'price' : soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[0].text,
            'change' : soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[1].text
    }
    except:
        return("Invalid Symbol")
    else:
        return stock

#print("Enter stock symbol")
symbol = input("Enter stock symbol: ")
print(getData(symbol))



