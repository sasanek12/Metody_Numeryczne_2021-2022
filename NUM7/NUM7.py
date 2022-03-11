import numpy as np                  # Biblioteka numeryczna
import matplotlib.pyplot as plt     # Biblioteka do tworzenia wykresow
# Biblioteka pozwalajaca obsluge argumentow linii polecen
import sys


# Funkcja
def fun(x):
    return 1/(1+25*(x**2))


# Funkcja obliczająca węzły
def node(n):
    return [-1+2*i/n for i in range(n+1)]


# Faktoryzacja Cholesky'ego
def cholesky(n):
    n = n-1
    L = []
    d0 = [0]*n
    d1 = [0]*n
    L.append(d0)
    L.append(d1)

    for i in range(n):
        if(i==0):
            L[1][i] = 2
        else:
            L[0][i] = 1/L[1][i-1]
            L[1][i] = np.sqrt(4-L[0][1]**2)

    return L
  


# Interpolacja metodą splajnów kubicznych
def interpolate(n, arg):
    x = node(n)
    y = list(map(lambda a: fun(a), x))
    h = 2/n
    E = [0]*(n+1)

    L = cholesky(n)

    # Podstawianie w przód
    c = 6/(h**2)
    E[1]=(c*(y[0]-2*y[1]+y[2])/L[1][0])
    for i in range(2, n):
        E[i] = (c*(y[i-1]-2*y[i]+y[i+1]) - L[0][i-1]*E[i-1])/L[1][i-1]

    # Podstawiania w tył
    E[n-1] = E[n-1] / L[1][n-2]
    for i in range(n - 2, 0, -1):
        E[i] = (E[i] - L[0][i] * E[i + 1]) / L[1][i-1]

    y_new = []  
    
    # Obliczanie splajnów
    for a in arg:
        a=round(a, 14)
        for i in range(n):
            if(a>=x[i] and a<=x[i+1]):
                s = E[i]*((x[i+1]-a)**3)/(6*h)+E[i+1]*((a-x[i])**3)/(6*h)+(a-x[i])*((y[i+1]-y[i])/h - h*(E[i+1]-E[i])/6) + y[i]-(E[i]*(h**2))/6
                y_new.append(s)
                break

    return y_new


# Funkcja tworząca wykres przedstawiajacy interpolację dla różnej ilości węzłów
def showFunc(arg):
    plt.figure(figsize=(8, 8))
    plt.title('Interpolacja naturalnymi splajnami kubicznymi dla funkcji\n' r'$f(x)=\frac{1}{1+25x^2}$ i siatki $x_i=-1+2\frac{i}{n}$')
    plt.plot(arg, fun(arg), 'r', label='f(x)')
    plt.plot(arg, interpolate(5, arg), 'b', label=r'$S_5(x)$')
    plt.plot(arg, interpolate(6, arg), 'c', label=r'$S_6(x)$')
    plt.plot(arg, interpolate(8, arg), 'm', label=r'$S_8(x)$')
    plt.plot(arg, interpolate(10, arg), 'g', label=r'$S_{10}(x)$')
    plt.plot(arg, interpolate(75, arg), 'y', label=r'$S_{75}(x)$')
    plt.plot(arg, interpolate(200, arg), 'k', label=r'$S_{200}(x)$')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.legend()
    plt.show()


# Funckja pokazująca błąd interpolacji
def showErr(arg):
    x = node(10)
    plt.title('Błąd interpolacji splajnami kubicznymi')
    plt.plot(arg, abs(fun(arg)-interpolate(10, arg)), 'r')
    plt.plot(x, len(x)*[0], 'go', label='węzły interpolacji')
    plt.xlabel('x')
    plt.ylabel('$|f(x) - s(x)|$')
    plt.legend()
    plt.grid()
    plt.show()


def main():
    # Sprawdzenie ilosci argumentow
    if(len(sys.argv) != 2):
        print("Niepoprawna ilosc argumentow")
        sys.exit()

    x_new = np.arange(-1.0, 1.01, 0.01)
    
    # Wybor działania
    if(sys.argv[1] == 'wykres'):
        showFunc(x_new)
    elif(sys.argv[1] == 'error'):
        showErr(x_new)
    else:
        print("Zly argument")
        sys.exit()



if __name__ == "__main__":
    main()
