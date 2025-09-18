# GIORNO 4: WEB SCRAPING ROBUSTO - Versione che Funziona!
# Strategia: Usiamo API pubbliche + scraping alternativo

import requests
import pandas as pd
import json
import time

print("🚀 WEB SCRAPING ROBUSTO - I tuoi film!")
print("=" * 60)

# I TUOI FILM
film_da_analizzare = [
    "the godfather",
    "full metal jacket", 
    "shining",
    "2001 A Space Odyssey",
    "apocalypse now",
    "blade runner",
    "the big lebowski",
    "fight club",
    "inception",
    "once upon a time in america",
    "taxi driver",
    "after hours"
]

print(f"🎬 Analizzeremo {len(film_da_analizzare)} film:")
for i, film in enumerate(film_da_analizzare, 1):
    print(f"{i:2}. {film}")

# METODO 1: OMDb API (gratuita, affidabile)
print(f"\n{'='*60}")
print("METODO 1: OMDb API (più affidabile)")
print("="*60)

def get_film_data_omdb(titolo):
    """Ottiene dati film da OMDb API (gratuita)"""
    
    # API key gratuita di esempio - funziona per pochi test
    api_key = "trilogy"  # Puoi registrarti per una tua key su omdbapi.com
    base_url = "http://www.omdbapi.com/"
    
    params = {
        'apikey': api_key,
        't': titolo,
        'type': 'movie'
    }
    
    try:
        print(f"🔍 Cercando: {titolo}")
        response = requests.get(base_url, params=params, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            
            if data.get('Response') == 'True':
                film_info = {
                    'titolo': data.get('Title', 'N/A'),
                    'anno': data.get('Year', 'N/A'),
                    'voto_imdb': data.get('imdbRating', 'N/A'),
                    'generi': data.get('Genre', 'N/A'),
                    'regista': data.get('Director', 'N/A'),
                    'attori': data.get('Actors', 'N/A')[:100] + '...' if len(data.get('Actors', '')) > 100 else data.get('Actors', 'N/A'),
                    'trama': data.get('Plot', 'N/A')[:150] + '...' if len(data.get('Plot', '')) > 150 else data.get('Plot', 'N/A')
                }
                print(f"✅ Trovato: {film_info['titolo']} ({film_info['anno']})")
                return film_info
            else:
                print(f"❌ Non trovato: {data.get('Error', 'Errore sconosciuto')}")
                return None
        else:
            print(f"❌ Errore HTTP: {response.status_code}")
            return None
            
    except Exception as e:
        print(f"❌ Errore: {e}")
        return None

# RACCOGLIAMO I DATI
print(f"\n🚀 Iniziamo la raccolta dati...")
dati_film_raccolti = []

for film in film_da_analizzare:
    print(f"\n{'-'*50}")
    
    # Prova con OMDb
    dati = get_film_data_omdb(film)
    
    if dati:
        dati_film_raccolti.append(dati)
        print(f"📊 Voto IMDb: {dati['voto_imdb']}")
    else:
        print(f"⚠️ Saltiamo '{film}' - prova manualmente con titolo esatto")
    
    # Pausa cortese
    time.sleep(1)

# RISULTATI
print(f"\n{'='*60}")
print("🎉 RACCOLTA COMPLETATA!")
print("="*60)

if dati_film_raccolti:
    print(f"✅ Dati raccolti per {len(dati_film_raccolti)} film!")
    
    # Crea DataFrame
    df = pd.DataFrame(dati_film_raccolti)
    
    # Mostra risultati
    print(f"\n📊 I TUOI FILM ANALIZZATI:")
    print("-"*80)
    for _, film in df.iterrows():
        print(f"🎬 {film['titolo']} ({film['anno']})")
        print(f"   📊 IMDb: {film['voto_imdb']} | 🎭 {film['generi']}")
        print(f"   🎬 Regista: {film['regista']}")
        print()
    
    # Salva in CSV
    df.to_csv('i_miei_film_analizzati.csv', index=False)
    print("💾 Salvato in 'i_miei_film_analizzati.csv'")
    
    # STATISTICHE SUI TUOI GUSTI
    print(f"\n📈 ANALISI DEI TUOI GUSTI:")
    print("-"*40)
    
    # Voti numerici
    voti_numerici = pd.to_numeric(df['voto_imdb'], errors='coerce')
    voti_validi = voti_numerici.dropna()
    
    if len(voti_validi) > 0:
        print(f"🏆 Voto medio dei tuoi film: {voti_validi.mean():.1f}")
        print(f"🥇 Film con voto più alto: {voti_validi.max()}")
        print(f"📉 Film con voto più basso: {voti_validi.min()}")
        
        # Film migliore
        idx_migliore = voti_numerici.idxmax()
        if pd.notna(idx_migliore):
            film_migliore = df.iloc[idx_migliore]
            print(f"🎯 Il tuo film meglio valutato: {film_migliore['titolo']} ({film_migliore['voto_imdb']})")
    
    # Decenni
    anni_numerici = pd.to_numeric(df['anno'], errors='coerce')
    anni_validi = anni_numerici.dropna()
    if len(anni_validi) > 0:
        print(f"🕰️ Range temporale: {int(anni_validi.min())}-{int(anni_validi.max())}")
        
        # Decade preferita
        decenni = (anni_validi // 10) * 10
        decade_preferita = decenni.mode().iloc[0] if len(decenni.mode()) > 0 else None
        if decade_preferita:
            print(f"📅 La tua decade preferita: {int(decade_preferita)}s")
    
    # Registi ricorrenti
    registi = df['regista'].value_counts()
    if len(registi) > 0:
        print(f"🎬 Regista che hai scelto più volte: {registi.index[0]}")

else:
    print("❌ Nessun film trovato. Possibili soluzioni:")
    print("1. Controlla la connessione internet")
    print("2. Prova con titoli inglesi più precisi")
    print("3. Registrati per API key gratuita su omdbapi.com")

print(f"\n✅ GIORNO 4 - PARTE 1 COMPLETATA!")
print("🔥 Hai fatto il tuo primo web scraping con dati REALI!")
print("🚀 Prossimo: Organizziamo tutto su GitHub!")
print("="*60)

# BONUS: Crea un piccolo report
if dati_film_raccolti:
    print(f"\n🎨 BONUS: IL TUO REPORT CINEMATOGRAFICO")
    print("="*60)
    
    with open('report_cinematografico.txt', 'w') as f:
        f.write("🎬 IL MIO REPORT CINEMATOGRAFICO\n")
        f.write("="*50 + "\n\n")
        f.write(f"Film analizzati: {len(dati_film_raccolti)}\n")
        if len(voti_validi) > 0:
            f.write(f"Voto medio: {voti_validi.mean():.1f}\n")
        f.write("\nFILM NEL DETTAGLIO:\n")
        f.write("-"*30 + "\n")
        
        for _, film in df.iterrows():
            f.write(f"\n🎬 {film['titolo']} ({film['anno']})\n")
            f.write(f"Voto IMDb: {film['voto_imdb']}\n")
            f.write(f"Generi: {film['generi']}\n")
            f.write(f"Regista: {film['regista']}\n")
            f.write(f"Trama: {film['trama']}\n")
            f.write("-"*30 + "\n")
    
    print("📄 Report salvato in 'report_cinematografico.txt'")
    print("👀 Aprilo per vedere l'analisi completa dei tuoi film!")