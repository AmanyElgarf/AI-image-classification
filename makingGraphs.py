import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("ProcessedInfo - Epoch Face Time.csv")
fig, ax = plt.subplots()
fig1, ax1 = plt.subplots()
df.plot(x='Percent Data', colormap='Spectral', ax=ax1, title = 'Face Training Time vs Epochs')
df.plot(kind='line',x='Percent Data',y='1', ax=ax)
df.plot(kind='line',x='Percent Data',y='2', ax=ax)
df.plot(kind='line',x='Percent Data',y='3', ax=ax)
df.plot(kind='line',x='Percent Data',y='4',ax=ax)
df.plot(kind='line',x='Percent Data',y='5', ax=ax)
df.plot(kind='line',x='Percent Data',y='6',ax=ax)
df.plot(kind='line',x='Percent Data',y='7',ax=ax)
df.plot(kind='line',x='Percent Data',y='8',ax=ax)
df.plot(kind='line',x='Percent Data',y='9',ax=ax)
df.plot(kind='line',x='Percent Data',y='10',ax=ax)
ax.set_ylabel("Percent Accuracy")
ax1.set_ylabel("seconds")
plt.show()
