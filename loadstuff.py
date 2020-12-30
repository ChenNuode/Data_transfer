import os
workingdir = os.getcwd()
#print(workingdir)

mylist = os.listdir(os.path.join(workingdir,"images"))

print(mylist)

divider = int(len(mylist)*0.8)
mylist1 = mylist[:divider]
mylist2 = mylist[divider:]

with open("train.txt",mode = "w") as file:
	for item in mylist1:
		file.write("custom_data/images/"+item+"\n")

with open("test.txt",mode = "w") as file:
	for item in mylist2:
		file.write("custom_data/images/"+item+"\n")

#./darknet detector train custom_data/obj.data cfg/yolo-obj.cfg custom_data/darknet53.conv.74