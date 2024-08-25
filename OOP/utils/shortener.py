from typing import List

class Shortener:
    def __init__(self) -> None:
        pass

    def firstHalf(self, list: List):
        print(round(len(list)/2))
        return list[0:round(len(list)/2)]
    
    def secondHalf(self, list: List):
        return list[round(len(list)/2):len(list)]
    

short = Shortener()

print(short.firstHalf([1,2,3,4,5]))
print(short.secondHalf([1,2,3,4,5]))