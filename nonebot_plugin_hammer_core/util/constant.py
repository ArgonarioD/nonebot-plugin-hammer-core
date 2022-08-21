"""
Example:
    consts = ConstNamespace.test_constant
    consts.TEST_A = 'a'
    consts.TEST_B = 'b'

    print(consts.TEST_A)
"""


class Const:
    def __setattr__(self, key, value):
        if key in self.__dict__:
            raise ConstError(key)
        self.__dict__[key] = value


class ConstError(RuntimeError):
    def __init__(self, key):
        super(ConstError, self).__init__(f'{key} cannot be modified')


class __ConstantNamespace:
    def __getattr__(self, item):
        if item not in self.__dict__:
            self.__dict__[item] = Const()
        return self.__dict__[item]


ConstNamespace = __ConstantNamespace()
