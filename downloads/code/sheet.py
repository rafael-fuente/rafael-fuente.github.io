import numpy as np

class Sheet():
    def __init__(self,rangX, rangY, Nx, Ny):
        self.x = np.linspace(rangX[0],rangX[1],Nx)
        self.y = np.linspace(rangY[0],rangY[1],Ny)
        self.xx,self.yy = np.meshgrid(self.x, self.y)
        
        self.Nx = np.int(Nx)
        self.Ny = np.int(Ny)
        self.f = np.zeros((int(self.Ny), int(self.Nx)))

        

    def rectangular_slit(self,x0, y0, lx, ly):
        """
        Creates a slit centered at the point (x0, y0) with width lx and height ly
        """
        self.f += np.select( [((self.xx > (x0 - lx/2) ) and (self.xx < (x0 + lx/2) )) and ((self.yy > (y0 - ly/2) ) and (self.yy < (y0 + ly/2) )),  True], [1, 0])