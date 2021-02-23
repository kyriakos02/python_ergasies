# get lottery ids
def get_lottery_ids(date: str):
    url = f'https://api.opap.gr/draws/v3.0/1100/draw-date/{date}/{date}/draw-id'
    data = requests.get(url).json()
    return data

lots = get_lottery_ids('2021-02-01')

# get dates
dates = pd.date_range(start="2021-02-01",end="2021-02-18")
dates = dates.map(lambda t: t.strftime('%Y-%m-%d')).to_list()
dates = pd.DataFrame(dates, columns = ["Date"])

# apply get lottery ids to dates
dates['Lotteries'] = dates['Date'].apply (lambda x: get_lottery_ids(x))



def common_winning_numbs(daylots: list):
    
    # get data for 1 lottery id
    def get_winning_numbers(lotid: str):
        url =f'https://api.opap.gr/draws/v3.0/1100/{lotid}'
        data = requests.get(url).json()
        winning_numbers = data['winningNumbers']['list']
        return winning_numbers
    
    # numbers selected in a day
    lots = list(map(get_winning_numbers, daylots))
    
    # merge the data for each day
    lots = sum(lots,[])
    
    # find the most frequent
    moc = list(max([(lots.count(chr),chr) for chr in set(lots)]))    
    return moc

dates['MostFrequentWinner'] = dates['Lotteries'].apply (lambda x: common_winning_numbs(x))

dates <- dates[['Date', 'MostFrequentWinner']]