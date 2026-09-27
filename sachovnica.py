from PIL import Image, ImageDraw

hracia_plocha = []
pocet_vysledkov = 0


def vytvor_sachovnicu():
    global hracia_plocha
    hracia_plocha = []

    for r in range(8):
        riadok = [0] * 8
        hracia_plocha.append(riadok)


def volne_policko(stlpec, riadok):
    for k in range(8):
        if hracia_plocha[riadok][k] == 1:
            return False
        if hracia_plocha[k][stlpec] == 1:
            return False

    for r in range(8):
        for s in range(8):
            if r + s == stlpec + riadok:
                if hracia_plocha[r][s] == 1:
                    return False

            if r - s == riadok - stlpec:
                if hracia_plocha[r][s] == 1:
                    return False

    return True


def ulozobrazok_sachovnice():
    obr = Image.new("RGB", (800, 800), "white")
    kresli = ImageDraw.Draw(obr)

    for r in range(8):
        for s in range(8):
            if (r + s) % 2 == 0:
                kresli.rectangle([s * 100, r * 100, (s + 1) * 100, (r + 1) * 100], fill="black")

    for r in range(8):
        for s in range(8):
            if hracia_plocha[r][s] == 1:
                kresli.ellipse([s * 100 + 10, r * 100 + 10, s * 100 + 90, r * 100 + 90], fill="purple")

    obr.save(f"riesenie_{pocet_vysledkov}.png")


def hladaj_damy(aktualny_riadok):
    global hracia_plocha
    global pocet_vysledkov

    if aktualny_riadok == 8:
        pocet_vysledkov += 1
        ulozobrazok_sachovnice()
        print(hracia_plocha)
        print("--------------------------------------")
    else:
        for s in range(8):
            if volne_policko(s, aktualny_riadok):
                hracia_plocha[aktualny_riadok][s] = 1
                hladaj_damy(aktualny_riadok + 1)
                hracia_plocha[aktualny_riadok][s] = 0


vytvor_sachovnicu()
hladaj_damy(0)

print("Počet riešení:", pocet_vysledkov)