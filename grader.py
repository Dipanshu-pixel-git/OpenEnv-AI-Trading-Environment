def score(reward):
    if reward <= 0:
        return 0.0
    elif reward < 500:
        return 0.3
    elif reward < 2000:
        return 0.6
    else:
        return 1.0