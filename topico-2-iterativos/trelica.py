b = [
    500,  # Eq 3 (Originalmente linha 2)
    0,    # Eq 6 (Originalmente linha 5)
    0,    # Eq 5 (Originalmente linha 4)
    0,    # Eq 4 (Originalmente linha 3)
    100,  # Eq 7 (Originalmente linha 6)
    0,    # Eq 10 (Originalmente linha 9)
    0,    # Eq 8 (Originalmente linha 7)
    0,    # Eq 1 (Originalmente linha 0)
    0,    # Eq 2 (Originalmente linha 1)
    0     # Eq 9 (Originalmente linha 8)
]

# 'A' reordenada para ter uma diagonal não-zero
A = [
  #  F_AB,  F_AC,  F_BC,   F_BD,   F_CD,   F_CE,   F_DE,   R_Ax,  R_Ay,  R_Ey
    [-0.707, 0,     -0.707, 0,      0,      0,      0,      0,     0,     0    ], # Eq 3 (resolve F_AB)
    [0,      1.0,   -0.707, 0,      0.5,    1.0,    0,      0,     0,     0    ], # Eq 6 (resolve F_AC)
    [0,      0,      0.707, 0,      0.866,  0,      0,      0,     0,     0    ], # Eq 5 (resolve F_BC)
    [-0.707, 0,      0.707, 1.0,    0,      0,      0,      0,     0,     0    ], # Eq 4 (resolve F_BD)
    [0,      0,      0,      0,     -0.866, 0,      -0.5,   0,     0,     0    ], # Eq 7 (resolve F_CD)
    [0,      0,      0,      0,      0,     -1.0,   -0.866, 0,     0,     0    ], # Eq 10 (resolve F_CE)
    [0,      0,      0,     -1.0,   -0.5,   0,      0.866,  0,     0,     0    ], # Eq 8 (resolve F_DE)
    [0.707,  1.0,    0,      0,      0,      0,      0,      1.0,   0,     0    ], # Eq 1 (resolve R_Ax)
    [0.707,  0,      0,      0,      0,      0,      0,      0,     1.0,   0    ], # Eq 2 (resolve R_Ay)
    [0,      0,      0,      0,      0,      0,      0.5,    0,     0,     1.0  ]  # Eq 9 (resolve R_Ey)
]

nomes_incognitas = [
    "F_AB", "F_AC", "F_BC", "F_BD", "F_CD", 
    "F_CE", "F_DE", "R_Ax", "R_Ay", "R_Ey"
]

# --- 2. O ALGORITMO DE GAUSS-SEIDEL ---

print("Iniciando o método de Gauss-Seidel...")

# Chute inicial (tudo zero)
F = [0.0] * 10
F_antigo = [0.0] * 10

# Parâmetros
precisao = 0.0001 
erro_maximo = 1.0  #apenas pro while funcionar, no inicio do codigo ele é zerado
max_iteracoes = 1000
iteracao = 0

# ax + soma  = constante                     -> normal
# x = [(constante) - (soma)] / a             -> isolando no codigo

while erro_maximo > precisao and iteracao < max_iteracoes:

    erro_maximo = 0.0

    for (i) in range(10):
        F_antigo[i] = F[i] #guardo o resultado antigo
        
    for (i) in range(10): 
        soma = 0.0
        for (j) in range(10):
            if i!=j:            
                soma = soma + A[i][j]*F[j]  #multiplica cada mults da matriz pelo chute de resultado do vetor F -> (x{})


        F[i] = (b[i] - soma) / A[i][i] #isola o termo ja calculando e atualizando no vetor F para ser usado
                                        #bug-> o programa iria bugar se caso a gente tentasse isolar um termo na equaçao e aquele termo nem existe ali, nao faz sentido
                                        # para isso temos que ter certeza que o termo que queremos isolar existe na equação, logo a diagonal principal NUNCA sao 0
    for (i) in range(10):
        erro_atual = abs(F[i] - F_antigo[i])
        if erro_atual > erro_maximo: #pega apenas o maior erro, se ele for menor que a precisao o programa acaba
            erro_maximo = erro_atual
        
    iteracao = iteracao + 1
       
print(f"\nSolucao encontrada apos {iteracao} iteracoes:")
print("-" * 30)
for i in range(10):

    # Para imprimir "F_AB: 750.0" em vez de "Índice 0: 750.0"
    print(f"{nomes_incognitas[i]:5}: {F[i]:10.4f}")