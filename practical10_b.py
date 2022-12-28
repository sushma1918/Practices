'''
Experiment 10
Write a program to implement try, except and finally block statements
-------------------------------------------------------
# working of try()
def divide(x, y):
	try:
		result = x // y
	except ZeroDivisionError:
		print("Sorry ! You are dividing by zero ")
	else:
		print("Yeah ! Your answer is :", result)
	finally:
		
		# regardless of exception generation.
		print('This is always executed')

divide(3, 2)
divide(3, 0)
----------------------------------------------------------
'''
# working of try()
def add(a, b):
    try:
        result = a + b
    except:
        print("Sorry ! can not do this operation")
    else:
        print(f"Adding number \n{a} + {b} = {result}") 

    finally:
        # this block is always executed
        print('Thank you')

add (3,2)
add(3, "2")          