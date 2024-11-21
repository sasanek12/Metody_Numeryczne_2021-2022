import numpy as np
import matplotlib.pyplot as plt
import time


def create_matrix_and_vector(N):
    A = np.ones((N, N), dtype=np.float64)
    np.fill_diagonal(A, 5)
    np.fill_diagonal(A[:, 1:], 3)
    b = np.full(N, 2, dtype=np.float64)
    return A, b


def jacobi(A, b, N, max_iterations=500, tolerance=1e-12):
    x = np.zeros_like(b, dtype=np.float64)
    iteration = 0
    while iteration < max_iterations:
        x_new = np.zeros_like(x, dtype=np.float64)
        for i in range(N):
            s1 = np.dot(A[i, :i], x[:i])
            s2 = np.dot(A[i, i + 1:], x[i + 1:])
            x_new[i] = (b[i] - s1 - s2) / A[i, i]
        if np.linalg.norm(x_new - x) < tolerance:
            break
        x = x_new
        iteration += 1
    return x


def gauss_seidel(A, b, N, max_iterations=500, tolerance=1e-12):
    x = np.zeros_like(b, dtype=np.float64)
    iteration = 0
    while iteration < max_iterations:
        x_new = np.copy(x)
        for i in range(N):
            s1 = np.dot(A[i, :i], x_new[:i])
            s2 = np.dot(A[i, i + 1:], x[i + 1:])
            x_new[i] = (b[i] - s1 - s2) / A[i, i]
        if np.linalg.norm(x_new - x) < tolerance:
            break
        x = x_new
        iteration += 1
    return x


def measure_time(N_values, method):
    times = []
    for N in N_values:
        A, b = create_matrix_and_vector(N)
        start_time = time.time()
        method(A, b, N)
        end_time = time.time()
        times.append(end_time - start_time)
    return times


N_values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 120, 150, 200, 250, 300, 350, 400]

jacobi_times = measure_time(N_values, jacobi)
gauss_seidel_times = measure_time(N_values, gauss_seidel)

plt.plot(N_values, jacobi_times, label='Metoda Jacobiego')
plt.plot(N_values, gauss_seidel_times, label='Metoda Gaussa-Seidela')
plt.xlabel('Wymiar N')
plt.ylabel('Czas (s)')
plt.yscale('log')
plt.legend()
plt.title('Czas rozwiązania w funkcji wymiaru N dla metod Jacobiego i Gaussa-Seidela')
plt.grid(True)
plt.show()