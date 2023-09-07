from time import sleep
x = int(input('Digite o primeiro valor: '))
y = int(input('Digite o segundo valor: '))
o = 0
soma = 0
while o != 5:
    print('''[1]Somar
      [2]Multiplicar
      [3]Maior
      [4]Novos Números
      [5]Sair do Programa''')
    
    o = int(input('Qual a sua opção: '))
    

    if(o == 1):
        soma = x + y
        print(soma)
    elif(o == 2):
        multi = x * y
        print(multi)
    elif(o == 3):
        if(x > y):
            print(f'O número {x} é maior que {y}')
        else:
            print(f'O número {y} é maior que {x}')
    elif(o == 4):
        print('Digite os novos números: ')
        x = int(input('Digite o primeiro valor: '))
        y = int(input('Digite o segundo valor: '))
    elif(o == 5):
        print('Finalizando...')
        sleep(1)
        break
    else:
        print('Opção invalida! Tente Novamente!')
print('Programa finalizado!!!')
    

