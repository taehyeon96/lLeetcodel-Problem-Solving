'''
### 메모

이거 전에 NHN 기출 풀 때 풀었던 문제랑 동일

건물의 높이들을 리스트로 입력받고
그안에 틈이 있으면 얼만큼의 물이 채워지는지 계산하는 문제

### 알고리즘 및 방법

mm <- max높이 저장해둠
각각 양쪽 끝에서 투포인터로 mm까지 이동하면서
**자기보다 낮은 건물이면** ans += (현위치 - 낮은 위치 = 매 순간의 물)
**자기랑 같거나 높은 건물이면** 현위치 갱신

```
left와 right 구분해서 mm까지만 이동하는 것으로 진행 + 투포인터 사용

left, right = 0, len(arr)           # cur 용 인덱스 위치 (포인터 1)

# 왼쪽부터
for i in range(0 to (mm + 1)):      # i는 이동하는 위치 (포인터 2)
    if arr[cur] > arr[i]:           # 낮아지는 구간
        water += (arr[cur]-arr[i])  # (기준 위치와 낮아진 만큼의 차)를 더해줌
        
    elif arr[cur] <= arr[i]:        # 높아지는 구간
        cur = i                     # 물을 채우는 기준 위치 갱신
    
# 반대로 오른쪽부터
for i in range(len() to mm):
    ~

```

'''

class Solution:
    def trap(self, arr: List[int]) -> int:
        left, right = 0, len(arr)-1
        
        mm = arr.index(max(arr))        # (중요!!!) max의 인덱스를 저장해야함
        water = 0
        
        # 왼쪽 투포인터 진행
        for i in range(0, mm + 1):
            print(left, arr[left], "||", i, arr[i], "||", water)
            if arr[left] > arr[i]:
                water += (arr[left] - arr[i])
            elif arr[left] <= arr[i]:
                left = i        
        
        # 오른쪽 투포인터 진행
        for i in range(right, mm, -1):
            print(left, arr[left], "||", i, arr[i], "||", water)
            if arr[right] > arr[i]:
                water += (arr[right] - arr[i])
            elif arr[right] <= arr[i]:
                right = i
        
        return water
            
            
            
            