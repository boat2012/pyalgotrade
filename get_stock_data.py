import sys
from pyalgotrade.tools import yahoofinance;

yahoofinance.download_daily_bars('2342.hk',int(sys.argv[1]), 'comb-%s.csv' % sys.argv[1])
