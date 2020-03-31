def beCheerful(name='', repeat=2):		# set defaults when declaring the parameters
	print(f"good morning {name}\n" * repeat)
# beCheerful()				# output: good morning (repeated on 2 lines)


beCheerful("tim")	#output: good morning tim (repeated on 2 lines)


beCheerful(name="john")			# output: good morning john (repeated on 2 lines)


beCheerful(repeat=6)			# output: good morning (repeated on 6 lines)
beCheerful('al',6)

beCheerful(name="michael", repeat=5)	# output: good morning michael (repeated on 5 lines)
# NOTE: argument order doesn't matter if we are explicit when sending in our arguments!


beCheerful(repeat=3, name="kb")		# output: good morning kb (repeated on 3 lines)
