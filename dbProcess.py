import matplotlib.pyplot as plt

import scipy.stats
import pandas as pd


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

# fig, ax = plt.subplots()
# colors = {'LS': 'red', 'HS': 'blue'}

# ax.scatter(df['Plant'], df['RametNumber'], c=df['snail'].map(colors))

filtered_df = df[df["SampleDay"] == 6]

filtered_df.boxplot(by=["Plant", "snail"], column="RametNumber")


plt.show()
