class WireCut:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second

    def display_info(self):
        print(f"code : {self.code}")
        print(f"color : {self.color}")
        print(f"second : {self.second}")

code, color, second = input().split()
second = int(second)
wire_cut = WireCut(code, color, second)
wire_cut.display_info()