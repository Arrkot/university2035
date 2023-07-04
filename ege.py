
# for x in range(0, 2):
#     for y in range(0, 2):
#         for z in range(0, 2):
#             for w in range(0, 2):
#                 if not ((x and (not y)) or (x == z) or w):
#                     print(x, y, z, w)


#
# from turtle import *
# tracer(0)
# screensize(1000,1000)
# r = 25
#
# for i in range(2):
#     fd(10*r)
#     rt(90)
#     fd(18 * r)
#     rt(90)
# up()
# fd(5*r)
# rt(90)
# fd(7 * r)
# lt(90)
# down()
# for i in range(2):
#     fd(10*r)
#     rt(90)
#     fd(7 * r)
#     rt(90)
# up()
# for x in range(-20, 20):
#     for y in range(-20, 20):
#         goto(x*r, y*r)
#         dot(4,"red")
# update()
# exitonclick()



#
# for n in range(1,100):
#     b = bin(n)[2:0]
#     if b.count('1')%2==0:
#         b= '10' + b[2:] + '0'
#     else:
#         b = '11' + b[2:] + '1'
# r = int(b,2)
# if r<35:
#         print(n)





# for n in range(1,100):
#     b=bin(n)[2:]
#     if n%3 == 0:
#         b = b+ b[-3:]
#     else:
#         a = 3*(n%3)
#         a1= bin(a)[2:]
#         b = b + a1
#     r = int(b,2)
#     if r <=170:
#         print(r)

# from itertools import *
# k=1
# for x in product("ЕЛМРУ",repeat=4):
#     s="".join(x)
#     if s[0]!="У" and s.count("М")==2 and s.count("Г")<=1:
#         f=s
#         q=k
#     k+=1
# print(q,f)

#
# from itertools import *
# k=0
# for x in product("ЕЛМРУ",repeat=4):
#     k += 1
#     s="".join(x)
#     if s[0]=="Л":
#         print(k)
#         break


#
# from itertools import *
#
# k = 0
# for x in product("АГИЛМОРТ", repeat=4):
#     k += 1
#     s = "".join(x)
#     if s[-2:] == "ИМ":
#         print(k, s)


# from itertools import *
#
# k = 0
# for x in product("АИМРЯ", repeat=4):
#     k += 1
#     s = "".join(x)
#     if s == "АРИЯ":
#         print(k)
#         break


# from itertools import *
#
# k = 0
# for x in product("АИМРЯ", repeat=4):
#     k += 1
#     s = "".join(x)
#     if k == 211:
#         print(s)
#         break


# from itertools import *
#
# k = 0
# for x in product("АВОРТ", repeat=6):
#     k += 1
#     s = "".join(x)
#     if s == "ВОРОТА":
#         print(k)
#         break


# for n in range(1,100):
#     b=bin(n)[2:]
#     b = b + b[-1]
#     if b.count('1')%2==0:
#         b = b +"0"
#     else:
#         b = b+ "1"
#     b = b + "0"
#     r = int(b,2)
#     if r >144:
#         print(r, b)


# for n in range(1,1000):
#     b = bin(2*n)[2:]
#     if b.count('1') %2 == 0:
#         b += '0'
#     else:
#         b += '1'
#     if b.count('1') %2 == 0:
#         b += '0'
#     else:
#         b += '1'
#     r = int(b,2)
#     if r > 1017:
#         print(n)
#         break


# for n in range(1,1000):
#     b = bin(2*n)[2:]
#     if b.count('1') %2 == 0:
#         b += '0'
#     else:
#         b += '1'
#     if b.count('1') %2 == 0:
#         b += '0'
#     else:
#         b += '1'
#     r = int(b,2)
#     if r < 80:
#         print(n)


# for i in range(4,10000):
#     s = '5' + i*'2'
#     while '72' in s or '522' in s or '2222' in s:
#         if '72' in s:
#             s =s.replace('72', '2', 1)
#         if '522' in s:
#             s=s.replace('522', '27', 1)
#         if '2222' in s:
#             s=s.replace('2222', '5', 1)
#
#     summ = s.count('5')*5 + s.count('2')*2 +s.count('7')*7
#     if summ == 63:
#         print(i)
#         break


# for x in reversed('0123456789abcdefghi'):
#     s = '98' + x + '79641'
#     s1 = '36' + x + ' 14'
#     s2 = '73' + x + '4'
#     s =int(s,19)
#     s1 = int(s1, 19)
#     s2 = int(s2, 19)
#     s3 = s + s1 + s2
#     if s3%18 == 0:
#          print(s3/18)


for x in reversed('0123456789abcdefghi'):
    s = '98' + x + '79641'
    s1 = '36' + x + '14'
    s2 = '73' + x + '4'
    s = int(s,19)
    s1 = int(s1,19)
    s2 = int(s2, 19)
    s3 = s + s1 + s2
    if s3%18 == 0:
         print(s3/18)
         break






