from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        actualans = []

        def backtrackfn(current_combination, remaining_target, start_index):
            if remaining_target == 0:
                actualans.append(list(current_combination))
                return
            elif remaining_target < 0:
                return

            for i in range(start_index, len(candidates)):
                current_combination.append(candidates[i])
                backtrackfn(current_combination, remaining_target - candidates[i], i)
                current_combination.pop()
        
        backtrackfn([], target, 0)
        return actualans
