from email import policy
from parallel_env import parallel_env
import random

def policy(observation, agent):
    action = random.randint(0, 2)
    return action

env = parallel_env()

observations = env.reset()
print(f"agents {env.agents}")
max_cycles = 500
while len(env.agents) == 2:
    actions = {agent: policy(observations[agent], agent) for agent in env.agents}
    observations, rewards, dones, infos = env.step(actions)
    env.render()