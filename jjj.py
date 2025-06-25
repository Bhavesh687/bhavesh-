def distinct_stamps(n):
    stamps = set()
    while n >0:
        stamps.add(n)
        n = n-1
        return stamps

    if __name__ == '__main__':
        n = int(input())
        print(len(distinct_stamps(n)))