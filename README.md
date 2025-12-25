# ⚽ Player Options Market

This project builds a mini **options market for footballers**.  
Each of the 25 players is treated like a financial asset:

- `value` = current market value (from Transfermarkt)
- `sigma` = annualised volatility of the player’s value

Volatility is not guessed — it is derived from **Sofascore match ratings**.

For each player:

1. Sofascore ratings were collected.
2. The standard deviation of ratings was computed.
3. This rating volatility was scaled/annualised and used as a proxy for **value volatility**.
4. The final annual volatility (e.g. `0.225` for 22.5%) is stored as `sigma` in `players_data`.

These values feed into a simple price simulation and into the **Black–Scholes** option pricing model.

---

## 📁 File Structure

| File | Purpose |
|------|---------|
| `market.py`     | Defines player universe (name, club, value, sigma). Builds players and simulates value changes daily based on volatility. |
| `pricing.py`    | Black–Scholes formulas: `d1`, `d2`, normal CDF, call/put pricing, `fair_price`. |
| `payoffs.py`    | Profit functions for long/short stock, calls, and puts. |
| `strategies.py` | Implements Protective Put, Covered Call, Straddle, Strangle strategies. |
| `main.py`       | Command-line interface. The menu system that the user interacts with. |

---

## 📈 Simulation Logic

Player price is simulated like a stock using a **random walk** based on volatility:

```python
sigma_daily = sigma / sqrt(365)                 # Daily volatility from annual sigma
shock = random.gauss(0, sigma_daily)            # Random price shock
new_value = player["value"] * (1 + shock)       # Update player value

---

## 🚀 How to Run

### Requirements
- Python 3 installed

### 1️⃣ Download the Project
Click the green **Code** button → **Download ZIP**  
Extract the folder.

### 2️⃣ Open Terminal / Command Prompt

#### Mac:
```sh
cd ~/Downloads/player_options_market-main
python3 main.py

#### Windows:
```bat
cd Downloads\player_options_market-main
python3 main.py

