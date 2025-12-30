

student = {
    "20121212":{
    "name":"student1",
    "age": 18,
    "score": 99
},
    "20121111212":{
    "name":"student2",
    # "age": 18,
    "score": 70
},
    "2012123312":{
    "name":"student1",
    "age": 80,
    # "score": 90
},
    "20121333323312":{
    "name":"student1",
    "age": 80,
    "score": 99
},
}

stu_ids = list(student)
stu_infos = list(student.values())

notes = []

for id in stu_ids:
    if 'age' not in student.get(id):
        notes.append(f"{id} lacks age")
    if 'score' not in student.get(id):
        notes.append(f"{id} lacks score")

print("Ids and lacking infos")
for note in notes:
    print(note)

print(stu_ids)
print(stu_infos)

ages = [a.get('age', 0) for a in stu_infos]

max_age, max_age_index = max(ages), ages.index(max(ages))
min_age, min_age_index = min(ages), ages.index(min(ages))

print(f"Max age: {max_age} Corresponding info: {stu_ids[max_age_index]} | {stu_infos[max_age_index]}")
print(f"Min age: {min_age} Corresponding info: {stu_ids[min_age_index]} | {stu_infos[min_age_index]}")

total = list(zip(stu_ids, stu_infos))
print(total)

rank_age = sorted(total, key=lambda x: (-x[1].get("age", 0), -x[1].get("score", 0), x[0]))

rank_score = sorted(total, key=lambda x: (-x[1].get("score", 0), -x[1].get("age", 0), x[0]))

print("rank_age:")
for a in rank_age: 
    print(a)

print("rank_score: ")
for a in rank_score:
    print(a)
