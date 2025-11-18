import numpy as np

# --- Entrada de Dados ---
x = np.array([0, 10, 20, 30, 40])
m1 = np.array([50.8, 86.2, 136, 72.8, 51])
m2 = np.array([113.6, 144.5, 185, 171.2, 95.3])

# Passo (h) - Como o espaçamento é constante, basta ver a distância entre os dois primeiros.

h = x[1] - x[0]

# Definir y (largura do rio em cada ponto)
y = m2 - m1 

# --- Regra dos Trapézios ---
# Fórmula: (h/2) * [y_0 + 2 * sum(y_meio) + y_n]

soma_meio = np.sum(y[1:-1])

area_trap = (h / 2) * (y[0] + 2 * soma_meio + y[-1])

# --- Regra de Simpson ---
# Fórmula: (h/3) * [y_0 + 4 * sum(y_ímpares) + 2 * sum(y_pares) + y_n]

# Índices ímpares (1, 3, 5...):
# Pula de 2 em 2 começando do índice 1 e exclui o último termo (y_n).
soma_impares = np.sum(y[1:-1:2]) 

# Índices pares (2, 4, 6...):
# Pula de 2 em 2 começando do índice 2 e exclui o último termo (y_n).
soma_pares = np.sum(y[2:-1:2])   

area_simpson = (h / 3) * (y[0] + 4 * soma_impares + 2 * soma_pares + y[-1])

# --- Resultados ---
print("\nResultados")
print("-" * 50)
print(f"\nÁrea aproximada (Regra dos Trapézios): {area_trap:.2f} m²")
print(f"Área aproximada (Regra de Simpson):  {area_simpson:.2f} m²\n")
print("-" * 50)