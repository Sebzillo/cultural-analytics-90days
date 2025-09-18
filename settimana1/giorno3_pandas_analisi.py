# GIORNO 3: Pandas Master Class per Cultural Data Analyst
# Trasformiamo i tuoi dati in analisi professionali!

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

print("🔥 GIORNO 3: PANDAS + VISUALIZZAZIONI AVANZATE")
print("=" * 60)

# STEP 1: CREA IL TUO DATASET (sostituisci con i TUOI dati!)
print("STEP 1: CREAZIONE DATASET PERSONALE")
print("-" * 40)

# I tuoi dati culturali (PERSONALIZZA QUESTI!)
dati_culturali = [
    # Film
    {'titolo': 'Il Padrino', 'tipo': 'Film', 'anno': 1972, 'creatore': 'F.F.Coppola', 'genere': 'Crime', 'voto': 10, 'fruizioni': 5, 'decade': '70s'},
    {'titolo': 'Vertigo', 'tipo': 'Film', 'anno': 1958, 'creatore': 'Hitchcock', 'genere': 'Thriller', 'voto': 9, 'fruizioni': 3, 'decade': '50s'},
    {'titolo': 'Citizen Kane', 'tipo': 'Film', 'anno': 1941, 'creatore': 'O.Welles', 'genere': 'Drama', 'voto': 9, 'fruizioni': 2, 'decade': '40s'},
    
    # Libri  
    {'titolo': '1984', 'tipo': 'Libro', 'anno': 1949, 'creatore': 'G.Orwell', 'genere': 'Dystopian', 'voto': 10, 'fruizioni': 3, 'decade': '40s'},
    {'titolo': 'Il Nome della Rosa', 'tipo': 'Libro', 'anno': 1980, 'creatore': 'U.Eco', 'genere': 'Mystery', 'voto': 9, 'fruizioni': 2, 'decade': '80s'},
    {'titolo': 'Cent\'anni di solitudine', 'tipo': 'Libro', 'anno': 1967, 'creatore': 'G.G.Márquez', 'genere': 'Realismo Magico', 'voto': 9, 'fruizioni': 1, 'decade': '60s'},
    
    # Vinili
    {'titolo': 'Dark Side of the Moon', 'tipo': 'Vinile', 'anno': 1973, 'creatore': 'Pink Floyd', 'genere': 'Progressive', 'voto': 10, 'fruizioni': 20, 'decade': '70s'},
    {'titolo': 'Kind of Blue', 'tipo': 'Vinile', 'anno': 1959, 'creatore': 'Miles Davis', 'genere': 'Jazz', 'voto': 10, 'fruizioni': 15, 'decade': '50s'},
    {'titolo': 'Abbey Road', 'tipo': 'Vinile', 'anno': 1969, 'creatore': 'The Beatles', 'genere': 'Rock', 'voto': 9, 'fruizioni': 25, 'decade': '60s'},
    {'titolo': 'What\'s Going On', 'tipo': 'Vinile', 'anno': 1971, 'creatore': 'Marvin Gaye', 'genere': 'Soul', 'voto': 9, 'fruizioni': 12, 'decade': '70s'}
]

# STEP 2: CREAZIONE DATAFRAME PANDAS
df = pd.DataFrame(dati_culturali)
print("✅ DataFrame creato!")
print(f"Dimensioni: {df.shape[0]} contenuti, {df.shape[1]} attributi")
print("\nPrime righe:")
print(df.head())

# STEP 3: ANALISI ESPLORATIVA CON PANDAS
print("\n" + "="*60)
print("STEP 3: ANALISI ESPLORATIVA")
print("-" * 40)

# Info generali
print("📊 INFO GENERALI:")
print(f"• Contenuti totali: {len(df)}")
print(f"• Tipi di contenuto: {df['tipo'].unique()}")
print(f"• Range temporale: {df['anno'].min()}-{df['anno'].max()}")
print(f"• Voto medio: {df['voto'].mean():.1f}")
print()

# Analisi per tipo
print("📈 ANALISI PER TIPO:")
analisi_tipo = df.groupby('tipo').agg({
    'voto': ['count', 'mean'],
    'fruizioni': 'sum',
    'anno': ['min', 'max']
}).round(1)
print(analisi_tipo)
print()

# I tuoi generi preferiti
print("🎭 I TUOI GENERI PREFERITI:")
generi_preferiti = df.groupby('genere')['voto'].agg(['count', 'mean']).sort_values('mean', ascending=False)
print(generi_preferiti.head())
print()

# STEP 4: VISUALIZZAZIONI PROFESSIONALI
print("\n" + "="*60)
print("STEP 4: VISUALIZZAZIONI AVANZATE")
print("-" * 40)

# Setup per grafici professionali
plt.style.use('default')
fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('🎨 LA TUA ANALISI CULTURALE PERSONALE', fontsize=16, fontweight='bold')

