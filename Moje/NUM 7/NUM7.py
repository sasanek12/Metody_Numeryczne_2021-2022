import numpy as np
import matplotlib.pyplot as plt


# Definicja funkcji y(x)
def y(x):
    return 1 / (1 + 10 * x ** 2)


# Generowanie punktów
def generate_points(n):
    x = np.linspace(-1, 1, n + 1)  # Jednorodna siatka punktów
    y_values = y(x)
    return x, y_values


# Interpolacja wielomianowa metodą Lagrange'a
def lagrange_interpolation(x, y_values):
    def Wn(xi):
        result = 0
        n = len(x) - 1
        for i in range(n + 1):
            # Obliczanie wielomianu bazowego Li(x)
            Li = 1
            for j in range(n + 1):
                if i != j:
                    Li *= (xi - x[j]) / (x[i] - x[j])
            result += y_values[i] * Li
        return result

    return Wn


# Funkcja sklejana 3. stopnia
def cubic_spline(x, y_values):
    n = len(x) - 1
    h = x[1] - x[0]

    # Macierz trójdiagonalna i prawa strona do wyznaczenia momentów
    A = np.zeros((n + 1, n + 1))
    b = np.zeros(n + 1)

    # Warunki brzegowe (s''(x0) = s''(xn) = 0)
    A[0, 0] = 1
    A[n, n] = 1

    # Wypełnianie macierzy dla pozostałych równań
    for i in range(1, n):
        A[i, i - 1] = h / 6
        A[i, i] = h / 3
        A[i, i + 1] = h / 6
        b[i] = (y_values[i + 1] - y_values[i]) / h - (y_values[i] - y_values[i - 1]) / h

    # Rozwiązanie układu równań
    M = np.linalg.solve(A, b)

    # Funkcja sklejana
    def s(xi):
        for i in range(n):
            if x[i] <= xi <= x[i + 1]:
                # Obliczanie wartości funkcji sklejaną
                hi = x[i + 1] - x[i]
                A = (x[i + 1] - xi) / hi
                B = (xi - x[i]) / hi
                C = ((A ** 3 - A) * hi ** 2) / 6
                D = ((B ** 3 - B) * hi ** 2) / 6
                return A * y_values[i] + B * y_values[i + 1] + C * M[i] + D * M[i + 1]

    return s


# Porównanie wyników i wizualizacja
def compare_results(n):
    x, y_values = generate_points(n)
    Wn = lagrange_interpolation(x, y_values)
    spline = cubic_spline(x, y_values)

    # Punkty do rysowania dokładnego wykresu
    x_dense = np.linspace(-1, 1, 500)
    y_actual = y(x_dense)
    y_lagrange = [Wn(xi) for xi in x_dense]
    y_spline = [spline(xi) for xi in x_dense]

    # Wykresy
    plt.figure(figsize=(12, 6))

    # Funkcja oryginalna i interpolacje
    plt.subplot(2, 1, 1)
    plt.plot(x_dense, y_actual, label='y(x) (oryginalna)', color='black')
    plt.plot(x_dense, y_lagrange, label='Interpolacja wielomianowa $W_n(x)$', linestyle='--')
    plt.plot(x_dense, y_spline, label='Interpolacja sklejana $s(x)$', linestyle=':')
    plt.scatter(x, y_values, color='red', label='Węzły interpolacji')
    plt.legend()
    plt.title(f'Interpolacja dla n = {n}')

    # Różnice
    plt.subplot(2, 1, 2)
    plt.plot(x_dense, y_actual - y_lagrange, label='$y(x) - W_n(x)$', linestyle='--')
    plt.plot(x_dense, y_actual - y_spline, label='$y(x) - s(x)$', linestyle=':')
    plt.legend()
    plt.title('Różnice między funkcją oryginalną a interpolacjami')

    plt.tight_layout()
    plt.show()


# Przykładowe wykonanie
compare_results(5)  # Można zmieniać wartość n dla różnych punktów
