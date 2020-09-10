
'''
I noticed many were being confused by the different ways to print a string.
Here I will show you all the ways known to me of printing a string, you choose whichever you like.
Personally I prefer the third method (C inherited) because it just keeps everything clean and organized.
First of all I will mention that order in all of these examples matters.
'''

# sample text
s = 'Vrije'
t = 'University'
x = 23

# comma separated
print(s, 'is a', t, 'and', x, 'is a number')

# concatenated
print(s + ' is a ' + t + ' and ' + str(x) + ' is a number') # do not forget to stringify integers or floats

# old style formatting (inherited from C languages)
print('%s is a %s and %i is a number' % (s, t, x))

# using .format
print('{} is a {} and {} is a number'.format(s, t, x))

# formatted string literals
print(f'{s} is a {t} and {x} is a number')
