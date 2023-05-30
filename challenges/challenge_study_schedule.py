def study_schedule(permanence_period, target_time):
    # """Faça o código aqui."""
    # raise NotImplementedError
    if target_time is None:
        return None

    students_no_periodo = 0

    for student in permanence_period:
        if (
            not isinstance(student, tuple)
            or len(student) != 2
            or not all(isinstance(tempo, int) for tempo in student)
        ):
            return None
        if student[0] <= target_time <= student[1]:
            students_no_periodo += 1

    return students_no_periodo
