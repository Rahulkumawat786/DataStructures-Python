'''
This python file contain Queue class
'''
class queue:
    ''' this is queue class defines all required function'''
    def __init__(self):
        '''constructor for initializing the required variable'''
        self.__size = 0
        self.__value = []

    def empty(self):
        '''
        return true if queue is empty
        :return:
        '''
        if self.__size==0:
            return True
        else:
            return False

    def front(self):
        '''
        return the front (i.e first element)
        :return:
        '''
        if self.empty():
            print("Queue is empty")
        else:
            return self.__value[0]

    def push(self,val):
        '''
        push given element into the queue return nothing
        :param val:
        :return:
        '''
        self.__value.append(val)
        self.__size+=1

    def pop(self):
        '''
        remove front element as it follow FIFO rule
        :return:
        '''
        if self.empty():
            print("Can't remove queue is empty!")
        else:
            self.__value.pop(0)
            self.__size-=1

    def __str__(self):
        return f"queue is {self.__value} \nsize : {self.__size}"