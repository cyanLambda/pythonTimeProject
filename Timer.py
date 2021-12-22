from time import sleep

#timer
def timer(x):
    #split to h, min and sec
    try:
        s = x.split(':')
        sec = int(s[2])
        min = int(s[1])
        h = int(s[0])
    except:
        print('')
        print('MISSINPUT (input example: 0:0:10)')
        exit()

    #too big values fix
    if sec >= 60 or min >= 60: print('value too big(max_sec=60)')
    else:
        #time goes down
        while True:
            if sec > 0:
                sec = sec - 1
            elif sec <= 0:
                if min > 0:
                    min = min - 1
                    sec = 60
                elif min <= 0:
                    if h > 0:
                        h = h - 1
                        min = 60
                    else:
                        break
            sleep(1)

            #visual representation
            if sec < 10: tsec = '0' + str(sec);
            else: tsec = str(sec)
            if min < 10: tmin = '0' + str(min);
            else: tmin = str(min)
            print(str(h) + ':' + str(min) +':'+ tsec)

        print('')
        print('[ ' + x + ' just passed' + ' ]')

#user interaction

print('[  timer.py  ]')
print('set timer. (ex. 0:0:10, hours:minutes:seconds)')
print('')
timer(input('>>'))
