x = 42
y = 0
print("here we go!!!!!!!!!!!!!!!!")
try:
    print(x / y)

#We can identify the type of error
except Exception as e:
    # Optionally, log e somewhere
    print('Sorry, something went wrong')
    print(e)

finally:
    print('This always runs on success or failure')


