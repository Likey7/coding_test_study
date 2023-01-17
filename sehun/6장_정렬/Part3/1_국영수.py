n = int(input())
student = []

for _ in range(n):
  student.append(input().split())

student.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in student:
  print(i[0])

# for i in range(n):
#   name, ko, en, ma = input().split()
#   student[i].append([name])
#   student[i].append(int(ko))
#   student[i].append(int(en))
#   student[i].append(int(ma))
#   #이름 아스키코도화
#   for i in range(len(student)):
#     for j in range(len(student[i][0])):
#       student[i][0][j] = ord(student[i][0][j])

# def counting_sort(student, what):
#   if what > 3:
#     what = 0
  
#   score = [0] * (100 + 1)

#   #계수정렬 시작
#   for i in range(len(student)):
#     score[student[i][what]].append(student[i][what])

  
#   #계수정렬된 행렬을 가공하여 저장
#   for i in range(len(score)):
#     if 1 < len(score[i]):
#         #2개이상이라면 다음정렬규칙으로 이동
#         what += 1
#         temp = counting_sort(score[i], what)
#         for k in temp:
#           score[i][k] = temp[k]
#     for j in range(score[i]):
#       student_new.append()
  
#   if 감소하는케이스:
#     student_new.reversed()
#   return student_new

#   for i in range(len(student)):
#     score[]
    
# #정렬된 학생들 이름 출력
# for i in range(n):
#   print(student[i][0])

# #인덱스값은 이름:0, 국어:1, 영어:2, 수학:3
# def quick_sort(student, start, end, i):
#   if start >= end:
#     return
#   pivot = start
#   left = start+1
#   right = end
  
#   while left <= right:
#     while left <= right and student[left][i] < student[pivot][i]

# #퀵소트로 학생들 리스트 정렬
# quick_sort(student, 0, len(n)-1, 1)