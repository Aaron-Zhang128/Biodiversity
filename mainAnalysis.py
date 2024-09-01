import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
import math
from scipy import stats

dataCO2 = pd.read_csv("Loutput_file.csv")


dataBiodiversity = pd.read_csv("Loutput_file.csv")
yearBio = dataBiodiversity["Year"]
scoreBio = dataBiodiversity["Living Planet Index"]

yearCO2=dataCO2["Year"]
scoreCO2=dataCO2["Annual CO₂ emissions"]

Africa = []
Asia = []
NorthAmerica = []
SouthAmerica = []
Oceana = []
Europe = []

for i in dataBiodiversity["Entity"]:
    if i == "Africa":
        Africa.append(dataBiodiversity[["Entity","Annual CO₂ emissions","Living Planet Index"]])

def F6machineLearningPublic(mlData):
    place = "North America"
    a = []
    b = []
    c=[]
    counter = 0
    for i in dataBiodiversity["Entity"]:
        

        if i == place:
            
            a.append(dataBiodiversity["Annual CO₂ emissions"][counter])
            b.append(((dataBiodiversity["Living Planet Index"][counter])))

        counter = counter + 1

    
    mlDataSet = []
    residual = []
 
    print(yearBio)
    print(scoreBio)
    inflation = [1.0285, 1.0384,0.9964,1.0164,1.0316,1.0207,1.0146,1.0162,1.0012,1.0126,1.0213,1.0244]
    x = [255129,183819,191820,164891,161621,164615,150497,143456,128814,153067,138000,168989]
    dataset = pd.read_csv("Lnorthamerica.csv")
    y = []
    
    
    for i in range(0,len(x)):
        inflationAmount = 1
        counter = len(x)-i-1

        while (counter > 0):

            inflationAmount = inflationAmount * inflation[len(inflation)-counter]
            counter = counter - 1

        x[i] = x[i] * inflationAmount
    for i in dataset["Annual CO₂ emissions"]:
        y.append(i)
    for i in range (0,len(x)):
        mlDataSet.append([x[i],y[i]])  #x y 

    
    
    # print(mlDataSet)
    x = np.array(mlDataSet)[:,0].reshape(-1,1)
    y = np.array(mlDataSet)[:,1].reshape(-1,1)
   
    print(x)
    print(y)
    
    abra = []
    babra = []
    
    for i in x:
        for j in i:
            abra.append(j)
            
    for i in y:
        for j in i:
            babra.append(j)   
    
    print("Standard Deviation")
    print(stats.tstd(babra))
    
    
    regress = LinearRegression()
    regress.fit(x,y)
    r = regress.score(x, y)
    

    predicted_y = regress.predict(x)
    
    m = regress.coef_
    c = regress.intercept_
    for i in range (0,len(x)):
        residual.append(y[i]-(m*x[i]+c) )

 
    print("R :"  + str(r))
    print("R-Squared: " + str(r*r))

    print("RESIDUAL")

    plt.title(place+ ' Annual Carbon Emissions (Kilotons) vs Investment into Public Transportation (Thousnds of Inflation Adjusted US-Dollars)')
    plt.xlabel('Investment into Public Transportation (Thousands of Inflation Adjusted US-Dollars)')
    plt.ylabel('Annual Carbon Emissions (Kilotons)')
    print("slope: " + str(m))
    print("y-int: " + str(c))
    plt.plot(x,m*x+c)
    plt.scatter(x, y)
    plt.show()



    return 0
F6machineLearningPublic(Africa)
