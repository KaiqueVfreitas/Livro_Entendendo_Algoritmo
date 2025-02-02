## Usar a recursão favorece o desempenho do programador enquanto coda, usar loops favorece o desempenho do programa 

def fatorial_recursivo(numero:  int) -> int:
    for i in range(numero-1, 0, -1):
        numero *= fatorial_recursivo(i)
    return numero

def fatorial_iterativo(numero:  int) -> int:
    for i in range(numero-1, 0, -1):
        numero *= i
        
    return numero

valor_digitado = int(input("Digite um número: "))
print(fatorial_recursivo(valor_digitado))
print("\n")
print(fatorial_iterativo(valor_digitado))