import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("covid_data.csv")

# Convert Date column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# 1. Line graph for confirmed cases
plt.figure()
plt.plot(data['Date'], data['Confirmed'])
plt.xlabel("Date")
plt.ylabel("Confirmed Cases")
plt.title("COVID-19 Confirmed Cases Over Time")
plt.show()

# 2. Line graph for recovered and deaths
plt.figure()
plt.plot(data['Date'], data['Recovered'], label="Recovered")
plt.plot(data['Date'], data['Deaths'], label="Deaths")
plt.xlabel("Date")
plt.ylabel("Number of Cases")
plt.title("Recovered vs Deaths")
plt.legend()
plt.show()

# 3. Bar chart for daily confirmed cases
plt.figure()
plt.bar(data['Date'], data['Confirmed'])
plt.xlabel("Date")
plt.ylabel("Confirmed Cases")
plt.title("Daily COVID-19 Confirmed Cases")
plt.show()

# 4. Pie chart
total_confirmed = data['Confirmed'].iloc[-1]
total_recovered = data['Recovered'].iloc[-1]
total_deaths = data['Deaths'].iloc[-1]

plt.figure()
plt.pie(
    [total_confirmed, total_recovered, total_deaths],
    labels=["Confirmed", "Recovered", "Deaths"],
    autopct='%1.1f%%'
)
plt.title("COVID-19 Case Distribution")
plt.show()         