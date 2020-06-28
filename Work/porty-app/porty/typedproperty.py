def typedproperty(name, expectedType):
    _privateName = '_' + name
    @property
    def prop(self):
        return getattr(self, _privateName)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, expectedType):
            raise TypeError(f'Expected {expectedType}')
        setattr(self, _privateName, value)

    return prop

String = lambda name: typedproperty(name, str)
Integer = lambda name: typedproperty(name, int)
Float = lambda name: typedproperty(name, float)