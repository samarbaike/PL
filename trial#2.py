import pandas as sm
fact = sm.read_csv('factbook.csv',header=0, sep=';', skiprows=[1]).head(10)
fact['Country']=fact['Country'].map({j: i for i, j in enumerate(fact["Country"])})
print(fact)
