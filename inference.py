import numpy as np
import pandas as pd
import os
import requests
from env.trading_env import TradingEnv

# 🔥 LLM CALL (paste here)
try:
    response = requests.post(
        os.environ.get("API_BASE_URL", "https://api.openai.com/v1/chat/completions"),
        headers={
            "Authorization": f"Bearer {os.environ.get('OPENAI_API_KEY', '')}",
            "Content-Type": "application/json"
        },
        json={
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": "Hello"}],
            "max_tokens": 5
        }
    )
    print("LLM call status:", response.status_code)
except Exception as e:
    print("LLM call failed:", e)


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
print("state:", state)

done = False

while not done:
    action = np.random.choice([0, 1, 2])
    result = env.step(action)

    print("[STEP]")
    print("action:", action)
    print("reward:", result.reward)

    done = result.done

print("[END]")