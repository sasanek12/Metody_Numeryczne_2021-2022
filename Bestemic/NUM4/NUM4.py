import numpy as np                  # Tylko do testów
import matplotlib.pyplot as plt     # Biblioteka do tworzenia wykresow
import time

def check():
    A = np.ones((n, n))
    A += np.diag([9] * n)
    A += np.diag([7] * (n - 1), 1)

    start = time.time()
    np.linalg.solve(A, b)
    return time.time()-start

def sherman():
    M = []
    M.append([9]*n)
    M.append([7]*(n-1) + [0])

    start = time.time()

    # Backward subtitution dla obu równań
    z = [0]*n
    x = [0]*n
    z[n-1] = b[n-1] / M[0][n-1]
    x[n-1] = 1 / M[0][n-1]

    for i in range(n - 2, -1, -1):
        z[i] = (b[n-2] - M[1][i] * z[i+1]) / M[0][i]
        x[i] = (1 - M[1][i] * x[i+1]) / M[0][i]


    delta = sum(z)/(1+sum(x))

    # Wyliczenie wyniku
    y=[]
    for i in range(len(z)):
        y.append(z[i]-x[i]*delta)

    end = time.time()-start

    if(not test):
        print(y)
    else:
        return end

n = 50
test = False
b = [5]*n
sherman()



# TESTOWANIE CZASU
# test=True
# N = []
# num = []
# real = []
# for i in range(50, 8000, 150):
#     n=i
#     N.append(n)
#     b = [5]*n

#     num.append(check()*1000000)
#     real.append(sherman()*1000000)

# plt.grid(True)
# plt.title('Czas pracy programu')
# plt.xlabel('n')
# plt.ylabel('mikrosekundy')
# plt.yscale('log')

# plt.plot(N, num)
# plt.plot(N, real)
# plt.legend(['Czas pracy biblioteki Numpy', 'Czas pracy zaimplementowanego algorytmu'])
# plt.show()
