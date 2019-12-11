# Operadores and y or
user_loged = True
user_admin = True

if user_loged and user_admin:
    print('Administrador')


if user_loged or user_admin:
    print('se cumplio una al menos')