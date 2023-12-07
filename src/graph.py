import matplotlib.pyplot as plt

# x, y 좌표 데이터 예제
x = [3, 6, 9, 12]
brute_force = [24, 699, 30977, 4042295]
greedy = [39, 666, 3059, 9985]
dp = [18, 176, 221, 358]

# 그래프 그리기
plt.plot(x, brute_force, '-', label='Brute Force', color='yellow') 
plt.plot(x, greedy,  '-', label='Greedy', color='red')  
plt.plot(x, dp,  '-', label='DP', color='blue')  
plt.xlabel('N')
plt.ylabel('comparisons count')
plt.title('comparisons count graph')
plt.yscale('log')  # y축을 로그 스케일로 변경
plt.legend()
plt.grid(True)
plt.show()