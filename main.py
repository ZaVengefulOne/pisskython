# Задача 5
# import math
#
#
# def main(x, z):
#     n = len(x)
#     result = 0
#     for i in range(1, n + 1):
#         result += 66 * pow(z[(n + 1 - i)-1] + pow(x[math.ceil((i / 2)-1)], 3), 7)
#     return result * 67
#
#
# print(main([-0.75, -0.38, -0.87, 0.53, -0.92, -0.02],
#            [0.11, -0.73, -0.08, -0.92, 0.84, -0.4]))


# Задача 6
# tree = ({2007, 1998, "GO"},
#         {2007, 1998, "MIRAH", 2001},
#         {2007, 1998, "MIRAH", 1987},
#         {2007, 1998, "MIRAH", 2003},
#         {2007, 2000, "GO"},
#         {2007, 2000, "MIRAH"},
#         {2007, 2000, "ORG", 2001},
#         {2007, 2000, "ORG", 1987},
#         {2007, 2000, "ORG", 2003},
#         {1990})
#
#
# def main(r):
#     s1 = set(r)
#     return [i for i in range(len(tree))
#             if not (len(tree[i] - s1))][0]
# #
# #
# print(main([1998,1971, 2003, "MIRAH", 2007]))


# Задача 6.2 (Артём)
# def main(data):
#     data = bin(int(data))[:-3]
#     w2 = int(data, 2) & 0b111111
#     data = data[:-6]
#     w3 = int(data, 2) & 0b111111
#     data = data[:-6]
#     w4 = int(data, 2) & 0b11
#     data = data[:-2]
#     w5 = int(data, 2) & 0b1111
#     data = data[:-4]
#     try:
#         w6 = int(data, 2) & 0b11
#         data = data[:-2]
#     except ValueError:
#         w6 = 0
#
#     temp = [w2, w3, w4, w5, w6]
#     lst = []
#     i = 2
#     j = 0
#     while i < 7:
#         lst.append(('W' + str(i), hex(temp[j])))
#         i += 1
#         j += 1
#     return lst
#
#
# print(main('5811642'))
# print(main('6535823'))
# print(main('1239758'))
# print(main('7850029'))


# Задача 7 (Транскодирования decimal to hex)
# def main(decimal_string):
#     bits = int(decimal_string)
#     x1 = bits & 1
#     x2 = bits >> 1 & 1
#     x3 = bits >> 2 & 3
#     x4 = bits >> 4 & 15
#     x5 = bits >> 8 & 7
#     result = (x4 & 15) | (x1 << 4) | (x2 << 5) | (x5 << 6) | (x3 << 9)
#     hex_string = "0x" + hex(result)[2:].zfill(2)
#     return str(hex_string)


# Задача 7 (Транскодирование hex to 16xBase)
# def main(hex_string):
#     data = int(hex_string, 16)
#     h1 = data & 0b11111
#     h2 = (data >> 5) & 0b11111111
#     h3 = (data >> 13) & 0b1111111
#     h5 = (data >> 27) & 0b11111111
#     h6 = (data >> 35) & 0b111111111
#
#     result = {
#         "H1": h1,
#         "H2": h2,
#         "H3": h3,
#         "H5": h5,
#         "H6": h6
#     }
#     print(result)


# Задача 8
# import re
#
#
# def parse_string(input_str):
#     regex = r"<%\s*glob\s?\[\s?(.*?)\s?\]\s*==>\s*(.*?)\s*%>"
#     matches = re.findall(regex, input_str)
#     result = []
#     for match in matches:
#         values = [v.strip() for v in match[0].split(",")]
#         result.append((match[1], values))
#     for i in range(len(result)):
#         for j in range(len(result[i][1])):
#             result[i][1][j] = result[i][1][j].replace("'", "")
#     return result


