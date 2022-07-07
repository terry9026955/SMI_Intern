try:
    a = 1 / 1
    print("End")
except Exception as e:
    print("Error!!!: ", e)
else:
    print("OK!")
finally:
    print("finally")