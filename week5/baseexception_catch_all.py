def risky_operation():
    raise KeyboardInterrupt("User pressed Ctrl+c")


try:
    risky_operation()
except BaseException as e:
    print(f"Caught a base exception :{e}")
    print(f"Type of exception is {type(e)}")
    
    