# Задача 10
#
# class MealyMachine:
#     def __init__(self):
#         self.state = 'A'
#
#     def draw(self):
#         if self.state == 'C':
#             self.state = 'D'
#             return 2
#         elif self.state == 'D':
#             self.state = 'B'
#             return 6
#         elif self.state == 'G':
#             self.state = 'D'
#             return 9
#         elif self.state == 'H':
#             self.state = 'D'
#             return 11
#         else:
#             raise MealyError("draw")
#
#     def begin(self):
#         if self.state == 'A':
#             self.state = 'B'
#             return 0
#         elif self.state == 'B':
#             self.state = 'C'
#             return 1
#         elif self.state == 'C':
#             self.state = 'A'
#             return 3
#         elif self.state == 'E':
#             self.state = 'E'
#             return 6
#         else:
#             raise MealyError("begin")
#
#     def speed(self):
#         if self.state == 'C':
#             self.state = 'D'
#             return 2
#         elif self.state == 'E':
#             self.state = 'F'
#             return 5
#         elif self.state == 'H':
#             self.state = 'F'
#             return 10
#         else:
#             raise MealyError("speed")
#
#     def swap(self):
#         if self.state == 'D':
#             self.state = 'E'
#             return 4
#         elif self.state == 'F':
#             self.state = 'G'
#             return 7
#         elif self.state == 'G':
#             self.state = 'H'
#             return 8
#         else:
#             raise MealyError("swap")
#
# class MealyError(Exception):
#     pass
#
# def main():
#     return MealyMachine()
#
# def raises(method, error):
#     output = None
#     try:
#         output = method()
#     except Exception as e:
#         assert type(e) == error
#     assert output is None
#
# def test():
#     o = main()
#     assert o.begin() == 0
#     assert o.begin() == 1
#     assert o.draw() == 2
#     assert o.swap() == 4
#     assert o.begin() == 6
#     assert o.speed() == 5
#     assert o.swap() == 7
#     assert o.swap() == 8
#     assert o.speed() == 10
#     assert o.swap() == 7
#     assert o.draw() == 9
#     assert o.swap() == 4
#     assert o.speed() == 5
#     assert o.swap() == 7
#     assert o.swap() == 8
#     assert o.draw() == 11
#
#     o = main()
#     assert o.begin() == 0
#     assert o.begin() == 1
#     assert o.begin() == 3
#     assert o.begin() == 0
#     assert o.begin() == 1
#     assert o.draw() == 2
#     assert o.swap() == 4
#     assert o.begin() == 6
#     assert o.speed() == 5
#     assert o.swap() == 7
#     assert o.draw() == 9
#     assert o.swap() == 4
#     assert o.speed() == 5
#     assert o.swap() == 7
#     assert o.swap() == 8
#     assert o.draw() == 11
#
#     o = main()
#     o.state = 'X'
#     raises(lambda: o.swap(), MealyError)
#     raises(lambda: o.speed(), MealyError)
#     raises(lambda: o.draw(), MealyError)
#     raises(lambda: o.begin(), MealyError)


# Задача 10.2 (Артём)
# class MealyMachine:
#     def __init__(self):
#         self.state = 'A'
#
#     def stay(self):
#         if self.state == 'A':
#             self.state = 'D'
#             return 1
#         elif self.state == 'D':
#             self.state = 'B'
#             return 6
#         elif self.state == 'C':
#             return 4
#         elif self.state == 'E':
#             self.state = 'B'
#             return 8
#         elif self.state == 'F':
#             self.state = 'G'
#             return 9
#         else:
#             raise MealyError("stay")
#
#     def sit(self):
#         if self.state == 'A':
#             self.state = 'B'
#             return 0
#         elif self.state == 'B':
#             self.state = 'C'
#             return 2
#         elif self.state == 'C':
#             self.state = 'D'
#             return 3
#         elif self.state == 'D':
#             self.state = 'E'
#             return 5
#         elif self.state == 'E':
#             self.state = 'F'
#             return 7
#         else:
#             raise MealyError("sit")
#
#
# class MealyError(Exception):
#     pass
#
#
# def main():
#     return MealyMachine()
#
#
# def raises(method, error):
#     output = None
#     try:
#         output = method()
#     except Exception as e:
#         assert type(e) == error
#     assert output is None
#
#
# def test():
#     o = main()
#     assert o.stay() == 1
#     assert o.sit() == 5
#     assert o.sit() == 7
#     try:
#         assert o.sit() == 0
#     except MealyError:
#         pass
#
#     o = main()
#     assert o.stay() == 1
#     assert o.stay() == 6
#     assert o.sit() == 2
#     assert o.stay() == 4
#     assert o.sit() == 3
#     assert o.sit() == 5
#     assert o.stay() == 8
#     assert o.sit() == 2
#     assert o.sit() == 3
#     assert o.sit() == 5
#     assert o.sit() == 7
#     assert o.stay() == 9
#
#     o = main()
#     o.state = 'X'
#     raises(lambda: o.sit(), MealyError)
#     raises(lambda: o.stay(), MealyError)
#
#
# test()


