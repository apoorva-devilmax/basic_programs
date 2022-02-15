def my_function(param: str) -> dict:
	test = param
	if len(test) > 5:
		return {'msg': 'success'}
	# end if
	return False
# end function my_function

print(my_function('ehe'))

# conclusion: type hinting does not restrict