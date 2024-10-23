import time
def atm_pin_test():
    pin = 1234
    wobj = open('E:\\pin_history.log','a')
    count = 0
    while(count <3):
        p = input('Enter a pin Number:')
        count +=1
        if(int(p) == pin):
            msg=f'Success pin is matched - {count}'
            t=f'pin Entry date/time is:{time.ctime()}'
            wobj.write(msg+" "+t+"\n") # write data to File
            print(f'Success pin is matched - {count}')
            break # exit from loop
        else:
            wobj.write(f'Failed - input pin:{p} is not valid ')
            wobj.write(f'Pin Entry date/time:{time.ctime()}\n')

    if(int(p) != pin):
        print('Sorry your pin is blocked')
        wobj.write('Sorry your input pin is blocked ')
        wobj.write(f'Entry date/time:{time.ctime()}\n')

    wobj.close()

if __name__ == '__main__':
    atm_pin_test()
