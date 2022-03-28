def rectangleArea(a, b):
    return a * b


def rectanglePerimeter(a, b):
    return 2 * (a + b)


def squareArea(a):
    return a * a


if __name__ == "_main_":

    while True:

        print("1 to find area of rectangle")
        print("2 to find perimeter of rectangle ")
        print("3 to find area of square ")
        print("4 to Exit")

        ch = int(input("Enter your Choice "))
        if ch == 1:
            l = int(input("Enter length:"))
            b = int(input("Enter breadth:"))
            print(rectangleArea(l, b))
        elif ch == 2:
            l = int(input("Enter length:"))
            b = int(input("Enter breadth:"))
            print(rectanglePerimeter(l, b))
        elif ch == 3:
            side = int(input("Enter side of square:"))
            print(squareArea(side))
        elif ch == 4:
            print("Incorrect Option:")
            break



































# def rectangleArea():
#
#    length=int(input("enter the length of the rectangle : "))
#
#    breadth=int(input("enter the breadth of the rectangle : "))
#    Area=length*breadth
#
#    print("Area of the rectangle is:",Area)
#
# def rectanglePerimeter():
#     Length=int(input("Enter Length:"))
#     Breadth=int(input("Enter Breadth:"))
#     perimeter=2*(Length+Breadth)
#     print("Perimeter of rectangle is:",perimeter)
#
# def squareArea():
#     Side=int(input("Enter size:"))
#     Square=Side*Side
#     print("Square of area is:", Square)
#
# if __name__ == "__main__":
#
#     while True:
#             print("\nPress ")
#             print("1 to find area of rectangle")
#             print("2 to find perimeter of rectangle ")
#             print("2 to find area of square ")
#             print("4 to Exit")
#
#             x = int(input("Select Option: "))
#             if x == 1:
#
#                 rectangleArea()
#
#             elif x == 2:
#
#                 rectanglePerimeter()
#
#             elif x == 3:
#
#                 squareArea()
#
#             else:
#
#                 print("Incorrect Option")
#             break
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # def rectanglearea(x,y):
# #     return x*y
# # def rectanglePerimeter(x,y):
# #     return 2(x+y)
# # def square(x):
# #     return x*x
# # if __name__ == "__main__":
# #     num1=float(input("enter length"))
# #     num2=float(input("enter breadth"))
# #     print("1.Area of rectangle:")
#
#
#
# # print("Menu-\n"
#     #
#     #       "1. RectangleArea\n"
#     #
#     #       "2. RectanglePerimeter\n"
#     #
#     #       "3. SquareArea\n")
#
#     # x = int(input("Select Option:")
#     # if x == 1:
#     #
#     #     rectangleArea()
#     #
#     # elif x == 2:
#     #
#     #     rectanglePerimeter()
#     #
#     # elif x == 3:
#     #
#     #     squareArea()
#     #
#     # else:
#     #
#     #     print("Incorrect Option")