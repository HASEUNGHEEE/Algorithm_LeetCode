class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # -2147483648 <= nums[i] <= 2147483647
        # nums = [0,2,3,4,6,8,9]
        output = []
        i = 0
        while i < len(nums):
            start = end = i
            # [0] => 0
            # [2] [2,3] [2,3,4] => 2->4 
            # (outofrange 주의) 끝인덱스+1이 nums 길이보다 작고, 다음 원소가 현재 원소+1 겂이면 끝 인덱스를 하나씩 증가시킨다
            while end+1 < len(nums) and nums[end+1] == nums[end]+1: end+=1
            if start == end:
                output.append(f'{nums[start]}') # output.append(str(nums[s]))
            else:
                output.append(f'{nums[start]}->{nums[end]}')
            
            i = end+1 # 끝 인덱스 + 1 값부터 다시 로직 반복
        return output