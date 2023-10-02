proibidas = ['assediada', 'assedio']
texto = ('motorista muito bom mas me senti assediada nunca mais usarei o serviço')

resultado =  'assediada' in proibidas

if resultado:
    print('reclamação atendida')
    autorizacaoMotorista = False