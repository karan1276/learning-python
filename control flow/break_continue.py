for i in range(2,100):
    for j in range(2,i):
        if i%j == 0:
            print i, " equals ", j, " * ", i/j
            break
    else: #this else clause is for "for loop", only executes is list is exausted, not when break is encountered
        print i, " is a prime"
