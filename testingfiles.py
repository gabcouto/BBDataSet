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
    print(estrArq2.unpack(Arq2.read(36)))

#012345678