import random

def run(env):
    state = env.reset()
    total_reward = 0

    while True:
        action = random.choice([0, 1, 2])
        result = env.step(action)
        total_reward += result.reward
        state = result.state
        if result.done:
            break

    return total_reward