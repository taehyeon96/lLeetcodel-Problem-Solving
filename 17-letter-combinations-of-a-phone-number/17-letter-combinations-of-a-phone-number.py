'''
### 메모

2에서 9까지 숫자가 주어졌을 때 전화번호로 조합 가능한 모든 문자를 출력

* combinations쓰는게 아니라 걍 브루트포스 최대 4번 돌려야함

* 입력값의 길이는 0 ~ 최대 4까지다
 - 맨첨에 len()==0일때 return None 전처리 해주자
 - 맨첨에 len()==1일 때는 해줄수가 없음. 왜냐면 7번 9번이 4개짜리임


그리고 저거 만들어줘야할듯.. 전화기 번호에 따른 문자들

### 알고리즘 및 방법
```
전처리 해주고

해시테이블을 만들어줘야하나
phone = {"2":"abc", "3":"def", "4":"ghi", ...} 이렇게 만든 다음에

dfs()

```

* dfs 어케하냐가 중요 (이런 유형 처음 풀었으니까 이해하자 꼭)

'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        def dfs(index, path):
            
            if len(path) == len(digits):
                result.append(path)
                return

            for i in range(index, len(digits)):
                for j in dic[digits[i]]:
                    dfs(i + 1, path + j)
        
        if not digits: return []
        
        dic = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", 
               "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz" }
        result = []
        
        dfs(0, "")
        
        return result
        
#         # 책 솔루션 - 나중에 다시 풀어보자
#         def dfs(index, path):
#             # 누른 번호 수만큼 왔으면 백트래킹 (일종의 전처리임 - 되돌아가는~> 백트래킹 = 함수 한 칸씩 되돌아가는거)
#             if len(path) == len(digits):  # input의 길이만큼만 dfs 수행할거임 (path는 버튼 누른 횟수)
#                 result.append(path)       # 모든 dfs결과물을 append()해줘야함. (return이 아님!)
#                 return
            
#             # dfs 깊이에 따라 반복횟수 달리 하기 위해 range()지정 = (0~4 -> 1~4 -> 2~4 -> 3~4 내가 원하던거 이거)
#             for i in range(index, len(digits)):
#                 # 다음차례 누른 번호의 모든 문자에 대해 dfs 진행
#                 for j in dic[digits[i]]:       # digits[i]에 해당하는 value값을 접근해야댐
#                     dfs(i + 1, path + j)       # dfs(index부터 하나씩 늘려서 깊이있게 ㄱ, paht에 다음 문자열 전부다 add하면서 dfs함)
        
        
#         if not digits:
#             return []
        
#         dic = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", 
#                "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz" }
#         result = []
        
#         dfs(0, "")    # 파라미터 : 해당 dfs에서 for문 돌릴 횟수 계산용, 걸어온길 
        
#         return result  # 여기서 최종리턴
        