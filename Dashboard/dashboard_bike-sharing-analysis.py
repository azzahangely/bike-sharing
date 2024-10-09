import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set the title of the app
st.title('Bike Rental Analysis Dashboard')

# Define the paths to CSV files
day_path = "Dashboard/day.csv"
hour_path = "Dashboard/hour.csv"

# Using pandas library to read the data from .csv file
day_df = pd.read_csv(day_path, delimiter=",")
hour_df = pd.read_csv(hour_path, delimiter=",") 

# Display both of the dataframes
st.subheader("Daily Bike Rental Data Overview")
st.write(day_df.head())
st.subheader("Hourly Bike Rental Data Overview")
st.write(hour_df.head())

# Day Data Analysis and Visualizations
st.subheader('Scatter Plots for Environmental Factors (Day Data)')
environmental_vars = ['temp', 'atemp', 'hum', 'windspeed']
fig, axs = plt.subplots(2, 2, figsize=(12, 10))
axs = axs.flatten()

for i, var in enumerate(environmental_vars):
    sns.scatterplot(x=day_df[var], y=day_df['cnt'], ax=axs[i])
    axs[i].set_title(f'{var.capitalize()} vs Rentals')
    axs[i].set_xlabel(var.capitalize())
    axs[i].set_ylabel('Count of Rentals')

plt.tight_layout()
st.pyplot(fig)

# Box plot for weather situation in day data
st.subheader('Box Plot for Weather Situation vs Rentals (Day Data)')
plt.figure(figsize=(10, 6))
sns.boxplot(x='weathersit', y='cnt', data=day_df, palette='Set2')
plt.title('Bike Rentals by Weather Situation (Day Data)')
plt.xlabel('Weather Situation')
plt.ylabel('Count of Rentals')
plt.xticks(ticks=[0, 1, 2, 3], labels=['Clear', 'Mist', 'Light Snow/Rain', 'Heavy Rain/Snow'])
st.pyplot(plt)

# Insights and Conclusions for Day Data
st.subheader('Insights and Conclusions')
st.write("""
**Insight:**
- The scatter plot for Temperature and Apparent Temperature variables has a positive trend, meaning as temperature increases, rentals increase.
- The scatter plot for Humidity shows a negative trend, indicating higher humidity correlates with fewer rentals.
- The scatter plot for Wind Speed shows a similar trend to humidity, with fewer rentals when wind speed is high.
- Clear weather likely has the highest median bike rentals and a wider range, indicating it is the most favorable weather for biking.

**Conclusion:**
- Bike rentals are positively influenced by higher temperatures, while higher humidity and wind speed are associated with fewer rentals.
""")

# Hour Data Analysis and Visualizations
st.subheader('Hourly Rentals by Season (Hour Data)')
hourly_season_rentals = hour_df.groupby(['hr', 'season'])['cnt'].mean().unstack()

# Line plot for hourly rentals by season
plt.figure(figsize=(12, 6))
for season in range(1, 5):  # 1 to 4 for each season
    plt.plot(hourly_season_rentals.index, hourly_season_rentals[season], label=f'Season {season}')

plt.title('Average Bike Rentals by Hour Across Seasons (Hour Data)')
plt.xlabel('Hour of the Day')
plt.ylabel('Average Rentals')
plt.xticks(range(0, 24))  # Show hours from 0 to 23
plt.legend(title='Season', loc='upper right')
plt.grid()
st.pyplot(plt)

# Insights and Conclusions for Hour Data
st.subheader('Insights and Conclusions')
st.write("""
**Insight:**
- Hourly trends show low rentals in the early morning for Spring, with Fall having the highest number of rentals at 73 during this period.
- Fall shows the highest peak in rentals, particularly at 8 am, indicating a preference for morning commutes.
- Summer has significant rental activity around noon, suggesting usage for leisure.

**Conclusion:**
- Fall consistently has the highest rentals throughout the day, while Spring and Winter show lower rentals, particularly in the morning and evening.
""")

st.markdown("---")
st.subheader("You're at the end of the page,")
st.markdown("""
This analysis was prepared by **Azzah Angeli**
Comp. Engineering Student | Indonesia
""")
