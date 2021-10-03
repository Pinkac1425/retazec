def pocet_suborov():
    while True:
        cislo = input("Počet súborov")
        try:
            return int(cislo)
        except ValueError:
            print("Iba celé číslo")

input = []
pocet = 0

with open("basnicka.txt") as subor:
    for slovo in subor:
        input += slovo.split()

for i in range(pocet_suborov()):
    pocet += 1
    if pocet ==len(input):
        pocet -= len(input)
    with open(f"""slovo{pocet}""", mode="w") as subor:
        print(input[pocer -1], file=subor)