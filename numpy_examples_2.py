
# Ponarejevalka
#################
'''
V nalogi, ki je še ni zagovorila, mora preiskovati nihanje vzmetnega nihala. Vemo, da se odmik vzmetnega nihala spreminja s časom kot x=Asin(ωt)
, kjer sta A
 in ω
 podani konstanti.

Napiši funkcijo odmik(A, omega, t_z, t_k), ki izračuna odmik na 10 točkah enakomerno porazdeljenih po intervalu [tz,tk]
.
'''
def odmik(A, omega, t_z, t_k):
    return A * np.sin(omega * np.linspace(t_z, t_k, 10))
    
#################
'''
Rezultati pri prejšnji nalogi so seveda brez merske napake, kot pa vsi vemo, je ta pri meritvah vedno prisotna, zato se je Lana odločila, da meritvam doda nekaj šuma. In sicer vsakemu elementu a[i] razen prvemu in zadnjemu želi prišteti A * sin(omega * (a[i + 1] + a[i - 1]) / 2) / 10. Za dane A, omega, t_z, t_k napiši funkcijo realni_odmik(A, omega, t_z, t_k), ki vrne meritve z dodanim šumom. Na primer:
'''
def realni_odmik(A, omega, t_z, t_k):
    x = A * np.sin(omega * np.linspace(t_z, t_k, 10))
    popravek = A * np.sin(omega * (np.roll(x, 1) + np.roll(x, -1)) / 2) / 10
    popravek[0] = 0
    popravek[len(popravek) - 1] = 0
    return x + popravek
    
def realni_odmik(A, o, t_z, t_k):
    odm = odmik(A, o, t_z, t_k)
    t = np.copy(odm)
    t += A * np.sin(o * ((np.roll(t, 1) + np.roll(t, -1)) / 2)) / 10
    odm[1:-1] = t[1:-1]
    return odm
    
#################
'''
Lana ni izbrala preveč dobre funkcije za dodajanje šuma in sedaj asistent sumi, da je podatke ponaredila. Ker tega seveda ne more dokazati, se je odločil, da jo kaznuje tako, da mu mora pomagati poiskati študente, ki so podatke vzeli od kolegov. Asistent meni, da če se povprečna frekvenca ω
 dveh študentov razlikuje za manj kot 2 %, je velika verjetnost, da je en študent prepisoval od drugega (prepisanim podatkom je le dodal nekaj šuma).

Lana ima meritve ostalih študentov na voljo v dveh tabelah, v tabeli X so meritve odmikov, v i-ti vrstici so vse meritve, ki pripadajo i-temu študentu. V tabeli T so v enakem formatu shranjene meritve časov. Za amplitudo vzami kar maksimalen odmik med meritvami.

Napiši funkcijo prepisovalci(X, T, omega_0), ki vrne urejen seznam (!) zaporednih številk učencev, katerih meritve frekvenc se od frekvence omega_0 razlikujejo za manj kot 2 % (kjer za osnovo pri računanju odstotkov vzamemo omega_0).
'''
def prepisovalci(X, T, omega_0):
    A = np.max(X, axis = 1)
    A = A.reshape((len(A), 1))
    omegas = np.mean(np.arcsin(X / A) / T, axis = 1)
    napake = np.abs((omegas - omega_0) / omega_0)
    prep = np.flatnonzero(napake < 0.02)
    return list(prep)

def prepisovalci(X, T, o0):
    A = (np.max(X, axis=1)).reshape(X.shape[0], 1)
    w = (np.abs(np.mean(np.arcsin(X / A) / T, axis=1) - o0) / o0) < 0.02   
    return np.argwhere(w == 1)


# Obsedena elektronika
#################
'''
Za začetek moramo iz rešitev odstraniti oskrunjene vrednosti. Meritve z manjkajočimi vrednostmi bi bile seveda neuporabne. Na srečo so sile v Albertovem eksperimentu dovolj majhne in vzorčenje dovolj hitro, da lahko manjkajoče vrednosti kar linearno interpoliramo iz sosednjih vrednosti.

Definirajte funkcijo razhudicene_hitrosti(hitrosti), ki sprejme ndarray oblike (3 x N). V prvi vrstici se nahajajo zaporedne meritve x komponente hitrosti, v drugi vrstici y komponente in v tretji z komponente. Časovni interval med zaporednimi meritvami je konstanten.

Funkcija naj vrne ndarray hitrosti, kjer so hudičeva števila (666) zamenjana z linearno interpoliranimi vrednostmi. Pri interpolaciji upoštevajte le sosednje hitrosti. Hudičeva števila se ne bodo pojavila na prvem, zadnjem ali zaporednih mestih.
'''
def razhudicene_hitrosti(hitrosti):
    return np.where(hitrosti == 666,
                    (np.roll(hitrosti, 1) + np.roll(hitrosti, -1)) / 2,
                    hitrosti)
                    
