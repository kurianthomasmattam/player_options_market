from payoffs import long_stock_profit, short_stock_profit, long_put_profit, short_put_profit, long_call_profit, short_call_profit

def protective_put_profit(K,ST,P,SO):
    "Protective put strategy where we long a stock and a put option in the same stock"
    profit=long_put_profit(K,ST,P)+long_stock_profit(SO,ST)
    return profit

def covered_call_profit(K,ST,C,SO):
    "Covered call strategy where we short a call and long the same stock to cover the call option"
    profit=short_call_profit(K,ST,C)+long_stock_profit(SO,ST)
    return profit

def straddle_profit(K,ST,P,C):
    "Straddle strategy where we long a put and a call option in the same stock"
    profit=long_put_profit(K,ST,P)+long_call_profit(K,ST,C)
    return profit

def strangle_profit(K_call,K_put,ST,P,C):
    "Strangle strategy where we long a put and a call option in the same stock Call strike price > Put strike price"
    profit=long_put_profit(K_put,ST,P)+long_call_profit(K_call,ST,C)
    return profit




