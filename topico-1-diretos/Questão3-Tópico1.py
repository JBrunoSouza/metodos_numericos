import numpy as np

# Classe de cores para o terminal 
class Cores:
    RESET = '\033[0m'       # Reseta a formatação
    NEGRITO = '\033[1m'     # Negrito
    VERMELHO = '\033[91m'   # Vermelho claro
    VERDE = '\033[92m'     # Verde claro
    AMARELO = '\033[93m'   # Amarelo claro
    AZUL = '\033[94m'      # Azul claro
    MAGENTA = '\033[95m'  # Magenta claro
    CIANO = '\033[96m'     # Ciano claro

# Configuração da biblioteca NumPy
np.set_printoptions(suppress=True, precision=4)

def eliminacao_gauss(A, b):
    """
    Resolve um sistema linear Ax = b usando o Método de Eliminação de Gauss
    com pivotação parcial para estabilidade numérica.
    """
    n = len(b)
    
    # Cria a matriz aumentada [A|b]
    Ab = np.hstack([A.astype(float), b.astype(float).reshape(-1, 1)])
    
    print(f"\n{Cores.CIANO}--- Matriz Aumentada Inicial [A|b] ---{Cores.RESET}")
    print(np.around(Ab, 4)) 

    # --- Fase 1: Eliminação (Triangulação) ---
    print(f"\n{Cores.CIANO}--- Iniciando Fase de Eliminação ---{Cores.RESET}")
    for i in range(n):
        # Pivotação Parcial
        max_row = i
        for k in range(i + 1, n):
            if abs(Ab[k, i]) > abs(Ab[max_row, i]):
                max_row = k
        
        # Troca a linha
        Ab[[i, max_row]] = Ab[[max_row, i]]
        if i != max_row:
            print(f"{Cores.MAGENTA}Pivotação: Trocando Linha {i+1} com Linha {max_row+1}{Cores.RESET}")
            print(np.around(Ab, 4))

        # Trata sistema singular
        if Ab[i, i] == 0.0:
            raise ValueError("Sistema não tem solução única (matriz singular).")

        # Zera os elementos abaixo do pivô
        for j in range(i + 1, n):
            multiplicador = Ab[j, i] / Ab[i, i]
            Ab[j, :] = Ab[j, :] - multiplicador * Ab[i, :]
            # Aplica cor amarela aos passos de cálculo
            print(f"{Cores.AMARELO}L{j+1} = L{j+1} - ({round(multiplicador, 4)}) * L{i+1}{Cores.RESET}")

        print(np.around(Ab, 4))

    print(f"\n{Cores.CIANO}--- Matriz Triangular Superior [U|c] ---{Cores.RESET}")
    print(np.around(Ab, 4))

    # --- Fase 2: Retrosubstituição ---
    print(f"\n{Cores.CIANO}--- Iniciando Fase de Retrosubstituição ---{Cores.RESET}")
    x = np.zeros(n)

    for i in range(n - 1, -1, -1):
        soma = 0.0
        for j in range(i + 1, n):
            soma += Ab[i, j] * x[j]
        
        x[i] = (Ab[i, n] - soma) / Ab[i, i]
        # Aplica cor verde aos cálculos da solução
        print(f"x[{i+1}] = ({round(Ab[i, n], 4)} - {round(soma, 4)}) / {round(Ab[i, i], 4)} = {round(x[i], 4)}{Cores.RESET}")

    return x

