class BaseFoo:
    # where is the constructor
    member_foo = 'foo'
    member_bar = 'bar'

    def __repr__(self):
        return self.member_foo + ' ' + self.member_bar


class Bar:
    new_member = 'hi'
    foo_instance = BaseFoo()


class InheritedFoo(BaseFoo):
    subclass_member = 'this is a member'
    def __init__(self,val):
        self.value = val


if __name__ == '__main__':
    f = BaseFoo()
    print(f)
    b = Bar()
    print(b)  # What will this do?
    print(b.foo_instance)
    print(InheritedFoo(0))  # What will this do?
    #
    first_instance = InheritedFoo(1)
    another_instance = InheritedFoo(2)

    test = type(InheritedFoo(1))
    print(test == InheritedFoo)  # is this a good way to find class type?
    print(isinstance(another_instance,InheritedFoo))  # is this a good way to find class type?
    print(test == BaseFoo)  # is this a good way to find class type?
    print(isinstance(another_instance, BaseFoo))  # is this a good way to find class type?
