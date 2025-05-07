#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    files = dir(hidden_4)
    alpha_list = []
    for i in files:
        if i.startswith('__'):
            continue
        else:
            alpha_list.append(i)
    filtered_names = sorted(alpha_list)
    for i in filtered_names:
        print("{}".format(i))