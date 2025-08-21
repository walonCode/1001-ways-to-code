class Shape:
    length = 0
    breath = 0
    width = 0

    def __init__(self, l:int, b:int, w:int):
        self.breath = b
        self.length = l
        self.width = w

    def volume(self) -> str:
        volume = self.breath * self.length * self.width

        return f"The volume is {volume}"
    
    def area(self) -> str:
        area = self.length * self.breath

        return f"The area is {area}"
    
    def perimeter(self) -> str:
        perimeter = 2*(self.length + self.breath)

        return f"The perimeter is {perimeter}"
    

def main():
    square = Shape(4,4,4)
    area = square.area()
    perimeter = square.perimeter()

    print(f"The area and perimeter of the square are {area, perimeter}")


if __name__ == "__main__":
    main()