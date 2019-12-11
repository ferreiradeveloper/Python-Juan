# Creando un diccionario simple
cancion = {
    'artista' : 'Metallica', #llave y valor
    'cancion' : 'Enter Sadman',
    'lanzamiento' : 1992,
    'like' : 5000
}

print(cancion)

# acceder a los elementos del diccionario
print(cancion['artista'])
print(cancion['lanzamiento'])

# mezclar con un string
musica = cancion['cancion']
artista = cancion['artista']

print(f'Estoy escuchando {musica} de {artista}')

# agregar new values
cancion['playlist'] = 'Heavy Metal'
print(cancion)

# modificar valores
cancion['cancion'] = 'Seek & Destroy'
print(cancion)

# eliminando elementos
del cancion['lanzamiento']
print(cancion)
