PyAlgoTrade
===========
从2015 07 31开始尝试学习使用git。
一点点读懂这个程序。

2015年7月31日 粗粗看一下廖雪峰的git教程，对git有一些了解了http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/00137586810169600f39e17409a4358b1ac0d3621356287000

[![version status](https://pypip.in/v/pyalgotrade/badge.png)](https://pypi.python.org/pypi/pyalgotrade)
[![downloads](https://pypip.in/d/pyalgotrade/badge.png)](https://pypi.python.org/pypi/pyalgotrade)
[![build status](https://travis-ci.org/gbeced/pyalgotrade.png?branch=master)](https://travis-ci.org/gbeced/pyalgotrade)
[![Coverage Status](https://coveralls.io/repos/gbeced/pyalgotrade/badge.svg?branch=master)](https://coveralls.io/r/gbeced/pyalgotrade?branch=master)


PyAlgoTrade is an **event driven algorithmic trading** Python library. Although the initial focus
was on **backtesting**, **paper trading** is now possible using:

 * [Bitstamp](https://www.bitstamp.net/) for Bitcoins
 * [Xignite](https://www.xignite.com/) for stocks

and **live trading** is now possible using:

 * [Bitstamp](https://www.bitstamp.net/) for Bitcoins

To get started with PyAlgoTrade take a look at the [tutorial](http://gbeced.github.io/pyalgotrade/docs/v0.17/html/tutorial.html) and the [full documentation](http://gbeced.github.io/pyalgotrade/docs/v0.17/html/index.html).

Main Features
-------------

 * Event driven.
 * Supports Market, Limit, Stop and StopLimit orders.
 * Supports any type of time-series data in CSV format like Yahoo! Finance, Google Finance, Quandl and NinjaTrader.
 * [Xignite](https://www.xignite.com/) realtime feed.
 * Bitcoin trading support through [Bitstamp](https://www.bitstamp.net/).
 * Technical indicators and filters like SMA, WMA, EMA, RSI, Bollinger Bands, Hurst exponent and others.
 * Performance metrics like Sharpe ratio and drawdown analysis.
 * Handling Twitter events in realtime.
 * Event profiler.
 * TA-Lib integration.

Installation
------------

PyAlgoTrade is developed using Python 2.7 and depends on:

 * [NumPy and SciPy](http://numpy.scipy.org/).
 * [pytz](http://pytz.sourceforge.net/).
 * [matplotlib](http://matplotlib.sourceforge.net/) for plotting support.
 * [ws4py](https://github.com/Lawouach/WebSocket-for-Python) for Bitstamp support.
 * [tornado](http://www.tornadoweb.org/en/stable/) for Bitstamp support.
 * [tweepy](https://github.com/tweepy/tweepy) for Twitter support.

You can install PyAlgoTrade using pip like this:

```
pip install pyalgotrade
```
