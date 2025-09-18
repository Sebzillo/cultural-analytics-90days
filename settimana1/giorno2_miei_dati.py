# GIORNO 2: Python Ripasso + Database Culturale Personale
# Obiettivo: Creare il tuo dataset di film, libri e vinili preferiti

print("🎬📚🎵 GIORNO 2: I TUOI DATI CULTURALI")
print("=" * 50)

# PARTE 1: RIPASSO PYTHON CON FILM
print("PARTE 1: GESTIONE DATI FILM")
print("-" * 30)

# Liste - I tuoi film preferiti
film_preferiti = [
    "Il Padrino", "Citizen Kane", "Casablanca", "Vertigo", 
    "2001: Odissea nello Spazio", "Tokyo Story"
]

print("I miei film preferiti:")
for i, film in enumerate(film_preferiti, 1):
    print(f"{i}. {film}")

# Dizionari - Dati dettagliati sui film
film_dettagliati = {
    "Il Padrino": {
        "anno": 1972,
        "regista": "Francis Ford Coppola",
        "genere": "Crime Drama",
        "voto_personale": 10,
        "visto_volte": 5
    },
    "Citizen Kane": {
        "anno": 1941,
        "regista": "Orson Welles", 
        "genere": "Drama",
        "voto_personale": 9,
        "visto_volte": 3
    },
    "Vertigo": {
        "anno": 1958,
        "regista": "Alfred Hitchcock",
        "genere": "Thriller",
        "voto_personale": 9,
        "visto_volte": 4
    },
    "Casablanca": {
        "anno": 1942,
        "regista": "Michael Curtiz",
        "genere": "Drama/Romance",
        "voto_personale": 9,
        "visto_volte": 2
    },
    "2001: Odissea nello Spazio": {
        "anno": 1968,
        "regista": "Stanley Kubrick",
        "genere": "Sci-Fi",
        "voto_personale": 8,
        "visto_volte": 3
    },
    "Tokyo Story": {
        "anno": 1953,
        "regista": "Yasujirō Ozu",
        "genere": "Drama",
        "voto_personale": 9,
        "visto_volte": 1
    },
    "Amélie": {
        "anno": 2001,
        "regista": "Jean-Pierre Jeunet",
        "genere": "Romantic Comedy",
        "voto_personale": 8,
        "visto_volte": 2
    },
    "La La Land": {
        "anno": 2016,
        "regista": "Damien Chazelle",                                       
        "genere": "Musical",
        "voto_personale": 9,
        "visto_volte": 2
    },
    "Inception": {
        "anno": 2010,
        "regista": "Christopher Nolan",                     
        "genere": "Sci-Fi",
        "voto_personale": 9,
        "visto_volte": 3
    }
}

print("\nDettagli film:")
for titolo, info in film_dettagliati.items():
    print(f"🎬 {titolo} ({info['anno']}) - Regista: {info['regista']}")
    print(f"   Genere: {info['genere']} | Voto: {info['voto_personale']}/10")
    print()

# PARTE 2: ESPANSIONE A LIBRI
print("PARTE 2: AGGIUNGENDO I LIBRI")
print("-" * 30)

libri_preferiti = {
    "1984": {
        "autore": "George Orwell",
        "anno": 1949,
        "genere": "Dystopian Fiction",
        "pagine": 328,
        "voto_personale": 10,
        "letto_volte": 3
    },
    "Il Nome della Rosa": {
        "autore": "Umberto Eco",
        "anno": 1980,
        "genere": "Historical Mystery",
        "pagine": 536,
        "voto_personale": 9,
        "letto_volte": 2
    },
    "Cent'anni di solitudine": {
        "autore": "Gabriel García Márquez",
        "anno": 1967,
        "genere": "Magical Realism",
        "pagine": 417,
        "voto_personale": 9,
        "letto_volte": 1
    },
    "Il Piccolo Principe": {
        "autore": "Antoine de Saint-Exupéry",
        "anno": 1943,
        "genere": "Children's Literature",
        "pagine": 96,
        "voto_personale": 8,
        "letto_volte": 4
    },
    "Orgoglio e Pregiudizio": {
        "autore": "Jane Austen",
        "anno": 1813,
        "genere": "Romance",
        "pagine": 279,
        "voto_personale": 9,
        "letto_volte": 2
    },
    "Il Signore degli Anelli": {
        "autore": "J.R.R. Tolkien",             
        "anno": 1954,
        "genere": "Fantasy",
        "pagine": 1216,
        "voto_personale": 10,
        "letto_volte": 3
    },
    "La Divina Commedia": {
        "autore": "Dante Alighieri",
        "anno": 1320,
        "genere": "Epic Poetry",
        "pagine": 798,
        "voto_personale": 9,
        "letto_volte": 1
    },
    "Il Gattopardo": {
        "autore": "Giuseppe Tomasi di Lampedusa",
        "anno": 1958,
        "genere": "Historical Fiction",
        "pagine": 301,
        "voto_personale": 8,
        "letto_volte": 1
    },
    "Fahrenheit 451": {
        "autore": "Ray Bradbury",
        "anno": 1953,   
        "genere": "Dystopian Fiction",
        "pagine": 158,
        "voto_personale": 9,
        "letto_volte": 2
    }
}

print("I miei libri preferiti:")
for titolo, info in libri_preferiti.items():
    print(f"📚 {titolo} - {info['autore']} ({info['anno']})")
    print(f"   {info['pagine']} pagine | Voto: {info['voto_personale']}/10")
    print()

# PARTE 3: AGGIUNGENDO VINILI
print("PARTE 3: LA COLLEZIONE VINILI")
print("-" * 30)

