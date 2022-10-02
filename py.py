from random import choice
e = 0 #Empate
v = 0 #Vitória
d = 0 #Derrota
while True:
    #INTERFACE
    print(31 * '=')
    print('   JOGO PEDRA, PAPEL TESOURA')
    print(31 * '=')
    
    #PERGUNTA
    oponentes = ['PEDRA', 'PAPEL', 'TESOURA']
    C = choice(oponentes)
    R = str(input('Faça sua escolha [PEDRA, PAPEL, TESOURA]:')).upper()
    if C  == 'PEDRA' and R == 'PEDRA':
        print('Deu empate ambos jogaram PEDRA')
        e = e + 1
    if C == 'PAPEL' and R == 'PAPEL':
        print('Deu empate ambos jogaram PAPEL')
        e = e + 1
    if C == 'TESOURA' and R == 'TESOURA':
        print('Deu empate ambos jogaram TESOURA')
        e = e + 1
 
    #COMPUTADOR GANHA
    if C == 'TESOURA' and R == 'PAPEL':
        print(f'Você perdeu, o computador jogou TESOURA')
        d = d + 1
    if C == 'PEDRA' and R == 'TESOURA':
        print('você perdeu, o computador jogou PEDRA')
        d = d + 1
    if C == 'PAPEL' and R == 'PEDRA':
        print('você perdeu, o computador jogou PAPEL')
        d = d + 1
    
    #JOGADOR GANHA
    if R == 'PAPEL' and C == 'PEDRA':
        print('Você ganhou, o computador jogou PEDRA')
        v = v + 1
    if R == 'PEDRA' and C == 'TESOURA':
        print('você ganhou, o computador jogou TESOURA')
        v = v + 1
    if R == 'TESOURA' and C == 'PAPEL':
        print('você ganhou, o computador jogou PAPEL')
        v = v + 1
        
    print(f'Vitórias: {v}')
    print(f'Derrotas: {d}')
    print(f'Empates: {e}')
    
    if R == 'PEDRA' or R == 'PAPEL' or R =='TESOURA':
        print('')
    else:
        print('Você digitou algo errado')
        print(' ')
