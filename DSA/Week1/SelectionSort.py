#User function Template for python3

# Author JimmyKurui - GeeksforGeeks Soln

class Solution: 
    def select(self, arr, i):
        # code here
        min = i; j=i+1;
        while j<len(arr):
            if(arr[j]<arr[min]):
                min = j
            j= j+1
        return min
    
    def selectionSort(self, arr,n):
        #code here
        i=0;
        for i in range(0,n-1):
            min = self.select(arr,i)
            if arr[min] != arr[i]:
                arr[i], arr[min] = arr[min], arr[i] 
        

