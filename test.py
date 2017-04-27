import time

def timetest( f ):
    def inner( *arg ):
        a = time.time()
        val = f( *arg )
        b = time.time()
        print "Elapsed Time:%f"%(b-a)
        return "Val: "+str(val)
    return inner

def names( f ):
    def inner( *arg ):
        print "Func Name:%s, Args: %s"%(f.func_name, arg )
        return f( *arg )
    return inner

@timetest
@names
def fib(n):
    def helper(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return helper(n-1) + helper(n-2)
    return helper(n)

@timetest
@names
def tail_fib(n):
    def helper(n, val, prev):
        if n == 0:
            return prev
        elif n == 1:
            return val
        else:
            return helper(n-1, val+prev, val)
    return helper(n, 1, 0)

print fib(5)
print tail_fib(30)
