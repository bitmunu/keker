import csv
import random
import os
import matplotlib.pyplot as plt
import numpy as np
def Parse(name, number_of_rows, b=False, delim = ','):
    rows = []
    aligns = []
    number = 0
    filename = name + ".csv"
    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=delim, quotechar='"')
        for row in reader:
            for column_index, entry in enumerate(row):
                if column_index >= len(aligns):
                    aligns.append(len(entry))
                else:
                    aligns[column_index] = max(aligns[column_index], len(entry))
            rows.append(row)


        try:
            for j in range(0, number_of_rows):
                for i in range(0, len(aligns)):
                    print("      ".join([f"{rows[j][i].ljust(int(aligns[i] + 1))}"]), end='')
                print(end='\n')
        except Exception as e:
            print(f"xdError: {str(e)}")


    #return len(rows), len(aligns)
    return rows

def Show(type="top", number_of_rows=5, delim=','):
    if type == "top":
        Parse("neweedata","top", number_of_rows, True)
    elif type == "bottom":
        Parse("neweedata", "bottom", number_of_rows, True)
    elif type == "random":
        Parse("neweedata", "random", number_of_rows, True)

#a, b = Parse('passengers', 145)

def split_csv_notes(list_of_lists, length):
    l1 = []
    l3 = {}
    l2 = []
    l4 = []
    for i in range(0, length):
        l1.append(list_of_lists[i][0])
        l2.append(l1[i].split(sep="-"))
        l2[i].append(list_of_lists[i][1])
        if i != 0:
            l4.append(int(list_of_lists[i][1]))
    l2.pop(0)
    l1.pop(0)

    for j in range(0, length-1):
        year = l2[j][0]
        l3[year] = []

    for s in range(0, length-1):
        year = l2[s][0]
        l3[year].append((l2[s][1], l2[s][2]))
        l2[s][0] = l2[s][1] + "." + l2[s][0]
        l2[s].pop(1)

    return l3, l4, l2

class Year:
    def __init__(self, y, months):
         self.year = y
         self.months = months

    def give_months(self):
        return self.months

    def appendus(self, month):
        self.months.append(month)

    def printo(self):
        print(self.months)

#for i in range(0, len(split_csv_notes(Parse('passengers', 145), 145))):
a, b, c = split_csv_notes(Parse('passengers', 145), 145)

fig = plt.figure(figsize=(2000, 1000))
ax = fig.add_subplot(121)
cc = []
bb = []
for i in range(0, len(c)):
    bb.append(c[i][0].split(".")[0])
    #bb.append(c[i][0])
for i in range(0, len(c)):
    cc.append(int(c[i][0].split(".")[1]) + int(c[i][0].split(".")[0]) * 0.01)
ax1 = plt.subplot(2, 2, 2)
lines = plt.plot(np.array(cc), np.array(b))
ax.bar(bb, b)
ax.grid()
ax1.grid()
plt.show()
