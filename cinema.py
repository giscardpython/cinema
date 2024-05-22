escolha = 1
tentativas = 1

# entrada de dados
nome = input('Informe o nome:\n')
idade = int(input('Informe a idade:\n'))

# verifica a sala
while escolha > 0 and tentativas <= 5:
    print ("Lista de Filmes\n")
    print('Sala 1 - A Volta dos Que Não Foram - classificação indicativa: 18.')
    print('Sala 2 - A Roda Quadrada - classificação indicativa: 14.')
    print('Sala 3 - Poeira em Alto Mar - classificação indicativa: 16.')
    print('Sala 4 - As Tranças do Rei Careca - classificação indicativa: 18.')
    print('Sala 5 - A Vingança do Peixe Frito - classificação indicativa: 16.')

    sala = int(input('\nEscolha a sala desejada (1 a 5):\n'))
    
    match sala:
        case 1:
            classificacao_indicativa = 18
            print (f'{nome}, que tem {idade} anos, escolheu a Sala 1 - A Volta dos Que Não Foram - classificação indicativa: {classificacao_indicativa}.')
        case 2:
            classificacao_indicativa = 14
            print (f'{nome}, que tem {idade} anos, escolheu a Sala 2 - A Roda Quadrada - classificação indicativa: {classificacao_indicativa}.')
        case 3:
            classificacao_indicativa = 0
            print (f'{nome}, que tem {idade} anos, escolheu a Sala 3 - Poeira em Alto Mar - classificação indicativa: Livre.')
        case 4:
            classificacao_indicativa = 18
            print (f'{nome}, que tem {idade} anos, escolheu a Sala 4 - As Tranças do Rei Careca - classificação indicativa: {classificacao_indicativa}.')
        case 5:
            classificacao_indicativa = 16
            print (f'{nome}, que tem {idade} anos, escolheu a Sala 5 - A Vingança do Peixe Frito - classificação indicativa: {classificacao_indicativa}')

    if (idade >= classificacao_indicativa):
        print (f'Impressao do ingresso para {nome} - Sala {sala}')
        escolha = 0
        tentativas = 6
    else:
        print (f'Você não tem a idade mínima para assistir o filme na Sala {sala}. Escolha outra sala de cinema!!!\n')
        tentativas = tentativas + 1

    



