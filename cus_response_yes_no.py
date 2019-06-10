import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Data/WA_Fn-UseC_-Marketing-Customer-Value-Analysis.csv')

# Print number of records and columns
print(df.shape)

# Print the file header, all columns + the first 5 rows
print(df.head())

# Print the names of all columns
print(df.columns)

# Print the number of customers that response yes or no
print(df.groupby('Response').count()['Customer'])

# Display the customers responses (yes, no) in a bar plot
ax = df.groupby('Response').count()['Customer'].plot(
    kind = 'bar',
    color = 'orchid',
    grid = True,
    figsize = (10, 7),
    title = "Customers Response"
)

ax.set_xlabel('Engaged')
ax.set_ylabel('Count')

plt.show()