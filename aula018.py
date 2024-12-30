'''
30/12/24
Davi Guedes
For Loop - Nested Loops
'''
# == For Loop Nested ==
    #Outer Loop
    #   Inner Loop

for numero1 in range(1,6):
    print('Produto' + str(numero1))
    for numero2 in range(5):
        print(numero1, numero2)
    