# Задача 10.3 (Артём)
# class MealyMachine:
#     def __init__(self):
#         self.state = 'A'
#
#     def draw(self):
#         if self.state == 'C':
#             self.state = 'D'
#             return 2
#         elif self.state == 'D':
#             self.state = 'B'
#             return 6
#         elif self.state == 'G':
#             self.state = 'D'
#             return 9
#         elif self.state == 'H':
#             self.state = 'D'
#             return 11
#         else:
#             raise MealyError("draw")
#
#     def begin(self):
#         if self.state == 'A':
#             self.state = 'B'
#             return 0
#         elif self.state == 'B':
#             self.state = 'C'
#             return 1
#         elif self.state == 'C':
#             self.state = 'A'
#             return 3
#         elif self.state == 'E':
#             self.state = 'E'
#             return 6
#         else:
#             raise MealyError("begin")
#
#     def speed(self):
#         if self.state == 'C':
#             self.state = 'D'
#             return 2
#         elif self.state == 'E':
#             self.state = 'F'
#             return 5
#         elif self.state == 'H':
#             self.state = 'F'
#             return 10
#         else:
#             raise MealyError("speed")
#
#     def swap(self):
#         if self.state == 'D':
#             self.state = 'E'
#             return 4
#         elif self.state == 'F':
#             self.state = 'G'
#             return 7
#         elif self.state == 'G':
#             self.state = 'H'
#             return 8
#         else:
#             raise MealyError("swap")
#
#
# class MealyError(Exception):
#     pass
#
#
# def main():
#     return MealyMachine()
#
#
# def raises(method, error):
#     output = None
#     try:
#         output = method()
#     except Exception as e:
#         assert type(e) == error
#     assert output is None
#
#
# def test():
#     o = main()
#     assert o.begin() == 0
#     assert o.begin() == 1
#     assert o.draw() == 2
#     assert o.swap() == 4
#     assert o.begin() == 6
#     try:
#         assert o.swap()
#     except AssertionError:
#         pass
#     assert o.speed() == 5
#     assert o.swap() == 7
#     assert o.swap() == 8
#     assert o.speed() == 10
#     try:
#         assert o.speed()
#     except AssertionError:
#         pass
#     assert o.swap() == 7
#     assert o.draw() == 9
#     assert o.swap() == 4
#     assert o.speed() == 5
#     assert o.swap() == 7
#     assert o.swap() == 8
#     assert o.draw() == 11
#
#     o = main()
#     assert o.begin() == 0
#     assert o.begin() == 1
#     assert o.begin() == 3
#     assert o.begin() == 0
#     try:
#         assert o.swap()
#     except AssertionError:
#         pass
#     assert o.begin() == 1
#     try:
#         assert o.swap()
#     except AssertionError:
#         pass
#     assert o.draw() == 2
#     assert o.swap() == 4
#     assert o.begin() == 6
#     assert o.speed() == 5
#     assert o.swap() == 7
#     assert o.draw() == 9
#     assert o.swap() == 4
#     assert o.speed() == 5
#     assert o.swap() == 7
#     assert o.swap() == 8
#     assert o.draw() == 11
#
#     o = main()
#     o.state = 'X'
#     raises(lambda: o.begin(), MealyError)
#     raises(lambda: o.draw(), MealyError)
#     raises(lambda: o.swap(), MealyError)
#     raises(lambda: o.speed(), MealyError)
#
#
# test()
