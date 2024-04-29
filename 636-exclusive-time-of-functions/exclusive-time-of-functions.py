class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        for i in logs:
            func_id, flag, timestamp = i.split(":")
            func_id = int(func_id)
            timestamp = int(timestamp)
            if flag == "start":
                stack.append([func_id, timestamp])
            else:
                last_id, last_timestamp = stack.pop()
                duration = timestamp - last_timestamp + 1
                res[last_id] += duration
                if stack:
                    res[stack[-1][0]] -= duration
        return res
        