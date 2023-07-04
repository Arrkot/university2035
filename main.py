#
#
# s = 'aabcca'
#
#
# def strcount1(s):
#     print('Hello')
#     for sym in set(s):
#         # print(sym)
#         counter = 0
#         for sub_sym in s:
#             if sub_sym == sym:
#                 counter += 1
#         print(f'{sym} - {counter}')
#
#
# strcount1(s)
# print(set(s))
#
#
# def strcounter(s):
#     syms_counter = {}
#     for sym in s:
#         syms_counter[sym] = syms_counter.get(sym, 0) + 1
#     print(syms_counter)
#
#
# strcounter(s)
#
#
# def palindrom12(s):
#     result = True
#     first = 0
#     last = len(s)-1
#     while first < last:
#         if s[first] != s[last]:
#             result = False
#             break
#         first += 1
#         last += -1
#     return result
# print(palindrom12('лепсспел'))
# print(palindrom12('helloworld'))

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















