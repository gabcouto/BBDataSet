# edição em arquivo binário
# Descobrir quantos bytes tem cada instância de cada um dos dois arquivos.
# Agora preciso pensar como vai ser meu arquivo de índice, de tal forma que consiga:
#   1) Recuperar as informações
#   2) Facilitar pro Felippo a exibição em ordem alfabética.
#   Como que vou pesquisar por índice?
#   gerador de índices?
#   ter um arquivo de índices ordenado?
#   Deixar pro Felippo a parte dos índices.
#   ter índices ordenados para cada uma das exibições que vamos querer ter.

import struct


# Arquivo 1 - Entidade Artista e Melhor Semana
estrArq1 = struct.Struct('15s I s s s I I')

 # Arquivo 2 - Entidade Músicas
estrArq2 = struct.Struct('15s I I f I I')

musica1 = (bytes("Girl Like Me", 'utf-8'),67,12,9.87,0,1)
packed_data = estrArq2.pack(*musica1)

unpacked_data = estrArq2.unpack(packed_data)
print('Unpacked Values:', unpacked_data)
print(unpacked_data[0])
# unpacked_data[0] = unpacked_data[0].decode('utf-8')
# print('Unpacked Values:', unpacked_data)
print(unpacked_data[0].decode('utf-8'))


f = open("demofile2.txt", "ab")
f.write(packed_data)
f.close()


f = open("demofile2.txt", "rb")
d = f.read()
fileout = estrArq2.unpack(d)
print(fileout)

print(fileout[0].decode('utf-8'))

# print(f.read())

# struct.unpack_from(format, /, buffer, offset=0)
# Unpack from buffer starting at position offset, according to the format string format. The result is a tuple even if it contains exactly one item. The buffer’s size in bytes, starting at position offset, must be at least the size required by the format, as reflected by calcsize().