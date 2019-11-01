import csv

count=0
before_frame=0
now_frame=0
frame_change_flag=0
header=[]
one_frame_data=[]

CSV_INPUT_FILE_NAME="d3_1_all"

f_write=open(CSV_INPUT_FILE_NAME+'_umeta.csv','w+',newline="")
writer=csv.writer(f_write)

with open(CSV_INPUT_FILE_NAME+'.csv','r') as f:
    reader=csv.reader(f)
    for row in reader:
        if count==0:
            header=row
            writer.writerow(header)
        else:
            before_frame=now_frame
            now_frame=row[1]
            if (int(now_frame)-int(before_frame))!=0:
                frame_change_flag=1
            if frame_change_flag==1:
                #print(one_frame_data)
                #バッファに貯めたデータを出力
                for i_inframe in range(len(one_frame_data)):
                    writer.writerow(one_frame_data[i_inframe])
                #バッファに貯めたデータのframeを+1して出力
                for i_inframe in range(len(one_frame_data)):
                    tmp_frame_num=int(one_frame_data[i_inframe][1])
                    tmp_frame_num+=1
                    one_frame_data[i_inframe][1]=tmp_frame_num
                    writer.writerow(one_frame_data[i_inframe])
                one_frame_data=[]
            else:
                one_frame_data.append(row)
        count+=1
        frame_change_flag=0

#print(header) #['', 'frame', 'human', 'point', 'x', 'y']