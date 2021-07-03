import numpy
def f7a(list_of_tuples):
    def z_scaling(features):
        mean_value = numpy.mean(features)
        sd = numpy.std(features)
        for j in range(len(features)):
            features[j] = features[j] - mean_value
            features[j] = features[j] / sd
        return features

    st_grade, st_works = [], []
    for i in range(len(list_of_tuples)):
        st_grade.append(list_of_tuples[i][1])
        st_works.append(list_of_tuples[i][2])
    st_grade = z_scaling(st_grade)
    st_works = z_scaling(st_works)
    list_of_students = []
    for k in range(len(list_of_tuples)):
        if len(list_of_tuples[k]) == 3:
            new_student_db = [list_of_tuples[k][0], st_grade[k], st_works[k]]
            list_of_students.append(new_student_db)
        else:
            new_student_db = [list_of_tuples[k][0], st_grade[k], st_works[k], list_of_tuples[k][3]]
            list_of_students.append(new_student_db)
    return list_of_students

def f7b(t, L):
    def oclade_dist(student_t, student_other):
        distance = 0
        for i in range(1, 3):
            distance += abs(student_t[i] - student_other[i]) ** 2
        return distance ** (1 / 2)

    k_nearest, distances = [], []
    for j in range(3):
        k_nearest.append(L[j])
        distances.append(oclade_dist(t, L[j]))
    max_dist = max(distances)
    for e in L[3:]:
        dist = oclade_dist(t, e)
        if dist < max_dist:
            max_index = distances.index(max_dist)
            k_nearest[max_index] = e
            distances[max_index] = dist
            max_dist = max(distances)
    return k_nearest

def f7c(t, L):
    close_students = f7b(t, L)
    labels = []
    for i in range(len(close_students)):
        labels.append(close_students[i][3])
    if labels.count(0) > labels.count(1):
        t.append(0)
    else:
        t.append(1)
    return t

