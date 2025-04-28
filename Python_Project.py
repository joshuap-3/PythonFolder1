# Creating a Retrospective Bar Graph of Counts of Video Games by Genre (2015 and earlier) :)

# Intro to Data Science
# This code is a simple data analysis and visualization script that reads a CSV file containing video game sales data,
# processes the data to remove entries after 2015, and then creates a bar graph to visualize the count of video games by genre.

# Importing Libraries
import matplotlib.pyplot as plt
import pandas as pd

# This is my test code!
print("Hello ICS Class!")

# Reading the data and printing the first 5 rows
data = pd.read_csv('vgsales.csv')
print(data.head()) 

# Dropping rows with Years greater than 2015
drop_row_index = data[data['Year'] > 2015].index
data = data.drop(drop_row_index)

# Creating a Retrospective Bar Graph of Counts of Video games by Genre (2015 and earlier) as a BarGraph
data['Genre'].value_counts().plot(kind = 'bar')

# Setting the title and labels for the bar graph
plt.title('Count of Video Games by Genre (2015 and earlier)')
plt.xlabel('Genre of Video Game')
plt.ylabel('Count')

# Adding grid lines for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Rotating x-axis labels for better readability
plt.xticks(rotation=45)

# Adjusting layout to prevent clipping of tick-labels
plt.tight_layout()

# Displaying the bar graph
plt.show()

# Plotting Global Sales by Genre
