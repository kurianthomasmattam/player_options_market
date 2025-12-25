from market import build_default_players, list_players, find_player, simulate_value_days
from pricing import fair_price
from strategies import (
    protective_put_profit,
    covered_call_profit,
    straddle_profit,
    strangle_profit,
)

def read_float(prompt,default_value):
    s=input(prompt).strip()
    if s=="":
        return default_value
    else:
        return float(s)

def read_int(prompt,default_value):
    s = input(prompt).strip()
    if s=="":
        return default_value
    else:
        return int(s)

def pricing_strategies(players,r):
    name=input('Player name(exact):')
    player=find_player(players,name)
    if player==None:
        print('Player not found.')
        return None

    S0=player['value']
    sigma=player['sigma']

    print(f"\nSelected: {player['name']} | {player['club']}")
    print(f"Current value S0 = {round(S0, 2)} | sigma = {round(sigma, 3)}")

    days_to_expiry = int(input("Days to expiry: ").strip())

    K_cc=read_float("Covered Call strike (default S0*1.05): ", S0 * 1.05)
    K_pp = read_float("Protective Put strike (default S0*0.95): ", S0 * 0.95)
    K_sd = read_float("Straddle strike (default S0): ", S0)
    K_sg_put  = read_float("Strangle put strike (default S0*0.90): ", S0 * 0.90)
    K_sg_call = read_float("Strangle call strike (default S0*1.10): ", S0 * 1.10)

    call_premium_cc=fair_price(S0, K_cc, days_to_expiry, r, sigma, "call")
    put_premium_pp = fair_price(S0, K_pp, days_to_expiry, r, sigma, "put")
    call_premium_straddle = fair_price(S0, K_sd, days_to_expiry, r, sigma, "call")
    put_premium_straddle = fair_price(S0, K_sd, days_to_expiry, r, sigma, "put")
    put_premium_strangle = fair_price(S0, K_sg_put, days_to_expiry, r, sigma, "put")
    call_premium_strangle = fair_price(S0, K_sg_call, days_to_expiry, r, sigma, "call")

    print("\n--- Black–Scholes premiums (today) ---")
    print("Covered Call (call premium):", round(call_premium_cc, 4))
    print("Protective Put (put premium):", round(put_premium_pp, 4))
    print("Straddle premiums: call", round(call_premium_straddle, 4), "| put", round(put_premium_straddle, 4))
    print("Strangle premiums: put", round(put_premium_strangle, 4), "| call", round(call_premium_strangle, 4))

    ST=read_float("\nEnter an expiry value ST to evaluate profits (default S0): ", S0)

    pp = protective_put_profit(K_pp, ST, put_premium_pp, S0)
    cc = covered_call_profit(K_cc, ST, call_premium_cc, S0)
    sd = straddle_profit(K_sd, ST, put_premium_straddle, call_premium_straddle)
    sg = strangle_profit(K_sg_call, K_sg_put, ST,put_premium_strangle, call_premium_strangle)

    print("\n--- Strategy PROFIT at expiry (given ST) ---")
    print("Protective Put profit:", round(pp, 4))
    print("Covered Call profit:  ", round(cc, 4))
    print("Straddle profit:      ", round(sd, 4))
    print("Strangle profit:      ", round(sg, 4))

def main():
    players = build_default_players() #Returns a list of player dictionaries
    r=read_float("Risk-free rate r (default 0.03): ", 0.03)

    running=True
    while running==True:
        print("\n===============================")
        print("Player Options Market (Top 25)")
        print("1) List players")
        print("2) Simulate player values forward (days)")
        print("3) Find a player by name")
        print("4) Price strategies + evaluate profit at ST")
        print("5) Quit")
        choice = input("Choose: ").strip()

        if choice=="1":
            list_players(players)
        elif choice=="2":
            n_days = read_int("How many days to simulate? (default 30): ", 30)
            if n_days <= 0:
                print("Number of days must be positive.")
            else:
                simulate_value_days(n_days, players)
                print("Done. Simulated", n_days, "days.")
        elif choice=="3":
            name = input("Player name (exact): ").strip()
            player = find_player(players, name)
            if player==None:
                print("Player not found.")
            else:
                print(
                player["name"],
                "|", player["club"],
                "| value:", round(player["value"], 2),
                "| sigma:", round(player["sigma"], 3),
            )
        elif choice == "4":
            pricing_strategies(players, r)

        elif choice=="5":
            running=False
        else:
                print("Invalid choice.")



if __name__=="__main__":
    main()













