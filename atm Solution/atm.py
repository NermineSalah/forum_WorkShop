balance = 500
request = 277
def ATM(request):
    while request > 0:
        if request > 100:
            print 'give 100'
            request =100
        elif request > 50:
            print 'give 50'
            request = 50
        elif request > 10:
            print 'give 10'
            request = 10
        elif request > 5:
            print 'give 5'
            request = 5
        else:
            if request == '0':
                print 'give 0'
                request = 0

  
ATM(request)    

