import Animal1
import Animal2
import Animal3

# Python Objects

pet = Animal1.Dog("Fito", 36)
sisterPet = Animal1.Dog("Scooby", 32)
brotherPet = Animal1.Dog("Sparky", 23)

catPet = Animal2.Cat("Garfield", 89)

print(pet.name, pet.age)
print(sisterPet)
pet.myfunc("Bark")

print(pet, catPet)

birdPet = Animal3.Bird("Polly", 79)

print(pet, catPet, birdPet)