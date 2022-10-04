from matplotlib import rcParams
import matplotlib.pyplot as plt
import matplotlib.style as mplstyle
mplstyle.use('fast')

#Cumulative total tests performed (for covid-testing-all-observations.csv)
CT = 6
#Daily change of cumulative total tests performed
DCCT = 7
#Positivity rate (short term) of tests performed
PR = 12

def fopen(filename, mode = 'r'):
    "Performs error checking and returns file object"
    try:
        file = open(filename, mode, encoding='utf-8-sig')
        return file
    except FileNotFoundError:
        print(filename, "could not be found. Quitting...")
        quit()


def compareCountryTests(countryA, countryB):
    "countryA and countryB should be the respective countries' ISO code. Plots amount of tests for each country as bar graph given ISO code"
    file = fopen(".\\Activity3\\covid-testing-all-observations.csv")
    file.readline() #throwaway first line containing column names
    countryAReport = []
    countryBReport = []

    for line in file:
        buffer = line.split(",")
        #We only want country A's data here, so only stop at lines with that country's ISO code
        if buffer[1] == countryA:
            #Add (date, change in cumulative total)
            if buffer[DCCT] == '':
                #In case of empty entries, add a zero
                countryAReport.append((buffer[2], 0.0))
            else:
                countryAReport.append((buffer[2], float(buffer[DCCT])) )
    file.close()
    #Reset file pointer 

    file = fopen(".\\Activity3\\covid-testing-all-observations.csv")
    file.readline() #throwaway first line containing column names
    for line in file:
        buffer = line.split(",")
        if buffer[1] == countryB:
            #Add (date, change in cumulative total)
            if buffer[DCCT] == '':
                countryBReport.append((buffer[2], 0.0))
            else:
                countryBReport.append((buffer[2], float(buffer[DCCT])) )
    file.close()

    #Grab column 1 from country reports (daily change in cumulative total)
    countryADict = dict(countryAReport)
    countryBDict = dict(countryBReport)
    countryAValues = countryADict.values()
    countryBValues = countryBDict.values()
    
    #Dates may be mismatched, so fill ends with empty entries
    if len(countryBValues) > len(countryAValues):
        bLength = len(countryBValues) 
        aLength = len(countryAValues)
        countryAValues = list(countryAValues)
        countryBValues = list(countryBValues)
        for i in range(0, bLength - aLength):
            countryAValues.append(0)
    
    elif len(countryAValues) > len(countryBValues):
        bLength = len(countryBValues) 
        aLength = len(countryAValues)
        countryAValues = list(countryAValues)
        countryBValues = list(countryBValues)
        for i in range(0, aLength - bLength):
            countryBValues.append(0)
    
    #Both countries should now have same number of entries, so either dates will do
    dates = countryADict.keys()
    #Axis subplot to control number of ticks
    dateAxis = plt.subplot()
    dayTicks = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900]
    rateTicks = [1000, 10000, 100000, 200000, 1000000, 2000000, 10000000, 20000000]
    dateAxis.set_xticks(dayTicks)
    dateAxis.set_yticks(rateTicks)

    plt.bar(dates, countryAValues, label=countryA)
    dayTicks = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900]
    rateTicks = [1000, 10000, 100000, 200000, 1000000, 2000000, 10000000, 20000000]
    dateAxis.set_xticks(dayTicks)
    dateAxis.set_yticks(rateTicks)
    plt.bar(dates, countryBValues, label=countryB, color = 'red')
    plt.title("Number of tests performed")
    plt.legend()
    filenamestr = countryA + "_" + countryB + "_testsPerformed.png"
    plt.savefig(filenamestr)
    plt.show(block = True)

def deathGraph(country):
    "Plots total deaths of a country over time given country name"
    file = fopen(".\\Activity3\\total_deaths.csv")
    firstLine = file.readline()
    firstLine = firstLine.split(",")
    countryReport = []

    #Find at what index we expect to see values for our target country
    indexOfCountry = 0
    for i, element in enumerate(firstLine):
        if element == country:
            indexOfCountry = i
            break

    for line in file:
        buffer = line.split(",")
        #Only read at the index of the target country (US is 220)
        if buffer[indexOfCountry] == '':
            countryReport.append((buffer[0], 0.0) )
        else:
            countryReport.append((buffer[0], float(buffer[indexOfCountry])) )
            
    file.close()
    dates = dict(countryReport).keys()
    dateAxis = plt.subplot()
    dayTicks = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900]
    dateAxis.set_xticks(dayTicks)
    deaths = dict(countryReport).values()
    labelString = country + " COVID-19 Deaths"
    plt.tight_layout
    plt.plot(dates, deaths)
    plt.title(labelString)
    filenamestr = country + "_Deaths.png"
    plt.savefig(filenamestr)
    plt.show(block = True)

def infectionRateGraph(country):
    "Plot positive covid infection rate given country ISO code"
    file = fopen(".\\Activity3\\covid-testing-all-observations.csv")
    file.readline() #throwaway first line containing column names
    countryReport = []

    for line in file:
        buffer = line.split(",")
        if buffer[1] == country:
            #Add (date, positvityRate)
            if buffer[PR] == '':
                countryReport.append((buffer[2], 0.0))
            else:
                countryReport.append((buffer[2], float(buffer[PR])) )
    file.close()
    
    dates = dict(countryReport).keys()
    dateAxis = plt.subplot()
    dayTicks = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900]
    posRate = dict(countryReport).values()
    labelString = country + " COVID-19 Positivity Rate"

    #Magic spacing code thank you ImportanceOfBeingEarnest https://stackoverflow.com/questions/44863375/how-to-change-spacing-between-ticks
    #This ended up only being partially useful and didnt work on other plots.
    plt.xticks(dayTicks)
    plt.gca().margins(x=0)
    plt.gcf().canvas.draw()
    tl = plt.gca().get_xticklabels()
    maxsize = max([t.get_window_extent().width for t in tl])
    m = 3
    s = maxsize / plt.gcf().dpi*len(dayTicks)+2*m
    margin = m/plt.gcf().get_size_inches()[0]
    plt.subplots_adjust(left=margin, right=1.-margin)
    plt.gcf().set_size_inches(s, plt.gcf().get_size_inches()[1])
    plt.tight_layout()

    #Make plot, title, save to file, and show
    plt.plot(dates, posRate)
    plt.title(labelString)
    filenamestr = country + "_PositivityRate.png"
    plt.savefig(filenamestr, dpi=300)
    plt.show(block = True)

def main():
    #Codes used for infection rate group and 
    infectionRateGraph('ESP')
    plt.clf()
    plt.close()
    compareCountryTests('USA', 'GBR')
    plt.clf()
    plt.close()
    deathGraph("United States")
main()