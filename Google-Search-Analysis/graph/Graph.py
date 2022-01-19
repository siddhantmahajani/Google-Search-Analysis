"""
Author: Siddhant Mahajani
Graph.py - To plot total Google Search
"""


import matplotlib.pyplot as plt


def plotTrendChart(data, searchVal):
    figure = plt.subplots(figsize=(7, 7))
    data[searchVal].plot()
    plt.style.use('fivethirtyeight')
    plt.title('Total Google Searches for {}'.format(searchVal), fontweight='bold')
    plt.xlabel('Year')
    plt.ylabel('Total Count')
    plt.show()