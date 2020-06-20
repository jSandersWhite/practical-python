# bounce.py
#
# Exercise 1.5

height = 100
bounceHeight = 0.6
bounceLimit = 10
bounce = 1

while bounce <= bounceLimit:
    height = round(height * bounceHeight, 4)
    print(bounce, height)
    bounce = bounce + 1
