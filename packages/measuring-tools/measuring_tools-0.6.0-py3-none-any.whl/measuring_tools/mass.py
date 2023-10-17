'''Functionality for mass conversion and mass equality checks.
Values of two different masses recorded in different measurements are considered equal
if the converted values within a relative tolerance or absolute tolerance of FLOAT_POINT_TOL.
The default for FLOAT_POINT_TOL is 1e-05.
'''


import functools
from math import isclose, floor, ceil
from measuring_tools import Measurement


def __dir__():
    return ('Mass', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__')


@functools.total_ordering
class Mass(Measurement):
    '''Mass Converter class
    * value is expected to be either an integer or a float
    * measurement can be one of four options (defaults to gram)
        - gram
        - kilogram
        - ton_us
        - pound
    '''


    def __init__(self, value: int | float, measurement: str='gram'):
        if measurement not in ('gram', 'kilogram', 'ton_us', 'pound'):
            raise ValueError('Value must be gram, kilogram, ton_us, or pound')
        super().__init__(value, measurement)


    def __format__(self, format_spec):
        """Format self.value based on the given format_spec
        format_spec (str):
            * '' is the default value and will return self.value as a string
            * 'abbrv' will return self.value with the appropriate SI abbreviation

        Raises
            * NameError if format_spec is not '' or 'abbrv'

        Return (str)
		"""
        if format_spec not in ('', 'abbrv'):
            raise NameError(f'format_spec must be abbrv or None. Recieved {format_spec!r}')

        if format_spec == '':
            return str(self.value)

        match self.measurement:
            case 'gram':
                symbol = 'g'
            case 'kilogram':
                symbol = 'kg'
            case 'ton_us':
                symbol = 'tn'
            case 'pound':
                symbol = 'lb'
        return f'{self.value}{symbol}'


    def __round__(self, ndigits):
        return Mass(round(self.value, ndigits=ndigits), self.measurement)


    def __abs__(self):
        return Mass(abs(self.value), self.measurement)


    def __floor__(self):
        return Mass(floor(self.value), self.measurement)


    def __ceil__(self):
        return Mass(ceil(self.value), self.measurement)


    def __eq__(self, other):
        match self.measurement:
            case 'gram':
                return isclose(self.value, other.to_gram().value, rel_tol=self.FLOAT_POINT_TOL, abs_tol=self.FLOAT_POINT_TOL)
            case 'ton_us':
                return isclose(self.value, other.to_ton_us().value, rel_tol=self.FLOAT_POINT_TOL, abs_tol=self.FLOAT_POINT_TOL)
            case 'pound':
                return isclose(self.value, other.to_pound().value, rel_tol=self.FLOAT_POINT_TOL, abs_tol=self.FLOAT_POINT_TOL)
            case 'kilogram':
                return isclose(self.value, other.to_kilogram().value, rel_tol=self.FLOAT_POINT_TOL, abs_tol=self.FLOAT_POINT_TOL)


    def __lt__(self, other):
        if self == other:
            return False
        match self.measurement:
            case 'gram':
                return self.value < other.to_gram().value
            case 'ton_us':
                return self.value < other.to_ton_us().value
            case 'pound':
                return self.value < other.to_pound().value
            case 'kilogram':
                return self.value < other.to_kilogram().value


    def __add__(self, other):
        match self.measurement:
            case 'gram':
                total = self.value + other.to_gram().value
            case 'ton_us':
                total = self.value + other.to_ton_us().value
            case 'pound':
                total = self.value + other.to_pound().value
            case 'kilogram':
                total = self.value + other.to_kilogram().value
        return Mass(total, self.measurement)


    def __sub__(self, other):
        match self.measurement:
            case 'gram':
                diff = self.value - other.to_gram().value
            case 'ton_us':
                diff = self.value - other.to_ton_us().value
            case 'pound':
                diff = self.value - other.to_pound().value
            case 'kilogram':
                diff = self.value - other.to_kilogram().value
        return Mass(diff, self.measurement)


    def __mul__(self, other):
        match self.measurement:
            case 'gram':
                product = self.value * other.to_gram().value
            case 'ton_us':
                product = self.value * other.to_ton_us().value
            case 'pound':
                product = self.value * other.to_pound().value
            case 'kilogram':
                product = self.value * other.to_kilogram().value
        return Mass(product, self.measurement)


    def __truediv__(self, other):
        match self.measurement:
            case 'gram':
                result = self.value / other.to_gram().value
            case 'ton_us':
                result = self.value / other.to_ton_us().value
            case 'pound':
                result = self.value / other.to_pound().value
            case 'kilogram':
                result = self.value / other.to_kilogram().value
        return Mass(result, self.measurement)


    def __floordiv__(self, other):
        match self.measurement:
            case 'gram':
                result = self.value // other.to_gram().value
            case 'ton_us':
                result = self.value // other.to_ton_us().value
            case 'pound':
                result = self.value // other.to_pound().value
            case 'kilogram':
                result = self.value // other.to_kilogram().value
        return Mass(result, self.measurement)


    def __mod__(self, other):
        match self.measurement:
            case 'gram':
                result = self.value % other.to_gram().value
            case 'ton_us':
                result = self.value % other.to_ton_us().value
            case 'pound':
                result = self.value % other.to_pound().value
            case 'kilogram':
                result = self.value % other.to_kilogram().value
        return Mass(result, self.measurement)


    def to_gram(self):
        '''Convert the length to gram'''
        measure = 'gram'
        match self.measurement:
            case 'gram':
                return self
            case 'ton_us':
                return Mass((self.value / 907_184.74) , measurement=measure)
            case 'pound':
                return Mass((self.value / 453.59237) , measurement=measure)
            case 'kilogram':
                return Mass((self.value / 1_000) , measurement=measure)


    def to_ton_us(self):
        '''Convert the length to ton_us'''
        measure = 'ton_us'
        match self.measurement:
            case 'ton_us':
                return self
            case 'gram':
                return Mass((self.value * 907_184.74) , measurement=measure)
            case 'pound':
                return Mass((self.value * 2_000) , measurement=measure)
            case 'kilogram':
                return Mass((self.value * 907.18474) , measurement=measure)


    def to_pound(self):
        '''Convert the length to pound'''
        measure = 'pound'
        match self.measurement:
            case 'pound':
                return self
            case 'gram':
                return Mass((self.value * 453.59237) , measurement=measure)
            case 'ton_us':
                return Mass((self.value / 2_000) , measurement=measure)
            case 'kilogram':
                return Mass((self.value / 2.2046226218) , measurement=measure)


    def to_kilogram(self):
        '''Convert the length to kilogram'''
        measure = 'kilogram'
        match self.measurement:
            case 'kilogram':
                return self
            case 'gram':
                return Mass((self.value * 1_000), measurement=measure)
            case 'ton_us':
                return Mass((self.value / 907.18474) , measurement=measure)
            case 'pound':
                return Mass((self.value * 2.2046226218) , measurement=measure)
