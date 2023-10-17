'''Functionality for volume conversion and volume equality checks.
Values of two different volumes recorded in different measurements are considered equal
if the converted values within a relative tolerance or absolute tolerance of FLOAT_POINT_TOL.
The default for FLOAT_POINT_TOL is 1e-05.
'''


import functools
from math import isclose, floor, ceil
from measuring_tools import Measurement


def __dir__():
    return ('Volume', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__')


@functools.total_ordering
class Volume(Measurement):
    '''Volume class comparing and converting Metric, British Imperial Units, and US Units
    * value is expected to be either an integer or a float
    * measurement can be one of three options (defaults to liter):
        - liter
        - gallon
        - gallon_us
    '''


    def __init__(self, value: int | float, measurement: str='liter'):
        if measurement not in ('liter', 'gallon', 'gallon_us'):
            raise ValueError('Value must be liter, gallon, gallon_us')
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
            case 'liter':
                symbol = 'L'
            case 'gallon':
                symbol = 'gal'
            case 'gallon_us':
                symbol = 'gal'
        return f'{self.value}{symbol}'

    def __round__(self, ndigits):
        return Volume(round(self.value, ndigits=ndigits), self.measurement)


    def __abs__(self):
        return Volume(abs(self.value), self.measurement)


    def __floor__(self):
        return Volume(floor(self.value), self.measurement)


    def __ceil__(self):
        return Volume(ceil(self.value), self.measurement)


    def __eq__(self, other):
        match self.measurement:
            case 'liter':
                return isclose(self.value, other.to_liter().value, rel_tol=self.FLOAT_POINT_TOL, abs_tol=self.FLOAT_POINT_TOL)
            case 'gallon':
                return isclose(self.value, other.to_gallon().value, rel_tol=self.FLOAT_POINT_TOL, abs_tol=self.FLOAT_POINT_TOL)
            case 'gallon_us':
                return isclose(self.value, other.to_gallon_us().value, rel_tol=self.FLOAT_POINT_TOL, abs_tol=self.FLOAT_POINT_TOL)


    def __lt__(self, other):
        if self == other:
            return False
        match self.measurement:
            case 'liter':
                return self.value < other.to_liter().value
            case 'gallon':
                return self.value < other.to_gallon().value
            case 'gallon_us':
                return self.value < other.to_gallon_us().value


    def __add__(self, other):
        match self.measurement:
            case 'liter':
                total = self.value + other.to_liter().value
            case 'gallon':
                total = self.value + other.to_gallon().value
            case 'gallon_us':
                total = self.value + other.to_gallon_us().value
        return Volume(total, self.measurement)


    def __sub__(self, other):
        match self.measurement:
            case 'liter':
                diff = self.value - other.to_liter().value
            case 'gallon':
                diff = self.value - other.to_gallon().value
            case 'gallon_us':
                diff = self.value - other.to_gallon_us().value
        return Volume(diff, self.measurement)


    def __mul__(self, other):
        match self.measurement:
            case 'liter':
                product = self.value * other.to_liter().value
            case 'gallon':
                product = self.value * other.to_gallon().value
            case 'gallon_us':
                product = self.value * other.to_gallon_us().value
        return Volume(product, self.measurement)


    def __truediv__(self, other):
        match self.measurement:
            case 'liter':
                result = self.value / other.to_liter().value
            case 'gallon':
                result = self.value / other.to_gallon().value
            case 'gallon_us':
                result = self.value / other.to_gallon_us().value
        return Volume(result, self.measurement)


    def __floordiv__(self, other):
        match self.measurement:
            case 'liter':
                result = self.value // other.to_liter().value
            case 'gallon':
                result = self.value // other.to_gallon().value
            case 'gallon_us':
                result = self.value // other.to_gallon_us().value
        return Volume(result, self.measurement)


    def __mod__(self, other):
        match self.measurement:
            case 'liter':
                result = self.value % other.to_liter().value
            case 'gallon':
                result = self.value % other.to_gallon().value
            case 'gallon_us':
                result = self.value % other.to_gallon_us().value
        return Volume(result, self.measurement)


    def to_liter(self):
        '''Convert the volume to liter'''
        measure = 'liter'
        match self.measurement:
            case 'liter':
                return self
            case 'gallon':
                return Volume((self.value * 4.54609513), measurement=measure)
            case 'gallon_us':
                return Volume((self.value * 3.78541178), measurement=measure)


    def to_gallon(self):
        '''Convert the volume to British Imperial Gallons'''
        measure = 'gallon'
        match self.measurement:
            case 'gallon':
                return self
            case 'liter':
                return Volume((self.value * 0.219969157), measurement=measure)
            case 'gallon_us':
                return Volume((self.value * 0.8326741846), measurement=measure)


    def to_gallon_us(self):
        '''Convert the volume to US Gallons'''
        measure = 'gallon_us'
        match self.measurement:
            case 'gallon_us':
                return self
            case 'liter':
                return Volume((self.value * 0.264172052), measurement=measure)
            case 'gallon':
                return Volume((self.value * 1.200949925), measurement=measure)
