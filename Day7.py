import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from pandas.plotting import register_matplotlib_converters
from matplotlib.backends.backend_pdf import PdfPages
import seaborn as sns
import datetime
register_matplotlib_converters()

# Define date range
date_rng = pd.date_range(start='1/1/2022', end='31/12/2022', freq='M')

# Generate random coffee sales data
np.random.seed(0)
sales_data = np.random.randint(500000,1000000,len(date_rng))

# Create dataframe
data = pd.DataFrame(date_rng, columns=['date'])
data['Coffee Sales'] = sales_data

# Create a line plot
plt.figure(figsize=(12, 8))
sns.lineplot(x='date', y='Coffee Sales', data=data)
plt.title('Monthly Coffee Sales in the UK (2022)')
plt.xlabel('Month')
plt.ylabel('Sales (in units)')

# Save the plot to a PDF file
pdf_pages = PdfPages('D:\Coffee_Sales_UK_2022.pdf')
pdf_pages.savefig(plt.gcf())
pdf_pages.close()

data.to_csv('D:\coffee_Sales_UK_2022.csv', index=False)

data.head()
