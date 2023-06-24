import statistics as Stat
import pandas as PD
import csv
import plotly.figure_factory as FF
import random

DF = PD.read_csv("medium_data.csv")
Data = DF["reading_time"].tolist()
Fig = FF.create_distplot([Data],["reading_time"],show_hist=False)
Fig.show()
print(" population mean =",Stat.mean(Data))

def random_set_of_mean(counter):
    Dataset = []
    for i in range(0,counter):
        random_in = random.randint(0,len(Data))
        value = Data[random_in]
        Dataset.append(value)
    mean = Stat.mean(Dataset)
    return mean

def show_fig(mean_list):
    DF = mean_list
    fig = FF.create_distplot([DF],["reading_time"],show_hist=False)
    fig.show()

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_mean = random_set_of_mean(30)
        mean_list.append(set_of_mean)
    show_fig(mean_list)
    print(" sampleing mean =",Stat.mean(mean_list))
setup()