vinili_collezione = {
    "The Dark Side of the Moon": {
        "artista": "Pink Floyd",
        "anno": 1973,
        "genere": "Progressive Rock",
        "prezzo_pagato": 25,
        "valore_stimato": 45,
        "condizioni": "VG+",
        "ascolti": 20
    },
    "Kind of Blue": {
        "artista": "Miles Davis",
        "anno": 1959,
        "genere": "Jazz",
        "prezzo_pagato": 35,
        "valore_stimato": 60,
        "condizioni": "NM",
        "ascolti": 15
    },
    "Abbey Road": {
        "artista": "The Beatles",
        "anno": 1969,
        "genere": "Rock",
        "prezzo_pagato": 40,
        "valore_stimato": 55,
        "condizioni": "VG+",
        "ascolti": 25
    },
    "Blue Train": {
        "artista": "John Coltrane",
        "anno": 1957,
        "genere": "Jazz",
        "prezzo_pagato": 30,
        "valore_stimato": 50,
        "condizioni": "NM",
        "ascolti": 10
    },
    "Rumours": {
        "artista": "Fleetwood Mac",
        "anno": 1977,
        "genere": "Rock",
        "prezzo_pagato": 20,
        "valore_stimato": 40,
        "condizioni": "VG+",
        "ascolti": 25
    },
    "Back to Black": {
        "artista": "Amy Winehouse",
        "anno": 2006,
        "genere": "Soul",
        "prezzo_pagato": 15,
        "valore_stimato": 30,
        "condizioni": "NM",
        "ascolti": 30
    },
    "The Wall": {
        "artista": "Pink Floyd",
        "anno": 1979,
        "genere": "Progressive Rock",
        "prezzo_pagato": 30,
        "valore_stimato": 50,
        "condizioni": "VG+",
        "ascolti": 18
    },
}
print("La mia collezione vinili:")
for titolo, info in vinili_collezione.items():
    profitto = info['valore_stimato'] - info['prezzo_pagato']
    print(f"🎵 {titolo} - {info['artista']} ({info['anno']})")
    print(f"   Pagato: €{info['prezzo_pagato']} | Valore: €{info['valore_stimato']} | Profitto: €{profitto}")
    print()

# PARTE 4: FUNZIONI PER ANALISI
print("PARTE 4: PRIME ANALISI")
print("-" * 30)

def analizza_collezione_film(film_dict):
    """Analizza la collezione di film"""
    anni = [info['anno'] for info in film_dict.values()]
    voti = [info['voto_personale'] for info in film_dict.values()]
    
    print(f"📊 ANALISI FILM:")
    print(f"   Numero film: {len(film_dict)}")
    print(f"   Anno più vecchio: {min(anni)}")
    print(f"   Anno più recente: {max(anni)}")
    print(f"   Voto medio: {sum(voti)/len(voti):.1f}")
    print()

def analizza_investimenti_vinili(vinili_dict):
    """Analizza gli investimenti in vinili"""
    investimento_totale = sum(info['prezzo_pagato'] for info in vinili_dict.values())
    valore_totale = sum(info['valore_stimato'] for info in vinili_dict.values())
    profitto_totale = valore_totale - investimento_totale
    
    print(f"💰 ANALISI INVESTIMENTI VINILI:")
    print(f"   Investimento totale: €{investimento_totale}")
    print(f"   Valore attuale: €{valore_totale}")
    print(f"   Profitto/Perdita: €{profitto_totale}")
    print(f"   ROI: {(profitto_totale/investimento_totale)*100:.1f}%")
    print()

# Eseguiamo le analisi
analizza_collezione_film(film_dettagliati)
analizza_investimenti_vinili(vinili_collezione)

# PARTE 5: PREPARAZIONE PER PANDAS
print("PARTE 5: PREPARAZIONE DATI PER PANDAS")
print("-" * 40)

# Convertiamo tutto in formato "flat" per Pandas
tutti_i_contenuti = []

# Aggiungi film
for titolo, info in film_dettagliati.items():
    tutti_i_contenuti.append({
        'titolo': titolo,
        'tipo': 'Film',
        'anno': info['anno'],
        'creatore': info['regista'],
        'genere': info['genere'],
        'voto': info['voto_personale'],
        'fruizioni': info['visto_volte']
    })

# Aggiungi libri
for titolo, info in libri_preferiti.items():
    tutti_i_contenuti.append({
        'titolo': titolo,
        'tipo': 'Libro',
        'anno': info['anno'],
        'creatore': info['autore'],
        'genere': info['genere'],
        'voto': info['voto_personale'],
        'fruizioni': info['letto_volte']
    })

# Aggiungi vinili
for titolo, info in vinili_collezione.items():
    tutti_i_contenuti.append({
        'titolo': titolo,
        'tipo': 'Vinile',
        'anno': info['anno'],
        'creatore': info['artista'],
        'genere': info['genere'],
        'voto': None,  # Non abbiamo voti per i vinili
        'fruizioni': info['ascolti']
    })

print("Dati preparati per Pandas:")
print(f"Totale contenuti culturali: {len(tutti_i_contenuti)}")
for contenuto in tutti_i_contenuti[:3]:  # Mostra primi 3
    print(f"   {contenuto['tipo']}: {contenuto['titolo']}")

print("\n🎯 PROSSIMO STEP: Domani trasformeremo questi dati in DataFrame Pandas!")
print("✅ GIORNO 2 COMPLETATO!")

# ESERCIZIO PER TE:
print("\n" + "="*50)
print("🏠 COMPITO A CASA:")
print("1. Modifica i dizionari con I TUOI film/libri/vinili preferiti")
print("2. Aggiungi almeno 2 film, 2 libri, 2 vinili tuoi")
print("3. Esegui il codice e vedi le TUE analisi personali")
print("4. Salva questo file come 'giorno2_miei_dati.py'")
print("="*50)