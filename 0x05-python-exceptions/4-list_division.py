#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    
    for i in range(list_length):
        try:
            new_list.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            new_list.append(None)
            print("division by 0")
            continue
        except TypeError:
            new_list.append(None)
            print("type error")
            continue
        except IndexError:
            new_list.append(None)
            print("index error")
            continue
        finally:
            pass
    return new_list
