from typing import Tuple
import struct
'''
class TrieNode(object):
    def __init__(self, char: str):
        self.char = char
        self.children = []
        # No fim do titulo, o ID`!= 0
        self.word_finished = 0

def add(root, word: str, id):
    node = root
    for char in word:
        found_in_child = False
        # Procura proxima letra nos filhos do nodo
        for child in node.children:
            if child.char == char:
                # faz a operação com o filho caso tenha achado
                node = child
                found_in_child = True
                break
        # Não encontrou o filho = proxima letra do titulo, então cria novo nodo
        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)
            node = new_node
    # Chegou no final bota o iD
    # Caso tenham 2 músicas de nome igual, coloca um 0 no fim do nome da ultima q chegou
    # e adiciona como se fosse nome0
    if node.word_finished == 0:
        node.word_finished = id
    else:
        add(node, "0", id)


def allids(root, arq):
        node = root
        # Se n tem mais filho, bota no arquivo a musica do id e retorna 0 pq trabalho com recursão aqui
        if not root.children:
            arq.seek(0,2) #pra n perder informação devido a recução da função
            arq.write(bytes(node.word_finished))##############################################################################
            #deleta o nodo pq ele é folha e n vai mais ser usado
            del node
            return 0
        # Defini oq seria uma ordem alfabética aqui, talvez possam ser tirados alguns simbolos pra melhor eficiencia################
        for char in "0123456789 AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'!#$%&\()*+,-./:;<=>?@[\\]_{|}":
            char_not_found = True
            # Procura por todos os filhos se tem o digito da vez
            for child in node.children:
                if child.char == char:
                    # Achamo
                    char_not_found = False
                    # Procura todas as palavras q esse filho pode ter
                    allids(child, arq)
                    # break pq n da pra ter 2 nodos filhos com o mesmo valor
                    break
        # Se tem id, coloca no arquivo a musica dele
        # Esse é o caso de have um palavra "dentro" de outra
        if node.word_finished > 0:
            arq.seek(0,2)
            arq.write(bytes(node.word_finished))##############################################################################
        del node
        return 0
'''
'''
#fazer vetor de 100 pointers para a class TrieNode
class TriePointer(object):
    def __init__(self, chave):
        self.chave = chave
        self.pointsto = TrieNode('*')
        self.proximo = None
'''
'''
def insereTrie(self, titulo:str ,chave, id):
    if self.chave==chave:   #se a chave é a msm do primeiro só adiciona a musica na trie
        add(self.pointsto, titulo, id)
    else:
        while self.proximo != None: #procura o lugar onde deve ser inserido
            if self.proximo.chave <= chave:
                self = self.proximo
        if self.chave!=chave:   #se n tiver a trie com a chave, cria ela
            trieaux=TriePointer(1)
            trieaux.proximo = self.proximo
            self.proximo = trieaux
            trieaux.chave = chave
            add(trieaux.pointsto, titulo, id)
        else:
            add(self.pointsto, titulo, id)

def allidspointer(self, arq):
    allids(self.pointsto, arq)
    if self.proximo != None:
        allidspointer(self.proximo, arq)

def prefixo0(node): #-> list[]:
    PossiveisIDS = []
    for child in node.children:
        if child.char == "0":
            PossiveisIDS = prefixo0(child)
    return PossiveisIDS.append(node.word_finished)

def find_prefix(root, prefix: str):
    #Procura se tem a musica na arvore
    node = root
    # Caso n tenha nenhum filho, já retorna falso
    if not root.children:
        return 0
    for char in prefix:
        char_not_found = True
        # Vai percorrendo os filhos até achar
        for child in node.children:
            if child.char == char:
                # Achamo a proxima letra.
                char_not_found = False
                # começa a procurar nessa letra
                node = child
                break
        # Não achou
        if char_not_found:
            return 0
    # Achou, mas pode ser q tenham outras iguais no filho 0
    
    #id=prefixo0(node, False)
            
    return node.word_finished

#inicializações do método em memória
peakranks = TriePointer(1)
wobsongs = TriePointer(1)
wobartists = TriePointer(1)
notasongs = TriePointer(1)
notaartista = TriePointer(1)
aparicoesartist = TriePointer(1)
SongTitles = TrieNode('*')
ArtistNames = TrieNode('*')

#Inserções do método em memória
#insereTrie(peakranks, nome da musica, valorpeakrank, iddamusica)
#insereTrie(wobsongs, nome da musica, valorwob, iddamusica)
#insereTrie(wobartists, nome do artista, valorwobart, iddoartista)
#insereTrie(notasongs, nome da musica, valornotas, iddamusica)
#insereTrie(notaartista, nome do artista, valornotaa, iddoartista)
#insereTrie(aparicoesartist, nome do artista, aparaicoes, iddoartista)
#add(SongTitles, nome da musica, iddamusica)
#add(ArtistNames, nome do artista, iddoartista)

#Passar pra arquivo do método em memória
#ARQpointer = open(ARQpeakA, ab)#####################################
#allidspointer(peakranks, ARQpointer)
#ARQpointer.close()####################################################
##### igual os outros

#IDtitulos = open (musica_titulo, ab)##################################
#allids(SongTitles)
#IDtitulos.close()#####################################################

#IDnomes = open(nome_artista, ab)######################################
#allids(ArtistNames)
#IDnomes.close()####################################################
'''

