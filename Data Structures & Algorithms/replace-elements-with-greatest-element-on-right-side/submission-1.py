class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        temp = [0 for i in range(len(arr))]

        for i in range(len(arr)-1, -1, -1):
            if i == len(arr)-1:
                temp[i] = arr[i]
            if i == len(arr)-2:
                temp[i] = arr[i+1]
            if i < len(arr)-2:
                temp[i] = max(temp[i+1], arr[i+1])
    
        temp[-1] = -1
        return temp