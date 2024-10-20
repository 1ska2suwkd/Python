marks = [90, 25, 67, 45, 80]
number = 0

for i in marks:
    number+=1
    if i>=60:
        print("%d번 학생 합격입니다." %number)
    else:
        print("%d번 학생 불합격입니다." %number)
