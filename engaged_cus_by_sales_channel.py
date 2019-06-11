import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Data/WA_Fn-UseC_-Marketing-Customer-Value-Analysis.csv')

by_offer_type_df = df.loc[
# count only engaged customers    
df['Response'] == 'Yes',].groupby(['Sales Channel' # engaged customers grouped by sales channel
]).count()['Customer'] / df.groupby('Sales Channel').count()['Customer']

ax = (by_offer_type_df * 100.0).plot(
kind = 'bar',
figsize = (7, 7),
color = 'skyblue',
grid = True
)
ax.set_ylabel('Engagement Rate (%)')

plt.show()
