import main as Zeiku
import os
print(Zeiku.about())
while True:
	try:
		text = input('Zeiku >> ')
		def g():
			print(text)
		g()
		result, error = Zeiku.run('<stdin>', text)
		if error: print(str(error))
		else: print(result)
	except KeyboardInterrupt:
		os.system('clear')
		print('Zeikython KeyboardInterrupt')
		exit()