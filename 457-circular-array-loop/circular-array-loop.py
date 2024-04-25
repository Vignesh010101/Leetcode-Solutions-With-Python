class Solution:
    def _is_node_red(self, nums, i):
        return True if nums[i] < 0 else False
    

    def _jumpto(self, nums, i):
        n = len(nums)
        offset = nums[i]
        if offset > 0:
            return (i + offset) % n

        idx = i - (-1 * offset) % n 
        return idx if idx >=0 else n + idx

    def circularArrayLoop(self, nums: List[int]) -> bool:
        for i, node in enumerate(nums):
            if isinstance(node, int):
                index = i
                if node > 0:
                    # follow white nodes
                    while True:
                        next_index = self._jumpto(nums, index)
                        # self-pointing node, abort
                        if next_index == index:
                            break

                        # already visited node, if part of same i then cycle, else abort and keep looking
                        if not isinstance(nums[next_index], int):
                            if nums[next_index] == str(i):
                                return True
                            else:
                                break
                        if not self._is_node_red(nums, next_index):
                            nums[index] = str(i)
                            index = next_index
                        else:
                            break # if reached red node, abort
                    
                else:
                    # follow red nodes
                    while True:
                        next_index = self._jumpto(nums, index)
                        if next_index == index:
                            break
                        if not isinstance(nums[next_index], int):
                            if nums[next_index] == str(i):
                                return True
                            else:
                                break

                        if self._is_node_red(nums, next_index):
                            nums[index] = str(i)
                            index = next_index
                        else:
                            break
        

        return False