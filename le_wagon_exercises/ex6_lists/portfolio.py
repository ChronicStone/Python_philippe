# pylint: disable=missing-docstring

aapl = [ 10, 154.12 ]
goog = [  2, 812.56 ]
tsla = [ 12, 342.12 ]
fb   = [ 18, 209.0  ]

portfolio = [ aapl, goog, tsla, fb ]


# Access the nb of facebook stocks
fb_stocks = portfolio[3][1]


market = [ 198.84, 1217.93, 267.66, 179.06 ]

def calcPnl(portfolio, market):
    totalPortfolio = 0
    marketEstimation = 0
    for index, val in enumerate(portfolio):
        totalPortfolio += portfolio[index][0] * portfolio[index][1]
        marketEstimation += portfolio[index][0] * market[index]
    return marketEstimation - totalPortfolio

