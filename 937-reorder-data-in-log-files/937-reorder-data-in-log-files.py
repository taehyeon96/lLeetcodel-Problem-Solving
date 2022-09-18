'''
### 메모

* <문제> 로그를 재정렬하라. 기준은 다음과 같다

  * 문자가 동일한 경우 식별자 순으로 정렬시킨다.
    - let 또는 dig 또는 a 또는 zo 이런거 바로 뒤 숫자 (let1 -> let2 -> let3)
    
  * 숫자 로그는 입력된 순서대로 정렬시키고
  
  * 최종 정렬 결과는 문자로 구성된 로그가 숫자 로그보다 앞에 오도록 정렬

```
Input: logs = ["dig1 8 1 5 1",
               "let1 art can",
               "dig2 3 6",
               "let2 own kit dig",
               "let3 art zero"]

Output: ["let1 art can",
         "let3 art zero",
         "let2 own kit dig",
         "dig1 8 1 5 1",
         "dig2 3 6"]
```

### 알고리즘 및 방법
```
일단 이중 리스트로 바꿔줘야될듯(각각 single space기준으로) --> tmp
그다음 for i in tmp
        if i[1] == isalpha() 이면
            text_list.append(i)
        else
            num_list.append(i)
            
       text_list.sort(key = lambda x:(x[1:], x[0])  # <---(중요) x[1:] 이게되네 ㄷㄷㄷ
       
       return text_list + num_list
```       
'''
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # 내가 푼
#         tmp = [list(map(str, i.split())) for i in logs] # 내용물을 리스트로 바꾸는
#         print("과정-->", tmp)
        
#         text = []
#         num = []
#         for i in tmp:
#             if i[1].isalpha():
#                 text.append(i)
#             else:
#                 num.append(i)
        
#         print("과정-->", text)
#         print("과정-->", num)
        
#         text.sort(key = lambda x:(x[1:], x[0]))    # <---(중요) x[1:] 이게되네 ㄷㄷㄷ
        
#         print("과정-->", text)
        
#         ans = [" ".join(i) for i in (text + num)]  # <---(중요) 이게되네 ㄷㄷㄷ
        
#         print("정답-->", ans)
#         print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
#         return ans
        
        # 책 솔루션 (큰 알고리즘은 나와 같음)
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        
        letters.sort(key = lambda x: (x.split()[1:], x.split()[0]))
        
        return letters + digits
       