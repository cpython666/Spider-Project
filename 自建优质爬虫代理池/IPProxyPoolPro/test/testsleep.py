from time import sleep

count = 0
while True:

    while True:
        if count>=10:
            sleep(1)
            print('sleeping')
        else:
            break
    print(1)
    sleep(0.2)
    count+=1
