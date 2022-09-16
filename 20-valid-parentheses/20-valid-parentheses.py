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

if len(s) == 1 or s[0] not in ['(', '[', '{']    # 시작할 때 예외처리
    return False
    
스택 만들고

for i in s:
    if i == 여는 괄호 종류:
        스택.append()
        
    else:
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
    
    