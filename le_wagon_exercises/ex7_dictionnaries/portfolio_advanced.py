# pylint: disable=missing-docstring

# TODO: start by defining a `portfolio` using a dict!

aapl = [ 10, 154.12 ]
goog = [  2, 812.56 ]
tsla = [ 12, 342.12 ]
fb   = [ 18, 209.0  ]

portfolio = {
    "AAPL": {
        "volume": aapl[0],
        "strike": aapl[1]
    },
    "GOOG": {
        "volume": goog[0],
        "strike": goog[1]
    },
    "TSLA": {
        "volume": tsla[0],
        "strike": tsla[1]
    },
    "FB": {
        "volume": fb[0],
        "strike": fb[1]
    },
}

# Print the volume of TLSA STOCKS
print("TSLA volume", portfolio["TSLA"]["volume"])

# Print strike of GOOG 
print("GOOG strike", portfolio["GOOG"]["strike"])


market = {
    "AAPL": 198.84,
    "GOOG": 1217.93,
    "TSLA": 267.66,
    "FB": 179.06
}
    
def calcPL(portfolio, market):
    totalPortfolio = 0
    marketEstimation = 0
    for key in portfolio:
        totalPortfolio += portfolio[key]["volume"] * portfolio[key]["strike"]
        marketEstimation += portfolio[key]["volume"] * market[key]
    return marketEstimation - totalPortfolio
    
print(calcPL(portfolio, market))


# API SECTION

from requests import get

real_time_market  = get("https://api.iextrading.com/1.0/tops/last?symbols=AAPL,GOOG,TSLA,FB").json()
print(real_time_market )

#real_time_market is a list of dictionnaries.

# Update market variable with live real values. With this code, we only update what already
# exists in our market var.
for val in real_time_market:
    if market[val['symbol']]:
        market[val['symbol']] = val['price']




