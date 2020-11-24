import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np
import seaborn as sns

df = pd.read_csv('sea-level.csv')

x = df['Year']

y = df['CSIRO Adjusted Sea Level']

plt.figure(figsize=(14,9))
plt.scatter(x, y)
plt.xlabel('Year')
plt.ylabel('CSIRO Adjusted Sea Level')
plt.title('Year Vs. CSIRO ASL')
plt.tight_layout()

line1 = linregress(x, y)

slope, intercept, r_value, p_value, std_err = line1

years_extended = x.append(pd.Series(range(2014, 2050)), ignore_index=True)

plt.plot(years_extended, years_extended*slope + intercept, color="blue")
plt.xlabel('Year')
plt.ylabel('CSIRO Adjusted Sea Level')

year_above_2000 = df.loc[df['Year']>=2000,'Year']
CSIRO_above_2000 = df.loc[df['Year']>=2000,'CSIRO Adjusted Sea Level']

line2 = linregress(year_above_2000,CSIRO_above_2000)

slope2, intercept2, r_value2, p_value2, std_err2 = line2

year_after_2000 = years_extended[years_extended>=2000]

plt.plot(year_after_2000,year_after_2000*slope2 + intercept2, color='red')
plt.xlabel('Year')
plt.ylabel('CSIRO Adjusted Sea Level')

plt.savefig('results.png')

