language = {'JavaScript': 62.3, 'HTML': 52.9, 'Python': 51, 'SQL': 51, 'TypeScript': 38.5}
print(language)  # print the dictionary

key = input("Enter the key to check: ")  # input from the user
if key in language:
    print("Key is present in the dictionary", '=', language[key])
else:
    print("Key is not present in the dictionary", '=', key)

import numpy as np
import matplotlib.pyplot as plt

# Extract data directly from the dictionary
languages = list(language.keys())  # ['JavaScript', 'HTML', 'Python', 'SQL', 'TypeScript']
scores = list(language.values())  # [62.3, 52.9, 51, 51, 38.5]

N = len(language)  # number of languages (5)
ind = np.arange(N)  # [0, 1, 2, 3, 4]

width = 0.35
plt.bar(ind, scores, width)

plt.ylabel('Scores')
plt.title('Scores by language')
plt.xticks(ind, languages)  # Use dictionary keys as x-axis labels
plt.yticks(np.arange(0, 81, 10))  # y-axis from 0 to 80, step=10
plt.show()