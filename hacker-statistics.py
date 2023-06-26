import numpy as np
import matplotlib.pyplot as plt

# set the seed
np.random.seed(1)

# generate a random float
np.random.rand()

# simulate a dice
# dice = np.random.randint(1,7)

# starting step
# step = 50

# set all_walks
# all_walks collates random walks
all_walks = []

# simulate random walk n times
for x in range(500):

    # set random walk
    # random walk cumulates successive random steps
    random_walk = [0]

    # roll the dice hundred times
    for x in range(100):

        # the current state of the random walk is the current step
        step = random_walk[-1]

        # roll the dice
        dice = np.random.randint(1,7)

        # set step based on roll of dice
        if dice <= 2:
            # ensure step is not a negative value
            step = max(0, step - 1)
        elif dice > 2 and dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)

        # implement clumsiness (adjust for error)
        if np.random.rand() <= 0.001:
            step = 0

        # update the state of random_walk
        random_walk.append(step)

    # update all_walks
    all_walks.append(random_walk[-1])

    # numpy version of all_works 
    np_all_walks = np.array(all_walks)

# plots
plt.plot(np_all_walks)
plt.show()

# probability of reaching x steps
probability = round((len(np_all_walks[np_all_walks >= 6]) / 500) * 100, 2)