###############################################Metodo em arquivo#######################################

#cria structs
IDsint = struct.Struct('I I')
IDsintaux = IDsint
sizeofstructint = 8
'''
    struct(){
        int id;
        int prox;
    }
'''
IDsstr = struct.Struct('180s I I')
sizeofstructstr = 190
'''
#cria arquivos com 100 structs nulas
ARQtitulos = "indices_titulos.bin"
ARQtreverso = "indices_reversos_titulos.bin"
ARQM = open(ARQtitulos, 'ab')
ARQMR = open(ARQtreverso, 'ab')
ARQnomes = "indices_nomes.bin"
ARQnreverso = "indices_reversos_nomes.bin"
ARQA = open(ARQnome, 'ab')
ARQAR = open(ARQnreverso, 'ab')
ARQpeakA = "indices_pr_artistas.bin"
ARQ0 = open(ARQpeakA, 'ab')
ARQpeakM = "indices_pr_musicas.bin"
ARQ1 = open(ARQpeakM, 'ab')
ARQwobA = "indices_wob_artistas.bin"
ARQ2 = open(ARQwobA, 'ab')
ARQwobM = "indices_wob_musicas.bin"
ARQ3 = open(ARQwobM, 'ab')
ARQnotasA = "indices_notas_artistas.bin"
ARQ4 = open(ARQnotasA, 'ab')
ARQnotasM = "indices_notas_musicas.bin"
ARQ5 = open(ARQnotasM, 'ab')

for i in range(0, 128): #128 pra alfabetico dar 100%
    ARQM.write(IDsstr.pack(bytes("}", 'utf-8'), 0, 0))
    ARQMR.write(IDsstr.pack(bytes(chr(0), 'utf-8'), 0, 0))
    ARQA.write(IDsstr.pack(bytes("}", 'utf-8'), 0, 0))
    ARQAR.write(IDsstr.pack(bytes(chr(0), 'utf-8'), 0, 0))
    ARQ0.write(IDsintaux.pack(0, 0))
    ARQ1.write(IDsintaux.pack(0, 0))
    ARQ2.write(IDsintaux.pack(0, 0))
    ARQ3.write(IDsintaux.pack(0, 0))
    ARQ4.write(IDsintaux.pack(0, 0))
    ARQ5.write(IDsintaux.pack(0, 0))
ARQM.close()
ARQMR.close()
ARQA.close()
ARQAR.close()
ARQ0.close()
ARQ1.close()
ARQ2.close()
ARQ3.close()
ARQ4.close()
ARQ5.close()
'''

#adiciona nomes em ordem alfabética em um arquivo de indices
def addcolstr (arq, id, word:str):
    #vai pro lugar do arquivo onde começa as palavras com o mesmo primeiro dígito
    arq.seek((ord(word[0])-1)*sizeofstructstr)
    Listastruct = list(IDsstr.unpack(arq.read(sizeofstructstr)))
    Listastruct[0] = Listastruct[0].decode('utf-8')
    #print(Listastruct)
    #enquanto está apontando para algo, vá para esse algo
    while Listastruct[0]<word:
        if Listastruct[2]==0:
            break
        arq.seek(Listastruct[2])
        Listastruct = list(IDsstr.unpack(arq.read(sizeofstructstr)))
        Listastruct[0] = Listastruct[0].decode('utf-8')
    arq.seek(-sizeofstructstr, 1)

    while Listastruct[0]>=word:
        if Listastruct[2]==0: #colocar na penultima posição
            aux=arq.tell()
            arq.seek(0,2)
            aux2 = arq.tell()
            arq.seek(aux)
            #print(arq.tell(), word, id, aux2)
            arq.write(IDsstr.pack(bytes(word, 'utf-8'), id, aux2))
            arq.seek(0,2)
            Listastruct[0] = bytes(Listastruct[0], 'utf-8')
            arq.write(IDsstr.pack(*Listastruct))
            arq.seek(0)
            return 0
        arq.write(IDsstr.pack(bytes(word, 'utf-8'), id, Listastruct[2]))
        arq.seek(Listastruct[2])
        word = Listastruct[0]
        id = Listastruct[1]
        Listastruct = list(IDsstr.unpack(arq.read(sizeofstructstr)))
        Listastruct[0] = Listastruct[0].decode('utf-8')
        arq.seek(-sizeofstructstr, 1)

