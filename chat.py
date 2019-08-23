import random
def space():
    print("~")

def restart():
    poemList()
    didUlike()

def Haiku():
    line1 = ["Run from your feelings.", "Pity to angels.","Falling, falling down.", "You can't escape Death.", "Life is full of loss.", "The daisies fall down.", "All is worth nothing."]
    line2 = ["Escape this unfeeling life.", "Birds are tethered to the sky.","As many stars as sinners.","Love is water. I'm drowning.", "Death is a fly. My corpse rots.", "Rain falls. Dust flies. Time goes on.", "Red roses come from heart's blood."]
    line3 = ["Only time will tell.", "Oh, how dull things are.","Sweet and sour life.","Immortal, alone.", "Weeping willows wilt.", "Eyes blind to sunshine.", "Sky empty of stars."]
    print(random.choice(line1))
    print(random.choice(line2))
    print(random.choice(line3))

def SadPoems():
    def IfAndThen():
        print("If and Then")
        print("...")
        print("If love be a drop of water")
        print("Then I drown in a sea of lies.")
        print("Sugar coated honey combs")
        print("Block out my bitter cries.")
        print("...")
        print("If hope be a shining star")
        print("Then my home is in the city.")
        print("A stray dies in the alley,")
        print("Arousing no one's pity.")
        print("...")
        print("If joy be a warm embrace")
        print("Then my hands are the coldest ice.")
        print("I have played the gambler's game;")
        print("I have rolled the worst of dice.")
        print("...")
        print("If death be a horde of flies")
        print("Then my corpse is rotting much.")
        print("A leaf falls down gracefully,")
        print("Missing the tree's loving touch.")
        space()

    def WillowRed():
        print("Willow Red")
        print("...")
        print("In a certain city with a name long forgotten,")
        print("Down a dreary road with a sidewalk long rotten,")
        print("Over there sits a hospital they call Willow Red")
        print("Where the bodies are breathing but the people are dead.")
        print("...")
        print("Within, she had a child. She was told it would kill her.")
        print("They cherished the life and called her a killer.")
        print("She birthed the child and died in the act.")
        print("The baby followed after in two hours, exact.")
        print("...")
        print("And so Mary died along with her lamb.")
        print("But such things are the norm in the home of the damned.")
        print("...")
        print("The surgeon, his hands, had touched many hearts.")
        print("He loved that his own would hunger such parts.")
        print("He ate and he ate ‘til he could stuff no more.")
        print("Despite the hearts eaten, a heartless carnivore.")
        print("...")
        print("And so Judas continued for years, months and days,")
        print("Yet he remains in the hospital as none there ever prays.")
        print("...")
        print("The inseparable twins named Abel and Cain,")
        print("Their hands held together throughout all the pain.")
        print("But one wanted freedom, to let go of the other.")
        print("And so Cain betrayed and severed his brother.")
        print("...")
        print("Both siblings passed in their hospital room.")
        print("Of course, at this place, they all meet their doom.")
        print("...")
        print("The windows are stained with a color too rusty.")
        print("The walls chip down slowly as their dull eyes grow dusty.")
        print("You can strive to live and then you can die.")
        print("You cannot be both in one instance or try.")
        print("...")
        print("But at this old hospital named Willow Red,")
        print("The bodies are breathing and the people are dead.")
        space()

    print("I have a few sad poems.")
    space()
    print("1- If and Then")
    print("2- Willow Red")
    space()
    sadChoose = input("Type in the number you want.")
    space()
    if sadChoose == "1":
        IfAndThen()
    elif sadChoose == "2":
        WillowRed()
    else:
        space()
        print("Pick a number that's actually there.")
        space()
        SadPoems()

def greet():
    space()
    print("Hello, my name is ChatPy.")
    space()
    name = input("What is your name?")
    space()
    print("It's nice to meet you,", name, ".")
    space()

def poemLike():
    like = input("Do you like poems? Yes or no?")
    if like == "yes":
        space()
        print("That's great! I like poems, too.")
        space()
    elif like == "no":
        space()
        print("Oh. You make me sad.")
        space()
        print("But you know what? I don't care. I'm a poem bot.")
        space()
    else:
        space()
        print("Yes or no? I'm a bot made by a teenager. I don't do things like 'maybe'.")
        poemLike()

def poemList():
    print("I know a few poems.")
    space()
    print("1- Sad ones")
    print("2- Happy ones")
    print("3- Vague haikus")
    space()
    poems = input("Type in the corresponding number of type of poem you want me to recite.")

    if poems == "1":
        space()
        print("You chose the sad ones.")
        space()
        SadPoems()
        space()

    elif poems == "2":
        space()
        print("Sorry. I lied. I don't have any happy poems.")
        space()
        SadPoems()
        space()

    elif poems == "3":
        space()
        print("You chose the vague haiku.")
        space()
        Haiku()
        space()
        print("These haikus are made from lines that are randomly generated and put together.")
        space()

    else:
        space()
        print("Please pick a number from the list.")
        space()
        poemList()

def didUlike():
    userInput = input("Did you like my poem? Yes or no?")
    if userInput == "yes":
        space()
        print("Thank you very much!")
        space()
    elif userInput == "no":
        space()
        print("Sorry.")
        space()
    another = input("Would you like another poem? Yes or no?")
    if another == "yes":
        restart()
    elif another == "no":
        space()
        print("I guess this is goodbye then.")

greet()

poemLike()

poemList()

didUlike()
