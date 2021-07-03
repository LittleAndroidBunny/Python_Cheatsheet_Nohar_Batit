global_scope_variable = 'bad practice'


def foo1():
    print("value upon entering function: ", global_scope_variable)
    # Will this work?
    #global_scope_variable = 'very bad practice'
    print(global_scope_variable)


foo1()
print("value out of function: ", global_scope_variable)


def foo2():
    global global_scope_variable
    print("value upon entering function: ", global_scope_variable)
    global_scope_variable = 'very bad practice'
    print("value after change in function: ", global_scope_variable)


foo2()
print("value out of function: ", global_scope_variable)


# horrible code ahead
HUNDRED = 100
ref_liters = 11
ref_km = 220
distance_traveled_km = 150
gas = 25


def liters_depleted(lit, kilometer):
    global gas
    lk = (lit / (kilometer / HUNDRED))
    gas -= (distance_traveled_km * lk)/HUNDRED


liters_depleted(ref_liters, ref_km)
print(gas)
