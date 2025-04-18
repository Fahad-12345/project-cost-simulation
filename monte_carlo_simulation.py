import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set random seed for reproducibility
np.random.seed(42)

# Parameters
num_simulations = 10000
mean = 50000      # Mean project cost
std_dev = 8000    # Standard deviation

# Simulate the risk variable (e.g., cost)
simulated_costs = np.random.normal(loc=mean, scale=std_dev, size=num_simulations)

# Summary statistics
mean_sim = np.mean(simulated_costs)
std_sim = np.std(simulated_costs)
min_sim = np.min(simulated_costs)
max_sim = np.max(simulated_costs)
percentile_90 = np.percentile(simulated_costs, 90)

print("Mean Cost:", mean_sim)
print("Standard Deviation:", std_sim)
print("Min Cost:", min_sim)
print("Max Cost:", max_sim)
print("90th Percentile:", percentile_90)

# Histogram
plt.figure(figsize=(10, 6))
sns.histplot(simulated_costs, bins=50, kde=True, color='skyblue')
plt.title('Monte Carlo Simulation - Project Cost Distribution')
plt.xlabel('Cost')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
plt.show()

# CDF Plot
plt.figure(figsize=(10, 6))
sns.ecdfplot(simulated_costs, color='green')
plt.title('Cumulative Distribution Function (CDF)')
plt.xlabel('Cost')
plt.ylabel('Cumulative Probability')
plt.grid(True)
plt.tight_layout()
plt.show()
