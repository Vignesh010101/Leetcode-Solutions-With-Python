class Solution:
    def lengthLongestPath(self, input: str) -> int:
        files_and_folders = input.split("\n")
        def get_num_tab(s: str) -> int:
            for i in range(len(s)):
                if s[i] != "\t": break
            return i

        def is_file(s: str) -> bool:
            return "." in s

        res = 0
        stack = []
        for s in files_and_folders:
            num_tabs = get_num_tab(s)
            while stack and stack[-1][1] >= num_tabs: stack.pop()
            path_len = len(s[num_tabs:])
            if stack: path_len += stack[-1][0] + 1
            stack.append((path_len, num_tabs))
            if is_file(s): res = max(res, path_len)

        return res