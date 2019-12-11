#sample with elif
ocupa = 'Jubilado'

if ocupa == 'Estudiante':
    print(' Tienes 50% de Descuento')
elif ocupa == 'Jubilado':
    print(' Tienes 75% de Descuento')
elif ocupa == 'Desempleado':
    print(' Tienes 10% de Descuento')
else:
    print(' Debes pagar el 100%')
