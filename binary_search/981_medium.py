from typing import List
import bisect

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        Uses a dictionary to store lists of (timestamp, value) pairs for each key.
        """
        self.store = {}  # key -> list of (timestamp, value) tuples

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        Stores the key with the value at the given timestamp.
        
        Args:
            key: Key to store the value under
            value: Value to store
            timestamp: Timestamp for this value
        """
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        """
        Returns the value associated with the key at the given timestamp.
        If no exact timestamp exists, returns the value with the largest timestamp 
        that is less than or equal to the given timestamp.
        
        Args:
            key: Key to look up
            timestamp: Timestamp to find value for
            
        Returns:
            Value associated with key at or before the timestamp, or empty string if not found
        """
        if key not in self.store:
            return ""
        
        # Binary search for the rightmost timestamp <= given timestamp
        # Using bisect_right on list of (timestamp, value) tuples
        # We need to search based only on timestamp, so we use a key function
        values = self.store[key]
        
        # Find the rightmost position where timestamp would be inserted
        # This gives us the largest timestamp <= target timestamp
        left, right = 0, len(values)
        while left < right:
            mid = (left + right) // 2
            if values[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid
        
        # If left == 0, no timestamp <= target timestamp exists
        if left == 0:
            return ""
        
        # Return the value at the found position (left - 1)
        return values[left - 1][1]

def run_time_map_test(operations: List[str], inputs: List[List], expected: List, test_name: str):
    """
    Tests the TimeMap operations.
    
    Args:
        operations: List of operation names ("TimeMap", "set", "get")
        inputs: List of inputs for each operation
        expected: Expected results for "get" operations
        test_name: Name/description of the test case
    """
    time_map = TimeMap()
    results = []
    expected_idx = 0
    
    print(f"{test_name}:")
    for i, op in enumerate(operations):
        if op == "TimeMap":
            time_map = TimeMap()
        elif op == "set":
            key, value, timestamp = inputs[i]
            time_map.set(key, value, timestamp)
        elif op == "get":
            key, timestamp = inputs[i]
            result = time_map.get(key, timestamp)
            results.append(result)
            expected_val = expected[expected_idx]
            print(f"    get({key}, {timestamp}) -> {result}, expected: {expected_val}, pass: {result == expected_val}")
            expected_idx += 1
    
    print(f"  Overall Pass: {results == expected}")
    print()

# Run test cases
run_time_map_test(
    ["TimeMap", "set", "get", "get", "set", "get", "get"],
    [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]],
    ["bar", "bar", "bar2", "bar2"],
    "Example 1: Basic TimeMap operations"
)

run_time_map_test(
    ["TimeMap", "set", "set", "get", "get", "get", "get", "get"],
    [[], ["a", "1", 1], ["a", "2", 2], ["a", 1], ["a", 2], ["a", 3], ["a", 0], ["b", 1]],
    ["1", "2", "2", "", ""],
    "Edge case: Multiple values for same key"
)

run_time_map_test(
    ["TimeMap", "set", "get", "get", "get"],
    [[], ["love", "high", 10], ["love", 10], ["love", 15], ["love", 5]],
    ["high", "high", ""],
    "Edge case: Get before any timestamp"
)

run_time_map_test(
    ["TimeMap", "set", "set", "set", "get", "get", "get"],
    [[], ["a", "1", 1], ["b", "2", 2], ["c", "3", 3], ["a", 1], ["b", 2], ["c", 3]],
    ["1", "2", "3"],
    "Edge case: Different keys"
)