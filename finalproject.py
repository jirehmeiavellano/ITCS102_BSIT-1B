# FINAL PROJECT
import os

os.system('cls')
print("\n ─────────────────୨ৎ─────────────────")
print("|     FINAL PROJECT  |  ITCS 101     |")
print(" ─────────────────୨ৎ─────────────────")
  
while True:
    print("│─────────────────୨ৎ─────────────────│")
    print("│ SELECT FROM THE FOLLOWING OPTIONS: │")
    print("│────────────────────────────────────│")
    print("│  1 - Basic Printing                │")
    print("│  2 - Numeric Data Types            │")
    print("│  3 - Boolean Operators/Expressions │")
    print("│  4 - Conditional Statement         │")
    print("│  5 - Types Of Loops                │")
    print("│  6 - Common List Operations        │")
    print("│  7 - Exit Program                  │")
    print("│─────────────────୨ৎ─────────────────│")

    choice = eval(input("SELECT FROM THE OPTIONS ABOVE ───> "))

    if choice == 1:
        os.system('cls')
        print("\n ───────────୨ৎ───────────")
        print("|     BASIC PRINTING     |")
        print(" ───────────୨ৎ───────────")
        input("\nClick 'ENTER' to continue: ")
        os.system('cls')

        while True:
            print("A - Printing")
            print("B - Using Input")
            print("C - Using End")
            print("D - Escape Sequence")
            print("E - Case Coversion")
            print("F - Strings Formatting")
            print("G - Back\n")
            printing = input("Enter your choice ───> ").lower()

            if printing == 'a':    
                os.system('cls')
                print("\n ───────୨ৎ───────\n|    PRINTING    |\n ───────୨ৎ───────")
                print("INPUT:\n\tprint(\"This is an example of basic printing in python.\")")
                print("OUTPUT:\n\tThis is an example of basic printing in python.")
                input("\nClick 'ENTER' to select another option: ")
                os.system('cls')
                continue

            elif printing == 'b': 
                os.system('cls')
                print("\n ─────────୨ৎ──────────\n|     USING INPUT     |\n ─────────୨ৎ──────────")  
                print("INPUT:\n\tdata = input(\"Type anything here that you wanted to be printed ───> \")\n\tprint(data)")
                print("OUTPUT: ")
                data = input("\tType anything here that you wanted to be printed ───> ")
                print("       ",data)
                input("\nClick 'ENTER' to select another option: ")
                os.system('cls')
                continue

            elif printing == 'c': 
                os.system('cls')
                print("\n ────────୨ৎ─────────\n|     USING END     |\n ────────୨ৎ─────────")   
                print("INPUT:\n\tprint(\"Stay Safe, Everyone!\", end = \" \")\n\tprint(\"Keep Warm and Dry.\", end = \" \")\n\tprint(\"Goodbye👋\")")
                print("OUTPUT:\n\tStay Safe, Everyone!", end = " ")
                print("Keep Warm and Dry.", end = " ")
                print("Goodbye👋")
                input("\nClick 'ENTER' to select another option: ")
                os.system('cls')
                continue
            
            elif printing == 'd': 
                os.system('cls')
                print("\n ───────────୨ৎ────────────\n|     ESCAPE SEQUENCE     |\n ───────────୨ৎ────────────")
                input("\nClick 'ENTER' to proceed: ")
                os.system('cls')

                print("\n ───────────୨ৎ────────────\n|     NEW LINE ( \\n )     |\n ───────────୨ৎ────────────")
                print("INPUT:\n\tprint(\"Needed To Do:\\n  - Finals Project\")\nOUTPUT:\n\tNeeded To Do:\n\t  - Finals Project")
                input("\nClick 'ENTER' to proceed to the next sequence: ")
                os.system('cls')
                
                print("\n ─────────୨ৎ─────────\n|     TAB ( \\t )     |\n ─────────୨ৎ─────────")
                print("INPUT:\n\tprint(\"Subject:\\tITCS101\")\nOUTPUT:\n\tSubject:\tITCS101")
                input("\nClick 'ENTER' to proceed to the next sequence: ")
                os.system('cls')

                print("\n ─────────────────୨ৎ─────────────────\n|     SINGLE QUOTATION ( \\\' \\\' )     |\n ─────────────────୨ৎ─────────────────")
                print("INPUT:\n\tprint(\"Click \\\'ENTER\\\'\")\nOUTPUT:\n\tClick 'ENTER'")
                input("\nClick 'ENTER' to proceed to the next sequence: ")
                os.system('cls')

                print("\n ─────────────────୨ৎ─────────────────\n|     DOUBLE QUOTATION ( \\\" \\\" )     |\n ─────────────────୨ৎ─────────────────")
                print("INPUT:\n\tprint(\"\\\"God's Plan Is Worth It\\\" - Isiah 30:18\")\nOUTPUT:\n\t\"God's Plan Is Worth It\" - Isiah 30:18")
                input("\nClick 'ENTER' to select another option: ")
                os.system('cls')
                continue
                
            elif printing == 'e':  
                os.system('cls')
                print("\n ───────────୨ৎ────────────\n|     CASE CONVERSION     |\n ───────────୨ৎ────────────")
                input("\nClick 'ENTER' to proceed: ")
                os.system('cls')

                print("\n ──────────────୨ৎ───────────────\n|     LOWERCASE [ .lower() ]    |\n ──────────────୨ৎ───────────────")
                print("INPUT:\n\ttypings = input(\"Type a short sentence here ───> \").lower()\n\tprint(f\"{typings}\")")
                print("OUTPUT:")
                typings = input("\tType a short sentence here ───> ").lower()
                print(f"\t{typings}")
                input("\nClick 'ENTER' to proceed to the next sequence: ")
                os.system('cls')

                print("\n ───────────────୨ৎ───────────────\n|     UPPERCASE [ .upper() ]     |\n ───────────────୨ৎ───────────────")
                print("INPUT:\n\ttypings = input(\"Type a short sentence here ───> \").upper()\n\tprint(f\"{typings}\")")
                print("OUTPUT:")
                typings = input("\tType a short sentence here ───> ").upper()
                print(f"\t{typings}")
                input("\nClick 'ENTER' to proceed to the next sequence: ")
                os.system('cls')

                print("\n ────────────────୨ৎ───────────────\n|     TITLE CASE [ .title() ]     |\n ────────────────୨ৎ───────────────")
                print("INPUT:\n\ttypings = input(\"Type a short sentence here ───> \").title()\n\tprint(f\"{typings}\")")
                print("OUTPUT:")
                typings = input("\tType a short sentence here ───> ").title()
                print(f"\t{typings}")
                input("\nClick 'ENTER' to proceed to the next sequence: ")
                os.system('cls')

                print("\n ─────────────────────୨ৎ─────────────────────\n|     CAPITALIZED CASE [ .capitalize() ]     |\n ─────────────────────୨ৎ─────────────────────")
                print("INPUT:\n\ttypings = input(\"Type a short sentence here ───> \").capitalize()\n\tprint(f\"{typings}\")")
                print("OUTPUT:")
                typings = input("\tType a short sentence here ───> ").capitalize()
                print(f"\t{typings}")
                input("\nClick 'ENTER' to select another option: ")
                os.system('cls')
                continue

            elif printing == 'f':  
                os.system('cls')
                print("\n ───────────୨ৎ───────────\n|    STRING FORMATTING    |\n ───────────୨ৎ────────────")
                print("INPUT:\n\tfrstname = input(\"Type your First Name here ───> \").title()\n\tmddlname = input(\"Type your Middle Name here ───> \").title()\n\tsurname = input(\"Type your Surname here ───> \").title()\n\tnickname = input(\"Type your Nickname here ───> \").title()\n\tprint(f\"Your government name is {frstname} {mddlname} {surname}. But I would just call you {nickname} for short ;)\")")
                print("OUTPUT: ")
                frstname = input("\tType your First Name here ───> ").title()
                mddlname = input("\tType your Middle Name here ───> ").title()
                surname = input("\tType your Surname here ───> ").title()
                nickname = input("\tType your Nickname here ───> ").title()
                print(f"\tYour government name is {frstname} {mddlname} {surname}. But I would just call you {nickname} for short ;)")
                input("\nClick 'ENTER' to select another option: ")
                os.system('cls')
                continue
            
            elif printing == 'g':  
                os.system('cls') 
                break
            else:
                os.system('cls')
                print("INVALID CHOICE, RE-ENTER YOUR CHOICE\n")
                continue
        continue

    elif choice == 2:
        os.system('cls')
        print("\n ─────────────୨ৎ─────────────")
        print("|     NUMERIC DATA TYPES     |")
        print(" ─────────────୨ৎ─────────────")
        input("\nClick 'ENTER' to continue: ")
        os.system('cls')

        while True:
            print("A - Classification Of Data")
            print("B - Arithmethic Operations")
            print("C - Back\n")
            numerical = input("Enter your choice ───> ").lower()

            if numerical == 'a':
                os.system('cls')
                print("\n ───────────────୨ৎ───────────────\n|     CLASSIFICATION OF DATA     |\n ───────────────୨ৎ───────────────")
                print("INPUT:\n\tnumeric = eval(input(\"Type any numerical data here ───> \n\tprint(\"The name of data type is \", type(numeric))")
                print("OUTPUT: ")
                numeric = eval(input("\tType any numerical data here ───> "))
                print("\tThe name of data type is ", type(numeric))
                input("\nClick 'ENTER' to select another option: ")
                os.system('cls')
                continue

            elif numerical == 'b':
                os.system('cls')
                print("\n ───────────────୨ৎ───────────────\n|     ARITHMETHIC OPERATIONS     |\n ───────────────୨ৎ───────────────")
                input("\nClick 'ENTER' to proceed: ")
                os.system('cls')

                print("\n ──────────୨ৎ──────────\n|    ADDITION ( + )    |\n ──────────୨ৎ──────────")
                print("INPUT:\n\tn1 = eval(input(\"Enter the first number: \"))\n\tn2 = eval(input(\"Enter the second number: \"))\n\tprint(\"The sum of\", n1, \"and\", n2,\"is\", n1 + n2)")
                print("OUTPUT: ")
                n1 = eval(input("\tEnter the first number: ")) 
                n2 = eval(input("\tEnter the second number: ")) 
                print("\tThe sum of", n1, "and", n2,"is", n1 + n2) 
                input("\nClick 'ENTER' to proceed to the next operation: ")
                os.system('cls')

                print("\n ───────────୨ৎ───────────\n|    SUBTRACTION ( - )   |\n ───────────୨ৎ───────────")
                print("INPUT:\n\tn1 = eval(input(\"Enter the first number: \"))\n\tn2 = eval(input(\"Enter the second number: \"))\n\tprint(\"The difference of\", n1, \"and\", n2, \"is\", n1 - n2)")
                print("OUTPUT: ")
                n1 = eval(input("\tEnter the first number: ")) 
                n2 = eval(input("\tEnter the second number: ")) 
                print("\tThe difference of", n1, "and", n2, "is", n1 - n2) 
                input("\nClick 'ENTER' to proceed to the next operation: ")
                os.system('cls')

                print("\n ─────────────୨ৎ─────────────\n|    MULTIPLICATION ( * )    |\n ─────────────୨ৎ─────────────")
                print("INPUT:\n\tn1 = eval(input(\"Enter the first number: \"))\n\tn2 = eval(input(\"Enter the second number: \"))\n\tprint(\"The product of\", n1, \"and\", n2, \"is\", n1 * n2)")
                print("OUTPUT: ")
                n1 = eval(input("\tEnter the first number: ")) 
                n2 = eval(input("\tEnter the second number: ")) 
                print("\tThe product of", n1, "and", n2, "is", n1 * n2) 
                input("\nClick 'ENTER' to proceed to the next operation: ")
                os.system('cls')

                print("\n ──────────୨ৎ──────────\n|    DIVISION ( / )    |\n ──────────୨ৎ──────────")
                print("INPUT:\n\tn1 = eval(input(\"Enter the first number: \"))\n\tn2 = eval(input(\"Enter the second number: \"))\n\tprint(\"The quotient of\", n1, \"and\", n2, \"is\", n1 / n2)")
                print("OUTPUT: ")
                n1 = eval(input("\tEnter the first number: ")) 
                n2 = eval(input("\tEnter the second number: ")) 
                print("\tThe quotient of", n1, "and", n2, "is", n1 / n2) 
                input("\nClick 'ENTER' to proceed to the next operation: ")
                os.system('cls')

                print("\n ────────────୨ৎ────────────\n|    EXPONENTIAL ( ** )    |\n ────────────୨ৎ────────────")
                print("INPUT:\n\tn1 = eval(input(\"Enter the first number: \"))\n\tn2 = eval(input(\"Enter the second number: \"))\n\tprint(n1, \"exponent by\", n2, \"is\", n1**n2)")
                print("OUTPUT: ")
                n1 = eval(input("\tEnter the first number: ")) 
                n2 = eval(input("\tEnter the second number: "))                
                print("       ", n1, "exponent by", n2, "is", n1**n2) 
                input("\nClick 'ENTER' to proceed to the next operation: ")
                os.system('cls')
                
                print("\n ──────────୨ৎ──────────\n|     MODULUS ( % )    |\n ──────────୨ৎ──────────")
                print("INPUT:\n\tn1 = eval(input(\"Enter the first number: \"))\n\tn2 = eval(input(\"Enter the second number: \"))\n\tprint(n1, \"and\", n2, \"is\", n1 % n2)")
                print("OUTPUT: ")
                n1 = eval(input("\tEnter the first number: ")) 
                n2 = eval(input("\tEnter the second number: "))  
                print("\tThe remainder of", n1, "and", n2, "is", n1 % n2) 
                input("\nClick 'ENTER' to proceed to the next operation: ")
                os.system('cls')

                print("\n ─────────────୨ৎ─────────────\n|    FLOOR DIVISION ( // )   |\n ─────────────୨ৎ─────────────")
                print("INPUT:\n\tn1 = eval(input(\"Enter the first number: \"))\n\tn2 = eval(input(\"Enter the second number: \"))\n\tprint(n1, \"and\", n2, \"is\", n1 // n2)")
                print("OUTPUT: ")
                n1 = eval(input("\tEnter the first number: ")) 
                n2 = eval(input("\tEnter the second number: "))  
                print("\tThe floor division of", n1, "and", n2, "is", n1 // n2)
                input("\nClick 'ENTER' to select another option: ")
                os.system('cls')
                continue

            elif numerical == 'c':  
                os.system('cls') 
                break
            else:
                os.system('cls')
                print("INVALID CHOICE, RE-ENTER YOUR CHOICE\n")
                continue
        continue

    elif choice == 3:
        os.system('cls')
        print("\n ───────────────────୨ৎ───────────────────")
        print("|     BOOLEAN OPERATIONS/EXPRESSIONS     |")
        print(" ───────────────────୨ৎ───────────────────")
        input("\nClick 'ENTER' to continue: ")
        os.system('cls')

        while True:
            print("A - Relational Operations")
            print("B - Logical Operations")
            print("C - Back\n")
            loops = input("Enter your choice ───> ").lower()

            if loops == 'a':    
                os.system('cls')
                print("\n ─────────────୨ৎ─────────────\n|    RELATIONAL OPERATIONS   |\n ─────────────୨ৎ─────────────")
                input("\nClick 'ENTER' to proceed: ")
                os.system('cls')

                print("\n ───────────୨ৎ────────────\n|     LESS THAN ( < )     |\n ───────────୨ৎ────────────")            
                print("INPUT:\n\tcmpr1 = input(\"Put any number here ───> \")\n\tcmpr2 = input(\"Put any number here ───> \")\n\tprint(f\"Example: {cmpr1} < {cmpr2}\\t|\\tResult: {cmpr1 < cmpr2}\")")
                print("OUTPUT: ")
                cmpr1 = input("\tPut any number here ───> ")
                cmpr2 = input("\tPut any number here ───> ")
                print(f"\tExample: {cmpr1} < {cmpr2}\t|\tResult: {cmpr1 < cmpr2}" )
                input("\nClick 'ENTER' to proceed to the next sequence: ")
                os.system('cls') 

                print("\n ───────────୨ৎ────────────\n|     GREATER THAN ( > )     |\n ─────────────୨ৎ─────────────")
                print("INPUT:\n\tcmpr1 = input(\"Put any number here ───> \")\n\tcmpr2 = input(\"Put any number here ───> \")\n\tprint(f\"Example: {cmpr1} > {cmpr2}\\t|\\tResult: {cmpr1 > cmpr2}\")")
                print("OUTPUT: ")
                cmpr1 = input("\tPut any number here ───> ")
                cmpr2 = input("\tPut any number here ───> ")
                print(f"\tExample: {cmpr1} > {cmpr2}\t|\tResult: {cmpr1 > cmpr2}" )
                input("\nClick 'ENTER' to proceed to the next sequence: ")
                os.system('cls')

                print("\n ──────────────────୨ৎ──────────────────\n|     LESS THAN OR EQUAL TO ( <= )     |\n ──────────────────୨ৎ──────────────────")
                print("INPUT:\n\tcmpr1 = input(\"Put any number here ───> \")\n\tcmpr2 = input(\"Put any number here ───> \")\n\tprint(f\"Example: {cmpr1} <= {cmpr2}\\t|\\tResult: {cmpr1 <= cmpr2}\")")
                print("OUTPUT: ")
                cmpr1 = input("\tPut any number here ───> ")
                cmpr2 = input("\tPut any number here ───> ")
                print(f"\tExample: {cmpr1} <= {cmpr2}\t|\tResult: {cmpr1 <= cmpr2}" )
                input("\nClick 'ENTER' to proceed to the next sequence: ")
                os.system('cls') 
                
                print("\n ───────────────────୨ৎ────────────────────\n|     GREATER THAN OR EQUAL TO ( >= )     |\n ───────────────────୨ৎ────────────────────")
                print("INPUT:\n\tcmpr1 = input(\"Put any number here ───> \")\n\tcmpr2 = input(\"Put any number here ───> \")\n\tprint(f\"Example: {cmpr1} >= {cmpr2}\\t|\\tResult: {cmpr1 >= cmpr2}\")")
                print("OUTPUT: ")
                cmpr1 = input("\tPut any number here ───> ")
                cmpr2 = input("\tPut any number here ───> ")
                print(f"\tExample: {cmpr1} >= {cmpr2}\t|\tResult: {cmpr1 >= cmpr2}" )
                input("\nClick 'ENTER' to proceed to the next sequence: ")
                os.system('cls') 

                print("\n ──────────୨ৎ──────────\n|     EQUAL ( == )     |\n ──────────୨ৎ──────────")
                print("INPUT:\n\tcmpr1 = input(\"Put any number here ───> \")\n\tcmpr2 = input(\"Put any number here ───> \")\n\tprint(f\"Example: {cmpr1} == {cmpr2}\\t|\\tResult: {cmpr1 == cmpr2}\")")
                print("OUTPUT: ")
                cmpr1 = input("\tPut any number here ───> ")
                cmpr2 = input("\tPut any number here ───> ")
                print(f"\tExample: {cmpr1} == {cmpr2}\t|\tResult: {cmpr1 == cmpr2}" )
                input("\nClick 'ENTER' to proceed to the next sequence: ")
                os.system('cls') 

                print("\n ────────────୨ৎ────────────\n|     NOT EQUAL ( != )     |\n ────────────୨ৎ────────────")
                print("INPUT:\n\tcmpr1 = input(\"Put any number here ───> \")\n\tcmpr2 = input(\"Put any number here ───> \")\n\tprint(f\"Example: {cmpr1} != {cmpr2}\\t|\\tResult: {cmpr1 != cmpr2}\")")
                print("OUTPUT: ")
                cmpr1 = input("\tPut any number here ───> ")
                cmpr2 = input("\tPut any number here ───> ")
                print(f"\tExample: {cmpr1} != {cmpr2}\t|\tResult: {cmpr1 != cmpr2}" )
                input("\nClick 'ENTER' to select another option: ")
                os.system('cls')
                continue

            elif loops == 'b':    
                os.system('cls')
                print("\n ─────────────୨ৎ─────────────\n|     LOGICAL OPERATIONS     |\n ─────────────୨ৎ─────────────")
                input("\nClick 'ENTER' to proceed: ")
                os.system('cls')

                print("\n ──────୨ৎ───────\n|   AND (and)   |\n ──────୨ৎ───────")
                print("INPUT: \n\tprint((101 > 59) and (44 < 34))\n\tprint((3478 > 2271) and (261 < 789))")
                print("OUTPUT: ")
                print("       ",(101 > 59) and (44 < 34))
                print("       ",(3478 > 2271) and (261 < 789))
                input("\nClick 'ENTER' to proceed to the next sequence: ")
                os.system('cls')

                print("\n ─────୨ৎ──────\n|   OR (or)   |\n─────୨ৎ──────") 
                print("INPUT: \n\tprint((972 > 234) or (261 < 789))\n\tprint((23 > 59) or (44 < 34))")
                print("OUTPUT: ")
                print("       ",(972 > 234) or (261 < 789))
                print("       ",(23 > 59) or (44 < 34))
                input("\nClick 'ENTER' to proceed to the next sequence: ")
                os.system('cls')

            
                print("\n ──────୨ৎ───────\n|   NOT (not)   |\n ──────୨ৎ───────")
                print("INPUT: \n\tprint(not (101 > 59) and (44 < 34))\n\tprint(not (972 > 234) or (261 < 789))")
                print("OUTPUT: ")
                print("       ",not (101 > 59) and (44 < 34))
                print("       ",not (972 > 234) or (261 < 789))
                input("\nClick 'ENTER' to select another option: ")
                os.system('cls')
                continue

            elif loops == 'c':  
                os.system('cls') 
                break
            else:
                os.system('cls')
                print("INVALID CHOICE, RE-ENTER YOUR CHOICE\n")
                continue
        continue

    elif choice == 4: 
        os.system('cls')
        print("\n ──────────────୨ৎ───────────────")
        print("|     CONDITIONAL STATEMENT     |")
        print(" ──────────────୨ৎ───────────────")
        input("\nClick 'ENTER' to proceed: ")
        os.system('cls')

        print("\n ──────────────୨ৎ───────────────\n|     CONDITIONAL STATEMENT     |\n ──────────────୨ৎ───────────────")
        print("\nINPUT:\n\tgwa = input(\"Enter Your SHS GWA ───> \")\n\tif int(gwa) <= 100 and int(gwa) >= 90:\n\t    print(\"Your Performance is Outstanding!\")\n\telif int(gwa) <= 89 and int(gwa) >= 85: \n\t    print(\"Your Performance is Very Satisfactory\")")
        print("\telif int(gwa) <= 84 and int(gwa) >= 80: \n\t    print(\"Your Performance is Satisfactory\")\n\telif int(gwa) <= 79 and int(gwa) >= 75: \n\t    print(\"Your Performance is Fairly Satisfactory\")\n\telif int(gwa) <= 74: \n\t    print(\"Your Performance Did Not Meet Expectation :(\") \n\telse:\n\t    print(\"Invalid Syntax\")") 
        print("OUTPUT:")
        gwa = input("\tEnter Your SHS GWA ───> ")
        if int(gwa) <= 100 and int(gwa) >= 90:
            print("\tYour Performance is Outstanding!")
        elif int(gwa) <= 89 and int(gwa) >= 85: 
            print("\tYour Performance is Very Satisfactory")
        elif int(gwa) <= 84 and int(gwa) >= 80:
            print("\tYour Performance is Satisfactory")
        elif int(gwa) <= 79 and int(gwa) >= 75:
            print("\tYour Performance is Fairly Satisfactory")
        elif int(gwa) <= 74: 
            print("\tYour Performance Did Not Meet Expectation :(")
        else:
            print("\tInvalid Syntax")
        input("\nClick 'ENTER' to select another option: ")
        os.system('cls')
        continue

    elif choice == 5:
        os.system('cls')
        print("\n ──────────୨ৎ──────────")
        print("|    TYPES OF LOOPS    |")
        print(" ──────────୨ৎ──────────")
        input("\nClick 'ENTER' to continue: ")
        os.system('cls')

        while True:
            print("A - For Loops")
            print("B - Ascending and Descending Loop")
            print("C - Nested For Loops")
            print("D - While Loops")
            print("E - Back\n")
            loops = input("Enter your choice ───> ").lower()

            if loops == 'a':    
                os.system('cls')
                print("\n ───────୨ৎ────────\n|    FOR LOOPS    |\n ───────୨ৎ────────")
                print("INPUT:\n\tprt = input(\"Type anything that you want to be printed ───> \")\n\ttimes = eval(input(\"How many times you want? \"))\n\tfor h in range(1, times + 1, 1):\n\t    print(h,\"-\", prt)")
                print("OUTPUT:")
                prt = input("\tType anything that you wanted to be printed ───> ")
                times = eval(input("\tHow many times you want? "))
                for h in range(1, times + 1, 1):
                    print("\t",h,"-", prt)
                input("\nClick 'ENTER' to proceed to the next loop: ")
                os.system('cls') 
                continue

            if loops == 'b':    
                os.system('cls')
                print("\n ──────────୨ৎ──────────\n|    ASCENDING LOOP    |\n ──────────୨ৎ──────────")
                print("INPUT:\n\tcount = eval(input(\"Until what number you want to count? \"))\n\tfor m in range(1, count + 1, 1):\n\t    print(m)")
                print("OUTPUT:")
                count = eval(input("\tUntil what number you want to count? "))
                for m in range(1, count + 1, 1):
                    print("\t",m)
                input("\nClick 'ENTER' to proceed to the next loop: ")
                os.system('cls')

                print("\n ──────────୨ৎ──────────\n|   DESCENDING LOOP    |\n ──────────୨ৎ──────────")
                print("INPUT:\n\tcountdown = eval(input(\"From what number you want to start the countdown? \"))\n\tfor e in range(countdown, 0, -1):\n\t    print(e)")
                print("OUTPUT:")
                countdown = eval(input("\tFrom what number you want to start the countdown? "))
                for e in range(countdown, 0, -1):
                    print("\t",e)
                input("\nClick 'ENTER' to proceed to the next loop: ")
                os.system('cls')
                continue
            
            if loops == 'c':    
                os.system('cls')
                print("\n ───────────୨ৎ────────────\n|     NESTED FOR LOOP     |\n ───────────୨ৎ────────────")
                print("INPUT:\n\tfor j in range(1, 11, 1):\n\t    for i in range(10, j, -1):\n\t        print(\" \", end = \" \")\n\t    for r in range(1, j, 1):\n\t        print(\"^\", end = \" \")\n\t    for a in range(1, j + 1, 1):\n\t        print(\"^\", end = \" \")\n\t    print()")
                print("OUTPUT:")
                for j in range(1, 11, 1):
                    for i in range(10, j, -1):
                        print(" ", end = " ")
                    for r in range(1, j, 1):
                        print("^", end = " ")
                    for a in range(1, j + 1, 1):
                        print("^", end = " ")
                    print()
                input("\nClick 'ENTER' to proceed to the next loop: ")
                os.system('cls')
                continue

            elif loops == 'd':  
                os.system('cls') 
                print("\n ────────୨ৎ────────\n|    WHILE LOOP    |\n ────────୨ৎ────────")
                print("INPUT: \n\tprint(\"Welcome to K-Drama Lister Program!\\n\")\n\tanime = []\n\twhile True:\n\t    title = input(\"Enter the Title of a K-Drama (then just type \'Exit\' to stop): \").title()\n\t    print(f\"'{title}' has been added to your list\")\n\t    if title == \'Exit\':\n\t\tprint(\"You have exited the K-Drama Lister Program ;)\\n\")\n\t\tbreak\n\t    kdrama.append(title)")
                print("\tprint(\"This are the list of the K-Drama title you have entered: \")\n\tnumbering = 0\n\tfor list in anime: \n\t    numbering += 1\n\t    print(f\"  {numbering}.) {list}\")")
                print("OUTPUT: \n\tWelcome to K-Drama Lister Program!\n")
                kdrama = []
                while True:
                    title = input("\tEnter the Title of a K-Drama (then just type 'Exit' to stop): ").title()
                    print(f"\t'{title}' has been added to your list")
                    if title == 'Exit':
                        print("\tYou have exited the K-Drama Lister Program ;)\n")
                        break
                    kdrama.append(title)

                print("\tThis are the list of the K-Drama title you have entered:")
                numbering = 0
                for list in kdrama: 
                    numbering += 1
                    print(f"\t  {numbering}.) {list}")
                input("\nClick 'ENTER' to select another option: ")
                os.system('cls')
                continue

            elif loops == 'e':  
                os.system('cls') 
                break
            else:
                os.system('cls')
                print("INVALID CHOICE, RE-ENTER YOUR CHOICE\n")
                continue
        continue
 
    elif choice == 6:
        os.system('cls')
        print("\n ──────────────୨ৎ──────────────")
        print("|    COMMON LIST OPERATIONS    |")
        print(" ──────────────୨ৎ──────────────")
        input("\nClick 'ENTER' to continue: ")
        os.system('cls')

        proguage = ['Python', 'JavaScript', 'TypeScript', 'SQL', 'C#', 'Perl']

        print("\n ─────────────────୨ৎ─────────────────\n|    APPEND [ list.append(item) ]    |\n ─────────────────୨ৎ─────────────────")
        print("INPUT:\n\tproguage = ['Python', 'JavaScript', 'TypeScript', 'SQL', 'C#', 'Perl']\n\tproguage.append('Bash/Shell')\n\tprint(proguage)")
        proguage.append('Bash/Shell')
        print("OUTPUT:\n       ",proguage)
        input("\nClick 'ENTER' to proceed to the next operation: ")
        os.system('cls')

        print("\n ────────────────────୨ৎ────────────────────\n|    INSERT [ list.insert(index, item) ]   |\n ────────────────────୨ৎ────────────────────")
        print("INPUT:\n\tproguage = ['Python', 'JavaScript', 'TypeScript', 'SQL', 'C#', 'Perl, Bash/Shell']\n\tproguage.insert(5, 'CSS')\n\tprint(proguage)")
        proguage.insert(5, 'CSS')
        print("OUTPUT:\n       ",proguage)
        input("\nClick 'ENTER' to proceed to the next operation: ")
        os.system('cls')

        print("\n ─────────────────୨ৎ─────────────────\n|    REMOVE [ list.remove(item) ]    |\n ─────────────────୨ৎ─────────────────")
        print("INPUT:\n\tproguage = ['Python', 'JavaScript', 'TypeScript', 'SQL', 'C#', 'CSS', 'Perl', 'Bash/Shell']\n\tproguage.remove('SQL')\n\tprint(proguage)")
        proguage.remove('SQL')
        print("OUTPUT:\n       ",proguage)
        input("\nClick 'ENTER' to proceed to the next operation: ")
        os.system('cls')

        print("\n ──────────────୨ৎ──────────────\n|    POP [ list.pop(index) ]   |\n ──────────────୨ৎ──────────────")
        print("INPUT:\n\tproguage = ['Python', 'JavaScript', 'TypeScript', 'C#', 'CSS', 'Perl', 'Bash/Shell']\n\tproguage.pop(2)\n\tprint(proguage)")
        proguage.pop(2)
        print("OUTPUT:\n       ",proguage)
        input("\nClick 'ENTER' to proceed to the next operation: ")
        os.system('cls')

        print("\n ────────────────୨ৎ────────────────\n|    REVERSE [ list.reverse() ]    |\n ────────────────୨ৎ────────────────")
        print("INPUT:\n\tproguage = ['Python', 'JavaScript', 'C#', 'CSS', 'Perl', 'Bash/Shell']\n\tproguage.reverse()\n\tprint(proguage)")
        proguage.reverse()
        print("OUTPUT:\n       ",proguage)
        input("\nClick 'ENTER' to proceed to the next operation: ")
        os.system('cls')

        print("\n ─────────────୨ৎ─────────────\n|    SORT [ list.sort() ]    |\n ─────────────୨ৎ─────────────")
        print("INPUT:\n\tproguage = ['Bash/Shell', 'Perl', 'CSS', 'C#', 'JavaScript', 'Python']\n\tproguage.sort()\n\tprint(proguage)")
        proguage.sort()
        print("OUTPUT:\n       ",proguage)
        input("\nClick 'ENTER' to proceed to the next operation: ")
        os.system('cls')

        print("\n ─────────────୨ৎ─────────────\n|    LENGTH [ len(list) ]    |\n ─────────────୨ৎ─────────────")
        print("INPUT:\n\tproguage = ['Bash/Shell', 'C#', 'CSS', 'JavaScript', 'Perl', 'Python']\n\tprint(len(proguage))")
        print("OUTPUT:\n       ",len(proguage))
        input("\nClick 'ENTER' to select another option: ")
        os.system('cls')
        continue

    elif choice == 7:
        os.system('cls')
        print("SYSTEM EXIT")
        break
    else:
        print("INVALID CHOICE, RE-ENTER YOUR CHOICE\n")
        continue

