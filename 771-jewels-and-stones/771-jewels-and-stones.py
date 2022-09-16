'''
### 메모

일단 대소문자 구분하는데
jewels에 있는게 한 묶음으로 보석이 아니라, 개별적으로 보석인거
* aA => a라는 보석이랑 A라는 보석이 있음
  - 따라서 a 1개, A 2개 총 3개가 답인거

### 알고리즘 및 방법

* 방법 1 
  - Counter 라이브러리(=딕셔너리) 쓰면 끝날듯 ~> 일단 객체 만들고
  - for 각각의 주얼리
    - 정답수 += 딕셔너리[키값]   (= 개수니까)

'''

# from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
#         # 1-1) 내가 푼 방식 1 - Counter 사용 (책 솔루션과 동일)
#         ans = 0
#         c = Counter(stones)    # Counter({'b': 4, 'A': 2, 'a': 1})
        
#         for i in jewels:            
#             ans += c[i]
            
#         return ans


#         # 1-2) 내가 푼 방식 2 - 파이썬다운 브루트포스 (책에 딕셔너리 안써도 된다는거 보고 푼)
#         return len([i for i in jewels for j in stones if i == j])
        

#         # 2) 책 솔루션 - Counter 쓰지 않고 직접 해시테이블 생성
#         freqs = {}
#         ans = 0
        
#         # 돌(s)의 빈도수 계산 = Counter 직접구현 (= 딕셔너리 생성 방법 중요!)
#         for char in stones:
#             if char not in freqs:  # 없으면 새롭게 추가
#                 freqs[char] = 1
#             else:
#                 freqs[char] += 1
                
#         # 보석(j)의 빈도수 합산
#         for char in jewels:
#             if char in freqs:
#                 ans += freqs[char]
#         return ans

        
        # 3) 책 솔루션 - defaultdict를 이용한 불필요한 비교 생략
        from collections import defaultdict
        
        freqs = defaultdict(int)
        ans = 0
        
        # 돌(s)의 빈도수 계산 = Counter 직접구현 (= 딕셔너리 생성 방법 중요!)
        for char in stones:
            freqs[char] += 1
        print(freqs)
        # 보석(j)의 빈도수 합산
        for char in jewels:
            ans += freqs[char]
            
        return ans        
                
                
#         # 4) 책 솔루션 - 파이썬다운 방식 (해시테이블X)
#         print(list(i for i in stones))
#         print(list(i in jewels for i in stones))
#         return sum(i in jewels for i in stones)
                