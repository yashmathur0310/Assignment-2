"""
This module contains an abstract class
which is implemented in a BubbleSort algorithm
and MergeSort in two other classes
"""
from abc import ABC, abstractmethod
import time
class Sort(ABC):
    """Abstract base class for sorting."""
    #constructor
    def __init__(self, items):
        #if usr input a list other than numbers
        #we must raise error
        if(len(items)==0):
            raise ValueError("list empty")
        if not(all(isinstance(x, (int, float)) for x in items)):
            raise TypeError("Wrong Input in list: only whole or fracs allowed!")
        self._items = items
        self.time = 0
    #every child class
    #must implement this
    @abstractmethod
    def _sort(self):
        """Returns the sorted list
        """
        pass
    def get_items(self):
        "getter method"
        return self._items
    def _time(self):
        """should be optionally overriden
        if the child class wants to timestamp
        """
        return self.time
###############################################################
class BubbleSort(Sort):
    """Class that represents a BubbleSort implementation."""
    def _sort(self):
        """Bubble sort implementation"""
        #if parent class throws error
        #we must handle it
        items = self.get_items()  # Get the items to be sorted
        n = len(items)
        for i in range(n):
            for j in range(0, n-i-1):
                if items[j] > items[j+1]:
                    items[j], items[j+1] = items[j+1], items[j]  # Swap if out of order
        return items
    def _time(self):
        """
        overriden to measure and return the time taken
        to sort the items if needed
        """
        start_time = time.time()
        self._sort()
        end_time = time.time()
        self.time = end_time - start_time
        return self.time
################################################################
class MergeSort(Sort):
    """Class that represents a MergeSort implementation."""
    def _sort(self):
        items = self.get_items()  # Get the items to be sorted
        if len(items) <= 1:
            return items
        # Split the list into two halves
        mid = len(items) // 2
        left_half = items[:mid]
        right_half = items[mid:]
        # Recursively sort each half
        left_half = MergeSort(left_half)._sort()
        right_half = MergeSort(right_half)._sort()
        # Merge the sorted halves
        return self._merge(left_half, right_half)
    def _merge(self, left, right):
        merged = []
        left_index = right_index = 0
        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1
        merged.extend(left[left_index:])
        merged.extend(right[right_index:])
        return merged
    def _time(self):
        # Measure and return the time taken to sort the items if needed
        start_time = time.time()
        self._sort()
        end_time = time.time()
        self.time = end_time - start_time
        return self.time
##few sample ip & op for testing & execution##
##uncomment to run##
#print(MergeSort(items=[1,23,4,-1,-9,1000,13,100000,1304141,14,1000,-999999])._sort())#randomly sorted
#print(MergeSort(items=[1,23,4,-1,-9,1000,13,100000,1304141,14,1000,-999999])._time())
#print(BubbleSort([1,23,4,-1,-9,1000,13,100000,1304141,14,1000,-999999])._sort())
#print(BubbleSort([1,23,4,-1,-9,1000,13,100000,1304141,14,1000,-999999])._time())
#print(BubbleSort(items=[1304141,100000,-9])._sort())#reverse sorted
#print(MergeSort(items=[1304141,100000,-9])._sort())#reverse sorted)
#if parent class throws error
#we must handle it
#let's see if we identify right errors
#try:
#    print(MergeSort([1000,"-999999"])._sort())#wrong input
#    print(BubbleSort([1000,"-999999"])._sort())#wrong input
#except (TypeError,ValueError) as te:
#    print(te)
#try:
#    print(MergeSort([])._sort())#empty list
#    print(BubbleSort([])._sort())#empty list
#except (TypeError,ValueError) as te:
#    print(te)