#1.Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

#print("Введите число")
#x=int(input())
#if x<=7 and x>=6:
#    print("Да")
#else:
#    print("Нет")


#2.Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

#3.Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти
#плоскости, в которой находится эта точка (или на какой оси она находится).

# print("Введите x")
# x=float(input())
# print("Введите y")
# y=float(input())

# if x>0 and y>0:
#     print("1")
# elif x>0 and y<0:
#     print("4")
# elif x<0 and y>0:
#     print("2")
# elif x<0 and y<0:
#     print("3")
# elif x==0 or y==0:
#     print("Неверно введены данные")

#4.Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# print("Введите номер четверь")
# x=int(input())
# if x==1:
#     print("x(0:+ifinity) y(0:+infinity)")
# elif x==2:
#     print("x(0:-ifinity) y(0:+ifinity)")
# elif x==3:
#     print("x(0:-ifinity) y(0:-ifinity)")
# elif x==4:
#     print("x(0:+ifinity) y(0:-ifinity)")
# else:
#     print("Вы ввлем неправильное число") 

#5.Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

print("Введите х1 и у1")
x1=float(input())
y1=float(input())
print("Введите x2 и y2")
x2=float(input())
y2=float(input())

S=((abs(x2-x1)**2)+(abs(y2-y1)**2))**0.5
print(round(S, 2))