# Input variables
# 입력 변수
month = 8
day = 15

# Single conditional statement
# 하나의 조건식

result = (
    "광복절" if (month == 8 and day == 15) else
    "그날" if ((month % 2 == 1 and day == 15) or (month % 2 == 0 and day == 16)) else
    "평일"
)

# Output result
# 결과 출력
print(result)
