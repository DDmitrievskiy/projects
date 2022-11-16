# Для некоторого списка [x1, x2, x3, ..., xn] нужно было вычислить последнюю цифру умножения
# x1 ^ (x2 ^ (x3 ^ (... ^ xn)))



def is_null(test_input, j = 0):
  if (test_input[j] != 0):
    return False
  if (len(test_input) == j + 1):
    return True
  if (test_input[j+1] != 0):
    return True
  k = len(test_input) - 1
  for i in range(j, len(test_input)):
    if (test_input[i] != 0):
      break
    k = i

  if ((k - j) % 2 == 0):
    return True
  else:
    return False
    

def is_one(test_input, j = 0):
  if (test_input[j] == 0):
    return not is_null(test_input, j)
  if (test_input[j] == 1):
    return True
  return len(test_input) - 1 != j and is_null(test_input, j+1)


def last_digit(test_input):
  for i in range(3):
    if (len(test_input) < 3):
      test_input.append(1)
  a = test_input[0] % 10
  is_null_a = is_null(test_input, 0)
  b = test_input[1]
  is_null_b = is_null(test_input, 1)
  c = test_input[2]
  is_null_c = is_null(test_input, 2)

  if (a == 5 or a == 6):
    if (is_null_b):
      return 1
    else:
      return a
  if (a == 0):
    if (test_input[0] != 0):
      return 0
    if (is_null_a):
      return 0
    else:
      return 1
  if (is_null_b):
    return 1
  if (is_null_c):
    return a

  if (test_input[2] == 0):
    test_input[2] = 1
    c = 1

  if (a == 1):
    return 1

  if (a == 2):
    arr = [ 6, 2, 4, 8 ]
  if (a == 3):
    arr = [ 1, 3, 9, 7 ]
  if (a == 4):
    arr = [ 6, 4 ]
  if (a == 7):
    arr = [ 1, 7, 9 , 3 ]
  if (a == 8):
    arr = [ 6, 8, 4, 2 ]
  if (a == 9):
    arr = [ 1, 9 ]

  if (a == 2 or a == 3 or a == 7 or a == 8):
    b_2 = b * b;
    b_3 = b_2 * b
    if (b % 4 == 2 and b_2 % 4 == 0 and b_3 % 4 == 0):
      if (is_one(test_input, 2)):
        ind = 2
      else:
        ind = 0
    elif (c % 2 != 0):
      ind = b % 4
    else:
      ind = (b_2) % 4
  else:
    ind = b % 2

  return arr[ind]