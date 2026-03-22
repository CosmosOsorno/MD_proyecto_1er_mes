import pandas as pd
import sqlite3

df = pd.read_csv('consulta_limpia.csv')
df = df.dropna()
df.drop_duplicates(subset='pl_name', keep='first')
conexion = sqlite3.connect('datos_mision.db')
df.to_sql('planetas', conexion, if_exists='replace')
conexion.close()
