import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

np.random.seed(42)

dates = pd.date_range(start = "2023-01-01", periods = 200)

prices = np.cumsum(np.random.randn(200))

df = pd.DataFrame({"date": dates, "close": prices})

df.set_index("date", inplace = True)

ema_short = df["close"].ewm(span = 12, adjust = False).mean()

ema_long = df["close"].ewm(span = 26, adjust = False).mean()

macd = ema_short - ema_long

signal = macd.ewm(span = 9, adjust = False).mean()

df["macd"] = macd

df["signal"] = signal

df["histogram"] = df["macd"] - df["signal"]

plt.figure(figsize = (12, 8))

plt.subplot(2, 1, 1)

plt.plot(df.index, df["close"], label="close price")

plt.title("price and macd")

plt.legend()

plt.subplot(2, 1, 1)

plt.plot(df.index, df["macd"], label="macd", color = "blue")

plt.plot(df.index, df["signal"], label="signal", color = "red")

plt.plot(df.index, df["histogram"], label="histogram", color = "green")

plt.legend()

plt.show()

