import random

room_items = {"floor": "pavimento", "ceiling": "soffitto", "shelf": "scaffale", "wall": "parete", "window": "finestra",
              "door": "porta", "chair": "sedia", "armchair": "poltrona", "couch": "divano", "carpet": "moquette",
              "cushions": "cuscini", "coffee table": "tavolino", "rug": "tappeto", "bed": "letto", "room": "stanza",
              "bathroom sink": "lavabo", "vacuum": "aspirapolvere"}

kitchen_items = {"kitchen": "cucina", "kitchen sink": "lavello", "fork": "forchetta", "spoon": "cuchiaio",
                 "knife": "coltello", "cup": "tazza", "plate": "piatto", "oven": "forno", "stove": "fornelli",
                 "refrigerator": "frigorifero", "microwave": "microonde", "sauce pan": "padella", "pot": "pentola",
                 "bowl": "ciotola"}

food_items = {"garlic": "aglio", "oil": "olio", "basil": "basilico", "cheese": "formaggio",
              "mozzarella": "mozzarella", "parmesan": "parmigiano", "tomato": "pomodoro", "sauce": "salsa",
              "vegetables": "verdura", "fruit": "frutta", "bread": "pane", "grain": "cereali", "liquid": "liquido",
              "powder": "polvere", "cream": "crema"}

ordinal_numbers = {"first": "primo", "second": "secondo", "third": "terzo", "fourth": "quarto", "fifth": "quinto",
                   "sixth": "sesto", "seventh": "septimo", "eighth": "ottavo", "ninth": "nono", "tenth": "decimo",
                   "eleventh": "undicesimo", "twelfth": "dodicesimo", "thirteenth": "tredicesimo",
                   "fourteenth": "quattordicesimo", "fifteenth": "quindicesimo", "sixteenth": "sedicesimo",
                   "seventeenth": "diciasettesimo", "eighteenth": "diciottesimo", "ninteenth": "diciannovesimo",
                   "twentieth": "ventesimo", "twenty-first": "ventunesimo", "twenty-second": "ventiduesimo",
                   "twenty-third": "ventitresimo", "twenty-fourth": "ventiquattresimo",
                   "twenty-fifth": "venticinquesimo", "twenty-sixth": "ventiseiesimo",
                   "twenty-seventh": "ventisettesimo", "twenty-eighth": "ventiottesimo",
                   "twenty-ninth": "ventinovesimo", "thirtieth": "trentesimo", "fourtieth": "quarantesimo",
                   "fiftieth": "cinquantesimo", "sixtieth": "sessantesimo", "seventieth": "settantesimo",
                   "eightieth": "ottantesimo", "nintieth": "novantesimo", "hundredth": "centesimo"}

direct_object_pronouns = {"1st person singular": "mi", "2nd person singular": "ti", "3rd person singular masc.": "lo",
                          "3rd person singular fem.": "la", "1st person plural": "ci", "2nd person plural": "vi",
                          "3rd person plural masc.": "li", "3rd person plural fem.": "le"}

indirect_object_pronouns = {"1st person singular": "mi", "2nd person singular": "ti",
                            "3rd person singular masc.": "gli", "3rd person singular fem.": "le",
                            "1st person plural": "ci", "2nd person plural": "vi", "3rd person plural": "loro"}

holiday_words = {"holiday": "festa", "to celebrate": "festeggiare"}

car_words = {"portiera": "door", "maniglia": "handle", "volante": "steering wheel", "il freno/i freni": "brakes",
             "finestrini": "windows", "parabrezza": "windshield", "tergicristalli": "wipers", "il faro/i fari":
             "headlights", "cruscotto": "dashboard", "paraurti": "bumper", "antenna": "antenna", "tettuccio": "roof",
             "il baule": "trunk", "le ruote": "tires", "incidentale": "accident", "assicurazione": "insurance"}

months_seasons = {"gennaio": "January", "febbraio": "February", "marzo": "March", "aprile": "April", "maggio": "May",
                  "giugno": "June", "luglio": "July", "agosto": "August", "settembre": "September", "ottobre":
                  "October", "novembre": "November", "dicembre": "December", "l'inverno": "winter", "l'estate":
                  "summer", "primavera": "spring", "lo autunno": "fall"}


def make_random(thing):
    randomized = {}
    while len(thing) != len(randomized):
        for keys in thing:
            key = random.choice(list(thing))
            if thing[key] not in randomized:
                randomized[key] = thing[key]
    return randomized


def quiz(choice):
    correct = 0
    wrong = 0
    print("Translate the word into Italian.")
    for item in choice:
        question = input(f'{item} in Italian is:\n')
        if choice[item] == question:
            print("Correct!")
            correct += 1
        else:
            print(f'Wrong. Answer is {choice[item]}')
            wrong += 1
            i = 0
            while i <= 5:
                i += 1
                review = input(f'{item} in Italian is:\n').lower()
                if choice[item] == review:
                    print("Correct!")
                else:
                    print(f'Wrong. Answer is {choice[item]}')
    else:
        print(f'Results\n'
              f'Correct: {correct}\n'
              f'Wrong: {wrong}\n'
              f'Total: {len(choice)}')


def menu():
    practice = True
    while practice:
        print("\nWelcome to Italian vocabulary practice.\nPlease enter the menu option number to begin.\n")
        print("1 - Room items quiz\n"
              "2 - Kitchen items quiz\n"
              "3 - Food items quiz\n"
              "4 - Ordinal numbers quiz\n"
              "5 - Direct Object Pronouns quiz\n"
              "6 - Indirect Object Pronouns quiz\n"
              "7 - Holiday words quiz\n"
              "8 - Car words\n"
              "9 - Months and seasons\n"
              "10 - Quit program\n")
        selection = input("Enter your selection: ")
        if selection == "1":
            print("Starting room items quiz")
            new_dict = make_random(room_items)
            quiz(new_dict)
        elif selection == "2":
            print("Starting kitchen items quiz")
            new_dict = make_random(kitchen_items)
            quiz(new_dict)
        elif selection == "3":
            print("Starting food items quiz")
            new_dict = make_random(food_items)
            quiz(new_dict)
        elif selection == "4":
            print("Starting ordinal numbers quiz")
            new_dict = make_random(ordinal_numbers)
            quiz(new_dict)
        elif selection == "5":
            print("Starting direct object pronouns quiz")
            new_dict = make_random(direct_object_pronouns)
            quiz(new_dict)
        elif selection == "6":
            print("Starting indirect object pronouns quiz")
            new_dict = make_random(indirect_object_pronouns)
            quiz(new_dict)
        elif selection == "7":
            print("Starting holiday words quiz")
            new_dict = make_random(holiday_words)
            quiz(new_dict)
        elif selection == "8":
            print("Starting car words quiz")
            new_dict = make_random(car_words)
            quiz(new_dict)
        elif selection == "9":
            print("Starting months and seasons quiz")
            new_dict = make_random(months_seasons)
            quiz(new_dict)
        elif selection == "10":
            practice = False
            print("Thank you for practicing.")
        else:
            "Please select an option."
    quit()


menu()
