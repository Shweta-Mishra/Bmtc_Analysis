#!/usr/bin/python -tt

def donuts(count):
  # +++your code here+++
  if count>=10:
    return 'Number of donuts: many'
  else:
    return 'Number of donuts: %d'%(count)
  
def both_ends(s):
  ln=len(s)
  if ln<2:
   return ''
  else:
   return s[0]+s[1]+s[ln-2]+s[ln-1]

# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
  print 'donuts'
  # Each line calls donuts, compares its result to the expected for that call.
  test(donuts(4), 'Number of donuts: 4')
  test(donuts(9), 'Number of donuts: 9')
  test(donuts(10), 'Number of donuts: many')
  test(donuts(99), 'Number of donuts: many')

  print 'both_ends'
  test(both_ends('spring'), 'spng')
  test(both_ends('Hello'), 'Helo')
  test(both_ends('a'), '')
  test(both_ends('xyz'), 'xyyz')


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
