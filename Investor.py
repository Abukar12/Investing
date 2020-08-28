from twelvedata import TDClient
MAX_INTREVAL = 2

#access utils
def p(data, index, intreval):
    return pull_from_frame(data, index, intreval)

def pull_from_frame(data, index, intreval):
    pulled = data.filter(regex=index).values.tolist()[intreval - 1][0]
    return pulled

#data client
td = TDClient(apikey="1354e1035b2d404c8ded01d402571d6a")

ts = td.time_series(
    symbol="GOOGL",
    interval="1h",
    outputsize=MAX_INTREVAL,
    timezone="America/New_York",
    #start_date=
    #end_date="YYYY-MM-DD"
    )

#Tech Indcators
bands = ts.with_bbands(time_period=800).as_pandas()
slows = ts.with_stoch().without_ohlc().as_pandas()
mas = ts.with_sma(time_period=800).without_ohlc().with_wma(time_period=800).without_ohlc().as_pandas()
#pull from frame
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

wma = p(mas, 'wma', 1)
wma2 = p(mas, 'wma', MAX_INTREVAL)

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
    
if (sma / close * 100 - 100) < -7:
    score = score + 2

if (close - low_band) > 0 and (close / low_band * 100 - 100) > 7:
    score = score + 10

if (close / low_band * 100 - 100) < 7:
    score = score - 10

if (close / low_band * 100 - 100) < 15:
    score = score - 10

print("")
print("")
print("Stock's score is", score,"/35")
print("")
