def run_strategy(df, short=20, long=50):
    df['SMA_S'] = df['Close'].rolling(window=short).mean()
    df['SMA_L'] = df['Close'].rolling(window=long).mean()
    df['Signal'] = 0  # initialize with 0s

    # Use iloc for position-based assignment
    signal_condition = (df['SMA_S'] > df['SMA_L']).astype(int)
    df.iloc[long:, df.columns.get_loc('Signal')] = signal_condition[long:]
    
    df['Position'] = df['Signal'].diff()
    df['Date'] = df.index
    return df
