import numpy as np
from main import Agent
import time
import threading


def run1(agent, event2):
    event2.wait()
    agent.run(None)
def run2(agent):
    agent.run(None)




def start1(env_name,training,render,event,event2):
    agent1 = Agent(env_name=env_name,
                   training=training,
                   player_number=1,
                   render=render)
    event.set()
    run1(agent1,event2)
    event2.clear()
    rewards1 = agent1.episode_rewards
    print()  # Newline.
    print("Rewards for {0} episodes:".format(len(rewards1)))
    print("- Min:   ", np.min(rewards1))
    print("- Mean:  ", np.mean(rewards1))
    print("- Max:   ", np.max(rewards1))
    print("- Stdev: ", np.std(rewards1))



def start2(env_name,training,render,event,event2):
    event.wait()
    event.clear()
    agent2 = Agent(env_name=env_name,
                   training=training,
                   player_number=2,
                   render=render)
    # Run the agent
    event2.set()
    time.sleep(1)
    run2(agent2)
    # Print statistics.
    rewards1 = agent2.episode_rewards
    print()  # Newline.
    print("Rewards for {0} episodes:".format(len(rewards1)))
    print("- Min:   ", np.min(rewards1))
    print("- Mean:  ", np.mean(rewards1))
    print("- Max:   ", np.max(rewards1))
    print("- Stdev: ", np.std(rewards1))
