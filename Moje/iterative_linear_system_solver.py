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