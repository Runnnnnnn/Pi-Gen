import numpy as np

class PiGeneration:
    """
    Summary of the class
    
    This class is designed to .....
    
    The attributes:
    numberOfSimulation(int) - required - the number of simulation times
    
    The Method:
    calc() - do the calculation
    
    The example of usage:
    obj = PiGeneration(1000)
    obj.calc()
    
    
    Todo List:
    1 - ...
    2 - ...
    3 - ...
     
    """

    def __init__(self, N):
        self.numberOfSimulation = N

    def calc(self):
        """
        This method is desgined to...
        It mainly has three parts:
            1. generate a list of uniform numbers for x and y
            2. count the number of points within the quarter circle(d=1)
            3. calculate the value of pi
        
        Input parametr: 
            None
        
        Returns:
            calculated Pi
        
        """
        #generate a list of uniform numbers for x and y
        x = np.random.uniform(0,1,self.numberOfSimulation)
        y = np.random.uniform(0,1,self.numberOfSimulation)

        #count the number of points within the quarter circle(d=1)
        z = (x**2+y**2)**0.5
        quarter = np.where(z<=1,1,0)

        #calculate the value of pi
        pii = sum(quarter)*4/float(self.numberOfSimulation)
        return pii

########### main function #####################
if __name__ == '__main__':
    obj = PiGeneration(1000)
    print(obj.calc())




