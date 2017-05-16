# Python interpreter for the eWagon esolang
# An interpreter running in an interpreted language... that sounds efficient!
# Feel free to modify this file!

# IMPORTant stuff
from sys import stdout, argv
from time import sleep

# Error function
def error(text):
	print('Error:', text)
	exit()

# Class for queues
class Queue():
	def __init__(self):
		self.q = []
	def eq(self, x):
		self.q.append(x)
	def dq(self):
		if len(self.q) < 1: error('Attempt to dequeue from empty queue.')
		return self.q.pop(0)
	def peek(self):
		if len(self.q) < 1: error('Attempt to peek from empty queue.')
		return self.q[0]
	def clr(self):
		self.q = []

# Class for stacks
class Stack():
	def __init__(self):
		self.s = []
	def push(self, x):
		self.s.append(x)
	def pop(self):
		if len(self.s) < 1: error('Attempt to pop from empty stack.')
		return self.s.pop(-1)
	def peek(self):
		if len(self.s) < 1: error('Attempt to peek from empty stack.')
		return self.s[-1]
	def clr(self):
		self.s = []

mq = Queue() # Main queue
aq = Queue() # Argument queue
ms = Stack() # Main stack
ls = Stack() # Loop stack
mode = 'queue'
code = ''
ip = 0 # Instruction pointer

def load(): # Load a file
	if len(argv) < 2: error('No .ewg file specified.')
	if argv[1][-3:] != 'ewg': error('File specified is not a .ewg file.')
	global code
	filepath = argv[1]
	c = open(filepath, 'r')
	code = c.read().replace('\n', ' ')

def argerror(args, cmd):
	if len(aq.q) < args: error('Not enough arguments supplied to \"%s\".' % cmd)

# Define all the commands
def queuemode():
	global mode
	if mode != 'queue':
		mq.q = ms.s
		ms.clr()
		mode = 'queue'

def stackmode():
	global mode
	if mode != 'stack':
		ms.s = mq.q
		mq.clr()
		mode = 'stack'

def peek():
	if mode == 'queue': aq.eq(mq.peek())
	elif mode == 'stack': aq.eq(ms.peek())

def pop():
	if mode == 'queue': aq.eq(mq.dq())
	elif mode == 'stack': aq.eq(ms.pop())

def discard():
	if mode == 'queue': mq.dq()
	elif mode == 'stack': ms.pop()

def add():
	argerror(2, '+')
	if mode == 'queue': mq.eq(aq.dq() + aq.dq())
	elif mode == 'stack': ms.push(aq.dq() + aq.dq())

def sub():
	argerror(2, '-')
	if mode == 'queue': mq.eq(aq.dq() - aq.dq())
	elif mode == 'stack': ms.push(aq.dq() - aq.dq())

def mul():
	argerror(2, '-')
	if mode == 'queue': mq.eq(aq.dq() * aq.dq())
	elif mode == 'stack': ms.push(aq.dq() * aq.dq())

def div():
	argerror(2, '-')
	if 0 in aq.q: error('Attempt to divide by zero.')
	if mode == 'queue': mq.eq(aq.dq() / aq.dq())
	elif mode == 'stack': ms.push(aq.dq() / aq.dq())

def equal():
	argerror(2, '=')
	if mode == 'queue':
		if aq.dq() == aq.dq(): mq.eq(1)
		else: mq.eq(0)
	elif mode == 'stack':
		if aq.dq() == aq.dq(): ms.push(1)
		else: ms.push(0)

def inequal():
	argerror(2, '_')
	if mode == 'queue':
		if aq.dq() != aq.dq(): mq.eq(1)
		else: mq.eq(0)
	elif mode == 'stack':
		if aq.dq() != aq.dq(): ms.push(1)
		else: ms.push(0)

def greater():
	argerror(2, '>')
	if mode == 'queue':
		if aq.dq() > aq.dq(): mq.eq(1)
		else: mq.eq(0)
	elif mode == 'stack':
		if aq.dq() > aq.dq(): ms.push(1)
		else: ms.push(0)

def less():
	argerror(2, '<')
	if mode == 'queue':
		if aq.dq() < aq.dq(): mq.eq(1)
		else: mq.eq(0)
	elif mode == 'stack':
		if aq.dq() < aq.dq(): ms.push(1)
		else: ms.push(0)

def printnum():
	argerror(1, '$')
	print(int(aq.dq()))

def shownum():
	argerror(1, '#')
	stdout.write(int(aq.dq()))

def printchar():
	argerror(1, '@')
	print(chr(aq.dq()))

def showchar():
	argerror(1, '!')
	stdout.write(chr(aq.dq()))

def numinput():
	if mode == 'queue': mq.eq(int(input()))
	elif mode == 'stack': ms.push(int(input()))

def interpret():
	global ip
	while 1:
#		print(':', code[ip], ip, mq.q, ms.s, aq.q, mode) # Prints some debug info
		# Commands/features that depend on the instruction pointer
		# Numbers
		if code[ip].isdigit():
			num = ''
			while 1:
				if code[ip] == ' ': break
				num += code[ip]
				ip += 1
			if mode == 'queue':	mq.eq(int(num))
			elif mode == 'stack': ms.push(int(num))
		# Strings
		elif code[ip] == '"':
			ip += 1
			while 1:
				if code[ip] == '"': break
				if mode == 'queue': mq.eq(ord(code[ip]))
				elif mode == 'stack': ms.push(ord(code[ip]))
				ip += 1
		# Loops
		elif code[ip] == '{': ls.push(ip)
		elif code[ip] == '}':
			if aq.dq() == 1:
				ip = ls.peek()
			else:
				ls.pop()
		# If-statements
		elif code[ip] == '[':
			if not aq.dq():
				while 1:
					if code[ip] == ']': break
					ip += 1
		
		# Commands for which I defined functions
		elif code[ip] == '~': queuemode()
		elif code[ip] == '`': stackmode()
		elif code[ip] == '%': peek()
		elif code[ip] == '^': pop()
		elif code[ip] == ',': discard()
		elif code[ip] == '+': add()
		elif code[ip] == '-': sub()
		elif code[ip] == '*': mul()
		elif code[ip] == '/': div()
		elif code[ip] == '=': equal()
		elif code[ip] == '_': inequal()
		elif code[ip] == '>': greater()
		elif code[ip] == '<': less()
		elif code[ip] == '$': printnum()
		elif code[ip] == '#': shownum()
		elif code[ip] == '@': printchar()
		elif code[ip] == '!': showchar()
		elif code[ip] == '&': numinput()
		elif code[ip] == '.': exit()
		ip += 1
#		sleep(0.1) # Delay

load()
# Run!
interpret()
