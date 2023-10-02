import random
numeroSorteado = random.randint( 1, 10)
#print(numeroSorteado)
chute = int(input("qual seu chute de 1 a 10?"))
if chute == numeroSorteado:
    print('parabéns acertou!!!!!!!')
else:
    print('errooooouuu!!!!')
