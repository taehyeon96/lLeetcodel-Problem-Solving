'''
### 메모

* **서로 다른 정수를 입력받아 가능한 "모든 순열"을 리턴하라**
  - Permutations
  - itertools사용 안하고 하는 방법
    - DFS 활용

* 위 그림에서 리프노드 (A33)의 모든 노드가 순열의 최종 결과다.
  - 레벨이 아래로 내려갈수록 자식 노드 개수는 점점 줄어든다
    - 루트는 3개, 인터널 2개, 리프 1개
    - 이는 순열의 수식이기도 하다.
    - 예를들어 3이면 3x2x1
    - 5이면 5x4x3x2x1
    - 이때 자식 수도 마찬가지로 5x4x3x2x1

### 알고리즘 및 방법

```

```
* 이전 값을 하나씩 덧붙여 계속 재귀 호출을 진행하다 리프노드에 도달한 경우(= len(elements)==0) 결과를 하나씩 추가
  - 앞서 전화기 다이얼 문제도 이렇게 풀 수 있다.
  
* 중요한 점은, 결과를 추가할 때 prev_elements[:] 로 처리해야한다는 점이다.
  - 파이썬은 **모든 객체를 참조하는 형태로 처리**되기 때문에
    - results.append(prev_elements)를 하면 **결과값이 추가되지 않고, prev_elements에 대해 참조가 추가**됨
    - 그리고 참조되는 값이 변경되면 저 값도 같이 바뀜!!!

* 따라서 반드시 복사할 땐 다음 방법들을 사용하자
  - [:]
  - copy()
  - deepcopy()
  
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # 1) DFS 풀이
        results = []
        prev_elements = []
        
        def dfs(elements):
            # A. 리프 노드일 때 결과 추가
            if len(elements) == 0:
                results.append(prev_elements[:])   # deepcopy를 이용해 복사 중요
            
            # B. 순열 생성 재귀 호출 (루트->인터널 이동하며 path기록)
            for e in elements:
                # 앞에서부터 하나씩만 빼보며 모든 경우의 수에 대한 dfs
                next_elements = elements[:]        # deepcopy를 이용해 복사 중요
                next_elements.remove(e)            # 슬라이싱할거기 때문에 remove사용 (1개남을 경우 [1:]하면 out of range)
                
                prev_elements.append(e)
                
                dfs(next_elements)
                prev_elements.pop()                # dfs 완전히 끝까지 간게 끝나면 결과에 path추가했으니, prev는 pop해야함
        
        dfs(nums)  #(= permutations(nums, len(nums)) 임)
                
        return results
        
        
        '''
        # 1) Permutations - DFS 구현 (위에 코드에서 바꿈)
        results = []
        prev_elements = []
        
        def dfs(elements,n):
            # A. 리프 노드일 때 결과 추가
            if len(elements) == len(nums)-n:
                results.append(prev_elements[:])   # deepcopy를 이용해 복사 중요
            
            # B. 순열 생성 재귀 호출 (루트->인터널 이동하며 path기록)
            for e in elements:
                # 앞에서부터 슬라이싱하여 모든 경우의 수에 대한 dfs
                next_elements = elements[:]        # deepcopy를 이용해 복사 중요
                next_elements.remove(e)            # 슬라이싱할거기 때문에 remove사용 (1개남을 경우 [1:]하면 out of range)
                
                prev_elements.append(e)
                
                dfs(next_elements,n)
                prev_elements.pop()                # dfs 완전히 끝까지 간게 끝나면 결과에 path추가했으니, prev는 pop해야함
        
        
        dfs(nums,2)  #(= permutations(nums, 내가 원하는 수) 임)
        
        print(results)
        
        return results
        
        '''
        
        
        
        
        