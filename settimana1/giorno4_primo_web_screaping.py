# GIORNO 4: WEB SCRAPING - Raccogliere Dati Reali da Internet!
# Obiettivo: Scrappare dati cinematografici reali da IMDb

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import re

print("🌐 GIORNO 4: WEB SCRAPING MASTERCLASS")
print("=" * 60)
print("Oggi raccoglieremo dati REALI da internet!")
print("=" * 60)

# STEP 1: Test di connessione
print("\nSTEP 1: TEST DI CONNESSIONE")
print("-" * 40)

def test_connessione():
    """Testa se possiamo connetterci a internet"""
    try:
        response = requests.get('https://httpbin.org/json', timeout=5)
        if response.status_code == 200:
            print("✅ Connessione internet OK!")
            return True
        else:
            print("❌ Problemi di connessione")
            return False
    except Exception as e:
        print(f"❌ Errore connessione: {e}")
        return False

# Testa connessione
if not test_connessione():
    print("⚠️ Controlla la tua connessione internet e riprova")
    exit()

# STEP 2: Primo scraping semplice - Quotes to Scrape (per imparare)
print("\nSTEP 2: PRIMO SCRAPING (TRAINING)")
print("-" * 40)
print("Iniziamo con un sito semplice per imparare...")

def scrape_quotes_training():
    """Scraping di training su quotes.toscrape.com"""
    url = "http://quotes.toscrape.com/"
    
    try:
        # Fai la richiesta
        response = requests.get(url)
        print(f"📡 Richiesta a {url}")
        print(f"📊 Status Code: {response.status_code}")
        
        if response.status_code == 200:
            # Parse dell HTML
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Trova tutte le citazioni
            quotes = soup.find_all('div', class_='quote')
            print(f"🎯 Trovate {len(quotes)} citazioni!")
            
            # Estrai dati
            dati_citazioni = []
            for quote in quotes[:3]:  # Solo prime 3 per test
                testo = quote.find('span', class_='text').text
                autore = quote.find('small', class_='author').text
                dati_citazioni.append({
                    'citazione': testo,
                    'autore': autore
                })
            
            # Mostra risultati
            print("\n📚 PRIME 3 CITAZIONI ESTRATTE:")
            for i, cit in enumerate(dati_citazioni, 1):
                print(f"{i}. \"{cit['citazione'][:50]}...\" - {cit['autore']}")
            
            return True
        else:
            print("❌ Errore nella richiesta")
            return False
            
    except Exception as e:
        print(f"❌ Errore: {e}")
        return False

# Esegui training
if scrape_quotes_training():
    print("✅ Training scraping completato!")
else:
    print("❌ Problemi nel training - verifica connessione")

# STEP 3: Preparazione per IMDb
print("\nSTEP 3: PREPARAZIONE SCRAPING IMDB")
print("-" * 40)

def cerca_film_imdb(titolo_film):
    """Cerca un film su IMDb e restituisce URL e dati base"""
    
    # Headers per simulare un browser vero
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        # URL di ricerca IMDb
        search_url = f"https://www.imdb.com/find?q={titolo_film.replace(' ', '+')}&ref_=nv_sr_sm"
        
        print(f"🔍 Cercando '{titolo_film}' su IMDb...")
        response = requests.get(search_url, headers=headers)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Trova primo risultato film
            result = soup.find('td', class_='result_text')
            if result:
                link = result.find('a')
                if link:
                    film_url = "https://www.imdb.com" + link.get('href')
                    titolo_completo = link.text
                    print(f"✅ Trovato: {titolo_completo}")
                    print(f"🔗 URL: {film_url}")
                    return film_url, titolo_completo
                
        print(f"❌ Film '{titolo_film}' non trovato")
        return None, None
        
    except Exception as e:
        print(f"❌ Errore nella ricerca: {e}")
        return None, None

