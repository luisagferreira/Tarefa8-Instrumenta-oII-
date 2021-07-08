# Luísa Gonçalves Ferreira

numero=int(input("Digite um número para calcular seu fatorial: "))
if numero>=0 and numero<20:
    contador = numero
    fatorial = 1
    print('O valor de {}! é: '.format(numero), end='')
    while contador > 0:
        print('{}'.format(contador), end='')
        if contador > 1:
            print('x', end='')
        else:
            print('=', end='')
        fatorial = fatorial * contador
        contador= contador- 1
    print('{}'.format(fatorial), end='')
else:
    print("Entrada não permitida!")