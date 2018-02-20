import heapq
import random
# The algorithm foo() accepts an array and three test cases. It will return the median of the array at each one of the test cases
# The data structure stremMedian uses two heaps - max heap and min heap:
# If the new element x is smaller than the root of maxHeap then we insert x to maxHeap.
# Else we insert x to minHeap
# If after insertion maxHeap has count of elements that is greater than 1 from the count of elements of minHeap,
# then we call Extract-Max on maxHeap and insert it to minHeap.
# Else if after insertion minHeap has count of elements that is greater than the count of elements of maxHeap,
# then we call Extract-Min on minHeap and insert it to maxHeap

class streamMedian:
    def __init__(self): # Initialize data structure
        self.minHeap, self.maxHeap = [], []  # Initializing two empty heaps
        self.N = 0 # number of elements

    def insert(self, num): #The insertion function
        if self.N % 2 == 0: # If the number of elements is even
            heapq.heappush(self.maxHeap, -1 * num) # insert to maxHeap
            self.N += 1
            if len(self.minHeap) == 0:
                return
            if -1 * self.maxHeap[0] > self.minHeap[0]: #if maxHeap is bigger than minHeap
                toMin = -1 * heapq.heappop(self.maxHeap) # Get one element out of minHeap
                toMax = heapq.heappop(self.minHeap) # and insert it to maxHeap
                heapq.heappush(self.maxHeap, -1 * toMax)
                heapq.heappush(self.minHeap, toMin)
        else:
            toMin = -1 * heapq.heappushpop(self.maxHeap, -1 * num) # Else pop from maxHeap and push to minHeap
            heapq.heappush(self.minHeap, toMin)
            self.N += 1

    def getMedian(self):
        if self.N % 2 == 0: # If number of elements is even
            return (-1 * self.maxHeap[0] + self.minHeap[0]) / 2.0 # Return the average of two middle elements
        else:
            return -1 * self.maxHeap[0] # Else return the root of maxHeap, which is the middle


# accepts a list and three test points, returns the median at each test point
def foo(vals, n1, n2, n3):
    holder = streamMedian()
    for i in range(len(vals)):
        holder.insert(vals[i])
        if i in [n1, n2, n3]:  # if current value equals one of the test cases
            print(holder.getMedian())  # print median until now
        elif i == len(vals)-1:         # print median at the end
            print(holder.getMedian())
    return False


def main():
    #A = input("Enter array numbers, seperated by a comma:\n")
    #test1 = input("Enter test case #1\n")
    #test2 = input("Enter test case #2\n")
    #test3 = input("Enter test case #3\n")
    #foo(A, test1, test2, test3)
    A = [random.randint(1,1000) for _ in range(20)]
    print(A)
    foo(A,(len(A)/2),(len(A)/4),2)

    raw_input("promt: ") #Just so the program will not exit automaticaly when running not from prompt
if __name__ == "__main__":
    main()
