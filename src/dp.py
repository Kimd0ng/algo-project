from itertools import product

#나중에 비교 횟수를 세기 위한 전역변수
comp = 0

#dp 알고리즘 구현
def is_time_overlap(time1, time2):
  global comp
  comp += 1
  return max(time1[0], time2[0]) < min(time1[1], time2[1])

#dict안에 넣어주기 위해 list을 tuple로 변환
def change_tuple(times, i, j):
  one_f = times[i][0]
  one_s = times[i][1]
  two_f = times[j][0]
  two_s = times[j][1]
  temp = ((one_f, one_s), (two_f, two_s))

  return temp

#memo안에 없는 경우 값을 저장해주고 memo안에 있는경우 값을 불러온다.
#한번 비교한 값들은 다시 비교를 진행하지 않는다.
def check_memo(times, memo):
  for i in range(len(times)):
      for j in range(i+1, len(times)):
         temp = change_tuple(times, i, j)

         if temp not in memo:
             if is_time_overlap(times[i], times[j]):
                memo[temp] = True
                return True
             else:
                memo[temp] = False
         else:
             if memo[temp] == True:
                return True
  return False

def find_schedule_dp(desired_courses, times_dict):
  possible_combinations = product(*(times_dict[course] for course in desired_courses))

  feasible_schedules = []
  memo = dict()
  for combination in possible_combinations:
      times = [time for lecture_times in combination for time in lecture_times.times]

      if not check_memo(times, memo):
          feasible_schedules.append([lecture.course_id for lecture in combination])

  return feasible_schedules