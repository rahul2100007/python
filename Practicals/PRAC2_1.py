
def money():
    amount = float(input("Enter an amount in double, for example 11.56: "))
    
    total_cents = int(round(amount * 100))
    
    dollars = total_cents // 100 
    remaining_cents = total_cents % 100
    
    quarters = remaining_cents // 25
    remaining_cents %= 25
    
    dimes = remaining_cents // 10 
    remaining_cents %= 10
    
    nickels = remaining_cents // 5     
    pennies = remaining_cents % 5 
    
    print(f"Your amount {amount:.2f} consists of")
    print(f"{dollars} dollars")
    print(f"{quarters} quarters")
    print(f"{dimes} dimes")
    print(f"{nickels} nickels")
    print(f"{pennies} pennies")

money()