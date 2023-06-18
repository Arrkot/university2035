

s = 'aabcca'


def strcount1(s):
    print('Hello')
    for sym in set(s):
        # print(sym)
        counter = 0
        for sub_sym in s:
            if sub_sym == sym:
                counter += 1
        print(f'{sym} - {counter}')


strcount1(s)
print(set(s))


def strcounter(s):
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0) + 1
    print(syms_counter)


strcounter(s)


def palindrom12(s):
    result = True
    first = 0
    last = len(s)-1
    while first < last:
        if s[first] != s[last]:
            result = False
            break
        first += 1
        last += -1
    return result
print(palindrom12('лепсспел'))
print(palindrom12('helloworld'))


