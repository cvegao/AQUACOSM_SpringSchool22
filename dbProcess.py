# import matplotlib
import csv


def dataCharge(fileName='Ramet_number.csv'):

    file = open(fileName)
    data = csv.reader(file)

    header = next(data)
    body = []

    for row in data:
        body.append(row)

    file.close()


print(body)
