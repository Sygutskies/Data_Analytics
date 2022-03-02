import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Data1.csv')
df.rename( columns={'Unnamed: 0':'Date'}, inplace=True )
df.set_index('Date')
plt.plot('Date', 'theta_1')