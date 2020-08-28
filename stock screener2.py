#API Key 1: 1354e1035b2d404c8ded01d402571d6a
#API Key 2:61a5842fb2f64893ba1ec203b005d3b2
#API Key 3: 644ccd59e83f4d23970afc6715f3d37a
from twelvedata import TDClient
import csv
import time

MAX_INTREVAL = 2
data = []
with open('companylists.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        data.append(row)
row = [x[0] for x in data]

gs = []
grs = []
# access utils
def p(data, index, intreval):
    return pull_from_frame(data, index, intreval)


def pull_from_frame(data, index, intreval):
    pulled = data.filter(regex=index).values.tolist()[intreval - 1][0]
    return pulled


# data client
for i in range(1,136):
    ticker = i

    
    Stock = (row[ticker])
    td = TDClient(apikey="644ccd59e83f4d23970afc6715f3d37a")

    ts = td.time_series(
        symbol=Stock,
        interval="1day",
        outputsize=MAX_INTREVAL,
        timezone="America/New_York",
    # start_date=
    # end_date="YYYY-MM-DD"
)

# Tech Indcators
    bands = ts.with_bbands(time_period=800).as_pandas()
    slows = ts.with_stoch().without_ohlc().as_pandas()
    mas = ts.with_sma(time_period=800).without_ohlc().as_pandas()
# pull from frame
    open = p(bands, 'open', 1)
    open2 = p(bands, 'open', MAX_INTREVAL)

    high = p(bands, 'high', 1)
    high2 = p(bands, 'high', MAX_INTREVAL)

    low = p(bands, 'low', 1)
    low2 = p(bands, 'low', MAX_INTREVAL)

    close = p(bands, 'close', 1)
    close2 = p(bands, 'close', MAX_INTREVAL)

    volume = p(bands, 'volume', 1)
    volume2 = p(bands, 'volume', MAX_INTREVAL)

    slow_k = p(slows, 'slow_k', 1)
    slow_k2 = p(slows, 'slow_k', MAX_INTREVAL)

    slow_d = p(slows, 'slow_d', 1)
    slow_d2 = p(slows, 'slow_d', MAX_INTREVAL)

    low_band = p(bands, 'lower_band', 1)
    low_band2 = p(bands, 'lower_band', MAX_INTREVAL)

    med_band = p(bands, 'middle_band', 1)
    med_band2 = p(bands, 'middle_band', MAX_INTREVAL)

    high_band = p(bands, 'upper_band', 1)
    high_band2 = p(bands, 'upper_band', MAX_INTREVAL)

    sma = p(mas, 'sma', 1)
    sma2 = p(mas, 'sma', MAX_INTREVAL)

    score = 0
# buy condition
    if slow_d and slow_k < 20:
        score = score + 3

    if slow_d and slow_k < 40:
        score = score + 3

    if slow_k > slow_d and (slow_k + slow_d) < 100:
        score = score + 7

    if (close2 / close * 100 - 100) < -5:
        score = score + 5

    if (close2 / close * 100 - 100) < -10:
        score = score + 2

    if (sma / close * 100 - 100) < -3:
        score = score + 3

    if (volume2 / volume * 100 - 100) < 5:
        score = score + 5

    if (sma / close * 100 - 100) < -7:
        score = score + 2

    if (close / low_band * 100 - 100) < 15:
        score = score - 5
    

    


    print("")
    print("")
    print("Stock's score is", score,"/ 35")
    print("")
   

    if score > 24 and score < 30: 
        f = (Stock)
        gs.append(f)
        print(f'Good Stock Tickers are {gs}')
    
    if score > 29: 
        f = (Stock)
        grs.append(f)
        print(f'great Stock Tickers are {grs}')

    
    #if i == 2:
        #break
    print(i)
    time.sleep(20)
print("")
print("")
print(f'The Good Stock Tickers Are {gs}')
print(f'The Great Stock Tickers Are {grs}')

    

