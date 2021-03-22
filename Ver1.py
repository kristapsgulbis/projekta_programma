from math import *

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

print("Tavs dzimums ir", dzimums)
print("Tava fiziskā sagatavotība ir", sagatavotiba)
print("Tava distance ir", distance)
print("Tava atbilde par iesildīšanos ir", vaiIesildities)

# Tiek aprēķināts, cik reižu vairāk / mazāk vingrinājumu atkārtojumi
if dzimums == 'S' or dzimums == 's':
    reizinatajs = reizinatajs * 0.85
elif dzimums == 'V' or dzimums == 'v':
    reizinatajs = 1

print("Tavs reizinatajs pec dzimuma ir", reizinatajs)

if sagatavotiba == 1:
    reizinatajs = reizinatajs * 0.25
elif sagatavotiba == 2:
    reizinatajs = reizinatajs * 0.66
elif sagatavotiba == 4:
    reizinatajs = reizinatajs * 1.5
elif sagatavotiba == 5:
    reizinatajs = reizinatajs * 2

print("Tavs reizinatajs pec sagatavotibas", reizinatajs)
