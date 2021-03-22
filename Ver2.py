dzimums = "nedefinēts"
sagatavotiba = "nedefinēts"
distance = "nedefinēts"
vaiIesildities = "nedefinēts"
reizinatajs = 1

# Jautā par dzimumu
while True:
    try:
        dzimums = str(input("Kāds ir Jūsu dzimums? (V/S)\n"))
        assert dzimums == "V" or dzimums == "v" or dzimums == "S" or dzimums == "s"
        break
    except AssertionError:
        print("Lūdzu ievadiet tikai burtu, kas ir V vai S.")
        continue

# Jautā par fizisko sagatavotību
while True:
    try:
        sagatavotiba = int(input("Kāda ir fiziskā pašreizējā fiziskā sagatavoītība (1 – zema / iesācējs / ar traumām  "
                                 "– 5 – nodarbojās ar vieglatlētiku ikdienā / augsta)\n"))

        assert 1 <= sagatavotiba <= 5
        break
    except AssertionError:
        print("Lūdzu ievadiet skaitli diapazonā no 1 līdz 5.")
        continue
    except ValueError:
        print("Lūdzu ievadiet tikai naturālu skaitli")
        continue

# Jautā par distanci
while True:
    try:
        distance = str(input("LČ disciplīna veglatlētikā (S, V, G)(Sprints (60 – 400m), Vidējās distances (800 – "
                             "1500m), Garās distances (3000m+))\n"))
        assert distance == "S" or distance == "s" or distance == "V" or distance == "v" or distance == "G" or distance == "g"
        break
    except AssertionError:
        print("Lūdzu ievadiet tikai burtu, kas ir S,V vai G")
        continue

# Jautā, vai vēlas arī, lai sagatavo iesildīšanos vingrnājumu kompleksu

while True:
    try:
        vaiIesildities = str(input("Vai vēlaties sastādīt arī iesildīšanās grafiku? (J/N)\n"))
        assert vaiIesildities == "J" or vaiIesildities == "j" or vaiIesildities == "N" or vaiIesildities == "n"
        break
    except AssertionError:
        print("Lūdzu ievadiet tikai burtu, kas ir J vai N.")
        continue

# Šis tikai testam
# print("Tavs dzimums ir", dzimums)
# print("Tava fiziskā sagatavotība ir", sagatavotiba)
# print("Tava distance ir", distance)
# print("Tava atbilde par iesildīšanos ir", vaiIesildities)

print("########################################\n")

# Tiek aprēķināts, cik reižu vairāk / mazāk vingrinājumu atkārtojumi
if dzimums == 'S' or dzimums == 's':
    reizinatajs = reizinatajs * 0.85
elif dzimums == 'V' or dzimums == 'v':
    reizinatajs = 1

# Šis tikai testam
# print("Tavs reizinatajs pec dzimuma ir", reizinatajs)

if sagatavotiba == 1:
    reizinatajs = reizinatajs * 0.25
elif sagatavotiba == 2:
    reizinatajs = reizinatajs * 0.66
elif sagatavotiba == 4:
    reizinatajs = reizinatajs * 1.5
elif sagatavotiba == 5:
    reizinatajs = reizinatajs * 2

# Šis tikai testam
# print("Tavs reizinatajs pec sagatavotibas", reizinatajs)

# Šeit tiek izdrukāti vingrinājumu / iesildīšanās saraksti
if vaiIesildities == 'J':
    print("Iesildīšanās vingrinājumi:")
    print("1. Lēnā skrējienā 800m")
    print("2. Izvēzēt kājas 30-40s")
    print("3. Izstaipīt augšstilbus 30-40s")
    print("4. Iesildīt / izapļot potītes 30-40s")
    print("5. Iesildīt / izapļot gurnus 30-40s")
    print("6. Apļot rokas 10x katrā virzienā")
    print("7. Apļot elkoņus 10x katrā virzienā \n")

if distance == 's' or distance == 'S':
    print("Sprinta vingrinājumi:")
    print("1. Atspoles skrējieni 20m x 5,", round(3 * reizinatajs), "katrā virzienā.")
    print("2. Sprinta skrējieni (60 – 400m),", round(5 * reizinatajs), "atkārtojumi.")
    print("3. Lēcieni uz augšu 15x,", round(3 * reizinatajs), "atkārtojumi.")
    print("4. Ceļu pievilkšana pie krūtīm 15x ar katru kāju,", round(3 * reizinatajs), "atkārtojumi.")
    print("5. Lēcieni uz priekšu (uz tālumu) 15x,", round(3 * reizinatajs), "atkārtojumi.")

elif distance == 'v' or distance == 'V':
    print("Vidējo distanču vingrinājumi:")
    print("1. 800 – 1500m skrējiens, tam seko 800 – 1500m lēns atpūtas skrējiens,", round(3 * reizinatajs), "apļi.")
    print("2. Skrējiens balstā pie sienas 1min,", round(3 * reizinatajs), "atkārtojumi.")
    print("3. “Sēdēšana” pret  sienu ", round(3 * reizinatajs), "minūtes.")
    print("4. Pietupieni uz vienas kājas,", round(10 * reizinatajs), "ar katru kāju.")
    print("5. 800 – 1500m skrējiens uz laiku, 1 reizi.")

elif distance == 'G' or distance == 'g':
    print("Garo distanču vingrinājumi:")
    print("1. Krosa / apvidus skrējiens,", round(5 * reizinatajs), "km.")
    print("     vai")
    print("2. Riteņbraukšana,", round(30 * reizinatajs), "km.")
    print("3. Gulēšana plankā,", round((1 * (reizinatajs*2)), 1), "minūtes.")
