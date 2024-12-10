import math

def NULL_not_found(object: any) -> int:
	not_null = True if object else False
	if type(object).__name__ == "float" and math.isnan(object):
		not_null = False
	if not_null:
		print("Type not Found")
		return(1)
	
	my_type = type(object)
	match my_type.__name__:
		case "NoneType":
			print(f"Nothing: {object} {my_type}")
		case "float":
			print(f"Cheese: {object} {my_type}")
		case "int":
			print(f"Zero: {object} {my_type}")
		case "str":
			print(f"Empty: {object}{my_type}")
		case "bool":
			print(f"Fake: {object} {my_type}")
	
	return(0)