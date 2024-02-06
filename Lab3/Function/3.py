def solve(legs, heads):
    rabbits = ((legs-(heads*2))/2)
    chickens = (heads - rabbits)
    return rabbits, chickens
legs = 94
heads = 35
rabbits, chickens = solve(legs, heads)
print("Rabbits: ", rabbits)
print("Chickens: ", chickens)
