def fibonacci(n):
    """
    Genera una lista de los primeros n números de Fibonacci.
    
    :param n: El número de términos de Fibonacci a generar.
    :return: Una lista con los primeros n números de Fibonacci.
    """
    fib_sequence = []
    a, b = 1, 2
    while len(fib_sequence) < n:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Ejemplo de uso
print(fibonacci(10))  # Imprime los primeros 10 números de Fibonacci
