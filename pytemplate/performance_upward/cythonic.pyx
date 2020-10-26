import cython


def prime_eratosthenes(int num):
    cdef:
        int i, j
        list prime_list, num_list

    prime_list = []
    num_list = []

    for i in range(2, num + 1):
        if i not in num_list:
            prime_list.append(i)
            for j in range(i * i, num + 1, i):
                num_list.append(j)

    return prime_list
