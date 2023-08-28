#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = 0
    count = 0
    new_list = [] 
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i] 
            new_list.append(result)
            count += 1
        except ZeroDivisionError:
            print("divition by 0")
            new_list.append(0)
            continue
        except IndexError:
            print("out of range")
            new_list.append(0)
            continue
        except TypeError:
            print("wrong type")
            new_list.append(0)
            continue
        finally:
            pass
    return new_list
