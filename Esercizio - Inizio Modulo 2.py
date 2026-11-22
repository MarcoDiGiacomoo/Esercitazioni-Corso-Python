import pandas as pd
import matplotlib.pyplot as plt

# Creiamo un dataset di esempio
dati = {'Settimana': [1, 2, 3, 4, 5, 6],
'Vendite': [250, 300, 400, 350, 450, 500]}

df = pd.DataFrame(dati)

# Calcoliamo la media delle vendite
media_vendite = df['Vendite'].mean()
print("Media vendite:", media_vendite)

colori = ["green" if v > media_vendite else "red" for v in df["Vendite"]]
# Creiamo un grafico a barre
plt.bar(df['Settimana'], df['Vendite'], color=colori)
plt.plot(df["Settimana"], df["Vendite"], color = "black", marker = "o", label = "Andamento Vendite")
plt.axhline(media_vendite, color='red', linestyle='--', label='Media')
plt.xlabel('Settimana')
plt.ylabel('Vendite')
plt.title('Vendite settimanali')
plt.legend()
plt.show()