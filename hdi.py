from statsmodels.stats.weightstats import ttest_ind
import pingouin as pg
 
# #happiness indexes for top HDI countries
hdi_f = [7.512, 7.365, 7.557, 5.425, 7.162, 7.636, 7.384, 7.041, 7.034, 7.415]

# #happiness indexes for top HDI countries from the end
hdi_l = [4.891, 4.197, 4.670, 5.048, 4.479, 3.574, 2.404, 5.003, 4.251, 5.075]
 
result = pg.ttest(hdi_f, hdi_l)
 
print(result)