# Grafico 1: Distribuzione per tipo
ax1 = axes[0, 0]
tipo_counts = df['tipo'].value_counts()
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']
bars = ax1.bar(tipo_counts.index, tipo_counts.values, color=colors)
ax1.set_title('📊 Distribuzione Contenuti per Tipo', fontweight='bold')
ax1.set_ylabel('Numero di Contenuti')
# Aggiungi valori sopra le barre
for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height + 0.1,
             f'{int(height)}', ha='center', va='bottom')

# Grafico 2: Timeline dei tuoi gusti
ax2 = axes[0, 1]
decade_counts = df['decade'].value_counts().sort_index()
ax2.plot(decade_counts.index, decade_counts.values, marker='o', linewidth=3, markersize=8, color='#FF6B6B')
ax2.fill_between(decade_counts.index, decade_counts.values, alpha=0.3, color='#FF6B6B')
ax2.set_title('⏰ Timeline dei Tuoi Gusti', fontweight='bold')
ax2.set_ylabel('Numero di Contenuti')
ax2.grid(True, alpha=0.3)

# Grafico 3: Voti vs Fruizioni (scatter plot)
ax3 = axes[1, 0]
colors_tipo = {'Film': '#FF6B6B', 'Libro': '#4ECDC4', 'Vinile': '#45B7D1'}
for tipo in df['tipo'].unique():
    data_tipo = df[df['tipo'] == tipo]
    ax3.scatter(data_tipo['voto'], data_tipo['fruizioni'], 
               label=tipo, color=colors_tipo[tipo], s=100, alpha=0.7)
ax3.set_title('🎯 Voto vs Frequenza Fruizione', fontweight='bold')
ax3.set_xlabel('Voto Personale')
ax3.set_ylabel('Numero Fruizioni')
ax3.legend()
ax3.grid(True, alpha=0.3)

# Grafico 4: Top creatori
ax4 = axes[1, 1]
top_creatori = df.groupby('creatore')['voto'].agg(['count', 'mean']).sort_values('mean', ascending=True).tail(6)
bars = ax4.barh(range(len(top_creatori)), top_creatori['mean'], color='#96CEB4')
ax4.set_yticks(range(len(top_creatori)))
ax4.set_yticklabels(top_creatori.index)
ax4.set_title('⭐ Top Creatori (Voto Medio)', fontweight='bold')
ax4.set_xlabel('Voto Medio')
# Aggiungi valori alla fine delle barre
for i, (idx, row) in enumerate(top_creatori.iterrows()):
    ax4.text(row['mean'] + 0.1, i, f'{row["mean"]:.1f}', va='center')

plt.tight_layout()
plt.savefig('analisi_culturale_personale.png', dpi=300, bbox_inches='tight')
plt.show()

print("✅ Grafici salvati come 'analisi_culturale_personale.png'")

# STEP 5: INSIGHTS AUTOMATICI
print("\n" + "="*60)
print("STEP 5: INSIGHTS AUTOMATICI SUI TUOI GUSTI")
print("-" * 50)

# Trova pattern nei tuoi gusti
print("🔍 PATTERN NEI TUOI GUSTI:")

# Decade preferita
decade_preferita = df.groupby('decade')['voto'].mean().idxmax()
print(f"• La tua decade preferita: {decade_preferita} (voto medio: {df.groupby('decade')['voto'].mean().max():.1f})")

# Tipo più "rewatchable"
tipo_piu_visto = df.groupby('tipo')['fruizioni'].mean().idxmax()
fruizioni_medie = df.groupby('tipo')['fruizioni'].mean()
print(f"• Contenuto più 'ri-fruibile': {tipo_piu_visto} (media: {fruizioni_medie.max():.1f} volte)")

# Correlazione voto-fruizioni
correlazione = df['voto'].corr(df['fruizioni'])
if correlazione > 0.5:
    print(f"• Ti piace ri-vedere/ri-leggere/ri-ascoltare quello che ami di più (correlazione: {correlazione:.2f})")
elif correlazione < -0.3:
    print(f"• Tendi a consumare di più contenuti che voti meno (correlazione: {correlazione:.2f})")
else:
    print(f"• Voto e fruizioni sono indipendenti nei tuoi gusti (correlazione: {correlazione:.2f})")

# Genere dominante
genere_dominante = df['genere'].mode().iloc[0]
print(f"• Il tuo genere ricorrente: {genere_dominante}")

print("\n" + "="*60)
print("🎉 CONGRATULAZIONI! HAI COMPLETATO IL GIORNO 3!")
print("✅ Pandas mastered")
print("✅ Visualizzazioni professionali create") 
print("✅ Insights automatici sui tuoi gusti generati")
print("✅ File PNG con analisi salvato")

print("\n🚀 DOMANI (Giorno 4): Web Scraping - Raccoglieremo dati REALI da Internet!")
print("Preparati con una lista di 5-10 film di cui vuoi analizzare le recensioni online!")
print("="*60)