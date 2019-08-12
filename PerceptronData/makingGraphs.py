import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("ProcessedInfo - Avg Accuracy Digit.csv")
fig, ax = plt.subplots()
df.plot(kind='line',x='Percent Data', y='Naive Bayes', ax=ax, title = 'Accuracy of Digits Naive Bayes vs Perceptron')
df.plot(kind='line',x='Percent Data', y='Perceptron', ax=ax)
ax.set_ylabel("Percent")
plt.show()