#adiciona nomes em ordem alfabetica reversa em um arquivo de string e indices
def addcolstrReverse (arq, id, word:str):
    #vai pro lugar do arquivo onde começa as palavras com o mesmo primeiro dígito
    arq.seek((127 - ord(word[0]))*sizeofstructstr)
    Listastruct = list(IDsstr.unpack(arq.read(sizeofstructstr)))
    Listastruct[0] = Listastruct[0].decode('utf-8')
    #enquanto está apontando para algo, vá para esse algo
    while Listastruct[0]>=word:
        if Listastruct[2]==0:
            break
        arq.seek(Listastruct[2])
        Listastruct = list(IDsstr.unpack(arq.read(sizeofstructstr)))
        Listastruct[0] = Listastruct[0].decode('utf-8')
    arq.seek(-sizeofstructstr, 1)

    while Listastruct[0]<word:
        if Listastruct[2]==0: #colocar na penultima posição
            aux=arq.tell()
            arq.seek(0,2)
            aux2 = arq.tell()
            arq.seek(aux)
            arq.write(IDsstr.pack(bytes(word, 'utf-8'), id, aux2))
            arq.seek(0,2)
            Listastruct[0] = bytes(Listastruct[0], 'utf-8')
            arq.write(IDsstr.pack(*Listastruct))
            arq.seek(0)
            return 0
        arq.write(IDsstr.pack(bytes(word, 'utf-8'), id, Listastruct[2]))
        arq.seek(Listastruct[2])
        word = Listastruct[0]
        id = Listastruct[1]
        Listastruct = list(IDsstr.unpack(arq.read(sizeofstructstr)))
        Listastruct[0] = Listastruct[0].decode('utf-8')
        arq.seek(-sizeofstructstr, 1)

#self = arquivo, id = indice, chave = peakrank/wob, adiciona num arquivo apenas de indices 
def addcolint (arq, id, chave):
    #vai pro lugar do arquivo onde começa o respectivo peakrank/wob
    arq.seek((chave-1)*sizeofstructint)
    Listastruct = list(IDsintaux.unpack(arq.read(sizeofstructint)))
    #enquanto está apontando para algo, vá para esse algo
    while Listastruct[1]!=0:
        arq.seek(Listastruct[1])
        Listastruct = list(IDsintaux.unpack(arq.read(sizeofstructint)))

    #já q o read passa, essa linha só volta 1 struct e salva esse lugar no aux
    arq.seek(-sizeofstructint, 1)
    Aux = arq.tell()
    #avança para o fim do arquivo e salvo em outro aux
    arq.seek(0,2)
    Listastruct[1] = arq.tell()
    #volta para o endereço do aux e coloca lá o endereço de onde o proximo será colocado 
    arq.seek(Aux)
    arq.write(IDsint.pack(*Listastruct))
    #vai para o endereço onde será feito o append
    arq.seek(0, 2)
    #coloca a nova struct
    arq.write(IDsint.pack(id, 0))
        
