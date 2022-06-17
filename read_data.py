import pandas as pd

df = pd.read_csv("./data/EquipamientosMunicipales.csv")
df = df[["X","Y","equipamien","idclase"]]

print(df)