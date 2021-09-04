  
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("tempdata.csv")
data = df["temp"].tolist()
population_mean = statistics.mean(data)
std_deviation = statistics.stdev(data)

print("population mean", population_mean)
print("standard deviation", std_deviation)

 #code to show the plot of raw data
fig = ff.create_distplot([data], ["temp"], show_hist=False)
fig.show()

dataset = []


for i in range (1,100) :
    random_index = random.randint(0,len(data))
    value = data[random_index]
    dataset.append(value)

mean=statistics.mean(dataset)
sd_deviation = statistics.stdev(dataset)

print("sample mean", mean)
print("standard deviation 2", sd_deviation )