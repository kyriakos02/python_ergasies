# 6103 available cryptocurrencies 
# import cryptocompare
# cryptocompare.get_coin_list(format =True)


# Create a dictionary containing a user's cryptocurrencies

# get the correspondind prices in EUR

def get_crypto_prices(cryptos: dict):
    
    # input cryptos to search for
    inputcr = ','.join(list(cryptos.keys()))
    url =f'https://min-api.cryptocompare.com/data/pricemulti?fsyms={inputcr}&tsyms=EUR'
    data = requests.get(url).json()
    for cr in data: data[cr] = data[cr]['EUR']
    result = {k: data[k]*cryptos[k] for k in data}
    return result

# for example's shake we 'll use Bitcoin (BTC), Etherium (ETH) and AMO 

testcryptos = {
    'BTC': 54,
    'ETH': 4,
    'AMO': 0.2
    }

get_crypto_prices(testcryptos)