# Stats dictionary
AtBats = 0
Hits = 1
Doubles = 2
Triples = 3
Homeruns = 4
Walks = 5


class Player():

    def __init__(self, playerName, stats):
        self.playerName = playerName
        self.stats = stats

        # Totals
        for statLine in stats:
            self.atBats = statLine[AtBats]
            self.hits = statLine[Hits]
            self.doubles = statLine[Doubles]
            self.triples = statLine[Triples]
            self.homeruns = statLine[Homeruns]
            self.walks = statLine[Walks]

def validateStats(stats):
    # Return true if stats are valid

    for statLine in stats:
        # All stats must have single digit
        for i in statLine:
            if i > 9:
                return False
        # number of Hits cannot be exceeded the # of At Bats.
        if statLine[Hits] > statLine[AtBats]:
            return False
        # Doubles, Triples, and Home runs cannot exceed # of Hits.
        if (statLine[Doubles] + statLine[Triples] + statLine[Homeruns]) > statLine[Hits]:
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

    # Change from strings to ints
    for statLine in cleanStats:
        for i in range(len(statLine)):
            statLine[i] = int(statLine[i])
    
    
    # First validate statistics. If invalid display error and exit the program
    if not validateStats(cleanStats):
        print("Error: Stats failed validation tests")
    else:
        player = Player(name, cleanStats)

