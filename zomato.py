import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#df -> dataframe pandas data structure
df = pd.read_csv("zomato_data.csv")
print(df)

#covert the data type of column rate

def rating(value):
    value=str(value).split('/')
    value=value[0];
    return float(value)

df['rate']=df['rate'].apply(rating)
print(df.head())

#finding there if any null value or not 
df.info()

#What type of restaurant do the majority of customers order from?
df.head()
sns.countplot(x=df['listed_in(type)'], palette="Set2")
plt.xlabel("Type of Restaurant")
plt.show()
#conclusion majority  of the resturant falls in dinning category (dining,cafes,others,buffet)


#How many votes has each type of resturant recevied from customers
df.head()
group_data = df.groupby('listed_in(type)')['votes'].sum()

# Creating a DataFrame from the grouped data
result = pd.DataFrame({'votes': group_data})

# Generating a list of colors
colors = plt.cm.rainbow(np.linspace(0, 1, len(result)))

# Plotting the data with different colors for each marker
plt.scatter(result.index, result['votes'], c=colors, marker="o", s=100)  # s=100 for marker size
plt.plot(result.index, result['votes'], c="black")  # Optional: To connect the markers with a line
plt.xlabel("Type of Restaurant", c="blue", size=20)
plt.ylabel("Votes", c="blue", size=20)
plt.show()

#dinning resturants has recieved maximum votes


#What are the ratings that the majority of resturants have received?
df.head()
plt.hist(df['rate'], bins=5, color="hotpink")
plt.title("Ratings Distribution")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.show()
#conclusion-the majority resturants received ratings from 3.5 to 4


#Zomato has observed that most couples order most of their food online.What is their average spending on each order?
#Average order spending by couples
couple_data = df['approx_cost(for two people)']

# Get unique values for color mapping
unique_values = couple_data.unique()

# Generate a color palette
palette = sns.color_palette("rainbow", len(unique_values))

# Plotting the countplot with different colors for each bar
sns.countplot(x=couple_data, palette=palette)

# Adding labels and title
plt.xlabel("Approximate Cost (for two people)")
plt.ylabel("Count")
plt.title("Distribution of Approximate Costs")
plt.show()
#conclusion-the majority of couples prefer resturants with an approximation cost of 300 rupees


#Which mode recevies maximum rating
sns.set_theme(style="whitegrid")

# Creating the boxplot with customized design
plt.figure(figsize=(8, 6))  # Adjusted figure size for better visibility
sns.boxplot(x='online_order', y='rate', data=df, palette="Set2", width=0.6, linewidth=2.5)

# Customizing the plot's appearance
plt.title("Boxplot of Ratings by Online Order Availability", fontsize=16, fontweight='bold', color='darkblue')
plt.xlabel("Online Order Available", fontsize=14, fontweight='bold', color='darkgreen')
plt.ylabel("Rating", fontsize=14, fontweight='bold', color='darkgreen')

# Customizing the tick labels
plt.xticks(fontsize=12, fontweight='bold', color='hotpink')
plt.yticks(fontsize=12, fontweight='bold', color='black')

# Adding gridlines for better readability
plt.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Showing the plot
plt.show()
#conslusion-offline order received lower rating in comparison to online order


#Which type of resturant received more offline orders,so that zomato can prove customers with some good offers? 
# Creating a pivot table
pivot_table = df.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)

# Plotting the heatmap with a lighter colormap
plt.figure(figsize=(10, 8))  # Adjusted figure size for better readability
sns.heatmap(pivot_table, annot=True, cmap='BuGn', fmt='d', linewidths=.5, linecolor='white')

# Adding titles and labels with customization
sns.heatmap(pivot_table, annot=True, cmap='PuBuGn', fmt='d', linewidths=.5, linecolor='white')
plt.xlabel("Online Order", fontsize=14, fontweight='bold', color='darkgreen')
plt.ylabel("Listed In (Type)", fontsize=14, fontweight='bold', color='darkgreen')

# Rotating x-axis labels for better readability
plt.xticks(rotation=45, ha='right', fontsize=12, fontweight='bold')
plt.yticks(fontsize=12, fontweight='bold')

# Showing the plot
plt.show()
#conclusion-dinning resturants primarily accept offline orders,whereas cafes primarily receives online order.This suggests that clients prefers oreders in person at resturants,but prefer online ordering at cafes.

