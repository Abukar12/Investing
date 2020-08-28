API_Key_1: '1354e1035b2d404c8ded01d402571d6a'
API_Key_2: '61a5842fb2f64893ba1ec203b005d3b2'
API_Key_3: '644ccd59e83f4d23970afc6715f3d37a'
API_Key_4: '7526755fae07412cb6b20b27acb4321c' 
API_Key_5: 'c9d9047973304487b936445bad3e63d9'
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

td = TDClient(apikey="1354e1035b2d404c8ded01d402571d6a")

# data client 1100
for ticker in row:
    
    ts = td.time_series(
        symbol=ticker,
        interval="1day",
        outputsize=MAX_INTREVAL,
        timezone="America/New_York",
    # start_date=
    # end_date="YYYY-MM-DD"
)

if ticker == 800:
    API = API_Key_2
if ticker == 1600:
    API = API_Key_3
if ticker == 2400:
    API = API_Key_4
if ticker == 3200:
    API = API_Key_5

# Tech Indcators
    bands = ts.with_bbands(time_period=100).as_pandas()
    mas = ts.with_stddev().without_ohlc().as_pandas()
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

    low_band = p(bands, 'lower_band', 1)
    low_band2 = p(bands, 'lower_band', MAX_INTREVAL)

    med_band = p(bands, 'middle_band', 1)
    med_band2 = p(bands, 'middle_band', MAX_INTREVAL)

    high_band = p(bands, 'upper_band', 1)
    high_band2 = p(bands, 'upper_band', MAX_INTREVAL)

    stddev = p(mas, 'stddev', 1)
    stddev2 = p(mas, 'stddev', MAX_INTREVAL)

    score = 0
# buy condition
    if close < 40:
        score = score + 5

    if close < 20:
        score = score + 5     

    if volume > 17500000:
        score = score + 5
    
    if (low / high * 100 - 100) < 2.5:
        score = score + 5 
    
    if stddev > 5:
        score = score + 10
    
    if stddev > 10:
        score = score + 5

    if stddev > 20:
        score = score + 5


    print("")
    print("")
    print("Stock's score is", score,"/ 40")
    print("")
   

    if score > 19 and score < 30: 
        f = (Stock)
        gs.append(f)
        print(f'Good Stock Tickers are {gs}')
    
    if score > 29: 
        f = (Stock)
        grs.append(f)
        print(f'great Stock Tickers are {grs}')

    time.sleep(15)
    #if i == 3:
     #   break
    print(i)

print("")
print("")
print(f'The Good Stock Tickers Are {gs}')
print(f'The Great Stock Tickers Are {grs}')


