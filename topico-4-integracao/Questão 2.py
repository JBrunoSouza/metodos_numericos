import numpy as np

# --- 1. Entrada de Dados ---
x = np.array([0, 10, 20, 30, 40])
m1 = np.array([50.8, 86.2, 136, 72.8, 51])
m2 = np.array([113.6, 144.5, 185, 171.2, 95.3])

# Passo (h) - assumindo espaçamento constante
h = x[1] - x[0]

# Definir y (largura do rio em cada ponto)
# y será: [62.8, 58.3, 49.0, 98.4, 44.3]
y = m2 - m1 

# --- 2. Regra dos Trapézios (Implementação Manual) ---
# Fórmula: (h/2) * [y0 + 2*(soma do miolo) + yn]

# y[0]   -> Primeiro elemento
# y[-1]  -> Último elemento
# y[1:-1] -> "Miolo": pega do índice 1 até o penúltimo
soma_meio = np.sum(y[1:-1])

area_trap = (h / 2) * (y[0] + 2 * soma_meio + y[-1])


# --- 3. Regra de Simpson 1/3 (Implementação Manual) ---
# Fórmula: (h/3) * [y0 + 4*(soma índices ímpares) + 2*(soma índices pares) + yn]
# Nota: "Ímpares" e "Pares" se referem à posição no vetor (índice 1, 2, 3...), 
# desconsiderando o primeiro (0) e o último.

# Índices ímpares (1, 3, 5...):
# Start=1, Stop=-1 (antes do último), Step=2
soma_impares = np.sum(y[1:-1:2]) 

# Índices pares (2, 4, 6...):
# Start=2, Stop=-1 (antes do último), Step=2
soma_pares = np.sum(y[2:-1:2])   

area_simpson = (h / 3) * (y[0] + 4 * soma_impares + 2 * soma_pares + y[-1])

# --- 4. Resultados ---
print("\nResultados")
print("-" * 50)
print(f"\nÁrea aproximada (Regra dos Trapézios): {area_trap:.2f} m²")
print(f"Área aproximada (Regra de Simpson):  {area_simpson:.2f} m²\n")
print("-" * 50)