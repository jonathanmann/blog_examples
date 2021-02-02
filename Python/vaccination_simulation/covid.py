#!/usr/bin/env python
import random

individual_spread = lambda x: x[random.randint(0,len(x) - 1)]
spread_distribution = [0] * 35 + [1] * 20 + [2] * 20 + [3] * 10 + [4] * 6  + [5,6,7,8,9,10,11,12,13]

def spread(current_gen,immune_pct):
    if current_gen == 0:
        return 0
    sample_next_gen = 0
    sample = 1000 
    if current_gen < sample:
        sample = current_gen
    for i in range(sample):
        if random.randint(1,100) <= int(immune_pct * 100):
            continue
        sample_next_gen += individual_spread(spread_distribution)
    next_gen = int(current_gen * (sample_next_gen/sample))
    return next_gen

total_population = 328200000
immune = 60000000
infected = 5000000
current_gen = infected
immune_pct = immune/total_population
vax_num = 0
fatalities = 450000
herd_immunity = .75

while current_gen and immune_pct < herd_immunity:
    immune += current_gen + vax_num
    immune_pct = immune/total_population
    current_gen = spread(current_gen,immune_pct)
    fatalities += current_gen * .007
    print("Infected: ",current_gen/1000,"K", "Immune: ",immune_pct)
print("Fatalities: ", round(fatalities/1000,2), "K")