def razhudicene_hitrosti(v):
    norm = v != 666
    i666 = norm == 0
    v = v * norm
    m = (np.sum(v, axis=1) / np.sum(norm!=0, axis=1)).reshape(v.shape[0], 1)
    sub = i666 * m
    return v + sub
    
#################
'''
Albert sicer potrebuje lokacije žogic, a ga nakup merilnika hitrosti sploh ne skrbi, saj se zaveda, da ga od željenega rezultata loči le integral. Pomagajte Albertu pri numerični implementaciji.

Definirajte funkcijo lokacije(zacetek, hitrosti, dt), ki sprejme začetne pozicije zacetek (ndarray dolžine 3), izmerjene hitrosti (ndarray oblike (3xN), vrstice enako kot v prejšnji podnalogi predstavljajo različne komponente) in časovni interval med meritvami dt.

Funkcija naj vrne ndarray oblike (3xN), v katerem so komponente lokacije žogice izračunane z najpreprostejšo obliko numerične integracije sn=szačetek+∑ni=0vidt
.
'''
def lokacije(zacetek, hitrosti, dt):
    return zacetek[:, np.newaxis] + np.cumsum(hitrosti * dt, axis = 1)
    
def lokacije(zacetek, hitrosti, dt):
    z = zacetek.reshape(zacetek.shape[0], 1)
    return z + np.cumsum(hitrosti*dt, axis=1)  
    
#################
'''
Albert je s svojimi izračuni napovedal statistiko rmaksimalnirkončni
, kjer je r
 razdalja od izhodišča (r=x2+y2+z2−−−−−−−−−−√
). rmaksimalni
 predstavlja največjo razdaljo, ki jo doseže žogica, rkončni
 pa razdaljo pri zadnji meritvi.

Pomagajte mu pri implementaciji, definirajte fukcijo razmerja(meritve), ki sprejme seznam lokacij za M ponovitev eksperimenta (ndarray dimenzije (Mx3xN), torej M ponovitev struktur, ki bi jih vrnila funkcija lokacije iz predhodne podnaloge) in vrne par, ki ima na prvem mestu povprečno vrednost in na drugem standardni odklon rmaksimalnirkončni
 izračunana iz podanih M eksperimentov.
'''
def razmerja(meritve):
    razdalje = np.sqrt(np.sum(np.square(meritve), axis = 1))
    razmerja = np.max(razdalje, axis = 1) / razdalje[:, -1]
    return np.average(razmerja), np.std(razmerja)


# Kvadratne funkcije
#################
'''
Napiši funkcijo kvadratna_funkcija(a, b, c), ki bo vrnila numpy array vrednosti funkcije a*x^2 + b*x + c izračunane v točkah definiranih v uvodnem besedilu.
'''
def kvadratna_funkcija(a, b, c):
    x_os = np.arange(0, 10, 1)
    return a * x_os ** 2 + b * x_os + c
    
def kvadratna_funkcija(a, b, c):
    r = np.arange(10)
    a = np.square(r) * a
    b = r * b
    return a + b + c
    
#################
'''
Definiraj funkcijo maksimum_kvadratnih(a1, b1, c1, a2, b2, c2), ki bo prejela dve kvadratni funkciji a1 * x^2 + b1 * x + c1 in a2 * x^2 + b2 * x + c2 in vrnila numpy array maksimumov vrednosti teh dveh funkcij v posamezni točki. 
'''
def maksimum_kvadratnih(a1, b1, c1, a2, b2, c2):
    prva = kvadratna_funkcija(a1, b1, c1)
    druga = kvadratna_funkcija(a2, b2, c2)
    return np.maximum(prva, druga)

def maksimum_kvadratnih(a1, b1, c1, a2, b2, c2):
    st = kvadratna_funkcija(a1, b1, c1)
    nd = kvadratna_funkcija(a2, b2, c2)
    prva_vecja = st > nd
    st *= prva_vecja
    nd *= (prva_vecja == 0)
    return st + nd
    
#################
'''
Pri tej nalogi bomo poskusili narisati kvadratno funkcijo. Dobiš boš podano kvadratno funkcijo, ti pa jo boš moral narisati na intervalu [0, 9]. Graf funkcije si bomo predstavljali kot 10 x 10 numpy tabelo. Prvi stolpec tabele bo predstavljal koordinato x = 0, drugi stolpec x = 1, itd. Spodnja vrstica bo predstavljala vrednost y = 0, vrstica višje vrednost y = 1 itd. Vsa polja v tabeli, ki so "pod" grafom označimo z 1, polja v tabeli nad grafom pa z 0.

Definiraj funkcijo narisi_graf(a, b, c), ki bo vrnila 10 x 10 numpy tabelo z grafom dane kvadratne funkcije, kot so primeri spodaj.
'''
def narisi_graf(a, b, c):
    x, y = np.meshgrid(np.arange(0, 10, 1), np.arange(0, 10, 1))
    vrednosti = a*x**2 + b*x + c
    graf = np.flip(y < vrednosti, axis=0).astype(int)
    return graf
    
    """
    vrednosti = kvadratna_funkcija(a, b, c)
    xy_tabela = np.fromfunction(lambda i, j : i, (10, 10))
    graf = np.where(xy_tabela < vrednosti, 1, 0)
    graf = np.flip(graf, axis=0) # Obrnemo x in y os
    return graf
    """

