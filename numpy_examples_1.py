'''Osnove numpy

Resitve:'''


#################
'''

'''

# Osnove numpy
#################
'''
Numpy tabelo lahko ustvarimo na več načinov. Ustvarimo jo lahko enostavno iz seznama z funkcijo np.array(). Definiraj funkcijo kvadrat(n), ki sestavi tabelo dolžine n, kjer so elementi kvadrati indeksa.
'''
def kvadrat(n):
    return np.array(range(n)) * range(n)

#################
'''
Definiramo pa jih lahko tudi drugače. Lahko že v naprej s funkcijo np.ones() ali pa np.zeros() ustvarimo numpy tabelo željenih dimenzij, potem pa jo uredimo.

Sestavi funkcijo tabela_enic(dim1, dim2), ki za argumenta sprejme dimenzijo tabele in vrne dvodimenzionalno tabelo željenih dimenzij zapolnjeno z enicami.
'''
def tabela_enic(dim1, dim2):
    return np.ones((dim1, dim2))
    
#################
'''
Sestavi funkcijo simetrija(dim1, dim2), ki sprejme dimenzije tabele in vrne tabelo v kateri je vsak element vsota indeksov.
a[i,j]=i+j
''' 
def simetrija(dim1, dim2):
    x = np.zeros((dim1, dim2))
    for i in range(dim1):
        for j in range(dim2):
            x[i, j] = i + j
    return x
    
def simetrija(dim1, dim2):
    '''Možna alternativa.'''
    d = max(dim1, dim2)
    x = np.reshape(np.arange(d*d) % d, (d, d))
    return (x + x.T)[:dim1, :dim2].astype(float)

#################
'''
Zdaj pa je čas da uporabiš moč numpy. Operacije med numpy tabelami so zelo enostavne. Tako lahko dve tabeli med seboj sešteješ kar z simbolom + in se bosta element za elementom seštela.
Enako velja tudi za množenje, deljenje, celoštevilko deljenje itd. S pomočjo prejšnjih funkcij, simetrični tabeli prištej kompleksno enico na vsakem mestu. Zapiši funkcijo carobni_kompleks(dim1, dim2).

Namig: Imaginarno enoto i v Pythonu zapišemo kot 1j.
'''
def carobni_kompleks(dim1, dim2):
    return simetrija(dim1, dim2) + 1j
    
#################
'''
Tabele lahko med seboj tudi primerjamo. Preverimo lahko torej če sta elementa v dveh tabelah enakih dimenzij enaka, večja, manjša. Tako lahko zapišeš funkcijo kdo_je_pravi_velikan(tabela1, tabela2), ki sprejme dve tabeli in vrne tabelo zgolj tistih elementov iz prve tabele, ki so večji od pripadajočih elementov v drugi tabeli, ostale vrednsoti pa so ničle. Namig:Spomni se, da je False 0 in True 1.
'''
def kdo_je_pravi_velikan(x, y):
    return x * (x > y)
    
#################    
'''
S pomočjo funkcij np.all(), np.any() in podobnih, lahko izvajaš tudi bolj zapletene logične operacije, kot recimo ugotoviš, če so vsi elementi večji ali pa preveriš če je vsaj en element večji. Zapiši funkcijo premisljeni_delilec(tabela1, tabela2), ki sprejme, dve tabeli in izvede operacijo deljenja, če ugotovi, da je operacija povsod definirana (da nikjer ne delimo z ničlo), sicer pa vrže None
'''
def premisljeni_delilec(tabela1, tabela2):
    if np.all(tabela2 != 0):
        return tabela1 / tabela2
    else:
        return None


# Generiranje tabel podatkov   
################# 
'''
Sestavite funkcijo vrednosti_sinusa(N), ki vrne vrednosti funkcije sinus v N ekvidistančnih točkah z intervala [0,2π].
'''
def vrednosti_sinusa(N):
    return np.sin(np.linspace(0, 2 * np.pi, N))

################# 
'''
Sestavite funkcijo linearna_funkcija(k, x_max, dx), ki vrne vrednosti linearne funkcije f(x) = kx, kjer so x vrednosti z intervala [0,xmax)
 z začetkom v 0 in razmaknjene za dx.
'''
def linearna_funkcija(k, x_max, dx):
    return k * np.arange(0, x_max, dx)

#################     
'''
Sestavite funkcijo dvodimenzionalni(N), ki vrne dvodimenzionalni array (N×N
 matriko). Prva vrstica naj vsebuje vrednosti 1, druga 2, itd., do N-te vrstice napolnjene z vrednostmi N.
'''
def dvodimenzionalni(N):
    return (np.ones((N, N)) * np.arange(1, N + 1)).T

