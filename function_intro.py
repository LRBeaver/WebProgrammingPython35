## SQUARE
#  def square(num):
#     return num * num
#
# number = 12
# print(square(number))

## CONVERT
# def convertTemp(temp, scale):
#     if scale == "c":
#         return (temp - 32.0) * (5.0/9.0)
#     elif scale == "f":
#         return temp * 9.0/5.0 + 32
#
# temp = int(input("Enter a temperature: "))
# scale = input("Enter the scale to convert to: ")
#
# converted = convertTemp(temp, scale)
# print("The converted temp is: " + str(converted))

## ONE PER LINE

def onePerLine(str):
    for i in str:
        print(i)

word = input("Enter a word: ")
onePerLine(word)
