import urllib.request

import json


API_KEY = '7LECVJHIWTPL9Z32'

def getStockData(symbol):
        baseURL = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol='
        ending = '&apikey=' + API_KEY

        fullURL = baseURL + symbol + ending
        print()
        print('Sending URL:', fullURL)

        connection = urllib.request.urlopen(fullURL)

        responseString = connection.read().decode()


        #print('Response is: ', responseString)
        d = json.loads(responseString)

        dic = {}

        
        for item in d['Global Quote']:
            ditem = item.split('. ')
            dic[ditem[1]]=d['Global Quote'][item]

        print("The current price of ", dic["symbol"], " is: ", dic["price"])
		
		print("Stock Quotes retrieved successfully!")
        

quit = {}
while quit != 'quit':
        stockSymbol = input('Enter a stock symbol: ')
        getStockData(stockSymbol)

        quit = input('To quit type quit or to look up another stock press any key and enter: ')
