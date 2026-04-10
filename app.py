from fastapi import FastAPI
import numpy as np
import pandas as pd
from env.trading_env import TradingEnv

app = FastAPI()

df = pd.DataFrame({
    'Open': np.random.rand(100)*100,
    'High': np.random.rand(100)*100,
    'Low': np.random.rand(100)*100,
    'Close': np.random.rand(100)*100,
    'Volume': np.random.randint(100,1000,100)
})

env = TradingEnv(df)

@app.post("/reset")
def reset():
    state = env.reset()
    return state.dict()

@app.post("/step")
def step(action: int):
    result = env.step(action)
    return {
        "state": result.state.dict(),
        "reward": result.reward,
        "done": result.done
    }