# Load the pyplot library with alias 'plt'
import matplotlib.pyplot as plt
# Load the Pandas library with alias 'pd'
import pandas as pd
# Load matplotlib for date labels
import matplotlib.dates as mdates

# Reads the csv file containing time series for General Electric stock
stock1 = pd.read_csv("GE.csv", parse_dates=True)

# Reads the csv file containing time series for JPMorgan stock
stock2 = pd.read_csv("JPM.csv", parse_dates=True)

# Select data rows
date = pd.to_datetime(stock1.Date)
# Select stock price at close
price1 = stock1.Close
price2 = stock2.Close

# Set 2 subplots and shares x axis
fig, (ax1, ax2)= plt.subplots(2, sharex=True)

# Set title
fig.suptitle('Yearly comparison of General Electric stock and JPMorgan stock')

# Set labels
ax1.set(ylabel='Price [USD]')
ax2.set(xlabel='Date', ylabel='Price [USD]')

# Plot time series
ax1.plot(date, price1)
ax2.plot(date, price2, 'tab:red')

# Date format
monthsMaj = mdates.MonthLocator((1,4,7,10)) # quarter major tics
monthsFmt = mdates.DateFormatter('%Y-%m') # set major ticks format
months = mdates.MonthLocator() # set minor ticks
ax1.xaxis.set_major_locator(monthsMaj)
ax1.xaxis.set_major_formatter(monthsFmt)
ax1.xaxis.set_minor_locator(months)

# Show the plot
plt.show()

