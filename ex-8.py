import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

plt.style.use('ggplot')     # Красивые графики
plt.rcParams['figure.figsize'] = (15, 5)    # Размер картинок

df = pd.read_csv('bikes.csv')
df['Berri 1'].plot()


print(df['Berri 1'][:5])    # выводим первые 5 строк в колонке Berri1

print(df[['Date', 'Berri 1']][:5])  # выводим первые 5 строк в колонок Date, Berri1


bikes = pd.read_csv('bikes.csv', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')
berri_bikes = bikes[['Berri 1']].copy()    # копируем столбец в новую переменную

print(berri_bikes[:5])
print(berri_bikes.index.weekday)
berri_bikes.loc[:, 'weekday'] = berri_bikes.index.weekday

weekday_counts = berri_bikes.groupby('weekday').sum()
weekday_counts.index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekday_counts.plot(kind='bar')

plt.show()
