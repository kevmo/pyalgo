import matplotlib.pyplot as plt
import random


def playSeries(numGames, teamProb):
    """Assumes numGames is an odd int,
        teamProb a float between 0 and 1.
    Returns True if better team wins series."""
    numWon = 0
    for game in range(numGames):
        if random.random() <= teamProb:
            numWon += 1
    return (numWon > numGames//2)


def simSeries(numSeries):
    prob = 0.5
    fracWon = []
    probs = []
    while prob <= 1.0:
        seriesWon = 0.0
        for i in range(numSeries):
            if playSeries(7, prob):
                seriesWon += 1
        fracWon.append(seriesWon/numSeries)
        probs.append(prob)
        prob += 0.01

    plt.plot(probs, fracWon, linewidth=5)
    plt.xlabel('Probability of winning a game')
    plt.ylabel("Probability of winning a series")
    plt.axhline(0.95)
    plt.ylim(0.5, 1.1)
    plt.title(str(numSeries) + 'Seven Game Series')
    plt.show()

simSeries(400)
