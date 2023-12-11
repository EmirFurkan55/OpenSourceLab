import requests

url = "https://api.artic.edu/api/v1/artworks"

# Sayfa numarası ve limit parametreleri
params = {
    "page": 1,  # Örnek olarak sayfa numarası 1
    "limit": 1  # Örnek olarak 1 eser limit
}

# API'ye GET isteği gönderin
response = requests.get(url, params=params)

# Yanıtın JSON formatında olduğunu kontrol edin ve ekrana yazdırın
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Hata: {response.status_code}")
    print(response.text)







