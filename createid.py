from typing import Tuple
import struct

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

#fazer vetor de 100 pointers para a class TrieNode
class TriePointer(object):
    def __init__(self, chave):
        self.chave = chave
        self.pointsto = TrieNode('*')
        self.proximo = None

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
#cria structs
IDsint = struct.Struct('I I I')

    struct(){
        int ant;
        int id;
        int prox;
    }

IDsintaux = IDsint
IDsintaux.pack(0, 0, 0)
sizeofstructint = 12

#cria arquivos com 100 structs nulas
ARQtitulos = "indices_titulos.bin"
ARQnomes = "indices_nomes.bin"
ARQpeakA = "indices_pr_artistas.bin"
#ARQ0 = open(ARQpeakA, 'ab')
ARQpeakM = "indices_pr_musicas.bin"
ARQ1 = open(ARQpeakM, 'ab')
ARQwobA = "indices_wob_artistas.bin"
#ARQ2 = open(ARQwobA, 'ab')
ARQwobM = "indices_wob_musicas.bin"
#ARQ3 = open(ARQwobM, 'ab')
ARQnotasA = "indices_notas_artistas.bin"
#ARQ4 = open(ARQnotasA, 'ab')
ARQnotasM = "indices_notas_musicas.bin"
#ARQ5 = open(ARQnotasM, 'ab')

for i in range(0, 102):
    #ARQ0.write(IDsintaux)
    ARQ1.write(IDsintaux.pack(0, 0, 0))
    #ARQ2.write(IDsintaux)
    #ARQ3.write(IDsintaux)
    #ARQ4.write(IDsintaux)
    #ARQ5.write(IDsintaux)
#ARQ0.close()
ARQ1.close()
#ARQ2.close()
#ARQ3.close()
#ARQ4.close()
#ARQ5.close()

#self = arquivo, id = indice, chave = peakrank/wob
def addcolint (arq, id, chave):
    #vai pro lugar do arquivo onde começa o respectivo peakrank/wob
    arq.seek(chave*sizeofstructint)

    IDintbits = arq.read(sizeofstructint)
    IDintaux = IDintbits
    #enquanto está apontando para algo, vá para esse algo
    while IDintaux[2]!=0:
        arq.seek(IDintaux)
        IDintbits = arq.read(sizeofstructint)
        IDintaux = IDintbits

    #já q o read passa, essa linha só volta 1 struct
    arq.seek(0-sizeofstructint, 1)
    #salva o endereço, o id e o -1 na struct que vai pro fim
    IDsint.pack(arq, id, 0)

    #pra n fazer um self.write(self.seek(0,2))
    #avança pro campo do proximo endereço e salva num aux
    Aux = arq.seek(8, 1)
    #avança para o fim do arquivo e salvo em outro aux
    Aux2 = arq.seek(0,2)
    #volta para o endereço do aux e coloca lá o endereço de onde o proximo será colocado 
    arq = Aux
    arq.write(Aux2)
    #vai para o endereço onde será feito o append
    arq.seek(0,2)
    #coloca a nova struct
    arq.write(IDsint)    

ARQ = open(ARQpeakM, 'a+b')
addcolint(ARQ, 789, 50)
ARQ.close()
        
#recebe arquivo e bool, if false -> reverso
def fetchindices(self, inorder):
    i=0
    IDlistaux = []
    if inorder:
        while i < 101:
            self.seek(i*sizeofstructint)
            while prox!=0:
                IDintaux = self.read(sizeofstructint)
                IDlistaux = IDintaux.unpack(sizeofstructint)
                #faz algo com o IDintaux[1] q é o id#########################3
                prox = IDintaux[2]
                self=prox
            i=i+1
    else:
        i=100
        while i >= 0:
            self.seek(i*sizeofstructint)
            while prox!=0:
                IDintaux = self.read(sizeofstructint)
                IDlistaux = IDintaux.unpack(sizeofstructint)
                #faz algo com o IDintaux[1] q é o id#########################3
                prox = IDintaux[2]
                self=prox
            i=i-1
'''