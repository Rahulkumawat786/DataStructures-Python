"""
This python file is implementation of Stack Class and related function
"""
class stack:
    def __init__(self):
        '''
        it is constructor that defines the private variable size and list of elements
        '''
        self.__size=0  #instance variable to store the size of stack
        self.__data=[] #instacce variable to store the element in the stack
    def empty(self):
        '''
        Input: nothing
        Output: return true if stack is empty
        :return:
        '''
        if self.__size==0:
            return True
        else:
            return False

    def push(self,value):
        '''
        iInput: a variable to push into the stack
        Output : nothing just push the given value into the stack
        :param value:
        :return:
        '''
        self.__data.append(value)
        self.__size+=1

    def pop(self):
        '''
        remove the top element from the stack but return nothing
        :return:
        '''
        if self.empty():
            print("stack is empty, can not be poped")
        else:
            self.__size-=1

    def top(self):
        '''
        return the top element of the stack
        :return:
        '''
        if self.empty():
            print("stack is empty")
            return -1
        return self.__data[self.__size-1]

    def size(self):
        '''
        return the size of the stack
        :return:
        '''
        return self.__size

# """
# using above stack class in programm
# """
# st = stack()
# for i in range(10):
#     st.push(i)
#
# while not st.empty():
#     print(st.top())
#     st.pop()