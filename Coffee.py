import plotly.express as px
import csv

with open("cups of coffee vs hours of sleep.csv") as i:
    df = csv.DictReader(i)
    plot = px.scatter(df,x="Coffee in ml",y="sleep in hours",color = "week")
    plot.show()
    
