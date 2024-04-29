import subprocess
import re

x = input("Podaj zakresy adresów IP (np. 192.168.0.0/24): ")

# Podzielenie adresu IP i maski sieciowej
adres_ip, maska = x.split("/")

# Zapisanie maski sieciowej
mask = maska

# Utworzenie polecenia nmap
polecenie = f"sudo nmap -sP -n {adres_ip}/{mask}"

print("Polecenie nmap:", polecenie)

# Wywołanie polecenia nmap i przechwycenie wyniku
wynik = subprocess.run(polecenie, shell=True, capture_output=True, text=True)

# Wyświetlenie wyniku
print("Output konsoli:")
print(wynik.stdout)

# Wyświetlenie błędów, jeśli wystąpiły
if wynik.stderr:
    print("Błąd konsoli:")
    print(wynik.stderr)

# Inicjalizacja listy adresów IP
ip = []

# Wyodrębnienie adresów IP z wyniku stdout
if wynik.stdout:
    # Wyrażenie regularne do wyszukiwania adresów IP w tekście
    regex = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"
    # Znalezienie wszystkich pasujących adresów IP w tekście
    adresy_ip = re.findall(regex, wynik.stdout)
    # Dodanie znalezionych adresów IP do listy
    for adres in adresy_ip:
        ip.append(adres)

# Wyświetlenie listy adresów IP
print("Lista adresów IP:")
for adres in ip:
    print(adres)

# Zapisanie adresów IP do pliku
with open("ips.txt", "w") as plik:
    for adres in ip:
        plik.write(adres + "\n")

print("Adresy IP zostały zapisane do pliku ips.txt")
