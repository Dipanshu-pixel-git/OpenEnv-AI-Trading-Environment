from pydantic import BaseModel

class State(BaseModel):
    open: float
    high: float
    low: float
    close: float
    volume: float
    balance: float
    shares_held: float

class Action(BaseModel):
    type: int  # 0=hold, 1=buy, 2=sell

class StepResult(BaseModel):
    state: State
    reward: float
    done: bool