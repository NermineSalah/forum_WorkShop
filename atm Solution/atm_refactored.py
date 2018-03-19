def withdraw(balance, request):
    print '============================'
    print 'Current balance = '+str(balance)
    
    if request > balance:
        print('Cant give you all this money')
    elif request < 0:
        print('More than Zero please!')
    else:
        while request > 0:
            if request >= 100:
                request = request - 100
                print('give 100')
            elif request >= 50:
                request = request - 50
                print('give 50')
            elif request >= 10:
                request = request - 10
                print('give 10')
            elif request >= 5:
                request = request - 5
                print('give 5')
            elif request < 5:
                print('give '+str(request))
                request = 0
    return balance - request

balance = 500

balance = withdraw(balance, 277)
balance = withdraw(balance, 30)
balance = withdraw(balance, 5)
