class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = []
        letters = []
        res_list = []

        for i in range(len(logs)):
            logs[i] = logs[i].split(' ')

        for log in logs:
            if 'a' <= log[1][0] and log[1][0] <= 'z':
                letters.append(log)
            else:
                digits.append(log)

        sorted_letters = sorted(letters, key = lambda x : (x[1:],x[0]))

        res_list = sorted_letters+digits
        for i in range(len(res_list)):
            res_list[i] = " ".join(res_list[i])

       
        return res_list