import scipy.stats as stats

#happiness indexes for top DI countries
Full_democracies = [7.365, 7.2, 7.557, 7.384, 7.821, 7.636, 7.512, 6.512, 6.474, 7.025]

#happiness indexes for top hybrid regimes countries
Hybrid_regimes = [5.155, 5.559, 3.750, 5.578, 3.760, 5.046, 4.339, 5.533, 5.399, 5.084]

t_stat, p_value = stats.ttest_ind(Full_democracies, Hybrid_regimes)

print({t_stat})
print({p_value})

alpha = 0.05

if p_value < alpha:
    print("Reject zero hypothesis")
else:
    print("Do not reject")