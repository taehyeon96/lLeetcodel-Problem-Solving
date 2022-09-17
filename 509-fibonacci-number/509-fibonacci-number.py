class Solution:
    
    # (중요) 클래스에서 global 변수는 여기에 선언
    global arr
    arr = [0] * 31   # n의 범위가 30까지이므로
    
    def fib(self, n: int) -> int:
        
        # 2번) 메모이제이션 (top-down) : 위에서부터 최고끝까지 내려간 후 하나씩 계산해 올라가되, 이미 있는 값은 계산X
        
        if n <= 1:  
            return n         # 0과 1은 인덱스넘버로 리턴해야함
        if arr[n] != 0:      # 값이 있으면
            return arr[n]
        
        arr[n] = self.fib(n-1) + self.fib(n-2)   # (중요) 클래스 안 재귀함수 사용법
        
        return arr[n]
        
#         # 1번) 타뷸레이션 (bottom-up) : 테이블을 앞으로 만들어나가는 방법
#         
#         arr[0], arr[1] = 0, 1
        
#         for i in range(2, n+1):
#             arr[i] = arr[i-2] + arr[i-1]
#         return arr[n]