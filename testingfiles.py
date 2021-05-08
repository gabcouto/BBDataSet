import struct
estrArq2 = struct.Struct('15s I I f I I')
Arq2 = open("musicas.bin", "rb")
d= estrArq2.unpack(Arq2.read(36))
print(d)
d= estrArq2.unpack(Arq2.read(36))
print(d)
x = input()
Arq2.seek(36*(int(x)))
print(estrArq2.unpack(Arq2.read(36)))

for x in range(0,327388,1000):
    Arq2.seek(36*(int(x)))
    tu = estrArq2.unpack(Arq2.read(36))
    print(tu)
    print(type(tu))
    print(tu[1], type(tu[1]))
    # quero devolver uma tupla, e se nao for encontrado o artista/musica, devolver a tuple vazia.
    # Parece que não posso ter índice zero. Felippo.
for x in (0,2,3,4):
    print(x)
#012345678