import matplotlib.pyplot as plt

def plot_signals(df, ticker):
    plt.figure(figsize=(12, 6))
    plt.plot(df['Close'], label='Close Price', alpha=0.6)
    plt.scatter(df[df['Signal'] == 1].index, df[df['Signal'] == 1]['Close'], label='Buy Signal', marker='^', color='g')
    plt.scatter(df[df['Signal'] == 0].index, df[df['Signal'] == 0]['Close'], label='Sell Signal', marker='v', color='r')
    plt.title(f'Trading Signals for {ticker}')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.savefig("results/signal_plot.png")
    plt.close()
