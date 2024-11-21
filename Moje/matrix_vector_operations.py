def create_matrix_and_vector(N):
    A = np.ones((N, N), dtype=np.float64)
    np.fill_diagonal(A, 5)
    np.fill_diagonal(A[:, 1:], 3)
    b = np.full(N, 2, dtype=np.float64)
    return A, b