inp = open('map.txt',mode = 'r')
out = open('pam.txt',mode = 'w')
x = inp.readline()
j = 0
map = []
while x != '':
	x = x.strip('\n')
	map.append(list(x.split(',')))
	for i in range(0,400):
		if int(map[j][i]) in [6,7,9,10,46,50,120,121,122,160,240,162,201,200,202,241,280,161,281]:
			map[j][i] = '-1'
		elif int(map[j][i]) in [242, 243, 244, 255, 256, 257, 282, 282, 283, 284, 295, 
		297, 322, 323, 324, 332, 335, 336, 337, 362, 
		363, 375, 376, 402, 403, 415, 416,528, 529,530,531,568,569,
		570,571,]:
			map[j][i] = '1'
		elif int(map[j][i]) in [8,47,48,49,86,87,88,89,90,126,127,128,129,130,166,167,168,169,170]:
			map[j][i] = '2'
	out.write(str(map[j][0]))
	for k in map[j][1:]:
		out.write(','+str(k))
	out.write('\n')
	j += 1
	x = inp.readline()
print(len(map))