#################     
'''
Sestavite funkcijo produkt_indeksov(N), ki vrne dvodimenzionalni array (N×N
 matriko). Vrednost komponente z indeksoma i in j naj bo i*j.
'''
def produkt_indeksov(N):
    return np.fromfunction(lambda i, j : i * j, (N, N))


# Iskanje po tabelah
#################
'''
Definirajte funkcijo vecji(a, b), ki sprejme dva enodimenzionalna seznama iste dolžine in vrne indekse mest, kjer je prvi seznam večji od drugega.
'''
def vecji(a, b):
    return np.flatnonzero(a > b)

#################
'''
Definirajte funkcijo zdruzena(a, b), ki sprejme dva enodimenzionalna seznama iste dolžine in vrne seznam z vrednostmi iz a, kjer so le te večje od 0 in vrednostmi iz b povsod drugje.
'''   
def zdruzena(a, b):
    return np.where(a > 0, a, b)

#################
'''
Definirajte funkcijo lokalni_maksimum(a), ki sprejme enodimenzionalen seznam in vrne indekse lokalnih maksimumov. Lokalni maksimum je element seznama, za katerega velja a[i-1] < a[i] > a[i+1]. Za robne elemente smatramo, da so lokalni maksimumi, če so večji od edinega soseda. Za reševanje sta koristni funkciji np.roll in np.pad.
'''  
def lokalni_maksimum(a):
    a = np.pad(a, (1, 1), 'minimum')
    return np.flatnonzero((a > np.roll(a, 1)) * (a > np.roll(a, -1))) - 1
    
    
# Osi in operacije med tabelami
#################
'''
Definiraj funkcijo 'celotni_tok(tabela)', ki kot argument sprejme tabelo, v kateri prva vrstica predstavlja število delcev, ki se giblje s hitrostjo iz druge vrstice in naboj iz zadnje vrstice, vrne pa celotni električni tok, definiran kot
j=∑m nm vm em,
kjer je em naboj, vm hitrost in nm število delcev z nabojem em in hitrostjo vm
'''
def celotni_tok(arr):
    return np.sum(np.prod(arr, axis=0))
    
#################
'''
Hitrost delcev lahko spreminja tako, da v eno izmed smeri vklopi električno polje E
. Le to hitrost delca z nabojem e
 spremeni kot
Δv(t)=e∫t0E(t′)dt′.
Če Aljaž hipno vklopi konstantno električno polje za čas t
, z vrednostjo E
, potem velja

vnova=vzačetna+Eet.
'''  
def celotni_tok_po_vklopu(arr, E, t):
    arr[1, :] = arr[1] + arr[2] * E * t
    return np.sum(np.prod(arr, axis=0))
    
def celotni_tok_po_vklopu(t, a1, a2):
    t[1] += a1*a2*t[2]
    return celotni_tok(t) 
    
#################
'''
A Aljaž hitro ugotovi, da v realnosti ne mora doseči povsem konstantnega polja, temveč le polje, ki poda odvisnost
vnova=vzačetna+Eeσln(exp(σt)+1).

Definiraj funkcijo celotni_tok_po_vklopu_realno(tabela, sigma, E, t), ki sprejme tabelo, parameter natančnosti σ
, maksimalno jakost polja E
 in čas t
.
'''
def celotni_tok_po_vklopu_realno(arr, sigma, E, t):
    arr[1, :] = arr[1] + arr[2] * E / sigma * np.log(np.exp(sigma * t) + 1)
    return np.sum(np.prod(arr, axis=0))

def celotni_tok_po_vklopu_realno(tabela, sigma, E, t):
    tabela[1] += E*tabela[2] / sigma * np.log(np.exp(sigma*t) + 1)
    return celotni_tok(tabela) 
    
#################
'''
Kljub upoštevanju tega popravka se rezultati eksperimenta ne ujemajo z modelom, zato se posvetuje pri profesorjih. Ti se mu povejo, da se pri določeni hitrosti delci zaletijo v steno zaradi magnetnih polj. Aljažu seveda nič ni jasno, a razume, da mora napisati program, ki bo upošreval le tiste delce, ki se ne zaletijo v steno.

Napiši funkcijo celotni_tok_po_vklopu_realno_stena(tabela, sigma, E, t, v_max), ki sprejme enake parametre kot prejšnja, in maksimalno dovoljeno hitrost, vrne pa celotni tok.
'''  
def celotni_tok_po_vklopu_realno_stena(arr, sigma, E, t, v0):
    arr[1, :] = arr[1] + arr[2] * E / sigma * np.log(np.exp(sigma * t) + 1)
    arr[1, :] = arr[1] * (np.abs(arr[1]) < v0)
    return np.sum(np.prod(arr, axis=0))

