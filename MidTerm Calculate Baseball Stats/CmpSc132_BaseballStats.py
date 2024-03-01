class Player():

    def __init__(self, playerName, stats):
        self.playerName = playerName
        self.rawStats = stats

# Stats dictionary
AtBats = 0
Hits = 1
Double = 2
Triples = 3
Homeruns = 4
Walks = 5

def validateStats(stats):
    # Return true if stats are valid

    # All stats must have single digit
    for i in stats:
        if int(i) > 9:
            return False
    # number of Hits cannot be exceeded the # of At Bats.
    if int(stats[Hits]) > int(stats[AtBats]):
        return False
    # Doubles, Triples, and Home runs cannot exceed # of Hits.
    if (int(stats[Doubles]) + int(stats[Triples]) + int(stats[Homeruns])) > int(stats[Hits]):
        return False

    return True


def removeNewLineChar(string):
    return string.replace('\n', '')

if __name__ == "__main__":
    
    file = "D:/School/CMPSCI 132/MidTerm Calculate Baseball Stats/Lab_BaseballStats.txt"

    # Open text file and read contents
    lines = []
    with open(file) as f:
        lines = f.readlines()
        f.close()

    # Create player object
    name = None
    rawStats = []

    for i in range(len(lines)):
        # If its the first line, it is the name
        if lines[i] == lines[0]:
            name = removeNewLineChar(lines[i])
        else:
            # Check if its not empty
            if removeNewLineChar(lines[i]) != '':
                rawStats.append(removeNewLineChar(lines[i]))

    print(name)
    print(rawStats)

    cleanStats = []
    # Convert list of strings into list of lists
    for stat in rawStats:
        cleanStats.append(stat.split())

    print(cleanStats)
    
    # First validate statistics
    for stat in rawStats:
        print('\nIs stat valid?: ' + validateStats(stat))
        