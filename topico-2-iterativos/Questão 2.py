def menu_principal():
    while(True):
        print("\n=== SOLUCIONADOR DE SISTEMAS LINEARES (GAUSS-SEIDEL) ===")
        print("1. Resolver o Problema da Treliça")
        print("2. Inserir um Novo Sistema Manualmente")
        print("3. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            CasoTrelica()
            
        elif escolha == '2':
            CasoManual()
            
        elif escolha == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")
            

def CasoTrelica():
    b = [
        500,  
        0,    
        0,   
        0,   
        100,  
        0,    
        0,    
        0,    
        0,    
        0     
    ]

    
    A = [
    #    F_AB,     F_AC,   F_BC,    F_BD,   F_CD,    F_CE,   F_DE,     R_Ax,  R_Ay,  R_Ey
        [-0.70711, 0,     -0.70711, 0,      0,       0,      0,        0,     0,     0    ], # Eq 3 (resolve F_AB)
        [0,       -1.0,   -0.70711, 0,      0.5,     1.0,    0,        0,     0,     0    ], # Eq 6 (resolve F_AC)
        [0,        0,      0.70711, 0,      0.86603, 0,      0,        0,     0,     0    ], # Eq 5 (resolve F_BC)
        [-0.70711, 0,      0.70711, 1.0,    0,       0,      0,        0,     0,     0    ], # Eq 4 (resolve F_BD)
        [0,        0,      0,       0,     -0.86603, 0,      -0.5,     0,     0,     0    ], # Eq 7 (resolve F_CD)
        [0,        0,      0,       0,      0,       -1.0,   -0.86603, 0,     0,     0    ], # Eq 10 (resolve F_CE)
        [0,        0,      0,      -1.0,   -0.5,     0,      0.86603,  0,     0,     0    ], # Eq 8 (resolve F_DE)
        [0.70711,  1.0,    0,       0,      0,       0,      0,        1.0,   0,     0    ], # Eq 1 (resolve R_Ax)
        [0.70711,  0,      0,       0,      0,       0,      0,        0,     1.0,   0    ], # Eq 2 (resolve R_Ay)
        [0,        0,      0,       0,      0,       0,      0.5,      0,     0,     1.0  ]  # Eq 9 (resolve R_Ey)
    ]

    nomes_incognitas = [
        "F_AB", "F_AC", "F_BC", "F_BD", "F_CD", 
        "F_CE", "F_DE", "R_Ax", "R_Ay", "R_Ey"
    ]

    print("Iniciando o método de Gauss-Seidel...")

    ResolveGaussSeidel(A,b,nomes_incognitas)

def ResolveGaussSeidel(A,b,nomes_incognitas):
    
    # Chute inicial (tudo zero)
    n = len(b)                     #conta a quantidade de equações no sistema                    
    F = [0.0] * n
    F_antigo = [0.0] * n

    # Parâmetros
    precisao = 0.0001 
    erro_maximo = 1.0              #apenas pro while funcionar, no inicio do codigo ele é zerado
    max_iteracoes = 1000
    iteracao = 0


    #pivotamento
    for (i) in range(n):
                pivo = A[i][i]                #coloca o termo a ser isolado no pivo

                if(abs(pivo)<0.0000001):      #se o pivo for muito proximo ou igual a zero... 
                    for (k) in range (i+1,n): #procura nas linhas abaixo e troca
                        if(abs(A[k][i])>abs(pivo)):
                            
                            temp = A[i]
                            A[i] = A[k]
                            A[k] = temp

                            temp = b[i]
                            b[i] = b[k]
                            b[k] = temp

    while erro_maximo > precisao and iteracao < max_iteracoes:

        erro_maximo = 0.0

        for (i) in range(n):
            F_antigo[i] = F[i] #guardo o resultado antigo
            
        for (i) in range(n): 
            soma = 0.0
            for (j) in range(n):
                if i!=j:            
                    soma = soma + A[i][j]*F[j]  # Soma os termos que não são da diagonal principal ja multiplicados pelos Chutes do vetor F

            F[i] = (b[i] - soma) / A[i][i] #isola o termo ja calculando e atualizando no vetor F para ser usado
                                          
        for (i) in range(n):
            erro_atual = abs(F[i] - F_antigo[i])
            if erro_atual > erro_maximo: #pega apenas o maior erro, se ele for menor que a precisao o programa acaba
                erro_maximo = erro_atual
            
        iteracao = iteracao + 1


    print(f"\nSolucao encontrada apos {iteracao} iteracoes:")
    print("-" * 30)
    for i in range(n):
        print(f"{nomes_incognitas[i]:5}: {F[i]:10.4f}")


def CasoManual():
    n = int(input("Quantas variaveis tem o sistema: "))
    A = []
    b = []
    nomes_incognitas = []
    
    #entrada de dados
    
    print(f"\nDigite os coeficientes da Matriz A ({n}x{n})")
    print("OBS: Digite os números separados por espaço (ex: 2.5 -1 0)")

    for (i) in range (n):
        entrada = input(f"Linha{i+1}: ").replace(",",".") # coloca a equação inteira e troca virgula por ponto
        linha = [float(x) for x in entrada.split()]         # separa cada valor digitado em um float num vetor

        A.append(linha)                    #adiciona o vetor a matriz
        nomes_incognitas.append(f"X{i+1}") #adiciona o nome a incognita

    print("\nDigite os termos independentes (Vetor b):")
    
    for (i)in range(n):
        val = float(input(f"Resultado da equação {i+1}: ").replace(",", "."))
        b.append(val)

    ResolveGaussSeidel(A, b, nomes_incognitas)
if __name__ == "__main__":
    menu_principal()