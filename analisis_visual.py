import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

conexion = sqlite3.connect('datos_mision.db')
query = "SELECT * FROM planetas"
df = pd.read_sql_query(query, conexion)
conexion.close()
df = df.dropna()
df = df[df['pl_rade'] > 0]
df['densidad'] = 5.51* df['pl_bmasse']/(df['pl_rade']**3)
df = df.sort_values(by='densidad', ascending=True)
df.to_csv('densidad.csv', index=False)
df_plot = df[(df['densidad'] > 0) & (df['densidad'] <= 20)]
sc = plt.scatter(df_plot['pl_rade'], df_plot['pl_bmasse'], c=df_plot['densidad'],cmap='tab20b', alpha=0.8)
plt.title('Masa vs. Radio')
plt.xlabel("Radio [R$ _\oplus$]")
plt.ylabel("Masa [M$ _\oplus$]")
plt.xscale('log')
plt.yscale('log')
cbar = plt.colorbar(sc)
cbar.set_label('Densidad [$ g/cm^3$]')
plt.scatter(1,1, label='Tierra (5.51 $ g/cm^3$)', c='red')
plt.scatter(11.2,317.8, label='Júpiter (1.33 $ g/cm^3$)', c='blue')
plt.scatter(3.8,17.2, label='Neptuno 1.64 $ g/cm^3$', c='cyan')
plt.legend()
plt.savefig('resultado.png')
plt.close()
