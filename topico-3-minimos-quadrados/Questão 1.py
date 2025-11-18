import numpy as np
import matplotlib.pyplot as plt

#DADOS DA TABELA
X = np.array([1971, 1972, 1974, 1978, 1982, 1986, 1989, 1993, 1997, 1999, 2000])

n_transistores = np.array([2250, 3300, 6000, 29000, 134000, 275000, 1200000, 3100000, 7500000, 9500000, 42000000])

# A Lei de Moore cresce exponencialmente.
# Se aplicarmos log10 dos dois lados, viramos uma reta: log10(N) = M*ano + C

Y = np.log10(n_transistores)

# n = Quantidade de pontos (amostras) que temos.

n = len(X)

# Cálculo dos somatórios necessários para o método dos mínimos quadrados

sum_X = np.sum(X)                                # Soma de todos os anos
sum_Y = np.sum(Y)                                # Soma de todos os log(transistores)
sum_XX = np.sum(X**2)                            # Soma dos anos ao quadrado (necessário para a inclinação)
sum_XY = np.sum(X * Y)                           # Soma do produto X*Y (correlaciona ano com transistor)

# Montagem do Sistema Linear
# |   n      sum_X  |   | C |     | sum_Y  |
# | sum_X    sum_XX | * | M |  =  | sum_XY |

A = np.array([[n, sum_X],
            [sum_X, sum_XX]])

B = np.array([sum_Y, sum_XY])

try:
    #Resolução do Sistema Linear
    coeficientes = np.linalg.solve(A, B)

    # Extrai os coeficientes C (linear) e M (angular)
    C = coeficientes[0]
    M = coeficientes[1]

    print("\n--- Coeficientes ---")
    print(f"M (coeficiente angular): {M:.4f}")
    print(f"C (coeficiente linear): {C:.4f}\n")
    
    print("--- Funções ---")
    print(f"Função Linear: log10(N) = ({M:.4f} * ano) + ({C:.4f})")
    print(f"Função Exponencial: N(ano) = 10^(({M:.4f} * ano) + ({C:.4f}))\n")

    anos_previsao = np.array([2010, 2020])

    #Calcular o valor na escala logarítmica (na reta)
    y_log_previsto = M * anos_previsao + C

    #Revertendo o logaritmo
    n_previsto = 10**y_log_previsto

    print("--- Transistores 2010 e 2020 ---")
    print(f"Previsão de transistores para {anos_previsao[0]}: {n_previsto[0]:,.0f}")
    print(f"Previsão de transistores para {anos_previsao[1]}: {n_previsto[1]:,.0f}\n")

    # Configurações do gráfico
    plt.figure(figsize=(10, 6))
    plt.scatter(X, Y, label='Dados da Tabela (log10)', color='blue')
    x_linha = np.array([X.min(), anos_previsao.max()]) 
    y_linha = M * x_linha + C
    plt.plot(x_linha, y_linha, 'r-', label='Linha de Regressão (Modelo)')
    plt.scatter(anos_previsao, y_log_previsto, color='red', marker='o', s=150, 
                zorder=5, label='Previsões (2010, 2020)')   
    plt.xlabel('Ano')
    plt.ylabel('log10(Número de Transistores)')
    plt.title('Lei de Moore')
    plt.legend() 
    plt.grid(True) 
    
    plt.show() # Exibe o gráfico

except np.linalg.LinAlgError:

    print("Não foi possível resolver o sistema!")