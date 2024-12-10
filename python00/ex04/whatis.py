import sys

try:
	if len(sys.argv) > 2:
		raise AssertionError("more than one argument is provided")
	elif len(sys.argv) == 2:
		try:
			nb = int(sys.argv[1])
			type = "Even" if nb % 2 == 0 else "Odd"
			print(f"I'm {type}")
		except ValueError:
			raise AssertionError("argument is not an integer")
except AssertionError as e:
	print(f"AssertionError: {e}")