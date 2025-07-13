#  Backtesting Engine for Trading Strategies

This is a Python project I built to simulate technical trading strategies on real historical stock data. The engine is modular and currently supports Moving Average Crossover and RSI strategies.

## What It Does

- Takes any stock ticker (like ADANIPOWER.NS)
- Runs the selected strategy on 4+ years of data
- Outputs Sharpe Ratio and Max Drawdown
- Saves trade logs and signal plots in a `results/` folder

## How to Run

```bash
pip install -r requirements.txt
python main.py --ticker SBIN.NS --strategy rsi