def celotni_tok_po_vklopu_realno_stena(tabela, sigma, E, t, v_max):
    tabela[1] += E*tabela[2] / sigma * np.log(np.exp(sigma*t) + 1)
    m = np.abs(tabela[1]) < v_max
    tabela[1] *= m
    return celotni_tok(tabela)
    

# Piramida
#################
'''
S knjižnico numpy si lahko privoščimo zelo uporabne manipulacije tabel, še posebaj več dimenzionalnih. Na tak način lahko ustvarimo tridimenzionalno tabelo, ki predstavlja štiristrano piramido. Piramido označimo z enicami, preostanek pa z ničlami. Sestavi funkcijo numpy_piramida, ki sprejme kot argument dolžino spodnjega roba piramide in skonstruira štiristrano numpy piramido z naklonom 45°
. Nična os naj bo višina.

Namig: pomagaj si z np.zeros() in np.ones()
''' 
def numpy_piramida(a):
    ''' funkcija skonstruira piramido s stranico dolžine a'''

    v = a // 2 + a % 2
    piramida = np.zeros((v, a, a))
    for i in np.arange(v):
        if i != 0:
            piramida[v - i - 1, i: -i, i: -i] = np.ones((a - 2*i, a - 2*i))
        else:
            piramida[v - i - 1, :, :] = np.ones((a - 2*i, a - 2*i))

    return piramida

#################
'''
Zapiši funkcije pticja_perspektiva(piramida), s_strani1(piramida) in s_strani2(piramida), ki sprejme piramido napisano na prejšnji način in vrne tabelo, ki prikazuje profil piramide iz ptičje perspektive in iz strani
''' 
def pticja_perspektiva(piramida):
    '''Funkcija sprejme piramido in pokaže njen 'profil' iz ptičje perspektive.'''
    return np.sum(piramida, axis=0)

def s_strani1(piramida):
    '''Funkcija sprejme piramido in pokaže njen 'profil' iz strani.'''
    return np.sum(piramida, axis=1)

def s_strani2(piramida):
    '''Funkcija sprejme piramido in pokaže njen 'profil' iz druge strani.'''
    return np.sum(piramida, axis=2)
    

# Več dimenzionalne tabele
#################
'''
Z numpy lahko učinkovito ustarjamo tabele raznoraznih oblik in dimenzij, z uporabo funkcij kot so np.ones() in np.zeros(). Definiraj funkcijo prazna_tabela(dimenzije, tip), ki sprejme željeno obliko in tip tabele in vrne tabelo željene oblike iz samih ničel.
''' 
def prazna_tabela(niz, tip):
    return np.zeros(niz, dtype=tip)
    
#################
'''
S tem močnim orožjem si lahko privoščimo izredno abstraktne manipulacije tabel. Napiši funkcijo sodi_so_2(tabela), ki sprejme prazno tabelo dimenzije 3 in na vseh mestih, kjer so vsi indeksi sodi postavi vrednost 2.
''' 
def sodi_so_2(tabela):
    tabela[::2, ::2, ::2] = np.ones((np.array(np.shape(tabela)) + 1 ) //2) * 2
    return tabela

def sodi_so_2(tabela):
    ''' To pa je alternativni način.'''
    oblika = np.shape(tabela)
    rezina = tuple([slice(0, oblika[i], 2) for i in range(3)])
    tabela[rezina] = np.ones((np.array(oblika) + 1 ) // 2) * 2
    return tabela
    
def sodi_so_2(t):
    indexs = np.fromfunction(lambda i, j, k: ((i)%2==0) * ((j)%2==0) * ((k)%2==0), t.shape, dtype=int) * 2.0
    return indexs
    
#################
'''
Pa pojdimo zdaj še korak dlje. Zapiši funkcijo sodi_so_3(tabela), ki sprejme prazno tabelo poljubne dimenzije in na vseh mestih, kjer so vsi indeksi sodi postavi vrednost 3. Namig: Poglej uradno rešitev prejšnje naloge.
'''
def sodi_so_3(tabela):
    oblika = np.shape(tabela)
    rezina = tuple([slice(0, oblika[i], 2) for i in range(len(oblika))])
    tabela[rezina] = np.ones(np.shape(tabela[rezina])) * 3
    return tabela