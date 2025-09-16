#Calculate After Renovation Value
def arv_analysis():
    arv = float
    return arv

#Calculate Renovation Cost
# def renovation_cost_analysis(subject_sqft, reno_budget):
#    reno_cost = subject_sqft * reno_budget
#    return reno_cost

#Calculate Renovation Tier


#Calculate Holding Cost
def holding_cost_analysis():
    holding_cost = float
    return holding_cost

#Calculate Max Offer
def max_offer_analysis(arv, reno_cost, holding_cost, target_profit):
    max_offer = arv - reno_cost - holding_cost - target_profit
    return max_offer

#Calculate Max Profit
def max_profit_analysis(arv, list_price, reno_cost, holding_cost):
    max_profit = arv - list_price - reno_cost - holding_cost
    return max_profit

#Calculate Min Profit
def min_profi_analysis(target_profit):
    min_profit = target_profit
    return min_profit

#Calculate Status
def status_analysis(max_profit, target_profit, list_price, max_offer):
    status = ""
    negotiation_margin_pct = 0.05
    if max_profit>= target_profit:
        status = "Profitable"
    elif list_price <= max_offer * (1 + negotiation_margin_pct):
        status = "Negotiable"
    return status