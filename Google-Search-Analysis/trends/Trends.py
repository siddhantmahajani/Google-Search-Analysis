"""
Author: Siddhant Mahajani
Trends.py - To search trends on Google
"""

from pytrends.request import TrendReq


def getTrends(searchVal):
    trendReq = TrendReq()
    trendReq.build_payload(kw_list=[searchVal])
    data = trendReq.interest_over_time()
    return data
