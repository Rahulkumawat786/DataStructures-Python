"""
Dequeue class
"""
class dequeue:
    def __init__(self):
        '''
        constructor initialize the dequeue
        '''
        self.__size = 0
        self.values = []

    def empty(self):
        '''
        return true if dequeue is empty
        :return:
        '''
        if self.__size==0:
            return True
        else:
            return False

    def push_back(self,val):
        '''
        push the given element at last
        :param val:
        :return:
        '''
        self.values.append(val)
        self.__size+=1

    def push_front(self,val):
        '''
        push the given element at front
        :param val:
        :return:
        '''
        self.values = [val] + self.values
        self.__size+=1

    def pop_back(self):
        '''
        pop last element if dequque is not empty return nothing
        :return:
        '''
        if self.empty():
            print("Can't pop!")
        else:
            self.values.pop()
            self.__size-=1

    def pop_front(self):
        '''
        pop front element if dequeue is not empty not return anything
        :return:
        '''
        if self.empty():
            print("Can't pop!")
        else:
            self.values = self.values[1:]
            self.__size-=1

    def front(self):
        '''
        return front element
        :return:
        '''
        if self.empty():
            return None
        else:
            return self.values[0]
    def back(self):
        '''
        return last element
        :return:
        '''
        if self.empty():
            return None
        else:
            return self.values[-1]



