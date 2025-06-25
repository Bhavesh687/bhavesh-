def swap_case(s):
    string =""
    for i in s:
        if i.isupper()== true:
            string = string+(i.lower())
        else:
            string= string = string+(i.upper())
    return string

if __name__ == '__main__':
