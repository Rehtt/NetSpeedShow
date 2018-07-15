import time

speed_down=[]
speed_up=[]
speed_name=[]

speed_up_1=[]
speed_down_1=[]

while True:
    i=open('/proc/net/dev','r').readlines()
    for p in i:
        p=p.split( )
        if p[1].isdigit() and p[1]!='0':
            index=0
            for i in range(len(speed_name)):
                if p[0]==speed_name[i]:
                    index=i
                    break
            if p[0] in speed_name:
                pass
            else:
                speed_name.append(p[0])
                speed_down_1.append(p[1])
                speed_up_1.append(p[9])
                speed_down.append(0)
                speed_up.append(0)
                break
            speed_down[index]=(float)((int)(p[1])-(int)(speed_down_1[index]))/1000
            speed_up[index]=(float)((int)(p[9])-(int)(speed_up_1[index]))/1000
            speed_down_1[index]=p[1]
            speed_up_1[index]=p[9]
    for i in range(len(speed_name)):
        print("网卡："+speed_name[i])
        print("上行："+speed_up[i])
        print("下行："+speed_down[i])
    time.sleep(1)
