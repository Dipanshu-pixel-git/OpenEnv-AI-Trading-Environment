import pandas as pd
from .models import State, StepResult

class TradingEnv:
    def __init__(self, df, initial_balance=10000):
        self.df = df.reset_index(drop=True)
        self.initial_balance = initial_balance
        self.reset()

    def reset(self):
        self.step_idx = 0
        self.balance = self.initial_balance
        self.shares = 0
        self.net_worth = self.initial_balance
        return self.state()

    def state(self):
        row = self.df.iloc[self.step_idx]
        return State(
            open=row['Open'],
            high=row['High'],
            low=row['Low'],
            close=row['Close'],
            volume=row['Volume'],
            balance=self.balance,
            shares_held=self.shares
        )

    def step(self, action: int):
        row = self.df.iloc[self.step_idx]
        price = row['Close']

        prev_net = self.net_worth

        if action == 1:  # BUY
            qty = self.balance // price
            self.balance -= qty * price
            self.shares += qty

        elif action == 2:  # SELL
            self.balance += self.shares * price
            self.shares = 0

        self.net_worth = self.balance + self.shares * price

        reward = (self.net_worth - prev_net)

        self.step_idx += 1
        done = self.step_idx >= len(self.df) - 1

        return StepResult(
            state=self.state(),
            reward=reward,
            done=done
        )