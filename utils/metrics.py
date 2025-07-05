import numpy as np

def calculate_returns(df):
    df['Returns'] = df['Close'].pct_change()
    df['Strategy'] = df['Returns'] * df['Signal'].shift()
    return df

def sharpe_ratio(df):
    return np.sqrt(252) * (df['Strategy'].mean() / df['Strategy'].std())

def max_drawdown(df):
    cum_returns = (1 + df['Strategy']).cumprod()
    peak = cum_returns.cummax()
    drawdown = (cum_returns - peak) / peak
    return drawdown.min()
