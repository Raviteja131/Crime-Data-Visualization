# -*- coding: utf-8 -*-
"""Crime_visualization.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17ap6HZonFgusl0xn0tx_vAH8pch9y2Q8
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('crime.csv',encoding='latin1')

df.head()

df.info()

len(df['OFFENSE_CODE_GROUP'].unique())

#considering the top 10 frequent crime groups only
crime_groups = df['OFFENSE_CODE_GROUP'].value_counts().nlargest(10).index
subset_df = df[df['OFFENSE_CODE_GROUP'].isin(crime_groups)]

"""# 1.Peak hours of crime"""

sns.heatmap(subset_df.pivot_table(index='HOUR', columns='OFFENSE_CODE_GROUP', aggfunc='size'), cmap='viridis', cbar_kws={'label': 'Number of Crimes'},linewidths=0.5)
plt.title('Peak Hours for Crime by type of crime')
plt.show()

"""# 2. Crime Frequency weekends and weekday"""

#selecting a set of crime groups
crime_groups = ['Larceny', 'Vandalism', 'Robbery', 'Burglary', 'Drug Violation']
subset_df = df[df['OFFENSE_CODE_GROUP'].isin(crime_groups)]

plt.figure(figsize=(10, 6))
sns.countplot(x='DAY_OF_WEEK', data=subset_df, order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], palette='viridis')
plt.title('Crime Frequency: Weekday vs. Weekend for Selected Crime Groups')
plt.xlabel('Day of Week')
plt.ylabel('Number of Crimes')
plt.show()

"""# 3. Crime group Frequency by district"""

plt.figure(figsize=(10, 8))
sns.countplot(x='DISTRICT', hue='OFFENSE_CODE_GROUP', data=subset_df, order=df['DISTRICT'].value_counts().index)
plt.title('Common Crime types in Each District')
plt.show()

"""# 4. Crime rate by district"""

plt.figure(figsize=(12, 8))
sns.countplot(x='DISTRICT', data=df, order=df['DISTRICT'].value_counts().index)
plt.title('Overall Crime Rates by District')
plt.show()

"""# 5. Crime rate trend over years"""

crime_count_by_year = df['YEAR'].value_counts().sort_index()
sns.lineplot(x=crime_count_by_year.index, y=crime_count_by_year.values, marker='o', color='purple')
plt.title('Overall Crime Rate Trend Over the Years')
plt.xlabel('Year')
plt.ylabel('Number of Crimes')
plt.xticks(crime_count_by_year.index, labels= crime_count_by_year.index)
plt.show()

"""# 6. Crime Rate by month"""

crime_count_by_month = df['MONTH'].value_counts().sort_index()
sns.barplot(x=crime_count_by_month.index, y=crime_count_by_month.values,color='red')
plt.title('Monthly Crime Frequency')
plt.xlabel('Month')
plt.ylabel('Number of Crimes')
plt.xticks(ticks=range(1, 13), labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.show()

"""# 7. Trends in shooting"""

#incidents where shooting has happened
shooting_df = df[df['SHOOTING'] == 'Y']
shooting_count_by_year = shooting_df['YEAR'].value_counts().sort_index()
sns.lineplot(x=shooting_count_by_year.index, y=shooting_count_by_year.values, marker='o')
plt.title('Shooting trends')
plt.xlabel('Year')
plt.ylabel('Number of Shooting incidents')
plt.xticks(shooting_count_by_year.index, labels= shooting_count_by_year.index)
plt.show()

shooting_count_by_year