def minimumCost(price, n): 

	price = sorted(price) 
	totalCost = 0

	for i in range(n - 1, 1, -2): 
		if (i == 2): 
			totalCost += price[2] + price[0] 

		else:  
			price_first = price[i] + price[0] + 2 * price[1] 
			price_second = price[i] + price[i - 1] + 2 * price[0] 
			totalCost += min(price_first, price_second) 
 
	if (n == 1): 
		totalCost += price[0] 

	else: 
		totalCost += price[1] 

	return totalCost 

price = [30, 40, 60, 70] 
n = len(price) 

print(minimumCost(price, n)) 
