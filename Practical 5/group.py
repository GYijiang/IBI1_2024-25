uk_contries = [57.11,3.13,1.91,5.45] # list of the UK countries
sorted_uk_contries = sorted(uk_contries) # sort the list
print(sorted_uk_contries) # print the sorted list
chn_contries = [65.77,41.88,45.28,61.27,85.15] # list of the Chinese provinces
sorted_chn_contries = sorted(chn_contries) # sort the list
print(sorted_chn_contries) # print the sorted list


import matplotlib.pyplot as plt
fig, (ax1, ax2) = plt.subplots(1, 2)# create the subplots
# create the pie chart for the UK countries
labels1 = 'England', 'Scotland', 'Wales', 'Northern Ireland'
sizes1 = [57.11,3.13,1.91,5.45]# sizes of the UK countries
explode1 = (0, 0, 0, 0) 
ax1.pie(sizes1, explode=explode1, labels=labels1, autopct='%1.1f%%',startangle=0)# create the pie chart
ax1.axis('equal')

# create the pie chart for the Chinese provinces
labels2 = 'Zhejiang', 'Fujian', 'Jiangxi', 'Anhui', 'Jiangsu'
sizes2 = [65.77,41.88,45.28,61.27,85.15]
explode2 = (0, 0, 0, 0, 0)
ax2.pie(sizes2, explode=explode2, labels=labels2, autopct='%1.1f%%',startangle=0)# create the pie chart
ax2.axis('equal')
plt.show()
