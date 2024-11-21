def measure_time(N_values, method):
    times = []
    for N in N_values:
        A, b = create_matrix_and_vector(N)
        start_time = time.time()
        method(A, b, N)
        end_time = time.time()
        times.append(end_time - start_time)
    return times