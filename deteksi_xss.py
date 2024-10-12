import requests
from urllib.parse import urlparse, parse_qs

# Meminta input URL dari pengguna
url = input("Masukkan URL target: ")

# Parse URL dan parameter
parsed_url = urlparse(url)
params = parse_qs(parsed_url.query)

# Memuat payload dari file
payloads = []
try:
    with open('xss_payloads.txt', 'r') as file:
        payloads = [line.strip() for line in file.readlines()]
except FileNotFoundError:
    print("File payload tidak ditemukan. Pastikan 'xss_payloads.txt' ada di direktori yang sama dengan skrip.")
    exit()

# Melakukan pengujian terhadap setiap payload
for key in params.keys():
    for payload in payloads:
        # Membuat salinan parameter dengan payload
        test_params = params.copy()
        test_params[key] = [payload]

        try:
            # Mengirim permintaan
            response = requests.get(parsed_url.scheme + '://' + parsed_url.netloc + parsed_url.path, params=test_params)
            # Memeriksa respons untuk indikasi kerentanan
            if payload in response.text:
                print(f"Kerentanan XSS mungkin ditemukan dengan payload: {payload}")
        
        except requests.exceptions.RequestException as e:
            print(f"Permintaan gagal: {e}")

print("Pengujian selesai.")
