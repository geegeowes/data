import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

df = pd.read_csv('data.csv') #DataFrame из файла

print(df)

#сорировка данных по датам
df = df.sort_values(by='Date')
print(df)

#проверяем на пустые ячейки
df.info()
missing_values = df.isnull().sum()
print(missing_values)
#узнать средние значения, отклонение, мин, макс
statistics = df.describe()
print(statistics)

#Графики
plt.hist(df['Price'], bins=10)
plt.xlabel('Цена')
plt.ylabel('Частота')
plt.title('Гистограмма распределения цен на продукты')
plt.show()

plt.scatter(df['Price'], df['Quantity'])
plt.xlabel('Цена')
plt.ylabel('Количество продаж')
plt.title('Диаграмма разброса - цена/количество продаж')
plt.show()

plt.scatter(df['Date'], df['Quantity'])
plt.xlabel('Дата')
plt.ylabel('Количество продаж')
plt.title('График продаж по датам')
plt.show()


#равна ли средняя цена продуктов в электронике ценам в мебели

elect = df.groupby('Category').get_group('Electronics')
furn = df.groupby('Category').get_group('Furniture')

print(elect)
print(furn)
t_statistic, p_value = stats.ttest_ind(elect['Price'], furn['Price']) 
print('t-статистика',t_statistic)
print('р-значение',p_value)
if p_value <0.05:
    print("Средние значения в электронике и мебели статистически значимо различаются.")
else:
    print("Средние значения в электронике и мебели не различаются с учетом статистической значимости.")


#корреляция между ценами и продажами
corr, p_value = stats.pearsonr(df['Price'], df['Sales'])
if p_value < 0.05:
    print("Есть статистически значимая корреляция.")
else:
    print("Нет статистически значимой корреляции.")