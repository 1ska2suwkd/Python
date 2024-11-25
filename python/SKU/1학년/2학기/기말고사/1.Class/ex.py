class Car:  # 클래스 이름 수정
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        self.km = 0  # 초기 주행 거리는 0으로 설정

    def drive(self, km):  # 주행 거리를 매번 입력받도록 수정
        if km > 0:
            self.km += km
            print(f"{self.brand} 자동차가 {km}km 주행합니다.")
        else:
            print("주행 거리는 0보다 커야 합니다.")

    def info(self):
        print(f"{self.brand} 자동차 정보: 브랜드={self.brand}, 색상={self.color}, 주행거리={self.km}km")


# 객체 생성
car1 = Car("기아", "흰색")
car2 = Car("쉐보레", "검정색")

# 메서드 호출
car1.drive(50)
car2.drive(30)

car1.info()
car2.info()