from pricing import positive_part

def long_stock_profit(S0,ST):
    "Calculates the profit of a long position in the stock"
    return ST-S0

def short_stock_profit(S0,ST):
    "Calculates the profit of a short position in the stock"
    return S0-ST

def long_put_profit(K,ST,P):
    "Calculates the profit of a long position in the put option"
    intrinsic_value=positive_part(K,ST,option_type="put")
    profit=intrinsic_value-P
    return profit

def short_put_profit(K,ST,P):
    "Calculates the profit of a short position in the put option"
    intrinsic_value=positive_part(K,ST,option_type="put")
    profit=P-intrinsic_value
    return profit

def long_call_profit(K,ST,C):
    "Calculates the profit of a long position in the call option"
    intrinsic_value=positive_part(K,ST,option_type="call")
    profit=intrinsic_value-C
    return profit

def short_call_profit(K,ST,C):
    "Calculates the profit of a short position in the call option"
    intrinsic_value=positive_part(K,ST,option_type="call")
    profit=C-intrinsic_value
    return profit














