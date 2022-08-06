n1 = int(input('Digite um valor : '))
n2 = int(input('Digite outro valor: '))
operacao = 0

while operacao != 5:
    print('--'*21)
    print('''O Menu de Operações com esses 2 nùmeros:
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA''')
    operacao = int(input('Operação escolhida: '))
    if operacao == 1:
        print('--'*21)
        print('A SOMA entre {} e {} é igual a {}'.format(n1, n2, n1+n2))
        print('--'*21)
    elif operacao == 2:
        print('--'*21)
        print('A MULTIPLICAÇÃO entre {} e {} é igual a {}'.format(n1,n2,n1*n2))
        print('--'*21)
    elif operacao == 3:
        print('--'*21)
        if n2 > n1:
            print('O maior número é o número {}'.format(n2))
            print('--'*21)
        else:
            print('O maior número é o número {}'.format(n1))
            print('--'*21)
    elif operacao == 4:
        print('--'*21)
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o outro valor: '))
        print('--'*21)
print('--'*21)
print('Fim do Algoritmo.')