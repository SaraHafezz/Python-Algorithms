import timeit
import random 
import matplotlib.pyplot as plt    
from scipy.optimize import curve_fit
import numpy as np


def linearSearch(n, arr):
    for i in arr:
        if i == n: return i
    return 0

def binarySearch(n, arr, first, last):
    if (first <= last):
        center = (first+last)//2
        if (n == arr[center]):
            return center
        elif (n < arr[center]):
            return binarySearch(n, arr, first, center-1)
        else:
            return binarySearch(n, arr, center+1, last)
 

def linearTest(arr):
    ele = random.randint(0, len(arr)-1)
    findEle = arr[ele]
    return(linearSearch(findEle, arr))

def binaryTest(arr):
    findEle = random.choice(arr)
    return(binarySearch(findEle, arr, arr[0], arr[len(arr)-1]))


def linearTime(length):
    result = timeit.repeat(lambda:linearTest(length), repeat = 1000, number = 100)
    return sum(result)/len(result)

def binaryTime(length):
    result = timeit.repeat(lambda:binaryTest(length), repeat = 1000, number = 100)
    return sum(result)/len(result)


def timeFunc(x,a,b):
    return a * np.log2(x) + b

testList1000 = [x for x in range(1000)]
testList2000 = [x for x in range(2000)]
testList4000 = [x for x in range(4000)]
testList8000 = [x for x in range(8000)]
testList16000 = [x for x in range(16000)]
testList32000 = [x for x in range(32000)]

testRanges = [testList1000,testList2000,testList4000,testList8000,testList16000,testList32000]

avgTimeLinear = []
avgTimeBinary = []


for i in testRanges:
    findBinaryTime = binaryTime(i)
    avgTimeBinary.append(findBinaryTime)
    findLinearTime = linearTime(i)
    avgTimeLinear.append(findLinearTime)

xPlot = np.array([1000*(2**i) for i in range(6)])
slope, intercept = np.polyfit(xPlot, avgTimeLinear,1)
linearBLF = [slope * x + intercept for x in xPlot]

paramBinary, conParamBinary = curve_fit(timeFunc, xPlot, avgTimeBinary, p0 = [1,1])
ansBinary = timeFunc(xPlot, *paramBinary)

print(f'Linear Model: t = ({slope})n + {intercept}')
print(f'Binary Model: t = ({paramBinary[0]})log2(n) + {paramBinary[1]}')

plt.subplot(1,2,1)
plt.title('Linear Search')
plt.xlabel('# of Elements')
plt.ylabel('Avg. Time for Execution (seconds)')
plt.scatter(xPlot, avgTimeLinear, label = 'Linear Search')
plt.plot(xPlot, linearBLF, label  = 'Line of Best Fit')
plt.legend()

plt.subplot(1,2,2)
plt.scatter(xPlot, avgTimeBinary, label= 'Binary Search')
plt.plot(xPlot, ansBinary, label = 'Line of Best fit')
plt.title('Binary Search')
plt.xlabel('# of Elements')
plt.ylabel('Avg. Time for Execution (seconds)')
plt.legend()

plt.tight_layout(pad = 1.0)
plt.show()


# The interpolated linear search data showed a linear function while 
# the interpolated binary search data showed a logarithmic function. 
# For the Linear search, the line of best fit's equation is (1.138e-06)n + 0.000187
# and for the Binary Search, the line of best fit's equation is (2.492e-05)log2n + 3.1359e-05.
# The results (graphs and models
# shown are as expected because the linear search time complexity, O(n)
# is linear and the binary search time complexity O(logn) is logarithmic.