
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set the title of the app
st.title('Bike Rental Analysis Dashboard')

# Define the paths to CSV files
day_path = "../Dataset/day.csv"
hour_path = "../Dataset/hour.csv"

# Using pandas library to read the data from .csv file
day_df = pd.read_csv(day_path, delimiter=",")
hour_df = pd.read_csv(hour_path, delimiter=",")

# Display both of the dataframes
st.subheader("Daily Bike Rental Data Overview")
st.write(day_df.head())
st.subheader("Hourly Bike Rental Data Overview")
st.write(hour_df.head())

# Analysis and Visualizations for Day Data

# Dropdown for selecting which dataset to visualize
data_choice = st.selectbox("Choose the dataset for analysis:", ["Day Data", "Hour Data"])

if data_choice == "Day Data":
    # Analysis and Visualizations for Day Data

    # Scatter plots for environmental factors in day data
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
    # Insights and Conclusions
    st.subheader('Insights and Conclusions')
    st.write("""
   **Insight:**
- The scatter plot for Temperature and Apparent Temperature variable has a positive trend, meaning as temperature increases, rentals increase.
- The scatter plot for Humidity variable shows a negative trend. It means that the higher humidity might correlate with fewer rentals.
- The scatter plot for Wind Speed variable is kinda similar to humidity. When the wind speed is high, then it has a fewer rentals trend.
- For the scatter plot regarding to weather variable, since the weathersit is categorical, i used boxplot instead. This shows that a clear weather likely has the highest median bike rentals and a wider range. It indicates the most favorable weather to biking.

*** The analysis indicates that bike rentals are **positively influenced by higher temperatures**, with both temperature and apparent temperature showing a positive correlation with rental counts, suggesting that favorable weather conditions encourage biking. On the other hand, higher humidity and wind speed are associated with a decline in rentals, indicating that poor weather conditions deter users from renting bike.
""")

elif data_choice == "Hour Data":
        # Hourly rentals analysis from hour data
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
        # Insights and Conclusions
        st.subheader('Insights and Conclusions')
        st.write("""
        **Insight:**
        - **Insight:**
        - From the hourly trends across all the seasons, it shows that in the early morning, 0 - 6, for spring season the average rentals are relatively low.
        - Still in the early morning, the summer season has a slightly higher rentals average than Spring, but the Fall season has the highest number at 73 rentals.
        - In the other hand, the winter season has a consistent rental average with Spring for early morning hour.
        - For the peak usage hours, Fall season sees the highest average of rentals number at around 420ish rentals at 8am. This indicates that this season is particularly popular for morning commutes.
        - For the midday peak usage hour, the Summer season continues to have a high rental at 300 rentals around noon. This indicates that probably people are using bikes at noon for leisure.
        - These plots reveals that Fall season consistently exhibits the highest average bike rentals throughout the day.
        - In contrast, both Spring and Winter show a lower average rentals, particularly in the early morning and evening, indicating these seasons are less conducive to biking.

        =>  Analysis of hourly trends across seasons indicates that bike rentals are generally low in the morning, especially in Spring, where average rentals remain consistently low. In contrast, Fall emerged as the strongest season for morning rentals, peaking at 73 rentals, while Summer showed a slightly higher rental average than Spring during this period, and Winter maintained a similarly low rental average as Spring. In particular, Autumn reached its highest average number of rentals at around 420 at 8am, indicating its popularity for early morning trips. Midday trends further highlight that Summer maintains significant rental activity, peaking at around 300 rentals at noon, which likely reflects leisure usage. Overall, Autumn consistently leads the way in average bike rentals throughout the day, while Spring and Winter show lower average rentals, especially during the morning and afternoon, indicating that these seasons are less favorable for cycling.
    """)

st.markdown("---")
st.subheader("You're at the end of the page,")
st.markdown("""
This analysis was prepared by **Azzah Angeli**
Comp. Engineering Student | Indonesia
""")

# If you running in a local directory, run in your terminal : 
# "streamlit run dashboard_bike-sharing-analysis.py"