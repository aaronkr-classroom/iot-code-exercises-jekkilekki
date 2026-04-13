# Initialize sum
# 합 초기화
total = 0

# Loop from 1 to 50
# 1부터 50까지 반복
for i in range(1, 51):
    # Check if even and not multiple of 3
    # 짝수이고 3의 배수가 아닌지 확인
    if i % 2 == 0 and i % 3 != 0:
        total += i

# Print result
# 결과 출력
print("Sum:", total)

# Initialize variables
# 변수 초기화
i = 1
total = 0

# While loop
# while 반복문
while i <= 50:
    # Check conditions
    # 조건 확인
    if i % 2 == 0 and i % 3 != 0:
        total += i
    i += 1  # Increment / 증가

# Print result
# 결과 출력
print("Sum:", total)
