class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        max_pop = float('-inf')
        earliest_year = 1950

        for year in range(1950,2051):
            pop = 0
            for b,d in logs:
                if b <= year and year < d:
                    pop += 1

            if pop > max_pop:
                earliest_year = year
                max_pop = pop

        return earliest_year