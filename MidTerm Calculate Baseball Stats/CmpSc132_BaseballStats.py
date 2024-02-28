class Player():

    def __init__(self, playerName, stats):
        self.playerName = playerName
        self.rawStats = stats

def removeNewLineChar(string):
    return string.strip()

if __name__ == "__main__":
    
    file = "D:/School/CMPSCI 132/MidTerm Calculate Baseball Stats/Lab_BaseballStats.txt"

    # Open text file and read contents
    lines = []
    with open(file) as f:
        lines = f.readlines()
        f.close()
        