# Ex 6.5 The Ackermann funcation

def ack(m, n):
    '''
    Implement the Ackermann function
    '''
    if m == 0:
        return n+1
    elif m>0 and n==0:
        return ack(m-1,1)
    elif m>0 and n>0:
        return ack(m-1, ack(m,n-1))
    


# Test code
print(ack(3,4))