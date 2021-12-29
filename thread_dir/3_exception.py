import time


list1 = [50301,50302,50303,50304]
def socket1(num):
    se_num = 0
    for i in range(int(num)):
        se_num += 1
        if se_num == 1:
            print('socket-server1 1')
        elif se_num == 2:
            print('socket-server1 2')
        elif se_num == 3:
            print('socket-server1 3')
        elif se_num == 4:
            print('socket-server1 4')
        elif se_num == 5:
            se_num = 1
            # print(se_num)
            print('socket-server1 1')
            # continue
        # print(se_num)




socket1(10)