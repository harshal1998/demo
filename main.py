class pattern:
    def pattern(self):
        n = int(input("no of rows:"))
        a = n*2
        b = 4
        for i in range(1,n+1):
            print(" "*a,end="")
            a-=2
            k = 64+n
            for j in range(i):
                print(chr(k-j),end="   ")
            print()

        for i in range(n-1,0,-1):
            # print("i:",i)
            print(" "*b,end="")
            b+=2
            k=64
            for j in range(i,0,-1):
                # print("j:",j)
                print(chr(k+j),end="   ")
            print()
obj=pattern()
obj.pattern()