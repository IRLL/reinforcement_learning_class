import gym
import time

env = gym.make('MDPGridworld-v0')

# prints out that both states and actions are discrete and their valid values
print env.observation_space
print env.action_space

# to access the values
print env.observation_space.n
print env.action_space.n

# added delay here so you can view output above
time.sleep(2) 

for i_episode in range(20):
    obs = env.reset()
    for t in range(100):
        env.render()
        # time.sleep(.5) # uncomment to slow down the simulation
        action = env.action_space.sample() # act randomly
        obs2, reward, terminal, _ = env.step(action)
        if terminal:
            print("Episode finished after {} timesteps".format(t+1))
            break
