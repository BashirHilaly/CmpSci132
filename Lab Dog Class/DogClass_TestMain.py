from dog import Dog


if __name__ == '__main__':
    my_dog = Dog(name="Buddy", gender=True, breed="Boston Terrier",
             weight=30, birthdate="05/15/2019", health=4,
             hasShots=True, monthsInKennel=2)

    #my_dog.setHealthRating(4)
    

    print(f"Dog Name: {my_dog.GetName()}")
    print(f"Dog Weight: {my_dog.GetWeight()} kg")
    print(f"Dog Gender: {'Male' if my_dog.GetGender() else 'Female'}")
    print(f"Dog Breed: {my_dog.GetBreed()}")
    print(f"Dog Birthdate: {my_dog.GetBirthDate()}")
    print(f"Dog Health Rating: {my_dog.getHealthRating()}/5")
    print(f"Has Shots: {'Yes' if my_dog.getHasShots() else 'No'}")
    print(f"Months in Kennel: {my_dog.getMonthsInKennel()}")
    print(f"Dog Age in Human Years: {my_dog.InHumanYears()}")
    print(my_dog.toString())  # Calls the __str__ method
