language = {'JavaScript' : 62.3, 'HTML' : 52.9, 'Python' : 51, 'SQL' : 51, 'TypeScript' : 38.5 } # dictionary
print(language) # print the dictionary
key = input("Enter the key to check: ") # input from the user
# check if the key is present in the dictionary
if key in language: 
    print("Key is present in the dictionary",'=', language[key])
# if the key is not present in the dictionary
# print the message
else:
    print("Key is not present in the dictionary",'=', key)
    

import numpy as np
import matplotlib.pyplot as plt # import the library
N = 5 # number of languages
scores = (62.3,52.9,51,51,38.5) # scores of the languages
# create an array of the languages
ind = np.arange(N)
# create the bar chart
width = 0.35
p1 = plt.bar(ind, scores, width)
# add some text for labels, title and axes ticks
plt.ylabel('Scores')# y-axis label
plt.title('Scores by language')# title of the chart
plt.xticks(ind, ('JavaScript', 'HTML', 'Python', 'SQL', 'TypeScript'))# x-axis labels
plt.yticks(np.arange(0, 81, 10))# y-axis ticks
plt.show()# display the chart