"""
a1 = input('digite o nome:')
a2 = input('digite o nome:')
a3 = input('digite o nome:')
"""
lista = ['ana', 'joão', 'maria']
existe = 'ana' in lista
print(existe)
print('#'* 10)

# --------------
bairro = ['Copa', 'Botafogo', 'Gloria']
existe = input('digite o bairro:').title()
resultado = existe in bairro
if resultado:
    print('bairro cadastrado')
else:
    print('bairro não cadastrado')
print(resultado)