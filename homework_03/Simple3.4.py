"""Написать функцию, которая принимает список, состоящий из объектов разных типов, и возвращает словарь, где:
ключи — типы данных объектов;
значения — списки объектов соответствующего типа."""

def lst_in_dct(lc_lst):
    set_of_types = {type(item) for item in lc_lst}
    dct = {item:[] for item in set_of_types}
    for item in lc_lst:
        dct[type(item)].append(item)
    return dct

lst = [1,'45',7,True,['q','w','e','r','t','y'],'62',5,'Hello',False,0,{1,2,3},None,{2,3},[6,6,6]]
print(lst_in_dct(lst))