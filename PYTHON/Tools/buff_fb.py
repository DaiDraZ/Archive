import termcolor,random,colorama

# line += colored(j, "yellow")
colorama.init(autoreset=True)
line = ''
for i in 'kajshdkhuiehkdjhghgffkhgjghjgyugjhgada':
	line += termcolor.colored(i,random.choice(["red",'yellow','blue','green']))
	print(line)