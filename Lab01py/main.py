import numpy as np
import matplotlib.pyplot as plt
print("Hello world!")
rand_array = np.random.rand(100)
print(rand_array)
plt.plot(rand_array, marker='o', linestyle='-', color='b')
plt.title('Масив з 100 випадкових елементів')
plt.xlabel('Індекс')
plt.ylabel('Випадкове значення')
plt.show()