#recebe arquivo,  bool inorder: if false -> reverso e bool tipo: if true é artista if false é musica
def fetchindices(arq, inorder, tipo):
    i=0
    if inorder:
        while i < 128:
            #vai pro primeiro indice com aquele peakrank/wob
            arq.seek(i*sizeofstructint)
            Listastruct = list(IDsint.unpack(arq.read(sizeofstructint)))

            #vai percorrendo todos ID daquela chave até não ter mais
            while Listastruct[1]!=0:
                if Listastruct[0] != 0:
                    if tipo == True:
                        artistPrint(Listastruct[0])
                    else:
                        songPrint(Listastruct[0])
                arq.seek(Listastruct[1])
                Listastruct = list(IDsint.unpack(arq.read(sizeofstructint)))

            #imprime o ultimo valor que precede o 0 e aumenta o valor da chave
            if Listastruct[0] != 0:
                if tipo == True:
                    artistPrint(Listastruct[0])
                else:
                    songPrint(Listastruct[0])
            i=i+1
    else:
        i=127
        while i >= 0:
            #vai pro ultimo indice com aquele peakrank/wob
            arq.seek(i*sizeofstructint)
            Listastruct = list(IDsint.unpack(arq.read(sizeofstructint)))
            #vai percorrendo todos ID daquela chave até não ter mais
            while Listastruct[1]!=0:
                if Listastruct[0] != 0:
                    if tipo == True:
                        artistPrint(Listastruct[0])
                    else:
                        songPrint(Listastruct[0])
                arq.seek(Listastruct[1])
                Listastruct = list(IDsint.unpack(arq.read(sizeofstructint)))
            #imprime o ultimo valor q precede o 0 diminui o valor da chave
            if Listastruct[0] != 0:
                if tipo == True:
                    artistPrint(Listastruct[0])
                else:
                    songPrint(Listastruct[0])
            i=i-1

#Percorre um arquivo de strings e indices em ordem (tipo True = artista, tipo False = musica)
def fetchAlfasIds(arq, tipo):
    i=0
    while i < 128:
        #vai pro primeiro indice com aquele peakrank/wob
        arq.seek(i*sizeofstructstr)
        Listastruct = list(IDsstr.unpack(arq.read(sizeofstructstr)))

        #vai percorrendo todos ID daquela chave até não ter mais
        while Listastruct[1]!=0:
            print(Listastruct[0].decode('utf-8'))
            if tipo == True:
                artistPrint(Listastruct[1])
            else:
                songPrint(Listastruct[1])
            arq.seek(Listastruct[2])
            Listastruct = list(IDsstr.unpack(arq.read(sizeofstructstr)))
        i=i+1

#recebe o arquivo de musica/artista, e oq está sendo procurado, retorna lista de Ids != [0] se existir
def find_index(arq, word:str):
    #pula pra onde começa as palavras com a msm letra inicial
    arq.seek((ord(word[0])-1)*sizeofstructstr)
    Listastruct = list(IDsstr.unpack(arq.read(sizeofstructstr)))
    Listastruct[0] = Listastruct[0].decode('utf-8')
    #procura a primeira que n vem antes q ela alfabeticamente
    while Listastruct[0]<word:
        #se todas vem antes e n tem:
        if Listastruct[2]==0:
            return [0]
        arq.seek(Listastruct[2])
        Listastruct = list(IDsstr.unpack(arq.read(sizeofstructstr)))
        Listastruct[0] = Listastruct[0].decode('utf-8')
    arq.seek(-sizeofstructstr, 1)

    #tira os quase 70 0s q tem dps do nome
    Listastruct[0] = Listastruct[0].rstrip(chr(0))

    #se estiver olhando para uma q vem dps, n tem a q está sendo procurada
    #se estiver olhando para uma igual, retorna todos ids dos nomes iguais
    if Listastruct[0]==word:
        indices = []
        while Listastruct[0] == word:
            indices.append(Listastruct[1])
            arq.seek(Listastruct[2])
            Listastruct = list(IDsstr.unpack(arq.read(sizeofstructstr)))
            Listastruct[0] = Listastruct[0].decode('utf-8')
            Listastruct[0] = Listastruct[0].rstrip(chr(0))
        return indices
    else:
        return [0]


'''
ARQ = open(ARQpeakM, 'r+b')
addcolint(ARQ, id, valorwob/peakrank)
ARQ.close()

ARQ = open(ARQpeakM, 'rb')
fetchindices(ARQ, bool) #True = ordem normal, False = reversa
ARQ.close()
'''
'''
ARQR = open(ARQtreverso, 'r+b')
ARQ = open(ARQtitulos, 'r+b')
addcolstr(ARQ, id, nome do negócio)
addcolstrReverse(ARQR, id, nome do negócio)
ARQ.close()
ARQR.close()

ARQ= open(ARQtitulos, 'rb')
ARQR = open(ARQtreverso, 'rb')
fetchAlfasIds(ARQ, bool(artista=true musica=false))
fetchAlfasIds(ARQR, bool (artista=true musica =false))
Lista = find_index(ARQ, string pra achar)
print(Lista)
ARQ.close()
ARQR.close()
'''