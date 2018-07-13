
def rec_mult(m,n):
    if n==0:
        return 0
    elif n >= 1 :
        #print 'After Multiplying'
        return  m+ rec_mult(m, n-1)
    elif n <= -1:
       # print 'After Multiplying'
        return  -m+ rec_mult(m, n+1)

for i in range(1,5):
    print 'Enter two no to multiply'
    m = int(raw_input('Enter first no\n'))
    n = int(raw_input('Enter Second no\n'))
    print rec_mult(m,n)


