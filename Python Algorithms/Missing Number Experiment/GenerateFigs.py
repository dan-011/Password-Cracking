from matplotlib import pyplot as plt
from TimeFunctions import time_function
from FindMissing import find_missing_1, find_missing_2, find_missing_3, find_missing_4
import random

x = [i*50 for i in range(21)] 
y1 = []

for n in x:
    L = [i for i in range(n+1)]
    random.seed()
    random.shuffle(L)
    L.pop()
    y1.append(time_function(find_missing_1, L)*1000) #can I do any unit?
plt.scatter(x, y1, c = "b", marker = "x",label = "find_missing_1")
plt.xlim([0, 1000])
plt.xlabel("Number of Items")
plt.ylabel("Time (ms)")
plt.savefig("find_missing_1.png")
#####################################################################

y2 = []
for n in x:
    L = [i for i in range(n+1)]
    random.seed()
    random.shuffle(L)
    L.pop()
    y2.append(time_function(find_missing_2, L)*1000)

plt.scatter(x, y2, c = "r", marker = "*", label = "find_missing_2")
plt.legend()
plt.savefig("find_missing_12.png")

plt.clf()
#####################################################################

#x = [i*50000 for i in range(21)] 
#^^ Commented this out to allow mimir cases to run ^^

y2 = []
for n in x:
    L = [i for i in range(n+1)]
    random.seed()
    random.shuffle(L)
    L.pop()
    y2.append(time_function(find_missing_2, L)*1000)

y3 = []
for n in x:
    L = [i for i in range(n+1)]
    random.seed()
    random.shuffle(L)
    L.pop()
    y3.append(time_function(find_missing_3, L)*1000)


plt.figure()
plt.scatter(x, y2, c = "r", marker = "*", label = "find_missing_2")
plt.scatter(x, y3, c = "y", marker = ".", label = "find_missing_3")
plt.xlim([0, 1000000])
plt.xlabel("Number of Items")
plt.ylabel("Time (ms)")
plt.legend()
plt.savefig("find_missing_23.png")

plt.clf()
#####################################################################

y4 = []
for n in x:
    L = [i for i in range(n+1)]
    random.seed()
    random.shuffle(L)
    L.pop()
    y4.append(time_function(find_missing_4, L)*1000)
plt.scatter(x, y3, c = "y", marker = ".", label = "find_missing_3")
plt.scatter(x, y4, c = "g", marker = "+", label = "find_missing_4")
plt.xlim([0, 1000000])
plt.xlabel("Number of Items")
plt.ylabel("Time (ms)")
plt.legend()
plt.savefig("find_missing_34.png")