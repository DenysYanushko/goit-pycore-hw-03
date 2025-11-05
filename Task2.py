import random 

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity > (max - min + 1):
        return []
    
    lottery_numbers = random.sample(range(min, max + 1), quantity)
    lottery_numbers = sorted(lottery_numbers)
    return lottery_numbers

lottery_numbers = get_numbers_ticket(1,49,6)
print("Your lotterry number:", lottery_numbers) 
    
