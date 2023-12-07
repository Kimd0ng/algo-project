from itertools import product

comp = 0

def is_time_overlap(time1, time2):
    global comp
    comp += 1
    return max(time1[0], time2[0]) < min(time1[1], time2[1])

def are_times_overlapping(times):
    for i in range(len(times)):
        for j in range(i+1, len(times)):
            if is_time_overlap(times[i], times[j]):
                return True
    return False

def find_schedule_brute(desired_courses, times_dict):
    possible_combinations = product(*(times_dict[course] for course in desired_courses))

    feasible_schedules = []
    for combination in possible_combinations:
        times = [time for lecture_times in combination for time in lecture_times.times]

        if not are_times_overlapping(times):
            feasible_schedules.append([lecture.course_id for lecture in combination])

    return feasible_schedules