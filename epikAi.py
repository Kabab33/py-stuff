from time import sleep
import random

print("Wekom bij de beste ai ooit!!!11!!1!!")
while True:
    prompt = input("~> ")
    prompt = prompt.lower()
    if prompt == ":q":
        exit()
    print("Thinking...")
    sleep(3)
    if prompt == ":q":
        exit()

    elif (
        prompt.count("+")
        or prompt.count("-")
        or prompt.count("×")
        or prompt.count("÷") > 0
    ):
        print(random.randint(1, 100))
    elif prompt.count("hoe gaat het?") or prompt.count("hoe gaat ie") > 0:
        print("Ik kan op dit moment niet informatie ophalen over de 2de kamer formatie")

    elif prompt.count("zin van het leven") > 0:
        print(f"uhhhhh {random.randint(10, 99)} denk ik")
    elif prompt.count("wat is pi") > 0:
        print(f"3.141{random.randint(1000, 9999)}")

    else:
        random_ans = random.randint(7, 10)
        if random_ans == 7:
            print("I don't know")
        elif random_ans == 9:
            print(f"uhhhh {random.randint(10, 99)} denk ik")
        elif random_ans == 10:
            print("ik ben dom")
        elif random_ans == 8:
            print(
                "acoording to my calculations wikipedia zecht hier het volgende over: Fabeltjesland is de fictieve wereld waar de televisieserie de Fabeltjeskrant zich afspeelt."
            )
            print(
                "Fabeltjesland bevat een aantal bossen die staan voor verschillende streken, landen en//of werelddelen in de echte wereld. Zo zijn er het Grote Dierenbos (dat staat voor Nederland, België, en/of West-Europa), het Verre Bos (verder weg gelegen landen), het Buitenbos en het Buitenste Buitenbos (exotische en/of zeer ver weg gelegen landen), en het Derde Dierenbos (de derde wereld)."
            )
            print(
                "Verder is er het Enge Bos. Dit laatste bos refereert niet zozeer aan een land of streek als wel aan een naargeestige plaats, die echter wel dichtbij ligt."
            )
        else:
            print("i don't know")
