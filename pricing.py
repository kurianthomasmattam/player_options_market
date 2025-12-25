import math

def normal_cdf(x):
    "Standard normal CDF which I calculate using the error function"
    return 0.5*(1+math.erf(x / math.sqrt(2)))

def find_d1_d2(S,K,T,r,sigma):
    "Finds the value of d1 and d2 in the Black-Scholes formula"
    present_value=K/(1+r)**T
    d1 = (math.log(S / present_value) / (sigma * math.sqrt(T))) + (sigma * math.sqrt(T)) / 2
    d2=d1-sigma*math.sqrt(T)
    return d1,d2

def call_price(S,K,T,r,d1,d2):
    "Calculates the price of the call option using the given d1 and d2"
    present_value = K / (1 + r) ** T
    C=(S*normal_cdf(d1))-(present_value*normal_cdf(d2))
    return C

def put_price(S,K,T,r,d1,d2):
    "Calculates the price of the put option using the given d1 and d2"
    present_value = K / (1 + r) ** T
    P=present_value*(1-normal_cdf(d2))-(S*(1-normal_cdf(d1)))
    return P

def positive_part(K,S,option_type):
    "Calculates the payoff"
    if option_type=="call":
        positive_term=S-K
        if positive_term>0:
            return positive_term
        else:
            return 0
    if option_type=="put":
        positive_term=K-S
        if positive_term>0:
            return positive_term
        else:
            return 0

def fair_price(S,K,days_to_expiry,r,sigma,option_type):
    "Calculates the fair price of the  option TODAY"
    T=days_to_expiry/365.0
    if T<=0:
        return positive_part(K,S,option_type)
    else:
        d1, d2 = find_d1_d2(S, K, T, r, sigma)
        if option_type=="call":
            return call_price(S,K,T,r,d1,d2)
        elif option_type=="put":
            return put_price(S,K,T,r,d1,d2)
        else:
            return None






