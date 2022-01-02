from typing import *

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        self.mergesort(asteroids)

        for a in asteroids:
            if mass < a:
                return False
            else:
                mass += a

        return True

    # sort list using mergesort
    def mergesort(self, list):
        # allocate auxiliary array
        aux = [None] * len(list)

        # call recursive mergesort function
        self.mergesortr(list, 0, len(list) - 1, aux)

    # perform mergesort using recursive algorithm
    def mergesortr(self, list, low, high, aux):
        if low >= high:
            return
        mid = low + (high - low) // 2

        # left half
        self.mergesortr(list, low, mid, aux)

        # right half
        self.mergesortr(list, mid+1, high, aux)

        self.merge(list, low, mid, high, aux)

    # merge list[low-mid] & list[mid+1-high] in sorted order 
    def merge(self, list, low, mid, high, aux):
        # copy to auxiliary array
        for i in range(low, high + 1):
            aux[i] = list[i]
        
        left = low
        right = mid + 1
        index = low

        # loop through aux and put min(aux[left], aux[right]) back into list
        while index <= high:
            # if left pointer is past bounds, add aux[right] to list
            if left > mid:
                list[index] = aux[right]
                right += 1
            
            # if right pointer is past bounds, add aux[left] to list
            elif right > high:
                list[index] = aux[left]
                left += 1
            
            # put min(aux[left], aux[right]) back into list
            else:
                if aux[left] <= aux[right]:
                    list[index] = aux[left]
                    left += 1
                else:
                    list[index] = aux[right]
                    right += 1

            index += 1

sol = Solution()

mass = 5
asteroids = [4,9,23,4]

print(sol.asteroidsDestroyed(mass, asteroids))