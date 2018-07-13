if __name__ == '__main__':
    t = raw_input()
    for i in range(0, int(t)):
        a = raw_input()
        b = raw_input()
        c = raw_input()
        d = raw_input()

        if(a==b==c==d):
            print 'Yes'
        elif(a==b and c==d or a==c and b==d or a==d and c==b):
            print "Yes"
        else:
            print "No"


