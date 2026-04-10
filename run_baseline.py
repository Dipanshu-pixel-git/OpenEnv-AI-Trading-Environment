import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
import pandas as pd
from env.trading_env import TradingEnv
from tasks.easy import run
from graders.grader import score

np.random.seed(42)

df = pd.DataFrame({
    'Open': np.random.rand(100)*100,
    'High': np.random.rand(100)*100,
    'Low': np.random.rand(100)*100,
    'Close': np.random.rand(100)*100,
    'Volume': np.random.randint(100,1000,100)
})

env = TradingEnv(df)
reward = run(env)

print("Reward:", reward)
print("Score:", score(reward))