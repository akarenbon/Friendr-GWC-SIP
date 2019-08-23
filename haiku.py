import random


line1 = ["Pity to angels.","Falling, falling down.", "You can't escape Death.", "Life is full of loss.", "The daisies fall down.", "All is worth nothing."]
line2 = ["Birds are tethered to the sky.","As many stars as sinners.","Love is water. I'm drowning.", "Death is a fly. My corpse rots.", "Rain falls. Dust flies. Time goes on.", "Red roses come from heart's blood."]
line3 = ["Oh, how dull things are.","Sweet and sour life.","Immortal, alone.", "Weeping willows wilt.", "Eyes blind to sunshine.", "Sky empty of stars."]

print("...")
print("Hello, I am a haiku generator.")
print("...")
print("Would you like to read a haiku?")
print("...")

print(random.choice(line1))
print(random.choice(line2))
print(random.choice(line3))
