import matplotlib.pyplot as plt

import scipy.stats
import pandas as pd
from scipy import stats


def data_loading(file_name='Ramet_number.csv'):
    """
    :return: DataFrame
    """
    data = pd.read_csv(file_name)
    return data


def is_normal(data, rows):
    result = scipy.stats.shapiro(data[rows, ])
    print(result)


df = data_loading()

"""
filtered_df = df[df["SampleDay"] == 6]

filtered_df.boxplot(by=["Plant", "snail"], column="PVI")

plt.ylabel("PVI")
plt.show()
"""
myLS = df[df["Plant"] == "My"]
myLS = myLS[myLS["snail"] == "LS"]
myLS = myLS[myLS["SampleDay"] == 6]
myHS = df[df["Plant"] == "My"]
myHS = myHS[myHS["snail"] == "HS"]
myHS = myHS[myHS["SampleDay"] == 6]
print(myLS, myHS, sep="\n")
print(f"My: {stats.kruskal(myLS['PVI'], myHS['PVI'])}")

pbLS = df[df["Plant"] == "PB"]
pbLS = pbLS[pbLS["snail"] == "LS"]
pbLS = pbLS[pbLS["SampleDay"] == 6]
pbHS = df[df["Plant"] == "PB"]
pbHS = pbHS[pbHS["snail"] == "HS"]
pbHS = pbHS[pbHS["SampleDay"] == 6]
print(f"PB: {stats.kruskal(pbLS['PVI'], pbHS['PVI'])}")
