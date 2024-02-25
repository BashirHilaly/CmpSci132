"""
----------------------------------------------------
-- CMPSC_132, Spring 2024, Bashir Hilaly
-- Lab: Dog Class
----------------------------------------------------
"""
from datetime import datetime

class Dog():

    allowableBreeds = ["boston terrier", "italian greyhound", "basenji", "chihuahua", "bichon frise", "bolognese dog", "pomeranian", "yorkshire terrier"]

    # ageTable[0] = Age of Dog; ageTable[1] = Age in Human Years;
    ageTable = [
        [ 1, 15 ],
        [ 2, 24 ],
        [ 3, 28 ],
        [ 4, 32 ],
        [ 5, 36 ],
        [ 6, 40 ],
        [ 7, 44 ],
        [ 8, 48 ],
        [ 9, 52 ],
        [ 10, 56 ],
        [ 11, 60 ],
        [ 12, 64 ],
        [ 13, 68 ],
        [ 14, 72 ],
        [ 15, 76 ],
        [ 16, 80 ]
    ]

    """
    Initializes a Dog object with the specified attributes.

    Args:
        name (str): Name of the dog.
        gender (bool): True if male, False if female.
        breed (str): Breed of the dog.
        weight (int): Weight of the dog.
        birthdate (str): Birthdate of the dog (format: mm/dd/yyyy).
        health (int): Health status (1 = very poor, 5 = healthy).
        hasShots (bool): True if the dog has received shots, False otherwise.
        monthsInKennel (int): Number of months the dog has been in the kennel.
    """

    def __init__(self, name: str, gender: bool, breed: str, weight: int, birthdate: str, health: int, hasShots: bool, monthsInKennel: int):
        
        self.name = name

        self.gender = gender

        if breed.lower() in self.allowableBreeds:
            self.breed = breed
        else:
            print("Invalid Breed")
            self.breed = None

        self.weight = weight

        # Checks if date is valid
        if int(birthdate.split("/")[0]) >= 1 and int(birthdate.split("/")[0]) <= 12 and int(birthdate.split("/")[2]) < 2025:
            self.birthdate = birthdate
        else:
            print("Invalid Birthdate")
            self.birthdate = None

        if health >=1 and health <= 5:
            self.health = health
        else:
            print("Invalid Health")
            self.health = None

        self.hasShots = hasShots

        self.monthsInKennel = monthsInKennel
    
    def SetName(self, name):
        self.name = name

    def GetName(self):
        return self.name

    def SetWeight(self, weight):
        self.weight = weight
    
    def GetWeight(self):
        return self.weight
    
    def SetGender(self, gender):
        self.gender = gender

    def GetGender(self):
        return self.gender

    def SetBreed(self, breed):
        # Checks if the breed is in our list
        validBreed = False
        if breed.lower() in self.allowableBreeds:
            validBreed = True
        else:
            pass

        if validBreed:
            self.breed = breed
        else:
            print("Error: Invalid Breed")

    def GetBreed(self):
        return self.breed

    def SetBirthDate(self, date):
        if int(date.split("/")[0]) >= 1 and int(date.split("/")[0]) <= 12 and int(date.split("/")[2]) < 2025:
            self.birthdate = date
        else:
            print("Invalid Birthdate")
            self.birthdate = None

    def GetBirthDate(self):
        return self.birthdate

    def setHealthRating(self, health):
        # Checks if it follows: (1 = very poor, 5 = healthy)
        validHealth = False
        if health >= 1 and health <= 5:
            validHealth = True
        else:
            pass

        if validHealth:
            self.health = health
        else:
            print("Error: Invalid Health Input")

    def getHealthRating(self):
        return self.health

    def setHasShots(self, hasShots: bool):
        self.hasShots = hasShots

    def getHasShots(self):
        return self.hasShots

    def setMonthsInKennel(self, timeInKennel):
        self.monthsInKennel = timeInKennel

    def getMonthsInKennel(self):
        return self.monthsInKennel


    def InHumanYears(self):
        # based on year dog was born and current year, calculate how old the dog is, then translate that into Human Years

        humanAge = None

        # First we get the actual age from the birthday
        birthDetails = self.GetBirthDate().split('/')
        birthMonth = int(birthDetails[0])
        birthDay = int(birthDetails[1])
        birthYear = int(birthDetails[2])

        birthDate = datetime(birthYear, birthMonth, birthDay)
        today = datetime.now()

        age = int((today - birthDate).days / 365)

        for i in self.ageTable:
            if i[0] == age:
                humanAge = i[1]
        
        return humanAge

    def toString(self):
        # This method will get all of the private data and and format it into a string, and return it
        return f"Dog Information:\n" \
               f"Name: {self.name}\n" \
               f"Gender: {'Male' if self.gender else 'Female'}\n" \
               f"Breed: {self.breed}\n" \
               f"Weight: {self.weight} kg\n" \
               f"Birthdate: {self.birthdate}\n" \
               f"Health: {self.health}/5\n" \
               f"Has Shots: {'Yes' if self.hasShots else 'No'}\n" \
               f"Months in Kennel: {self.monthsInKennel}"