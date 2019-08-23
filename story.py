# Update this text to match your story.
start = '''
You wake up one morning and find that you aren't in your bed; you aren't even in your room.
You're in the middle of a giant maze.
A sign is hanging from the ivy: "You have one hour. Don't touch the walls."
There is a hallway to your right and to your left.
'''

print(start)

print("Type 'l' to go left or 'r' to go right.") # Update to match your story.
user_input = input()
if user_input == "l":
    print("You decide to go left and the room you enter has a cake in the middle.") # Update to match your story.
    cake = input("Do you eat the cake? Yes or no?")
    if cake == "yes":
        print("The cake was poisoned. You have died. Restart the game.")
    if cake == "no":
        print("You notice a fly die after it takes a bite out of the cake. The cake was poisoned.")
        print("You managed to live! A door opens in the wall and you walk through.")
        print("You see a golden scale with a feather weighing down on one side.")
        print("In front of the scale there is a small gold block and a pile of sand on a rag.")
        print("You realize that you need to balance the scale if you want to leave")
        scale = input("Which object will you place on the other side of the scale? The gold or the sand?")
        if scale == "gold":
            print("You put the gold on to the scale.")
            print("It does not balance out")
            print("DUN DUN DUN")
            print("The ceiling collapse on you. ")
            print("Restart game.")
        if scale == "stand":
            print("You put the sand on to the scale.")
            print("It balances perfectly!")
            print("You notice two doors open. They both look like the way back home.")
            door = input("Which door do you choose? The left one or the right one?")
            if door == "left":
                print("You decided to go through the left door.")
                print("Suddenly, everything goes dark.")
                print("You wake up one morning and find that you aren't in your bed. you aren't even in your room. You're in the middle of a giant maze.")
                print("Restart the game?")
            if door == "right":
                print("You decided to go through the right door.")
                print("The shining sunlight almost blinds you. You walk out of the maze and into your bedroom.")
                print("You realize that it was all a horrible dream.")
                print("...")
                print("Or was it?")
elif user_input == "r":
    print("You choose to go right and you see a clown standing still in the middle of the room.")
    print("He's not responding to anything you do or say. There's a pie on the table in front of him.")
    pie = input("Do you want to throw the pie in his face? Yes or no?")
    if pie == "yes":
        print("The clown becomes angry! You are dead. Restart the game.")
    if pie == "no":
        print("The clown let's you live. He points at the wall and a door opens.")
        print("You see a dog. He looks like a very good boy.")
        print("He says 'Woof woof, human. If you can answer my riddle you will live.''")
        ready = input("Are you ready? Yes or no?")
        if ready == "no":
            print("Then why are you here?")
            ready = input("Are you ready now?")
        if ready == "yes":
            print("He says 'I am a odd number. Take away a letter and I become even.'")
            answer = input("What number am I?")
            if (answer == "7" or answer == "seven"):
                print("The dog barks very happily. 'You are correct!' he says.")
                print("A trap door opens below you and you fall into darkness.")
                print("You notice two doors open. They both look like the way back home.")
                door = input("Which door do you choose? The left one or the right one?")
                if door == "left":
                    print("You decided to go through the left door.")
                    print("Suddenly, everything goes dark.")
                    print("You wake up one morning and find that you aren't in your bed. you aren't even in your room. You're in the middle of a giant maze.")
                    print("Restart the game?")
                if door == "right":
                    print("You decided to go through the right door.")
                    print("The shining sunlight almost blinds you. You walk out of the maze and into your bedroom.")
                    print("You realize that it was all a horrible dream.")
                    print("...")
                    print("Or was it?")
            else:
                if (answer != "7" or answer != "seven"):
                    print("The dog growls and bites your neck. You are dead. Restart the game.")
