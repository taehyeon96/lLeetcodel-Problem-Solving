'''
### 메모

대표적인 BFS DFS 문제임 (섬 개수 찾기)

그냥 
for
    for
        if graph[i][j] is 1
            bfs( 이 안에서 방문한 위치는 1을 0으로 바꿔줌 )
            
* (중요) 중첩 함수(Nested Function)이란
  - 함수 내 위치한 또다른 함수로,
  - 해당 함수의 바깥에 위치한 함수들과 달리
  - 부모 함수의 변수를 자유롭게 읽을 수 있다는 장점이 있다. --> 여기선 graph가 해당됨!!

'''
from collections import deque

class Solution:
            
    def numIslands(self, graph: List[List[str]]) -> int:       
        
#         def bfs(i, j):
#             que = deque()
#             que.append((i, j))
#             graph[i][j] = '0'     # visit check

#             dy, dx = [-1, 0, 1, 0], [0, -1, 0, 1]    # 상 좌 하 우

#             while que:
#                 y, x = map(int, que.popleft())

#                 for i in range(4):
#                     ny, nx = y + dy[i], x + dx[i]

#                     if 0<=ny and ny < len(graph) and 0<=nx and nx < len(graph[0]) and graph[ny][nx] == '1':
#                         graph[ny][nx] = '0'
#                         que.append((ny,nx))

        def dfs(y, x):
            graph[y][x] = '0'     # visit check

            dy, dx = [-1, 0, 1, 0], [0, -1, 0, 1]    # 상 좌 하 우
            
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]

                if 0<=ny and ny < len(graph) and 0<=nx and nx < len(graph[0]) and graph[ny][nx] == '1':
                    dfs(ny, nx)

        ans = 0
        for y in range(len(graph)):
            for x in range(len(graph[0])):
                if graph[y][x] == '1':
                    dfs(y, x)
                    ans += 1
        return ans