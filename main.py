import argparse
from utils.data_loader import load_data
from utils.metrics import calculate_returns, sharpe_ratio, max_drawdown
from utils.plotter import plot_signals
from strategies.moving_average import run_strategy as ma_strategy
from strategies.rsi_strategy import run_strategy as rsi_strategy
import pandas as pd

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--ticker', type=str, default='ADANIPOWER.NS')
    parser.add_argument('--strategy', type=str, choices=['ma', 'rsi'], default='ma')
    args = parser.parse_args()

    df = load_data(args.ticker, '2020-01-01', '2024-12-31')

    if args.strategy == 'ma':
        df = ma_strategy(df)
    elif args.strategy == 'rsi':
        df = rsi_strategy(df)

    df = calculate_returns(df)

    sharpe = sharpe_ratio(df)
    mdd = max_drawdown(df)

    print(f"Sharpe Ratio: {sharpe:.2f}")
    print(f"Max Drawdown: {mdd:.2%}")

    df[['Date', 'Signal', 'Close']].dropna().to_csv("results/trade_log.csv", index=False)
    plot_signals(df, args.ticker)
