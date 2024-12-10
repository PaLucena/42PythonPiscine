def all_thing_is_obj(object: any) -> int:
	if type(object).__name__ == "str":
		print(f"{object} is in the kitchen : {type(object)}")
	elif type(object).__name__ == "tuple":
		print(f"Tuple : {type(object)}")
	elif type(object).__name__ == "list":
		print(f"{type(object).__name__.capitalize()} : {type(object)}")
	elif type(object).__name__ == "dict":
		print(f"{type(object).__name__.capitalize()} : {type(object)}")
	elif type(object).__name__ == "set":
		print(f"{type(object).__name__.capitalize()} : {type(object)}")
	else:
		print("Type not found")

	return(42)
