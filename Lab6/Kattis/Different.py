import math

for line in sys.stdin:
    ab = line.split()
    a = int(ab[0])
    b = int(ab[1])
    # lös testfallet och beräkna svaret
    print(abs(a-b))
