import pandas as pd

df = pd.read_csv("/home/pepe/Escritorio/Hackatroll/PROYECTO/backend/data/EquipamientosMunicipales.csv")
df = df[["X","Y","equipamien","idclase"]]

print(df)