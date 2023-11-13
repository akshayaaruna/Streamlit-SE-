import numpy as np
import pandas as pd
import random

# Given sets of values for each column
dYear = [2018,2019,2020,2021,2022]
dSeason= ["PostMonsoon","Rainy","Summer","Winter"]
# dSeason= ["Winter","Summer"]
dProducts = ["T-shirt", "Jeans", "Dress", "Jacket", "Shorts", "Shirt", "Tops","Leggings"]
# SalesPercentage = [round(random.uniform(10, 100), 2) for _ in range(num_samples)]

# Number of samples
num_samples = 100000


# Generate random data within given sets of values
# fYear = np.random.choice(dYear, num_samples)
# fSeason = np.random.choice(dSeason, num_samples)
# fProducts = np.random.choice(dProducts, num_samples)
fYear = random.choices(dYear, k=num_samples)
fSeason = random.choices(dSeason, k=num_samples)
fProducts = random.choices(dProducts, k=num_samples)
fSalesPercentage = [round(random.uniform(10, 100),2) for _ in range(num_samples)]
# Create a DataFrame
data = {
    'Year': fYear,
    'Season': fSeason,
    'Products': fProducts,
    'SalesPercentage':fSalesPercentage
}

df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('random_dataset.csv', index=False)

print('Random dataset based on given sets of values saved to random_dataset.csv')
