def median(ar):
    n = len(ar)
    return sorted(ar)[n/2]

if __name__=='__main__':
    n = raw_input().split()
    ar = list(map(int ,raw_input().split()))
    print median(ar)