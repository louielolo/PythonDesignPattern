def deepcopy(cls):
    '''使用递归实现deepcopy'''
    if isinstance(cls, dict):
        dct = {}
        for k, v in cls.items():
            dct[k] = deepcopy(v)
        return dct
    elif isinstance(cls, list):
        li = []
        for item in cls:
            li.append(deepcopy(item))
        return li
    elif isinstance(cls, tuple):
        li = []
        for i in cls:
            li.append(deepcopy(i))
        return tuple(li)
    else:
        return cls

import copy

if __name__ == '__main__':
    lst = [1, 2, 3, 6, 4, ([5, 6, 8, 7, [7, 8, {"acb": 89375, "dxt": "kgfjolij", "v": 222}, 5, 4, 7]], (2,5,{"z":2}))]

    res = deepcopy(lst)
    print(res,'deep',id(res[5][0]))
    print('lst', id(lst[5][0]))
    ls = copy.copy(lst)
    print('ls', id(ls[5][0]))