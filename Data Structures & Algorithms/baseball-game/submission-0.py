class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # Given a list of string values which are operations. operations are limited to ints, +, and letters 'D' and 'C'.
        # Traverse the list of operations, and add integers to a secondary list based off of the operations described.
        # Sum up the final list after the last operation is completed, and return the total.

        scores = []
        sum = 0
        for i in range(len(operations)):
            if operations[i] == "+":
                scores.append(scores[-1] + scores[-2])
            elif operations[i] == "D":
                scores.append(scores[-1] * 2)
            elif operations[i] == "C":
                scores.pop()
            else:
                scores.append(int(operations[i]))
        for i in range(len(scores)):
            sum += scores[i]
        
        return sum