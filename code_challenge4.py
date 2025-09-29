print("Hello, Welcome to Manga Reader Recommender!!")
print("Answer a few questions to find Manga that you could read.")

pick_genre = input("What genre you find interesting? (Romance, Drama, Sci-fi): ")
if pick_genre.lower() == 'romance':
    duration = input("How long the the Manga should be? (Short-Length, Medium-Length, Full-Length): ")
    if duration.lower() == 'short-length':
        era = input("In which year do you prefer? (2000s, 2020s): ")
        if era == '2000s':
            print("The Manga that I would recommend is \"Honeymoon Salad\"")
        elif era == '2020s':
            print("The Manga that I would recommend is \"The Girl I Like Forgot Her Glasses\"")
        else:
            print("Sorry, I couldn't find Manga that suit to your preferences:(")
    if duration.lower() == 'medium-length':
        era = input("In which year do you prefer? (2000s, 2020s): ")
        if era == '2000s':
            print("The Manga that I would recommend is \"V.B Rose\"")
        elif era == '2020s':
            print("The Manga that I would recommend is \"In the Clear Moonlit Dusk\"")
        else:
            print("Sorry, I couldn't find Manga that suit to your preferences:(")
    if duration.lower() == 'full-length':
        era = input("In which year do you prefer? (2000s, 2020s): ")
        if era == '2000s':
            print("The Manga that I would recommend is \"Dengeki Daisy\"")
        elif era == '2020s':
            print("The Manga that I would recommend is \"Kaguya-sama: Love War\"")
        else: 
            print("Sorry, I couldn't find Manga that suit to your preferences:(")
    
if pick_genre.lower() == 'drama':
    duration = input("How long the the Manga should be? (Short-Length, Medium-Length, Full-Length): ")
    if duration.lower() == 'short-length':
        era = input("In which year do you prefer? (2000s, 2020s): ")
        if era == '2000s':
            print("The Manga that I would recommend is \"Real\"")
        elif era == '2020s':
            print("The Manga that I would recommend is \"Is Love the Answer?\"")
        else:
            print("Sorry, I couldn't find Manga that suit to your preferences:(")
    if duration.lower() == 'medium-length':
        era = input("In which year do you prefer? (2000s, 2020s): ")
        if era == '2000s':
            print("The Manga that I would recommend is \"Beck\"")
        elif era == '2020s':
            print("The Manga that I would recommend is \"Frieren: Beyond Journey's End\"")
        else:
            print("Sorry, I couldn't find Manga that suit to your preferences:(")
    if duration.lower() == 'full-length':
        era = input("In which year do you prefer? (2000s, 2020s): ")
        if era == '2000s':
            print("The Manga that I would recommend is \"Bagamond\"")
        elif era == '2020s':
            print("The Manga that I would recommend is \"The Apothecary Diaries\"")
        else:
            print("Sorry, I couldn't find Manga that suit to your preferences:(")
    
if pick_genre.lower() == 'sci-fi':
    duration = input("How long the the Manga should be? (Short-Length, Medium-Length, Full-Length): ")
    if duration.lower() == 'short-length':
        era = input("In which year do you prefer? (2000s, 2020s): ")
        if era == '2000s':
            print("The Manga that I would recommend is \"Planetes\"")
        elif era == '2020s':
            print("The Manga that I would recommend is \"Takopi's Original Sin\"")
        else:
            print("Sorry, I couldn't find Manga that suit to your preferences:(")    
    if duration.lower() == 'medium-length':
        era = input("In which year do you prefer? (2000s, 2020s): ")
        if era == '2000s':
            print("The Manga that I would recommend is \"Fullmetal Alchemist\"")
        elif era == '2020s':
            print("The Manga that I would recommend is \"Sakamoto Days\"")
        else:
            print("Sorry, I couldn't find Manga that suit to your preferences:(")
    if duration.lower() == 'full-length':
        era = input("In which year do you prefer? (2000s, 2020s): ")
        if era == '2000s':
            print("The Manga that I would recommend is \"20th Century Boys\"")
        elif era == '2020s':
            print("The Manga that I would recommend is \"Dandadan\"")
        else:
            print("Sorry, I couldn't find Manga that suit to your preferences:(")   
