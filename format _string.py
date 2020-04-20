from functools import reduce

print(
    len(
        list(
            filter(
                lambda x:x>0,
                list(
                    map(
                        int,
                        input().split()))))))