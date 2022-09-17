'''
### 메모

* input형태
  - TreeNode{val: 3, 
            left: TreeNode{val: 9, left: None, right: None}, 
            right: TreeNode{val: 20, 
                            left: TreeNode{val: 15, left: None, right: None}, 
                            right: TreeNode{val: 7, left: None, right: None}}}

### 알고리즘 및 방법

그래프 문제로 바꿔서 풀면?  => 불가
-> 그래프형태로 만들어줌
-> 근데 val 범위가 -100부터 100까지임 안됨

### 책 솔루션 설명
* BFS를 사용한다
  - 이유 : 동일 레벨은 depth가 동일하게 계산되야함 = BFS
  - DFS쓰면 depth를 ++해나갈 때 계속 중첩돼서 동일 레벨(형제노드)인데 dpth가 달라질 수 있음


* que에 부모노드를 넣어주고 BFS 시작
  - while 한바퀴 돌 때마다 depth ++
  - (중요) BFS로 해야되는 이유 : (= len(que) 하면 반복이 루트노드일 때 1번만, 인터널일 때 2번만, ... => depth 동일해짐)
  - for 0~현재 노드 개수  
    - if left 있으면 que.append()
    - if right 있으면 que.append()

* **(중요) 즉, BFS로 진행하면서 레벨단위로 큐에 append()하고 depth를 체크해나감**
  - 레벨단위로 하는 방법 
    - for문에 현재 레벨의 노드 수만큼만 반복해서, 
    - 현재 레벨의 자식 노드들 전부 넣고 while로 돌아감
    
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0
        
        que = deque()
        que.append(root)
        depth = 0
        
        while que:
            depth += 1                             # 레벨 방문할 때마다 ++됨
        
            for _ in range(len(que)):              # 현재 레벨의 노드 수만큼만 반복 (루트=1, 인터널=2)
                current_level_node = que.popleft() # 현재 레벨의 모든 노드의 자식 노드를 전부 append() ~> BFS를 위해 
                
                if current_level_node.left != None:
                    que.append(current_level_node.left)
                if current_level_node.right != None:
                    que.append(current_level_node.right)
                
        return depth
                