
class Node:
    """Node Class
    used to define Node in Linked Based Stack
    """
    def __init__(self):
        self.Data = None
        self.Next = None


class Stack_Pointer_Based:
    """ Stack_Pointer_Based Class
    use Linked Nodes to construct the Stack
    """

    def __init__(self):
        self.Top = Node()
        self.Top = None

    def Push(self,item):
        self.New_Node = Node()
        self.New_Node.Data = item
        self.New_Node.Next = self.Top
        self.Top = self.New_Node



    def Pop(self):
        if self.isEmpty() :
            print("Stack is Empty")
        else:

            tem = self.Top
            print(tem.Data)
            self.Top = self.Top.Next

    def GetStakTop(self):
        if self.isEmpty():
            print("Stack is Empty GetStakTop")
        else:
            print(self.Top.Data)
            return self.Top.Data


    def isEmpty(self):
        return (self.Top == None )#or  (self.Top.Next == None)


class Stack:
    """ Stack Class
    use Normal List(array) to construct the Stack
    """
    def __init__(self):
        self.Top = -1
        self.s = []

    def isEmpty(self):
        return self.Top < 0


    def Push(self,item):

        self.s.append(item)
        self.Top+=1

    def Pop(self):

        if self.isEmpty():
            print("Stack is Empty Pop")
        else:
            del(self.s[self.Top])
            self.Top=self.Top-1

    def GetStakTop(self):
        if self.isEmpty():
            print("Stack is Empty GetStakTop")
        else:
            return self.s[self.Top]

    def printStack(self):

        if self.isEmpty():
            print("Stack is Empty printStack")
        else:
            tem  = self.s.copy()
            tem.reverse()
            print(tem)




if __name__ == "__main__":
    stack  = Stack_Pointer_Based()
    stack.Push(112)
    stack.Push(20)
    stack.Push(110 )
    stack.GetStakTop()
    stack.Push(20)
    stack.Pop()
