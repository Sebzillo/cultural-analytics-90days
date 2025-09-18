import pandas as pd
import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

print("🎬 Welcome to Cultural Data Analytics!")
print("=" * 40)

# Test 1: Pandas
print("✅ Test Pandas...")
films = pd.DataFrame({
    'titolo': ['Citizen Kane', 'Casablanca', 'Il Padrino'],
    'anno': [1941, 1942, 1972],
    'voto': [8.3, 8.5, 9.2]
})
print(films)
print()

# Test 2: Matplotlib
print("✅ Test Matplotlib...")
plt.figure(figsize=(8, 4))
plt.bar(films['titolo'], films['voto'])
plt.title('I Miei Film Preferiti')
plt.ylabel('Voto IMDb')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('test_grafico.png')
plt.show()
print("Grafico salvato come 'test_grafico.png'")
print()

# Test 3: Web Requests
print("✅ Test Web Scraping...")
try:
    response = requests.get('https://httpbin.org/json')
    if response.status_code == 200:
        print("✅ Connessione web OK!")
    else:
        print("❌ Problemi di connessione")
except Exception as e:
    print(f"❌ Errore: {e}")

print()
print("🚀 Setup completato! Sei pronto per l'avventura!")
print("=" * 40)