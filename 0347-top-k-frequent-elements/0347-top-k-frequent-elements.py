class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # stores frequency of each element in dictionary
        freq = Counter(nums)

        # converts the keys of 'freq' into an array
        elements = list(freq.keys())

        # Step 3: Sort elements based on their frequency (descending..highest freq element first)
        elements.sort(key=freq.get, reverse=True)

        # Step 4: Return first k elements
        return elements[:k]