zs = 0
import math
def n_enic(i, a, b, c):
    n = math.ceil((i**2)*a + (i)*b + c)
    
    if n <= 0:
        return 0
    if n > 10:
        n = 10
        
    z = np.zeros((10, ), dtype=int)
    z[0:n] = np.ones((n,))
    
    zs[i] = z
    return 0
    
def narisi_graf(a, b, c):
    global zs
    zs = np.zeros((10, 10), dtype=int)
    g = np.vectorize(n_enic)
    
    np.fromfunction(lambda i: g(i, a, b, c), (10, ), dtype=int)
    return np.rot90(zs)
    

# Popravljalec cevi
#################
'''
Napiši funkcijo kje(hitrosti, t), ki za prvi argument sprejme hitrosti robotka v metrih na sekundo, za drugi argument pa čas t v sekundah in vrne oddaljenost od izhodišča (v metrih) ob času t. Če je čas t
 prevelik, naj funkcija vrne False.

Kakršnakoli uporaba for ali while zanke bo kaznovana z nič točkami, kot da naloge nebi reševali.
'''
def kje(v, t):
    N = int(t // 0.01)
    if N <= len(v):
        return np.sum(v[:N] * 0.01)
    return False

#################
'''
V resnici pa cevi niso ravne. Na vsake toliko časa robotek pride do zavoja. Kadar cev zavije se robotek prilagodi obliki in zabeleži pod kakšnim kotom je zavil. Cevi so na ravnini, zato se lahko zavrti samo okoli ene osi. Napiši funkcijo kotopot(pot), ki za argument sprejme tabelo naslednje oblike. Tabela je iz kompleksnih števil. Vsaka vrstica v njej ima na prvem mestu število katerega realna komponenta je kot, na vseh ostalih pa števila, ki imajo za realno komponento hitrost, za imaginarno komponento pa 0
, če je to realna hitrost, ki jo je potrebno upoštevati, oziroma 1
, če je to imaginarna hitrost, ki je ne smemo upoštevati. Funkcija kotopot(pot) naj vrne novo tabelo, ki bo vrstice iz prejšnje spremenila tako, da bo prvi element predstavljal kot, drugi element pa prepotovano pot od enega do drugega ovinka.

Kakršnakoli uporaba for ali while zanke bo kaznovana tako, da se maksimalno število točk prepolovi.
'''
def kotopot(pot):
    novi = np.zeros((len(pot), 2))
    novi[:, 0] = np.real(pot[:, 0])
    resnica = np.imag(pot[:, 1:]) == 0
    novi[:, 1] = np.sum(np.real(pot[:, 1:]) * resnica * 0.01, axis = 1)
    return novi
    
#################
'''
Sedaj zapiši funkcijo ogljisca(seznam), ki za argument sprejme rezultat funkcije kotopot (oblika tabele seznam je enaka kot oblika rezultata funkcije kotopot), vrne pa seznam koordinat zavojev, oblike [[x_0, y_0], [x_1, y_1], ..., [x_N, y_N]], kjer indeks pove za kateri zavoj po vrsti gre. Privzemi, da so koti, ki jih sporoča robot absolutni koti glede na x
 os zapisani v radianih.

Kakršnakoli uporaba for ali while zanke bo kaznovana z nič točkami, kot da naloge nebi reševali.
'''
def ogljisca(seznam):
    baza = np.zeros((len(seznam), 2))
    baza[:, 0] = np.cos(seznam[:, 0]) * seznam[:, 1]
    baza[:, 1] = np.sin(seznam[:, 0]) * seznam[:, 1]
    return np.cumsum(baza, axis=0)

def ogljisca(seznam):
    baza = np.zeros((len(seznam), 2))
    baza[:, 0] = np.cos(seznam[:, 0]) * seznam[:, 1]
    baza[:, 1] = np.sin(seznam[:, 0]) * seznam[:, 1]

    def maska(rob, baza):
        return np.fromfunction(lambda i, j: i < rob, np.shape(baza))
    velika_maska = np.fromfunction(lambda i, j, k: maska(i + 1, baza),
                                   (len(baza), len(baza), len(baza[0])))

    return np.sum(velika_maska * baza, axis=1)