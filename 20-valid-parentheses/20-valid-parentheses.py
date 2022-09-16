'''
### 메모

(()) O
([)] <----이거 어떻게??
(((]]] X
([()])O
]() X

[((])) <---- 이거는?
(( <--- 틀려야함
(){}}{ <----틀려야함

### 알고리즘 및 방법

if len(s) == 1:    # 시작할 때 예외처리
    return False
    
스택 만들고

for i in s:
    if i == 여는 괄호 종류:
        스택.append()
        
    else:
        if 스택이 비어잇으면(= 여는 괄호가 없는데 닫는괄호 나온 경우) 중요
            return false
            
        open = 스택.pop()
        if open == '(' and (i == ']' or i == '}'):
            return False
        elif open == '[' and 다른케이스면:
            return False
        elif open == '{' and 다른케이스면:
            return False
return True        
'''
class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) == 1:    # 시작할 때 예외처리
            return False
    
        stack = []

        for i in s:
            if i in ['(', '[', '{']:
                stack.append(i)
                
            else:
                if not stack:
                    return False
                
                nono = stack.pop()
                if nono == '(' and (i == ']' or i == '}'):
                    return False
                elif nono == '[' and (i == ')' or i == '}'):
                    return False
                elif nono == '{' and (i == ')' or i == ']'):
                    return False
        
        if stack:
            return False
        else:
            return True      
        
#         # 솔루션 코드 - 책정답
#         stack = []
#         # "여는 괄호"를 value로 --> if A in arr 할 때 활용하기 위함
#         table = {
#             ')' : '(',
#             ']' : '[',
#             '}' : '{'
#         }
        
#         for c in s:
#             if c not in table:
#                 stack.append(c)
                
#             # 스택이 비어있거나(여는게 없는데 닫는게 나옴) or 스택pop이 매칭되지 않으면 false
#             elif not stack or table[c] != stack.pop():
#                 return False
#         return len(stack) == 0
            
            
    
    