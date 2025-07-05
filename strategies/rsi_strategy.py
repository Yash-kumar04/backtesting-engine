import pandas as pd

def run_strategy(df, period=14, oversold=30, exit_rsi=50, stop_loss=0.10):
    df = df.copy()

    # Calculate RSI
    delta = df['Close'].diff()
    gain = delta.where(delta > 0, 0).rolling(window=period).mean()
    loss = -delta.where(delta < 0, 0).rolling(window=period).mean()
    RS = gain / loss
    df['RSI'] = 100 - (100 / (1 + RS))

    # Initialize signals
    df['Signal'] = 0
    position = 0
    entry_price = None

    for i in range(period, len(df)):
        rsi_now = df['RSI'].iloc[i].item()
        current_price = df['Close'].iloc[i].item()


        if position == 0 and rsi_now < oversold:
            # Buy signal
            df.iloc[i, df.columns.get_loc('Signal')] = 1
            position = 1
            entry_price = current_price

        elif position == 1:
            rsi_exit = rsi_now > exit_rsi
            stop_loss_triggered = entry_price is not None and current_price < entry_price * (1 - stop_loss)

            # Make sure both are bools now
            if bool(rsi_exit) or bool(stop_loss_triggered):
                df.iloc[i, df.columns.get_loc('Signal')] = 0
                position = 0
                entry_price = None

    df['Position'] = df['Signal'].diff()
    df['Date'] = df.index
    return df
