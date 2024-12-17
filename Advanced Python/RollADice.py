import random
import matplotlib as mp
import matplotlib.pyplot as plt

mp.use('TkAgg')

total_roll = 6 * 10 ** 6

rolls = [random.randint(1, 6) for _ in range(total_roll)]
from collections import Counter

results = Counter(rolls)

print(results)

# Prepare data for the bar graph
faces = list(results.keys())
counts = list(results.values())

# Plot the bar graph
plt.figure(figsize=(10, 6))
plt.bar(faces, counts, color='skyblue', edgecolor='black')

# Add labels and title
plt.xlabel('Dice Face', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.title(f'Dice Rolls Distribution ({total_roll} Rolls)', fontsize=16)

# Add value labels on top of bars
for i, count in enumerate(counts):
    plt.text(faces[i], count + 2000, str(count), ha='center', fontsize=12)

# Show the plot
plt.xticks(faces, fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
