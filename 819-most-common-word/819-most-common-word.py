'''
### 메모
* 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라
* 대소문자 구분을 하지 않으며, 구두점(마침표, 쉼표 등) 또한 무시한다.

* 단어 기준인거 같으니 ........ B
  - split()을 써서 리스트에 저장하고 Counter쓰면 될듯
  
* 그중에서 banned는 제외시켜야함 ........ A
  - split()해서 리스트 저장하기 전에
    - for i in banned: 기존문자열.replace(i, "")
    
    
### 알고리즘 및 방법

```
소문자로 바꾼다 <-- 히든테케 1번 때문에 가장 먼저 수행

특수문자를 " "로 제거한다 <-- 히든테케 2번 때문에 " "로 제거해야함(안그럼 애들이 달라붙음)

" "를 기준으로 분리해서 리스트로 만든다 <-- 히든테케 3번 때문에 banned 제거 전에 수행

리스트에 banned가 있으면 제거해준다

counter

return most_common(1)
```
### 히든테케
```
1)
Input       "Bob. hIt, baLl"
            ["bob", "hit"]
            
Output      "ball"
-----------------------------------------------------
2) 생각해보면 이거도 어이없네 ㅋ;;;
Input       "a, a, a, a, b,b,b,c, c"
            ["a"]
            
Output      "b"

-----------------------------------------------------
3) 미쳤나 이거... 이걸알려줘야지 첨부터;
   --> replace하면 안되겟네.. 첨부터 리스트로 끊어서 저장하고 for문 돌려야할듯
Input       "abc abc? abcd the jeff!"
            ["abc","abcd","jeff"]

Output      "the"


```
<중요> replace() 결과는 어디에 꼭 할당해줘야함
'''
from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        # 책 솔루션 - 정규식 사용 (중요) - 외워야함 이건
        
        '''
        정규식에서 \w 는 단어문자를 뜻하며, ^은 not을 의미한다.
        따라서 다음 정규식은 단어문자가 아닌 모든 문자를 공백으로 치환하는 역할을 한다
        '''
        
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
        
        c = Counter(words)
                
        return c.most_common(1)[0][0]
        
#         # 내가 푼 - 2차
#         paragraph = paragraph.lower()
                
#         for i in ("!", "?", "'", ",", ";", "."):
#             paragraph = paragraph.replace(i, " ")  # 히든테케 2 --> " "
        
#         # 히든테케 3 때문에 먼저 리스트 만들고 일일히 비교 (replace 사용 불가)
#         paragraph = paragraph.split()    
        
#         if banned:
#             for i in range(len(banned)):
#                 for j in range(len(paragraph)):
#                     if banned[i] == paragraph[j]:
#                         paragraph[j] = ""
        
#         c = Counter(paragraph)
        
#         if len(c) > 1 and c.most_common(1)[0][0] == "":
#             return c.most_common(2)[1][0]
#         else:        
#             return c.most_common(1)[0][0] 
    
    
#         # 내가 푼 - 1차 - 히든테케땜에 틀리게된 케이스 
#         paragraph = paragraph.lower()
        
#         if banned:
#             for i in banned:
#                 paragraph = paragraph.replace(i, "")
                
#         for i in ("!", "?", "'", ",", ";", "."):
#             paragraph = paragraph.replace(i, " ")
            
#         arr = paragraph.split()
#         c = Counter(arr)
        
#         return c.most_common(1)[0][0]