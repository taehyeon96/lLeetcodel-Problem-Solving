# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


'''
### 메모
* 링크드리스트 기본문제, 팰린드롬은 리트코드 125 문자열 문제에서 설명
* input 설명 
  - head에 ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}}
  
* 단방향 연결리스트이므로, 반대부터 오는게 불가
* 그리고 자료형 자체를 node로 주었기 때문에 결국 순차적으로 O(n)으로 가면서 체크해야할거같음

### 알고리즘 및 방법
걍 하나씩 꺼내서 리스트에 따로 저장해두지 모
그 이후는 리트코드 125랑 똑같이

* 베이직 솔루션도 내 방식이랑 같다 (리스트에 따로 저장후 팰린드롬 판별)
  - 대신 리트코드 125 문제처럼 리스트에서/deque에서 pop(0)과 pop()를 비교했다
  
### 솔루션 해설
* 내가 푼 방법으로도 풀이가 있고
* 런너(runner)를 이용한 풀이가 있음
  - 연결리스트 문제의 정통 풀이법은 사실 런너를 이용함
  - slow는 한칸, fast는 두 칸씩 이동하는데
  - fast가 링크드리스트 끝에 도달하면
  - slow는 반드시 링크드리스트 중앙에 도착하는걸 보장함 (그림으로 그려봐 두칸씩 이동하니까 당연)

* 그리고, reversn은 새로운 링크드 리스트임 (slow의 역순 링크드리스트)
  - slow이동하면서 새롭게 생성해줄 것임
  
* 따라서 slow가 중간지점부터 한칸씩 이동하고
  - reversn은 반대로 한칸씩 이동해서
  - 둘이 똑같은지 비교
  
  
'''
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:        
        arr = []
        
        while 1:
            arr.append(head.val)
            
            if head.next == None: break   # while조건으로 두면 마지막 노드는 무시되어버림
                
            head = head.next
            
        if arr == arr[::-1]:   # 리스트 vs 리스트역순이 같으면 true
            return True
        else:
            return False

#         # 솔루션 - 런너(runner)를 이용한 풀이
#         reversn = None
#         slow = fast = head
        
#         while fast and fast.next:
#             # fast는 두 칸 이동
#             fast = fast.next.next
            
#             # 리버스 링크드리스트 생성과 동시에 slow는 한 칸 이동 (동시할당해야 시간초과X 주의)
#             reversn, reversn.next, slow = slow, reversn, slow.next
            
#         # 링크드리스트의 길이가 홀수인 경우 주의(slow를 한칸 더 이동해서 중앙 맞춰줌)
#         if fast:
#             slow = slow.next
            
#         # 팰린드롬 여부 확인
#         while reversn and reversn.val == slow.val:
#             slow, reversn = slow.next, reversn.next    # 한칸씩 이동
            
#         return not reversn
        
    
    
    