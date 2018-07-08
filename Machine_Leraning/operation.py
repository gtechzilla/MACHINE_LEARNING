#Creating my own nerual network class
#the classes begin in small letters as this is the syntax when using tensorflow
 class Operation():
    def __init__(self,input_nodes=[]):
        #initialize input variable that stores the input_node list
        self.input_nodes=input_nodes
        #intialize an empty output_node list stored in output_node variable
        self.output_nodes=[]

        #appends input_nodes to output node list
        for node in input_nodes:
            node.output_nodes.append(self)
    #initialize compute method,but its passed since it will be overwritten
    def compute(self):
        pass

#making the add class that inherits from operation class
class add(Operation):
    #initialize the class with x and y arguments
    def __init__(self,x,y):
        #tells the class to inherit the values of x and y from operation class as a list object
        super().__init__([x,y])
    def compute(self,x_var,y_var):
        self.inputs=[x_var,y_var]
        return x_var + y_var

class multiply(Operation):
    def __init__(self,x,y):
        super().__init__([x,y])
    def compute(self,x_var,y_var):
        self.inputs=[x_var,y_var]
        return x_var * y_var

class matmulti(Operation):
    def __init__(self,x,y):
        super().__init__([x,y])
    def compute(self,x_var,y_var):
        self.inputs=[x_var,y_var]
        return x_var.dot(y_var)

class Placeholder():
    def __init__(self):
        self.output_node=[]

        _default_graph.placeholders.append(self)

class Variable():
    def __init__(self,initial_value=None):
        self.value=initial_value
        self.output_nodes=[]

        _default_graph.variables.append(self)

class Graph():

    def __init__(self):
        self.operations=[]
        self.placeholders=[]
        self.variables=[]

    def set_as_default(self):
        global _default_graph
        _default_graph=self
'''
A=10
b=1
x="x"
z=A * int(x)+b
'''
g=Graph()
g.set_as_default()
A=Variable(10)
b=Variable(1)
x=Placeholder()

y=multiply(A,x)
z=add(y,b)
