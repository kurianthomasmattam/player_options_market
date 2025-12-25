## Project Overview

This project builds a mini **options market for footballers**.  
Each player is treated like a financial asset:

- `value` = current market value (from Transfermarkt)
- `sigma` = annualised volatility of the player’s value

Volatility is not guessed: it is derived from **Sofascore match ratings**.

For each player:

1. Sofascore ratings were collected.
2. The standard deviation of ratings was computed.
3. This rating volatility was scaled/annualised and used as a proxy for **value volatility**.
4. The final annual volatility (e.g. `0.225` for 22.5%) is stored as `sigma` in `players_data`.

These values feed into a simple price simulation and into the **Black–Scholes** option pricing model.

### File Structure

| File | Purpose |
|------|---------|
| `market.py` | Defines the player universe (name, club, value, sigma), helper functions to build and list players, and a simulation engine that updates values using daily random shocks based on sigma. |
| `pricing.py` | Contains the Black–Scholes implementation: normal CDF, `d1`/`d2`, call/put price functions, a `positive_part` payoff helper, and a `fair_price` function that returns the theoretical call/put price given `S`, `K`, `T`, `r`, and `sigma`. |
| `payoffs.py` | Provides basic profit functions for individual positions: long/short stock, long/short calls, long/short puts. These are purely payoff-level and do not depend on players. |
| `strategies.py` | Builds classic option strategies by combining the basic payoffs: Protective Put, Covered Call, Straddle, and Strangle. Each function returns total strategy profit as a function of strikes, premiums, and expiry price `ST`. |
| `main.py` | The command-line interface. Shows a menu, lets the user list players, simulate future values, search for a player, and price/evaluate option strategies for a chosen player. It calls into `market.py`, `pricing.py`, and `strategies.py`. |

### Simulation Logic

The value simulation treats the player’s value like a stock following a simple random walk:

- Annual volatility: `sigma` (from Sofascore-based calculations).
- Daily volatility: `sigma_daily = sigma / sqrt(365)`.
- Each day, a random shock is drawn from `N(0, sigma_daily)` and applied multiplicatively:

```python
shock = random.gauss(0, sigma_daily)
new_value = player["value"] * (1 + shock)
