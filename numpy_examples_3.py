
# Mafijski piknik
#################
'''
Merilnik proizvajalca A zajema meritve v enakomernih časovnih razmikih Δt
, prva meritev je ob času Δt
. Napiši program povprecni_pretok_a(x, S, delta_t), ki za zaporedne meritve višine gladine soda s presekom S shranjene v 1D tabeli (np.ndarray) x izračuna povprečen pretok v času do začetka vsake meritve ter rezultate vrne v 1D tabeli. Povprečen pretok je enak celotnemu pretočenemu volumnu deljenemu s celotnim pretečenim časom.
'''
def povprecni_pretok_a(x, S, delta_t):
    t = np.arange(delta_t, delta_t * (len(x) + 1), delta_t)
    return S * x / t
    
#################
'''
Merilnik proizvajalca B meritve zajema ob poljubnih časih, časovni interval med (i - 1)-to in i-to meritvijo podamo v 1D tabeli delta_t na mestu i. So pa nekatere meritve tega merilnika napačne, in sicer pokažejo višino, ki je večja od 0
. Te meritve izloči iz podatkov in jih ne uporabi v obdelavi. Napiši funkcijo povprecni_pretok_b(x, S, delta_t), ki naredi enako kot prejšnja funkcija, le za merilnik proizvajalca B. Predpostaviš lahko, da je vsaj ena meritev veljavna.
'''
def povprecni_pretok_b(x, S, delta_t):
    t = np.cumsum(delta_t)
    valid = (x <= 0)
    return S * x[valid] / t[valid]
    
#################
'''
Po nekaj vrčkih piva so se študentje spomnili veliko zabavnejše uporabe nakupljenih senzorjev. Odločili so se, da bodo izmerili kako hitro (oziroma s kolikšnim največjim pretokom) lahko človek pije pivo. Vsakemu udeležencu eksperimenta so priredili sod z merilnikom proizvajalca A. Meritve za i-tega udeleženca shranimo v 2D tabelo podatki v i-to vrstico. Prav tako so določili, da je največji teoretični pretok skozi človeško grlo enak phi_max (phi_max < 0), torej vsi udeleženci, ki so ob katerem koli času pili s povprečnim pretokom po absolutni vrednosti večjim (zaradi negativnega znaka to pomeni manjšim) od phi_max, so goljufali.

Napiši funkcijo najhitrejsi_pivec(podatki, S, delta_t, phi_max), ki vrne par (tuple), v katerem je na prvem mestu po absolutni vrednosti največji (ker so vsi smiselni pretoki negativni, to pomeni najmanjši) izmerjen povprečni pretok ob poljubnem času, pri čemer dosežki goljufivcev niso upoštevani, in na drugem mestu seznam (list) zaporednih števil udeležencev, ki so goljufali. Predpostaviš lahko, da vsaj en udeleženec ni goljufal.
'''
def najhitrejsi_pivec(podatki, S, delta_t, phi_max):
    t = np.arange(delta_t, delta_t * (podatki.shape[1] + 1), delta_t)
    phi = podatki * S / t
    phi = np.min(phi, axis = 1)
    goljufi = np.flatnonzero(phi < phi_max)
    zmagovalna_vrednost = np.min(phi[phi >= phi_max])
    return (zmagovalna_vrednost, list(goljufi))
    

# Klada na klancu - numpy
#################
'''
Če želimo čas potovanja sunka pretvoriti v razdaljo moramo rešiti preprosto enačbo s=12cairt
, kjer je s
 razdalja od klade do senzorja, cair
 hitrost zvoka v zraku in t
 čas potreben za odboj. Na žalost je hitrost zvoka v zraku odvisna od temperature, zato moramo upoštevati tudi to. Privzemi, da se hitrost zvoka v zraku (izražena v ms
) izračuna kot cair=401.88T−−−−−−−√
; kjer je T
 temperatura izražena v Kelvinih. Ob vsaki ponovitvi eksperimenta si v 1D tabelo temperatura zapišemo temperaturo zraka v kelvinih.

Sestavi funkcijo pretvori_v_razdaljo(casi, temperatura), ki nam čase med poslanim pulzom (merjeno v ms
) in njegovo zaznavo pretvori v razdaljo izraženo v metrih.

Primer za eno ponovitev eksperimenta (N=1)
 in dve ponovitvi:
'''
def pretvori_v_razdaljo(casi, temperature):
    return 0.5 * casi * 1e-3 * np.sqrt(401.88 * np.atleast_2d(temperature).T)
    
#################
'''
Sedaj bi iz dobljenih položajev klade radi izračunali hitrosti. Sestavi funkcijo povprecne_hitrosti(polozaji), ki sprejme prej izračunane položaje oblike (N,Nt)
 vrne pa tabelo, ki na prvem mestu vsake vrstice vsebuje povprečno hitrost ponovitve, na nadaljnjih mestih pa izračunane trenutne hitrosti med eksperimenti v enotah ms
. Časi med posameznimi meritvami položaja so konstantni in znašajo 0.01 s
. Izhodna tabela bo torej oblike (N,Nt)
 (Nt−1
 trenutnih hitrosti +1
 za povprečno hitrost).
'''
def povprecne_hitrosti(polozaji):
    vs = (polozaji[:, 1:] - polozaji[:, :-1]) / 0.01
    vs_avg = np.atleast_2d(np.average(vs, axis=1))
    return np.concatenate((vs_avg.T, vs), axis=1)

# alternativa
def povprecne_hitrosti(polozaji):
    vs = (polozaji[:, 1:] - polozaji[:, :-1]) / 0.01
    return np.pad(vs, ((0, 0), (1, 0)), "mean")
    
