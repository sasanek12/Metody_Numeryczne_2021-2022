import numpy as np                  # Biblioteka numeryczna
import matplotlib.pyplot as plt     # Biblioteka do tworzenia wykresow
import sys                          # Biblioteka pozwalajaca obsluge argumentow linii polecen

# Funkcja liczaca pochodna w przod
def pochodna_przod(system, funkcja, punkt, h):
    return system((funkcja(punkt + h) - funkcja(punkt)) / h)

# Funkcja liczaca pochodna centralna
def pochodna_centralna(system, funkcja, punkt, h):
    return system((funkcja(punkt + h) - funkcja(punkt - h)) / (2 * h))

# Funkcja obliczajaca blad miedzy pochodna wyliczona numerycznie a rzeczywista wartoscia pochodnej
def blad(system, pochodna, funkcja, punkt, h, df):
    return np.absolute(pochodna(system, funkcja, punkt, h) - df)

# Funkcja rysujaca wykres w skali logarytmicznej
def wykres():
    plt.grid(True)
    plt.title('Blad przyblizenia pochodnej funkcji cos(x) w punkcie')
    plt.xlabel('h')
    plt.ylabel("$|D_hf - f'|$")
    plt.loglog(h, blad(system, pochodna_przod, funkcja, punkt, h, df))
    plt.loglog(h, blad(system, pochodna_centralna, funkcja, punkt, h, df))
    plt.legend(['Pochodna w przod', 'Pochodna centralna'])
    plt.savefig(name)

# Funkcja wypisujaca bledy
def wypisz_blad():
    p = blad(system, pochodna_przod, funkcja, punkt, h, df)
    c = blad(system, pochodna_centralna, funkcja, punkt, h, df)

    print("Blad ze wzoru w przod")
    print('{0:20} - {1}'.format('h', 'blad'))
    for x in range(miejsca):
        print(
            '{0:20.{2}f} - {1:.{2}f}'.format(h[x], p[x], np.absolute(precyzja)))

    print("\nWyniki ze wzoru centralnego")
    print('{0:20} - {1}'.format('h', 'blad'))
    for x in range(miejsca):
        print(
            '{0:20.{2}f} - {1:.{2}f}'.format(h[x], c[x], np.absolute(precyzja)))


#### Main ####

# Sprawdzenie ilosci argumentow
if(len(sys.argv) != 3):
    print("Niepoprawna ilosc argumentow")
    sys.exit()

# Wybor dokladnosci
if(sys.argv[1] == 'float'):
    system = np.float32
    precyzja = -7
    name = 'wykres_f.svg'
elif(sys.argv[1] == 'double'):
    system = np.float64
    precyzja = -16
    name = 'wykres_d.svg'
else:
    print("Zly argument")
    sys.exit()

# Zmienne z wartosciami pomocniczymi
punkt = 0.3
miejsca = 250
h = system(np.logspace(precyzja, 0, num = miejsca))     # Funkcja zwraca tablice liczb rozlozonnych rownomiernie w skali logarytmicznej z zadanego zakresu
df = system(-1*(np.sin(punkt)))                         # Dokladna pochodna funkcji
funkcja = np.cos

# Wybor dzialania programu
if(sys.argv[2] == 'wykres'):
    wykres()
elif(sys.argv[2] == 'blad'):
    wypisz_blad()
else:
    print("Zly argument")
    sys.exit()
