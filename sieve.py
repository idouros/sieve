import numpy as np

def main():
    m = 7920
    a = np.array(range(0, m+1), dtype=bool)
    a[1] = False
    #print(a)


    for curr in range(2, m+1):
        if a[curr] == True:
            print(curr)
            step = curr
            i = step + curr
            while i < (m+1):
                a[i] = False
                i += step

if __name__ == "__main__":
    main()