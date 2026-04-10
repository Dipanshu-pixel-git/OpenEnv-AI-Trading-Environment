def run(env):
    state = env.reset()
    total_reward = 0

    while True:
        action = 1 if state.close > state.open else 0
        result = env.step(action)
        total_reward += result.reward
        state = result.state
        if result.done:
            break

    return total_reward