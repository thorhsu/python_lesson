# 汽車類別
class Cars:
    # 建構式
    def __init__(self, seat, color):
        self.seat = seat
        self.color = color
    def __str__(self):
      return f"this car's color is {self.color} and has {self.seat} seats"
    # 廂型車
    @classmethod
    def van(cls):
        return cls(6, "black")
    # 跑車
    @classmethod
    def sports_car(cls):
        return cls(4, "yellow")
van = Cars.van()
sports_car = Cars.sports_car()
print(van)
print(sports_car)