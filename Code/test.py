import matplotlib.pyplot as plt
import numpy as np

# Hypothetical data for illustration
ues = np.arange(1, 21)  # 20 UEs
predicted_power_coefficients = np.random.uniform(0.5, 1.0, size=20)
traditional_power_coefficients = np.random.uniform(0.3, 0.9, size=20)

# Plotting the results
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.bar(ues, predicted_power_coefficients, color='b', alpha=0.7, label='Predicted')
plt.bar(ues, traditional_power_coefficients, color='r', alpha=0.5, label='Traditional')
plt.xlabel('UEs')
plt.ylabel('Power Coefficient')
plt.title('Power Control Coefficients (Predicted vs Traditional)')
plt.legend()

plt.subplot(1, 2, 2)
se_predicted = np.random.uniform(1, 5, size=20)
se_traditional = np.random.uniform(0.5, 4, size=20)
plt.plot(ues, se_predicted, 'b-o', label='Predicted')
plt.plot(ues, se_traditional, 'r-s', label='Traditional')
plt.xlabel('UEs')
plt.ylabel('Spectral Efficiency (SE)')
plt.title('Spectral Efficiency (Predicted vs Traditional)')
plt.legend()

plt.tight_layout()
plt.show()
