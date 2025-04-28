# Test File

import matplotlib.pyplot as plt
import pandas as pd

print("Hello World")

#plt.plot([1, 2, 3], [4, 5, 6])
#plt.show()

data = pd.read_csv('vgsales.csv')
print(data.head()) 


drop_row_index = data[data['Year'] > 2015].index
data = data.drop(drop_row_index)

data['Genre'].value_counts().plot(kind = 'bar')
plt.title('Count of Video Games by Genre (2015 and earlier)')
plt.xlabel('Genre of Video Game')
plt.ylabel('Count in millions')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plotting Global Sales by Genre


#data.plot(x = 'Genre', y = 'Global_Sales', kind = 'bar')
#plt.title('Global Sales by Genre')
#plt.xlabel('Genre')
#plt.ylabel('Global Sales (in millions)')

#plt.show()
