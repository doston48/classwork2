def number_checker (num):
    if not isinstance(num, int):
      print("Only integer data type is allowed!")
    if num > 0:
       print ("Positive number!")
    elif num < 0:
        print ("Negative number!")
    else:
        print ("Zero!")