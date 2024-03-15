# Calculo de IMC - Índice de Massa Corporal 

'''
Qual é a sua Altura em cm:
Qual é o seu peso em km:
'''

# MENOR QUE 18,5 MAGREZA 
# ENTRE 18,5 E 24,9 NORMAL 
# ENTRE 25,0 E 29,9 SOBRPESO 
# ENTRE 30,0 E 39,9 OBESIDADE 
# MAIOR QUE 40,0    OBESIDADE GRAVE 

altura = float(input('Qual é a sua altura em cm?'))
peso = float(input('Qual é o seu peso em Km?'))

IMC = peso / (altura/100)**2
    
if IMC < 18.5: 
    print('MAGREZA' )
elif IMC >= 18.5 and IMC < 24.9: 
    print('NORMAL' )
elif IMC >= 25.0 and IMC < 29.9: 
    print('SOBRPESO' )
elif IMC >= 30.0 and IMC < 39.9:
    print('OBESIDADE')
else:
    print('OBESIDADE GRAVE' )
