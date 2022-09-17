'''
### 알고리즘 및 방법

**일단 기본적으로 바이너리서치는 "정렬되어있어야 함"을 전제로 푼다**(안되어있다면 정렬시키고)
여러 방법이 있음

* 1) 라이브러리 사용
  - (중요) 핵심은 if nums[index] == target:  <--- 이게맞으면 정답, 아니면 -1하면 된다

* 2) 기본 바이너리 서치 구현


'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
#         # 2) 기본 바이너리 서치 구현
#         start = 0
#         end = len(nums)-1
        
#         while start <= end:
#             pivot = (start+end) // 2
            
#             if target < nums[pivot]:
#                 end = pivot - 1
#             elif nums[pivot] < target:
#                 start = pivot + 1
#             else:
#                 return pivot
            
#         return -1
        
        # 1) 라이브러리 사용
        from bisect import bisect_left
        
        index = bisect_left(nums, target)
        
        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1
        