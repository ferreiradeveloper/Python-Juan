#if en Python 
#  revisar si una condición es mayor a
balance = 500
if balance > 0:
    print('puedes pagar')
else:
    print('no tiene suficiente saldo')

# Likes
likes = 200
if likes == 200:
    print('Excelente, 200 Likes')

# if con texto
leng = 'Python'
if leng == 'Python':
    print('Excelente decisión')

leng = 'PHP'
if not leng == 'Python':
    print('deberias estudiar Python')

#Evaluar un Boolean
user_authen = True

if user_authen: # == True
    print('Access to the system')
else:
    print('Access Denied')
    
#Evaluar un elemento de una Lista
lenguajes = ['Python','R','c#','JavaScript','PHP']
if 'PHP' in lenguajes:
    print('Esta')
else:
    print ('No esta')

#if anidados
user_authen = True
user_admin = True

if user_authen:
    if user_admin:
        print('Acceso Total')
    else:
        print('Acceso al Sistema')
else:
    print('debes iniciar sesión')
