from fastapi import FastAPI
import numpy as np
import pandas as pd
from env.trading_env import TradingEnv


def create_app():
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
        return {"state": state.dict()}

    @app.post("/step")
    def step(action: dict):
        action_value = action.get("action", 0)
        result = env.step(action_value)
        return {
            "state": result.state.dict(),
            "reward": float(result.reward),
            "done": bool(result.done)
        }

    return app


def main():
    import uvicorn
    app = create_app()
    uvicorn.run(app, host="0.0.0.0", port=7860)


if __name__ == "__main__":
    main()