#################
'''
Pri obdelavi podatkov opaziš, da imajo nekateri eksperimenti veliko večjo razpršenost rezutatov kot drugi - razpršenost merimo s standarno deviacijo, ki jo za določen eksperiment izracunamo kot 1N∑i(vi−vaverage)2−−−−−−−−−−−−−−−−√
. Zaveš se, da obstaja možnost, da si med pripravo posameznih ponovitev eksperimenta po pomoti pritisnil na gumb, ki preklaplja med visoko in nizko časovno ločljivostjo senzorja. Pokvarjene ponovitve si se odločil odstraniti iz seta meritev, tako da jih ne boš upošteval.

Sestavi funkcijo koncno_povprecje(polozaji, meja_std), ki sprejme položaje klade za vse ponovitve eksperimenta ter mejo standardne deviacije. Funkcija naj izračuna standardno deviacijo hitrosti za vsako ponovitev, ter izloči vse eksperimente, kjer ta vrednost znaša več kot določena meja. Na preostalih eksperimentalnih ponovitvah naj nato izračuna in vrne povprečno hitrost povrečnih hitrosti zaokroženo na 2 decimalki.
'''
def koncno_povprecje(polozaji, meja_std):
    povp = povprecne_hitrosti(polozaji)
    vs_avg = povp[:, 0]
    vs = povp[:, 1:]
    sigmas = np.sqrt((1 / (len(polozaji[0]) - 1)) * np.sum(np.square(vs.T - vs_avg).T, axis=1))
    return round(np.average(vs[np.where(sigmas < meja_std)]), 2)

# alternativa - uporabimo vgrajeno funkcijo std()
def koncno_povprecje(polozaji, meja_std):
    hitrosti = povprecne_hitrosti(polozaji)[:, 1:]
    return round(hitrosti[np.where(hitrosti.std(axis=1) < meja_std)].mean(), 2)
    

# Viseči most
#################
'''
Reka se nahaja na y
 koordinati y_r. Napiši funkcijo je_poplavljen(ver, y_r), ki sprejme viseči most ver in y
 koordinato reke y_r ter vrne True, če most sega v reko in False sicer.
'''
def je_poplavljen(ver, y_r):
    return np.min(ver[1, :]) < y_r
    
#################
'''
Napiši funkcijo lahko_sestavi(ver, l, delta), ki sprejme viseči most ver, kot je opisano zgoraj, dolžine palic l, ki jih imamo na razpolago. Tabela l ima enako dolžino, kot je dolžina vrstice v tabeli ver manj 1, tj. len(l)=len(ver[0])−1
. Zadnji vhodni parameter delta pove, za koliko največ palice lahko odstopajo od točnih dolžin.
'''
def lahko_sestavim(ver, l, delta):
    dx = ver[0, 1:] - ver[0, :-1]
    dy = ver[1, 1:] - ver[1, :-1]
    return np.alltrue(np.abs((np.sort(np.sqrt(dx ** 2 + dy ** 2)) - np.sort(l))) <= delta)
    
#################
'''
Žogo poševno vržemo iz točke (x,y)
 z začetno hitrostjo (vx,vy)
. Napiši funkcijo presecisce(x, y, vx, vy, k, n), ki sprejme x in y koordinato začetne točke, vx in vy komponenti začetne hitrosti in k, ki je vrstica smernih koeficientov premic z začetnimi vrednostmi n in vrne tabelo x
 koordinat in y
 koordinat presečišč trajektorije žoge in premic (v prvi vrsti naj bodo x
 koordinate, v drugi pa y
 koordinate). Če se premica in parabola ne sekata, naj bosta koordinati presečišč np.nan (seveda so vrednosti np.nan tudi v vseh presečiščih pri negativnem času), če pa se sekata v več točkah, naj bosta koordinati kasnejši, tj. tisti kjer se sekata ob kasnejšem času. Za gravitacijski pospešek vzemi g=π2
.
'''
def presecisce(x, y, vx, vy, k, n):
    """
    - položaj točke P(t) = (x + vx*t, y + vy*t - gt²/2), vstavimo v Y = kX + n
    - dobimo kvadratno enačbo.
    """
    g = np.pi ** 2
    a = g / 2
    b = k * vx - vy
    c = n - y + k * x
    D = b ** 2 - 4 * a * c
    D = np.where(D < 0, np.nan, D)
    t1 = (-b + np.sqrt(D)) / (2 * a)
    t2 = (-b - np.sqrt(D)) / (2 * a)
    t = np.maximum(t1, t2)
    t = np.where(t < 0, np.nan, t)
    x = x + vx * t
    y = k * x + n
    return np.array([x, y])
    
#################
'''
Napiši funkcijo kje_odboj(x, y, vx, vy, ver), ki sprejme začetno lego in hitrost žoge ter koordinate visečega mostu ver enako kot zgoraj, vrne pa indeks členka, na katerem se zgodi odboj (če pade točno na dva členka, naj vrne manjši indeks). Če do odboja ne pride, naj funkcija vrača -1.
'''
def kje_odboj(x, y, vx, vy, ver):
    ver_x = ver[0, :]
    ver_y = ver[1, :]
    k = ((ver_y - np.roll(ver_y, 1)) / (ver_x - np.roll(ver_x, 1)))[1:]
    n = (ver_y[:-1] - k * ver_x[:-1])
    presecisca = presecisce(x, y, vx, vy, k, n)[0]
    kateri_clenki = np.nonzero(np.less_equal(ver_x[:-1], presecisca) & np.less_equal(presecisca, ver_x[1:]))
    if np.size(kateri_clenki):
        return np.min(kateri_clenki)
    else:
        return -1