# -*- coding: utf-8 -*-
"""LAB2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12OthjZBQZu5Zbzw7je7qvrdRnmzW0G-g
"""

def generate_pattern01(n, current=0, result=""):
    if current == n:
        return result
    line = "*" * (current + 1)
    return generate_pattern01(n, current + 1, result + line + "\n")


def generate_pattern02(n, current=0, result=""):
    if current == n:
        return result
    line = " " * (n - current - 1) + "*" * (current + 1)
    return generate_pattern02(n, current + 1, result + line + "\n")


def generate_pattern03(n, current=0, result=""):
    if current == n:
        return result
    line = "*" * (n - current)
    return generate_pattern03(n, current + 1, result + line + "\n")


def generate_pattern04(n, current=0, result=""):
    if current == n:
        return result
    line = " " * (n - current - 1) + "* " * (current + 1)
    return generate_pattern04(n, current + 1, result + line + "\n")


def generate_pattern05(n, current=0, result=""):
    if current == n:
        return result
    line = " " * current + "* " * (n - current)
    return generate_pattern05(n, current + 1, result + line + "\n")


# รับค่า x จากผู้ใช้
x = int(input("Enter a number (integer): "))

# แสดงผลลัพธ์สำหรับแต่ละฟังก์ชัน generate_pattern
pattern = generate_pattern01(x)
print(pattern, end="")
print("-------------")

pattern = generate_pattern02(x)
print(pattern, end="")
print("-------------")

pattern = generate_pattern03(x)
print(pattern, end="")
print("-------------")

pattern = generate_pattern04(x)
print(pattern, end="")
print("-------------")

pattern = generate_pattern05(x)
print(pattern, end="")
print("-------------")

# รับค่าความสูงจากผู้ใช้
height = int(input("Enter height for triangle: "))

# พิมพ์สามเหลี่ยมน้อยไปหลัง
for i in range(1, height + 1):
    print(' '.join('*' * i))
print('-------------')

# พิมพ์สามเหลี่ยมใหญ่ลงมาหลัง
for n in range(height, 0, -1):
    print(' '.join('*' * n))
print('-------------')

# พิมพ์สามเหลี่ยมแบบลากซ้าย
for i in range(height):
    for j in range(height - i - 1):
        print(" ", end="")
    for k in range(i + 1):
        print("*", end=" ")
    print()
print('-------------')

# พิมพ์สามเหลี่ยมแบบลากขวา
for i in range(height, 0, -1):
    for j in range(height - i):
        print(" ", end="")
    print(" ".join("*" * i))
print('-------------')

# พิมพ์สามเหลี่ยมแบบกลับหัวลง
for i in range(height):
    for j in range(height - i - 1):
        print(" ", end=" ")
    for k in range(i + 1):
        print("*", end=" ")
    print()