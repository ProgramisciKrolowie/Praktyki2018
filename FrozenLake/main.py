import numpy as np
import gym
import random

env = gym.make("FrozenLake-v0")

akcje = env.action_space.n
stany = env.observation_space.n

qtable = np.zeros((stany,akcje))
print(qtable)
# Left | Down | Right | Up
ilEpizodow = 500000
learningRate = 0.8
maxSteps = 99
gamma = 0.8

epsilon = 0.99
maxEpsilon = 0.99
minEpsilon = 0.05
decay_rate = 0.0001

rewards = []

for episode in range(ilEpizodow):   #cala gra (informacje o niej)
    s1 = env.reset()
    step = 0
    done = False
    iloscNagrod = 0

    for step in range (maxSteps): # pojedyncze kroki
        losowanko = random.uniform(0, 1)
        if losowanko > epsilon:
            akcja = np.argmax(qtable[s1, :])
            if step == 1 and episode == 41370:
                print(s1)
                print(qtable)
                print((qtable[s1, :]))
                print(akcja)

        else:
            akcja = env.action_space.sample()
        s2, nagroda, done, info = env.step(akcja)

        qtable[s1, akcja] = qtable[s1, akcja] + learningRate *\
            (nagroda + gamma * np.max(qtable[s2, :]) - qtable[s1, akcja])
        iloscNagrod += nagroda
        s1 = s2
        if done:
            break

    epsilon = minEpsilon + (maxEpsilon - minEpsilon) * np.exp(-decay_rate * (episode + 1))
    rewards.append(iloscNagrod)

    #print("epizod: " + str(episode) + " | epsilon: " + str(epsilon) + " | nagroda: " + str(nagroda))

    if (episode % 100000) == 0:
        print("H A L K O")

print("Score over time: " + str(sum(rewards)/ilEpizodow))
print(qtable)

for episode in range(5):
    s1 = env.reset()
    step = 0
    done = False
    print("****************************************************")
    print("EPISODE: ", episode)

    for step in range(maxSteps):
        env.render()
        
        action = np.argmax(qtable[s1, :])

        s2, reward, done, info = env.step(action)

        if done:
            break
        s1 = s2
env.close()
