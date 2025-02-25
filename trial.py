import pandas as panda
cars = panda.read_csv('cars.csv', header=0, sep=';', skiprows=[1])


cars = cars[cars['Cylinders']==8]
print(cars.head(20))