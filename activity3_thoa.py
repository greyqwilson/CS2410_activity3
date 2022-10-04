#Author: Thoa Nguyen
# CS2410 Fall 2022
#Pie chart code for percentage of people with covid 19 by top 10 most populous countries
import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Us', 'China', 'Mexico', 'Russia','India','Brazil','Pakistan','Nigeria','Bangladesh','indonesia'
sizes = [13269503953, 37622096, 1028236358, 2220000000,9215075561,6208000000,347955430,64293818,387483890,987820633]
explode = (0, 0.7, 0, 0.4,0,0,1.0,1.5,0.7,0.4)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
plt.title("Pie Chart Of Covid Case In 2021\n")
ax1.pie(sizes, explode=explode, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.legend(labels,loc="lower left")
plt.show()

#Line graph for number of people vaccinated
from matplotlib import pyplot as plt #another way of import
years = ["2019", "2020", "2021", "2022"]
gdp = [0,372355, 48199814483,59454746436]
# create a line chart, years on x-axis, gdp on y-axis
plt.plot(years, gdp, color='green', marker='o', linestyle='solid')
# add a title
plt.title("People Fully Vaccinated In United States")
# add a label to the y-axis
plt.ylabel("# of people get vaccines")
plt.show(
