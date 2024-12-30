'''
Davi Guedes
30/12/2024
For Loop (IF & ELSE)
'''
#Enviar um email COM OS DETALHES da compra online {no maximo 3 tentativas} para compras confirmadass !

compra_confirmada = False
dados_compra= 'Compra no valor de R$12.50 Confirmada'


for enviar in  range(3):
    if compra_confirmada:
        print(dados_compra)
        print('Detalhes da compra enviados no email.')
        break
else:
    print('Falha na compra')
