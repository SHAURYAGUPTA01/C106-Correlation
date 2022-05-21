import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    hours=[]
    size = []
    with open(data_path) as f:
        data = csv.DictReader(f)
        for i in data:
            hours.append(float(i["Average time spent watching TV in a week (hours)"]))
            size.append(float(i["Size of TV"]))
    return { "x" : size  , "y" : hours }

def findCorrelation(ds):
    c = np.corrcoef(ds["x"],ds["y"])
    print(c[0,1])

def plotgraph(data_path):
    with open(data_path) as i:
        df = csv.DictReader(i)
        plot = px.scatter(df, x = "Size of TV", y = "Average time spent watching TV in a week (hours)" )
        plot.show()
    
def setup():
    dp = "Size of TV,_Average time spent watching TV in a week (hours).csv"
    ds=getDataSource(dp)
    findCorrelation(ds)
    plotgraph(dp)

setup()
# Corrcoef is 0 hence we can say that data is not correlated