def estrai_dati_film_imdb(film_url):
    """Estrae dati dettagliati da una pagina film IMDb"""
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        print(f"📊 Estraendo dati da: {film_url}")
        response = requests.get(film_url, headers=headers)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Estrai titolo
            titolo = "N/A"
            titolo_elem = soup.find('h1')
            if titolo_elem:
                titolo = titolo_elem.text.strip()
            
            # Estrai voto IMDb
            voto = "N/A"
            voto_elem = soup.find('span', class_='sc-bde20123-1')
            if voto_elem:
                voto = voto_elem.text.strip()
            
            # Estrai anno
            anno = "N/A"
            anno_elem = soup.find('a', href=re.compile(r'/year/'))
            if anno_elem:
                anno = anno_elem.text.strip()
            
            # Estrai generi
            generi = []
            generi_elems = soup.find_all('a', href=re.compile(r'/search/title/.*genres='))
            for elem in generi_elems:
                generi.append(elem.text.strip())
            
            dati_film = {
                'titolo': titolo,
                'anno': anno,
                'voto_imdb': voto,
                'generi': ', '.join(generi) if generi else 'N/A',
                'url': film_url
            }
            
            print(f"✅ Dati estratti per: {titolo}")
            return dati_film
            
        else:
            print(f"❌ Errore HTTP: {response.status_code}")
            return None
            
    except Exception as e:
        print(f"❌ Errore estrazione: {e}")
        return None

# STEP 4: Scraping dei tuoi film
print("\nSTEP 4: SCRAPING DEI TUOI FILM")
print("-" * 40)

# I TUOI FILM DA ANALIZZARE (SOSTITUISCI CON I TUOI!)
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
    "after hours",
]

print("🎬 FILM DA ANALIZZARE:")
for i, film in enumerate(film_da_analizzare, 1):
    print(f"{i}. {film}")

print(f"\n🚀 Iniziamo lo scraping di {len(film_da_analizzare)} film...")

# Lista per raccogliere tutti i dati
dati_tutti_film = []

for film in film_da_analizzare:
    print(f"\n{'='*50}")
    print(f"🎯 ANALIZZANDO: {film}")
    print('='*50)
    
    # Cerca film
    url, titolo_completo = cerca_film_imdb(film)
    
    if url:
        # Estrai dati
        dati = estrai_dati_film_imdb(url)
        if dati:
            dati_tutti_film.append(dati)
            print(f"✅ {film} completato!")
        else:
            print(f"❌ Errore estrazione dati per {film}")
    else:
        print(f"❌ {film} non trovato")
    
    # Pausa cortese tra richieste
    print("⏳ Pausa di cortesia...")
    time.sleep(2)

# STEP 5: Risultati finali
print("\n" + "="*60)
print("🎉 SCRAPING COMPLETATO!")
print("="*60)

if dati_tutti_film:
    print(f"✅ Dati raccolti per {len(dati_tutti_film)} film!")
    
    # Crea DataFrame
    df_film = pd.DataFrame(dati_tutti_film)
    print("\n📊 DATASET FINALE:")
    print(df_film.to_string())
    
    # Salva in CSV
    df_film.to_csv('film_scraped_imdb.csv', index=False)
    print("\n💾 Dati salvati in 'film_scraped_imdb.csv'")
    
    # Statistiche rapide
    print(f"\n📈 STATISTICHE RAPIDE:")
    print(f"• Film analizzati: {len(df_film)}")
    if 'voto_imdb' in df_film.columns:
        voti_numerici = pd.to_numeric(df_film['voto_imdb'], errors='coerce')
        voti_validi = voti_numerici.dropna()
        if len(voti_validi) > 0:
            print(f"• Voto IMDb medio: {voti_validi.mean():.1f}")
            print(f"• Voto più alto: {voti_validi.max()}")
            print(f"• Voto più basso: {voti_validi.min()}")
    
else:
    print("❌ Nessun dato raccolto - verifica connessione e titoli film")

print("\n🚀 PROSSIMO STEP: Organizzeremo tutto su GitHub!")
print("✅ GIORNO 4 - PARTE 1 COMPLETATA!")
print("="*60)