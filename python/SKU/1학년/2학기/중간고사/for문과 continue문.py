"""
총 5명의 학생이 시험을 보았는데 시험 점수가 60점 이상이면 합격이고 그렇지 않으
면 불합격이다. 합격인 사람에게만 축하 메시지를 보내도록 작성 하시오.
"""

marks = [90, 25, 67, 45, 80]
number = 0

for i in marks:
    number += 1
    if i>=60:
        print("%d번 학생 합격입니다." %number)
    else:
        continue
