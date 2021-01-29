# 汽車類別
class Cars:
    # 速率靜態方法
    @staticmethod
    def speed_rate(distance, minute):
        return distance / minute

def speed_rate(distance, minute):
    return distance / minute        
# 透過物件呼叫
van = Cars()
van_rate = van.speed_rate(10000, 20)
print("van rate: ", van_rate)
# 透過類別呼叫
sports_car_rate = Cars.speed_rate(20000, 20)
print("sports car rate: ", sports_car_rate)
print("static: ", Cars.speed_rate(2000, 10))
print("geneic: ", speed_rate(2000, 10))