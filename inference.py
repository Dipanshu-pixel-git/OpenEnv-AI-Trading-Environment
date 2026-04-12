import numpy as np
import pandas as pd
from env.trading_env import TradingEnv

# Create dummy data
df = pd.DataFrame({
    'Open': np.random.rand(10)*100,
    'High': np.random.rand(10)*100,
    'Low': np.random.rand(10)*100,
    'Close': np.random.rand(10)*100,
    'Volume': np.random.randint(100,1000,10)
})

env = TradingEnv(df)

print("[START]")

state = env.reset()
print("Initial State:", state)

done = False

while not done:
    action = np.random.choice([0,1,2])
    result = env.step(action)

    print("[STEP]")
    print("Action:", action)
    print("Reward:", result.reward)

    done = result.done

print("[END]")