"""
This module contains an abstract class
which is implemented in a Linear Search algorithm
and Binary Search algorithm in two other classes
"""
from abc import ABC, abstractmethod
import time
"""Module with the base implementation of a Search class."""
class Search(ABC):
    """Abstract base class for searching."""
    def __init__(self, items,target):
        self._items = items
        self._target=target
    #every child class must implement this
    @abstractmethod
    def _search(self):
        """Returns the first index
        if item found
        else should return None.
        """
        pass
    #getter methods
    def get_items(self):
      return self._items
    def get_target(self):
      return self._target
    #child may override as per need
    def _time(self):
      self.time = 0
      return self.time
###########################################################
class LinearSearch(Search):
    """Class that represents a Linear Search implementation."""
    def _search(self):
      items=self.get_items()
      target=self.get_target()
      for index, item in enumerate(items):
        if item == target:
          return index
      return None  # Return None if the target is not found
    def _time(self):
        # Measure and return the time taken to search the items if needed
        start_time = time.time()
        sorted_items = self._search()
        end_time = time.time()
        self.time = end_time - start_time
        return self.time #in millisec
#################################################################
class BinarySearch(Search):
    """Class that represents a Binary Search implementation."""
    #private method to check list is sorted
    def __is_sorted(self):
      """our binary search algorithm requires lst
      sorted in ascending order
      """
      lst=self.get_items()
      return all(lst[i] <= lst[i+1] for i in range(len(lst) - 1))
    def _search(self):
      items=self.get_items()
      if(self.__is_sorted() is False):
        return "Please use our sorting algorithms first on the input."
      target=self.get_target()
      #binary search requires array
      #to be sorted
      left, right = 0,len(items)-1
      while (left <= right):
        mid = (left + right)//2
        if items[mid]==target:
          return mid
        elif items[mid]<target:
          left = mid + 1
        else:
          right = mid - 1
      return None  # Return None if the target is not found
    def _time(self):
      # Measure and return the time taken to search the items if needed
      start_time = time.time()
      sorted_items = self._search()
      end_time = time.time()
      self.time = end_time - start_time
      return self.time
##few sample ip & op for testing & execution##
##uncomment to run##
#print(BinarySearch([-999999,25,1000],-23)._search())#when not in list
#print(LinearSearch([1,23,4,-1,-9,1000,13,100000,1304141,14,1000,-999999],-23)._search())#when not in list
#print(LinearSearch([1,23,4,-1,-9,1000,13,100000,1304141,14,1000,-999999],23)._search())
#print(BinarySearch([1,23,4,-1,-9,1000,13,100000,1304141,14,1000,-999999],23)._search())#error msg as array not sorted!
#from Sort import MergeSort#proves we can import from our Sort module
#print(BinarySearch(MergeSort(items=[1,23,4,-1,-9,1000,13,100000,1304141,14,1000,-999999])._sort(),23)._search())
