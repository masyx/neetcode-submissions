class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        prev_days = []
        answer = [0] * len(temperatures)
        for curr_day in range(1, len(temperatures)):
            prev_days.append(curr_day - 1)
            curr_temp = temperatures[curr_day]
            while prev_days and temperatures[prev_days[-1]] < curr_temp:
                prev_day = prev_days.pop()
                answer[prev_day] = curr_day - prev_day
        return answer


        