class Team:  # The Teams are stored twice (sorted by name and standings)
    """ The class Team has two static attributes named standings[] and team{}. The list standings contains
        all teams ordered by the amount of wins they received. To get the actual amount of wins you can convert
        the Team into a String and the amount will occur in that string. Alternatively you can get the length of
        standings by len(standings). The dictionary teams also contains all teams sorted by names. """
    standings = []  # Save standings in one List
    teams = {}  # Save all Teams in one dict

    def __init__(self, name):  # A new Team gets a name and no wins. Has to be in arr standings and teams
        """__init__(self, name) : constructor of Team. Initialises a name and the array _wins. _wins does not
              contain any values because the team did not win yet."""
        self._name = name
        self._wins = []
        Team.standings.append(self)
        Team.teams[name] = self

    def __str__(self):  # prints Team like: "name: *** #wins = * won against: ***"
        """__str__(self) converts an object from type Team into a string: "name: [NAME] \t #wins = __ won against: \
        [-wins]" """
        wonAgainst = ""
        for j in range(len(self._wins)):
            wonAgainst += self._wins[j].getName() + Team.formatName(self._wins[j].getName()) + " | "
        wonAgainst = wonAgainst[0:-2]
        return "name: " + self._name + Team.formatName(self._name) + "\t #wins = " + \
               str(len(self._wins)) + "\t won against: " + wonAgainst

    def addWin(self, other):  # Adds Team (other) that self won against to _wins; Expects String of the Team that losses
        assert self._name != other, "A Team can't win against themselves!"
        other = other.strip()
        self._wins.append(Team.teams[other])
        Team.sortStandings()

    def getWins(self):
        wins = list(map(lambda x: str(x), self._wins))
        return wins

    def getName(self):
        return self._name

    @staticmethod
    def sortStandings():  # Sorts the list
        Team.standings.sort(key=lambda x: len(x.getWins()), reverse=True)

    @staticmethod
    def printStandings():  # Prints List of standings
        if len(Team.standings) == 0:
            print("No Team inserted!")
            return
        for i in range(len(Team.standings) - 1):
            print("0" + str(i + 1), ". ", Team.standings[i], sep="")
        print("10. ", Team.standings[9], sep="")

    @staticmethod
    def formatName(name):  # Some Team have len(name) = 2; Most have len(name) = 3 - formatName adds " " before name
        if len(name) == 2:
            return " "
        return ""

    @staticmethod
    def saveStandings(filename):
        with open(filename, "w") as f:
            for i in range(len(Team.standings) - 1):
                f.write("0" + str(i + 1) + ". " + str(Team.standings[i]) + "\n")
            f.write("10. " + str(Team.standings[9]))

    @staticmethod
    def initialise(filename):  # inserts teams with standing into program
        with open(filename, "r") as f:
            lines = f.readlines()
            for i in lines:  # Create all Teams in the Tournament
                startName = i.find("name: ") + len("name: ")
                name = i[startName:startName + 3].strip(" ")
                Team(name)
            for k in lines:  # Add ._wins-List for all Teams
                startName = k.find("name: ") + len("name: ")
                name = k[startName:startName + 4].strip()
                startWins = k.find("won against: ") + len("won against: ")
                if startWins < 39:  # In case Team did not win yet. Don't add anything to wins[]
                    continue
                # Put all team names in one Array that Team of line k won against
                wins = list(map(lambda x: x.replace("\n", ""), k[startWins:].split(" | ")))
                for i in wins:
                    if wins[0] != "":
                        Team.teams[name].addWin(i.strip())


help(Team)
