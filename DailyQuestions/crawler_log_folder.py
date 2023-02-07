class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ops = 0

        for log in logs:
            if log == '../':
                if ops : ops -= 1

            elif log == "./":
                continue

            else:
                ops += 1

        return ops