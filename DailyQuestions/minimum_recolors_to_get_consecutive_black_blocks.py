class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = right = cur_sum = ops = 0
        min_ops = len(blocks)

        while left <= right:

            if cur_sum == k:
                min_ops = min(min_ops,ops)
                if blocks[left] == 'W':
                    ops -= 1
                left += 1
                cur_sum -= 1

            if right == len(blocks): break

            if blocks[right] == 'W':
                ops += 1

            cur_sum += 1
            right += 1
        

        return min_ops