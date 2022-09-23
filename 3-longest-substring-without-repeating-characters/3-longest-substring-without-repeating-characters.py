'''
### 메모

* 중복 문자가 없는 가장 긴 부분 문자열(substring)의 길이를 구해라
  - 문제 주의해야될 조건 : 기존 데이터의 인덱스가 그대로 유지되어야함 
  - 3번 테케이서 wke 가 답 = 부분 문자열
  - 3번 테케에서 pwke는 답아님 = 서브시퀀스(subsequence)

* ex) abcabcbb
  - "abc"ab~~
  
* ex) pwwkew    이게핵심
  - pw"wke"~~


### 알고리즘 및 방법

* 나의 방식
```
ans = [arr[0]]                   첨에 하나 넣어주고
answer = 0

for i in (1~len)                 1부터 시작

    if arr[i-1] == arr[i]:       앞뒤 같은거면
        ans.clear()              기존에 있떤거 다 날려버려
        ans.append(arr[i])       대신 현재는 추가

    elif arr[i] in ans:          현재가 기존에 있는 값이야
        ans = ans[:i] + arr[i]   배열에 그 값 전까지 다 날려버리고 새로운거랑 ++ 

    else:                        완전 새로운거야
        ans.append(arr[i])       그냥 추가
        
    answer = max(answer, len(ans)) max길이를 기록하면 끗
```      

### 히든테케 주의사항

진짜 너무 억지 아니냐

* 1번 : ""
  - 정답 0
* 2번 : " "
  - 정답 1
  
'''
class Solution:
    def lengthOfLongestSubstring(self, arr: str) -> int:
        
        if arr == "":       return 0  # 1번 해결용
        elif len(arr) == 1: return 1  # 2번 해결용
        
        arr = list(arr)               # 만약을 대비한 공백도 인식
        
        ans = [arr[0]]
        answer = 0
        for i in range(1,len(arr)):
            if arr[i-1] == arr[i]:
                ans.clear()
                ans.append(arr[i])
            elif arr[i] in ans:
                ans = ans[ans.index(arr[i])+1:] + list(arr[i])
            else:
                ans.append(arr[i])
                
            answer = max(answer, len(ans))
        
        return answer