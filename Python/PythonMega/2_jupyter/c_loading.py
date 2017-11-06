import pandas as pds

data=pds.read_csv('loading_jupyter/supermarkets.csv')

print(data.loc[:,'ID':'Country'])

# How to execute notebook without opening it?
# == ipython file
