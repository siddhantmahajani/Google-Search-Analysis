"""
Author: Siddhant Mahajani
Main.py - To input string to search, and execute main program
"""

from graph import Graph
from trends import Trends


def execute(searchVal):
    trend_data = Trends.getTrends(searchVal)
    Graph.plotTrendChart(trend_data, searchVal)


if __name__ == "__main__":
    searchVal = input('Enter the keyword to find total Google Searches over time?\n')
    execute(searchVal)
