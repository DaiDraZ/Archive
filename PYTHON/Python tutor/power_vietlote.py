from random import *
import time,os


import matplotlib.pyplot as plt



#f = open('power.txt',module='r',type='unicode-8-sig')
arr = []
f = {x:0 for x in range(1,46)}
ANS = [0,0]
win = []
count_roll = 0
num_mega = 45
max_number_pass = 0#so luong day so trung
def sums():
	for i in f.keys():
		ANS[0] += f[i]
def tansuat(x):
	strg = f'{x} : {f[x]} - '
	ANS[1] = round(f[x]/ANS[0]*100,7)
	# for i in range(0,int(f[x]/ANS[0]*100)+1):
	#  	strg += '|'
	if x < 10:
		return '0' + strg + f'{round(f[x]/ANS[0]*100,7)}%'
	else:
		return strg + f'{round(f[x]/ANS[0]*100,7)}%'

def lib(x):#tinh so luong cac so tu 1 ---> 45/55
	f[x] += 1
n = int(input('Nhap so lan quay : '))
arr_luck = list(map(int,input('Nhap day so ngau nhien [6 so] : ').split()))
def test():#kiem tra day so ngau nhien co trung voi day so trung thuong khong
	ans = 0
	for k in range(0,6):
		if arr[k] in arr_luck:
			if arr[k] < 10:
				arr[k] = f'(0{arr[k]})'
			else:
				arr[k] = f'({arr[k]})'
			ans += 1
		else:
			if arr[k] < 10:
				arr[k] = f'0{arr[k]}'
	return ans
for i in range(0,n):#TAO DAY SO TRUNG THUONG
	first = randint(1,num_mega)							
	arr.append(first)
	lib(first) # luu tru so luong 
	while True:
		nu = randint(1,num_mega)
		if nu not in arr:
			lib(nu)
			arr.append(nu)
			if len(arr) == 6:
				string = ''
				kq = test()
				for i in range(0,6):
					string += str(arr[i]) + ' '
				a = '-'*(36-len(string))
				print(f'{string}{a}>  {kq} \n')
				if kq == 6:
					count_roll += 1
				if kq >= max_number_pass:
					win = arr
					max_number_pass = max(max_number_pass,kq)
				arr = []
				break
	#time.sleep(0.01)

print(f'Co {count_roll} lan trung so')
print(f'Co {max_number_pass} so trung voi bo so la {win}')
sums()
print('TAN SO XUAT HIEN : ')
for x in range(1,num_mega + 1):
	if x not in f:
		if x < 10:
			print(0 ,str(x),' : 0%')
		else:
			print(x,' : 0%')
	else:
		print(tansuat(x))
		array_lucky = []
value = list(f.items())
value.sort(key = lambda x : x[1],reverse = True)
data = []
for i in range(0,6):
	data.append(value[i][0])
	data.sort(reverse = False)
def best_array_number():
	return f'The best lucky array is  {data[0]}-{data[1]}-{data[2]}-{data[3]}-{data[4]}-{data[5]}'
print(best_array_number())

# ve do thi 

catelories_plt = [int(i) for i in range(1,num_mega + 1)]
value_plt = [f[i]%100 for i in range(1,num_mega + 1)]

plt.bar(catelories_plt,value_plt)
plt.title('Xac suat xuat hien cac con so')
plt.xlabel('catelories_plt')
plt.ylabel('value_plt')
plt.show()
time.sleep(3)
SystemExit(0)
