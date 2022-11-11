import math
def area_calc(height, width, cover):
    quant = math.ceil((height * width) / cover)

    print(f"You'll need {quant} cans of paint")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
test_c = int(input("Cover of wall: "))

area_calc(test_h, test_w, test_c)