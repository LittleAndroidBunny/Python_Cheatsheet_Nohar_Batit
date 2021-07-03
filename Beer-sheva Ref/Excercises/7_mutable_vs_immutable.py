# This script is part of tutorial number 4 of introduction of computer science for EE students at BGU.
# Topics:
#   - consider memory allocation behind the scene.
#   - Discuss its implications regarding nature of variables.

# id changes when assigning new value - new allocation
int_var = 1
print("value:", str(int_var),  ",id: ", id(int_var))

int_var = 2
print("value:", str(int_var), ",id: ", id(int_var))

second_int = int_var
print("value:", str(second_int), ",id: ", id(second_int))


# validation
print(int_var == second_int)
print(int_var is second_int)


# same for float
float_var = 1.0
print("value:", str(float_var), ",id: ", id(float_var))

float_var = 2.0
print("value:", str(float_var), ",id: ", id(float_var))



# same for string
str_var = "I'm a lumberjack and I'm OK."
print("value: " + str_var + ",id: ", id(str_var))

str_var = "i sleep all night and I work all day."
print("value: " + str_var + ",id: ", id(str_var))

# Will this work?
str_var[0] = str_var[0].capitalize()
# Will this work?
str_var = str_var.capitalize()
print(str_var)
