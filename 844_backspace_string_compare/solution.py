class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # Время:  O(n + m) n = len(s), m = len(m)
        # Память: O(n + m)
        # Если решать через указатели, то по памяти О(1)
        stack_of_s = []
        stack_of_t = []

        for char in s:
            if char != "#":
                stack_of_s.append(char)
            elif stack_of_s:
                stack_of_s.pop()

        for char in t:
            if char != "#":
                stack_of_t.append(char)
            elif stack_of_t:
                stack_of_t.pop()
    
        return stack_of_s == stack_of_t
