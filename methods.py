

# Methods

# Very similar to functions
# class MethodExamples:
#     this_can_be_accessed_easily = "Hi I am easily found!"
#
#     def __init__(self):
#         self.this_can_be_accessed_easily = "Hi I am easily found"


class MethodExamples:
    def __init__(self):
        self.__this_can_be_accessed_easily = "Hi I am easily found!" # __ use this to set public and private in Python

x = MethodExamples()

print(x.this_can_be_accessed_easily)
x.this_can_be_accessed_easily = "I have been changed!"
print(x.this_can_be_accessed_easily)

# A lot of other languages we have to use Public and Private for access.

