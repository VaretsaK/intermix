

def best_worse_student(**students):
    student_names = list(students.keys())
    avrg_marks = [sum(x) / len(x) for x in students.values()]

    best_student = max(avrg_marks)
    worse_student = min(avrg_marks)

    return "Best student is " + student_names[avrg_marks.index(best_student)],\
        "Worse student is " + student_names[avrg_marks.index(worse_student)]


if __name__ == "__main__":
    print(best_worse_student(Student_1=[1, 2, 3, 8],
                             Student_2=[2, 3, 1, 7],
                             Student_3=[3, 4, 5, 9],
                             Student_66=[6, 7, 8],
                             Student_8=[8, 9]))
