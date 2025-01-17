import sys
import locale

sys.stdout.reconfigure(encoding='utf-8')

def is_fibonacci(number):
    a, b = 0, 1
    while b <= number:
        if b == number:
            return True
        a, b = b, a + b
    return False

try:
    number = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
    if is_fibonacci(number):
        print(f"O número {number} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {number} não pertence à sequência de Fibonacci.")
except ValueError:
    print("Por favor, insira um número inteiro válido.")
