'''
### 메모

배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 전부 출력하라

이때, 인덱스값 i, j, k는 전부 다른 수임

브루트포스가 있고
combinations가 있을듯 (인덱스의 중복이 없으므로 combinations를 선택)

* 특이한게, 결과값의 각 원소들이 정렬된 상태로 있네..?
  - 일단 젤 앞에 sort를 해주긴 하는데
  - 정렬된 리스트를 가지고 뭔가 속도나 이런 측면에서 최적화한 방법이 있을라나?
    - 정렬된 결과물이 시간초과 극복할 힌트같은데

* **시간초과 결과를 보고 깨달은 후ㅋ**

* 피벗값(중앙값) 찾아서 걔를 기준으로 좌/우 나눌까?
  - 내가 말하는 중앙값은 음수랑 양수를 구분하는 값임
  - 음수끼리 더할필요 없고, 양수끼리 더할필요 없자나 값이 0이 나와야하니까

이때 두가지 케이스임
왼쪽에서 오면서 왼쪽+1인애 포함 3개
오른쪽에서 오면서 오른쪽-1인애 포함 3개

### 알고리즘 및 방법
```
일단 sort()

pivot = bisect_left(0)     # 0 또는 음수와 양수가 갈라지는 위치의 인덱스값을 찾음(lowerbound)
for left in range(pivot-1):
    for right in range(len(nums), pviot+1, -1):
        sub = [nums[left], nums[left+1], nums[right]]
        if sum(sub) == 0 and sub not in result:
            ans.append(sub)
        
        sub = [nums[left], nums[right-1], nums[right]]
        if sum(sub) == 0 and sub not in result:
            ans.append(sub)

```

### 히든테케 주의사항
```
1)
Input   [0,0,0,0]
Output  [[0,0,0]]

2)
Input   [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Output  [[0,0,0]]

```
'''
from bisect import bisect_left

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # 책 솔루션 : 생각은 비슷하나 좀 다르다
        results = []
        nums.sort()
        
        for i in range(len(nums) - 2):
            # 중복된 값 건너뛰기 (위에 for문 조건 걸 필요없이 if에 0이상일때 쓰면 되네)
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # 간격을 좁혀가며 합 sum 게산 <-- 나랑 다른 부분
            left, right = i+1, len(nums)-1
            
            while left < right:
                suma = nums[i] + nums[left] + nums[right]
                if suma < 0:
                    left += 1
                elif suma > 0:
                    right -= 1
                else:
                    # sum = 0인 경우이므로, 정답추가
                    results.append((nums[i], nums[left], nums[right]))
                    
                    # 그리고 left, right의 다음값이 동일값이면 스킵해버리기(중복 제거를 위해)
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                        
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                        
                    left += 1
                    right -= 1
                    
        return results
                            
#------------------------------------------------------------------------------------
#         # 3차 접근 : 투포인터로 왼/오 이동하면서 계산 -> 시간초과는 해결한듯 하나 새로운 문제점 찾음(히든테케)
#         result = []
#         if len(nums) == 3 and sum(nums) == 0:
#             result.append(nums)
#             return result
                
#         nums.sort()        
#         pivot = bisect_left(nums, 0)
#         for left in range(pivot-1):
#             for right in range(len(nums)-1, pivot, -1):
#                 sub = [nums[left], nums[left+1], nums[right]]
#                 if sum(sub) == 0 and sub not in result:
#                     result.append(sub)

#                 sub = [nums[left], nums[right-1], nums[right]]
#                 if sum(sub) == 0 and sub not in result:
#                     result.append(sub)
#         return result
#------------------------------------------------------------------------------------        
#         # 1차 접근 : combinations를 사용한 방식 - 시간초과 (이게아닌가?)
#         result = []
#         nums.sort()
#         C = combinations(nums, 3)
        
#         for c in C:
#             if sum(c) == 0 and list(c) not in result:
#                 result.append(list(c))
#------------------------------------------------------------------------------------
#         return result

#         # 2차 접근 : 브루트포스
#         result = []
#         nums.sort()
#         print(nums)
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 for k in range(j+1, len(nums)):
#                     if nums[i]+nums[j]+nums[k] == 0 and [nums[i],nums[j],nums[k]] not in result:
#                         result.append([nums[i],nums[j],nums[k]])
#         return result