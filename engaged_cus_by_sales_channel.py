import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Data/WA_Fn-UseC_-Marketing-Customer-Value-Analysis.csv')

# Count
by_sales_channel_df = df.loc[  
df['Response'] == 'Yes',].groupby(['Sales Channel' # engaged customers grouped by renewal offer type
]).count()['Customer'] / df.groupby('Sales Channel').count()['Customer']

ax = (by_sales_channel_df * 100.0).plot(
kind = 'bar',
figsize = (7, 7),
color = 'skyblue',
grid = True
)
ax.set_ylabel('Engagement Rate (%)')

plt.show()