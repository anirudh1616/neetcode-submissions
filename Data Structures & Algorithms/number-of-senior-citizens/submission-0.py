class Solution:
    def countSeniors(self, details: List[str]) -> int:
        counter = 0
        for i in range(len(details)):
            temp_string = details[i]
            first_dig = temp_string[11]
            second_dig = temp_string[12]
            current = first_dig + second_dig
            age = int(current)
            if age > 60:
                counter += 1
        
        return counter
            