def main_problema_minas():
    """
    (c) Encontra a solução do sistema linear com os dados do problema.
    """
    print(f"{Cores.AZUL}{Cores.NEGRITO}{'='*60}{Cores.RESET}")
    print(f"{Cores.AZUL}{Cores.NEGRITO}  RESOLVENDO O PROBLEMA DAS MINAS (TÓPICO 01 - QUESTÃO 3){Cores.RESET}")
    print(f"{Cores.AZUL}{Cores.NEGRITO}{'='*60}{Cores.RESET}")
    
    """
    (a)  Apresenta o problema na forma de um sistema de equações lineares.
    """
    print(f"\n{Cores.CIANO}--- (a) Modelagem do Sistema Linear ---{Cores.RESET}")
    print("Definindo: x1 = Mina 1, x2 = Mina 2, x3 = Mina 3")
    print("Equações (por material):")
    print(f" 0.55*x1 + 0.25*x2 + 0.25*x3 = 4800   (Areia){Cores.RESET}")
    print(f" 0.30*x1 + 0.45*x2 + 0.20*x3 = 5800   (Cascalho Fino){Cores.RESET}")
    print(f" 0.15*x1 + 0.30*x2 + 0.55*x3 = 5700   (Cascalho Grosso){Cores.RESET}")
    
    
    A = np.array([
        [0.55, 0.25, 0.25],  # Areia
        [0.30, 0.45, 0.20],  # Cascalho Fino
        [0.15, 0.30, 0.55]   # Cascalho Grosso
    ])
    b = np.array([4800, 5800, 5700])

    try:
        solucao = eliminacao_gauss(A, b)
        
        print(f"\n{Cores.CIANO}{Cores.NEGRITO}--- (c) Solução do Problema das Minas ---{Cores.RESET}")
        print(f"A quantidade de metros cúbicos (m³) a ser minerada é:{Cores.RESET}")
        print(f"{Cores.VERDE}  Mina 1 (x1): {solucao[0]:.2f} m³{Cores.RESET}")
        print(f"{Cores.VERDE}  Mina 2 (x2): {solucao[1]:.2f} m³{Cores.RESET}")
        print(f"{Cores.VERDE}  Mina 3 (x3): {solucao[2]:.2f} m³{Cores.RESET}")
    
    except ValueError as e:
        print(f"\n{Cores.VERMELHO}{Cores.NEGRITO}Erro ao resolver o sistema: {e}{Cores.RESET}")

def main_generico():
    """
    (b) Programa capaz de resolver problemas semelhantes.
    """
    print(f"\n{Cores.AZUL}{Cores.NEGRITO}{'='*60}{Cores.RESET}")
    print(f"{Cores.AZUL}{Cores.NEGRITO}   Calculadora de Sistemas Lineares (Método de Gauss){Cores.RESET}")
    print(f"{Cores.AZUL}{Cores.NEGRITO}{'='*60}{Cores.RESET}")
    try:
        n = int(input("Digite o número de equações (e variáveis) do novo sistema: "))
        if n <= 0:
            print(f"{Cores.VERMELHO}O número deve ser positivo.{Cores.RESET}")
            return

        A = np.zeros((n, n))
        b = np.zeros(n)

        print(f"\n{Cores.CIANO}--- Entrada da Matriz de Coeficientes (A) ---{Cores.RESET}")
        for i in range(n):
            for j in range(n):
                A[i, j] = float(input(f"Digite o coeficiente A[{i+1}][{j+1}]: "))

        print(f"\n{Cores.CIANO}--- Entrada do Vetor de Constantes (b) ---{Cores.RESET}")
        for i in range(n):
            b[i] = float(input(f"Digite a constante b[{i+1}]: "))

        solucao = eliminacao_gauss(A, b)
        
        print(f"\n{Cores.CIANO}{Cores.NEGRITO}--- Solução do Sistema (x) ---{Cores.RESET}")
        for i in range(n):
            print(f"{Cores.VERDE}  x[{i+1}]: {round(solucao[i], 4)}{Cores.RESET}")
    
    except ValueError:
        print(f"{Cores.VERMELHO}{Cores.NEGRITO}Erro na entrada de dados. Por favor, insira apenas números.{Cores.RESET}")
    except Exception as e:
        print(f"{Cores.VERMELHO}{Cores.NEGRITO}Ocorreu um erro inesperado: {e}{Cores.RESET}")


# --- Bloco de Execução Principal ---
if __name__ == "__main__":
    
    main_problema_minas()
    
    while True:
        print(f"\n{Cores.AZUL}{'='*60}{Cores.RESET}")
        print("Opções do Programa:")
        print("1: Resolver um novo sistema de equações")
        print("2: Sair do programa")
        escolha = input("Digite sua escolha (1 ou 2): ")

        if escolha == '1':
            main_generico()
        elif escolha == '2':
            print(f"\n{Cores.CIANO}Encerrando o programa!{Cores.RESET}")
            break
        else:
            print(f"{Cores.VERMELHO}Escolha inválida. Por favor, digite 1 ou 2.{Cores.RESET}")
