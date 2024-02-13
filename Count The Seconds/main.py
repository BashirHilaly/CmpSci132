
# Change for loops to while loops
def clock(militaryTime):

    totalSeconds = 0
    secondsInADay = 86400

    currentHour = 0
    currentSecond = 0
    currentMinute = 0

    amOrPM = "AM"

    while totalSeconds < (secondsInADay-1):
        totalSeconds += 1

        # Increment the seconds
        currentSecond += 1
        # Check for any display changes on the clock
        if currentSecond == 60:
            currentSecond = 0
            currentMinute += 1
        if currentMinute == 60:
            currentMinute = 0
            currentHour += 1
        if not militaryTime:
            if currentHour == 13:
                currentHour = 1
                amOrPM = "PM"
            print(f'[ {currentHour} : {currentMinute} : {currentSecond} ] {amOrPM}')
        else:
            print(f'[ {currentHour} : {currentMinute} : {currentSecond} ]')


if __name__ == "__main__":

    # True for military time 
    clock(True)