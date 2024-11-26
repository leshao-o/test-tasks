def get_intersections(intervals1: list[int], intervals2: list[int]) -> list[tuple[int, int]]:
    intersections = []
    for i in range(0, len(intervals1), 2):
        # Берем начало и конец интервалов ученика
        start1 = intervals1[i]
        end1 = intervals1[i + 1]
        for j in range(0, len(intervals2), 2):
            # Берем начало и конец интервалов преподавателя
            start2 = intervals2[j]
            end2 = intervals2[j + 1]
            # Если интервалы пересекаются, то добавляем их в список пересечений
            start = max(start1, start2)
            end = min(end1, end2)
            if start < end:
                intersections.append((start, end))
    return intersections


def appearance(intervals: dict[str, list[int]]) -> int:
    lesson_start, lesson_end = intervals['lesson']
    pupil_intervals = intervals['pupil']
    tutor_intervals = intervals['tutor']
    
    # Получаем пересечения
    pupil_tutor_intersections = get_intersections(pupil_intervals, tutor_intervals)
    
    # Получаем пересечения с уроком
    pupil_tutor_lesson_intersections = []
    for start, end in pupil_tutor_intersections:
        mutual_lesson_start = max(start, lesson_start)
        mutual_lesson_end = min(end, lesson_end)
        if mutual_lesson_start < mutual_lesson_end:
            pupil_tutor_lesson_intersections.append((mutual_lesson_start, mutual_lesson_end))

    # Суммируем продолжительность всех пересечений
    total_time = sum(end - start for start, end in pupil_tutor_lesson_intersections)
    return total_time

tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    # {'intervals': {'lesson': [1594702800, 1594706400],
    #          'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
    #          'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    # 'answer': 3577
    # },
    {'intervals': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]


if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['intervals'])
        print(test_answer)
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
