class Player():

    def __init__(self, playerName, stats):
        self.playerName = playerName
        self.rawStats = stats

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
            # Check if
            rawStats.append(removeNewLineChar(lines[i]))
    
    print(name)
    print(rawStats)
        