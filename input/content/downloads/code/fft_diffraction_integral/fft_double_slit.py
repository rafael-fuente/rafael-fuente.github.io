import numpy as np

class Sheet():
    def __init__(self,extentX, extentY, Nx, Ny):
        self.x = np.linspace(extentX[0],extentX[1],Nx)
        self.y = np.linspace(extentY[0],extentY[1],Ny)
        self.xx,self.yy = np.meshgrid(self.x, self.y)
        
        self.Nx = np.int(Nx)
        self.Ny = np.int(Ny)
        self.f = np.zeros((int(self.Ny), int(self.Nx)))

        

    def rectangular_slit(self,x0, y0, lx, ly):
        """
        Creates a slit centered at the point (x0, y0) with width lx and height ly
        """
        self.f += np.select( [((self.xx > (x0 - lx/2) ) & (self.xx < (x0 + lx/2) )) & ((self.yy > (y0 - ly/2) ) & (self.yy < (y0 + ly/2) )),  True], [1, 0])


#simulation input:

Lx = 1.4
Ly = 0.4
Nx= 2500
Ny= 1500

sheet = Sheet(extentX = [-Lx, Lx] , extentY = [-Ly, Ly], Nx= Nx, Ny= Ny)

#slit separation 
mm = 1e-3
D = 128 * mm

sheet.rectangular_slit(x0 = -D/2, y0 = 0, lx = 22 * mm , ly = 88 * mm)
sheet.rectangular_slit(x0 = +D/2, y0 = 0, lx = 22 * mm , ly = 88 * mm)

# distance from slit to the screen (mm)
z = 5000

# wavelength (mm)
λ = 18.5*1e-7
k = 2*np.pi/λ

from scipy.fftpack import fft2
from scipy.fftpack import fftshift

fft_c = fft2(sheet.f * np.exp(1j * k/(2*z) *(sheet.xx**2 + sheet.yy**2)))
c = fftshift(fft_c)



#plot with matplotlib
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(6, 6))
ax1 = fig.add_subplot(2,1,1)  
ax2 = fig.add_subplot(2,1,2,sharex=ax1, yticklabels=[])  

abs_c = np.absolute(c)

#screen size mm
Lx_screen = Nx*z*λ/(4*Lx)
Ly_screen = Ny*z*λ/(4*Ly)

x_max = (np.pi/Lx * (Nx//2 - 1))*z*λ/(2*np.pi)
y_max = (np.pi/Ly * (Ny//2 - 1))*z*λ/(2*np.pi)

ax1.imshow(abs_c, extent = [-Lx_screen, Lx_screen, -Ly_screen,Ly_screen], cmap ='gray', interpolation = "bilinear", aspect = 'auto')

ax2.plot(np.linspace(-Lx_screen,Lx_screen, len(abs_c[0])), abs_c[len(abs_c)//2]**2, linewidth = 1)

ax1.set_ylabel("y (mm)")
ax2.set_xlabel("x (mm)")
ax2.set_ylabel("Probability Density $|\psi|^{2}$")
ax1.set_xlim([-2,2])
ax2.set_xlim([-2,2])
ax1.set_ylim([-1,1])
plt.setp(ax1.get_xticklabels(), visible=False)


plt.show()
