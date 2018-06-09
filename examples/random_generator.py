"""
In this example we show how a random generator is coded.
All generators inherit from the DataGenerator class
The class yields tuple (bid_price,ask_price)
"""
import numpy as np
from tgym.gens import RandomWalk


time_series_length = 10
mygen = RandomWalk()
prices_time_series = [mygen.next() for _ in range(time_series_length)]
print(prices_time_series)
