class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        idx = 0
        res = n
        for s in sandwiches:
            count = 0
            while count < n and students[idx] != s:
                idx += 1
                idx %= n
                count += 1
                
            if students[idx] == s:
                students[idx] = -1
                res -= 1
            else:
                break
        return res