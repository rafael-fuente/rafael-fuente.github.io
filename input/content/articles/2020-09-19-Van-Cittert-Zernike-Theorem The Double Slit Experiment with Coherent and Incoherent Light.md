Title: Visualizing the Van-Cittert Zernike Theorem - The Double Slit Experiment with Coherent and Incoherent Light
Date: 2020-09-19 11:20
Author: Rafael de la Fuente
Tags: Optics, Maxwell Equations, FDTD, Light Coherence

<figure class="video_container">
  <iframe width="769" height="432" src="https://www.youtube.com/embed/5cyzdsd6AOs" frameborder="0" allowfullscreen="true"> </iframe>
</figure>

<br /> 

What happens when the **double slit experiment** is performed with **incoherent light** (for example with a light bulb)? And how it differs when it is performed with **coherent light**  (for example with a laser)?

The main idea of these simulations is to answer this question, simulating the light propagating through the double slit at different time scales: (femtoseconds, picoseconds and microseconds) to show their differences.


## How I made the simulations:
---

The simulations were done using the finite-difference time-domain method (FDTD) applied to Maxwell equations.

The incoherent light is simulated computing the field created by oscillating dipoles sources with random phases and wavelengths and randomly placed inside the light source dimensions (a rectangle). The dipoles represent the electronic transitions of the excited atoms of the light source.

The microseconds and picoseconds simulations are obtained when the field is averaged over that period of time.

The **source code** of the simulations is:

[https://github.com/rafael-fuente/Incoherent-Light-Simulation/tree/master/double\_slit\_simulations](https://github.com/rafael-fuente/Incoherent-Light-Simulation/tree/master/double_slit_simulations)

You can change the parameters of the simulations just typing the values you want in the scripts that are indicated.

While the femtoseconds simulations only took a few minutes to be completed, the microsecond simulations [2:28](https://www.youtube.com/watch?v=5cyzdsd6AOs&t=148s) took hundreds of hours to be completed in a personal computer!

In the femtoseconds scale you can slow down the video to x0.25 in youtube settings if you find the flickering annoying. Also the video is uploaded at HD 1440p to avoid the artifacts that youtube video encoder creates with the waves at lower resolutions. You can see all fine details of the waves if you watch the video at this resolution.

## More explanations:
---

\- The blinking on the femtosecond time scale is because when the light is reflected on the double slit wall is due to a standing wave formed by interference from the incident and reflected waves, with an oscillation frequency equal to the frequency of the wave.

\- In microseconds time scale [1:20](https://www.youtube.com/watch?v=5cyzdsd6AOs&t=80s) and any longer time scale, no incoherent light interference pattern should be visible as we observe in most of our daily life. But a stationary wave is still visible in the microseconds time scale near the double slit wall. However because its size is very small , you won't notice it at macroscopic scale and instead you will see a uniform pattern. (notice that the space scale of the simulations are 60 x 30 μm)

Finally, comment how the irradiance patterns on the screen at the microsecond time scale can be approximated using the Van-Cittert Zernike theorem and Fraunhofer approximation:

$$I ∝ sinc^2{\left( \frac{𝜋 a x}{z λ}\right)} \left( 1 + γ  \cos{\left(\frac{2𝜋D}{zλ}  x\right)}\right) $$

where:

$$D = \text{ distance between the slits}$$

$$a = \text{ slits width}$$

$$γ \text{  is the degree  of spatial coherence:  }  γ = sinc{\left(\frac{2 𝜋 D M}{L λ}\right)}$$

$$M = \text{ width of the light source}$$

$$z = \text{ distance from the screen to the double slit}$$

$$L = \text{ distance from the light source to the double slit}$$

<br /> 

Although this formula does not produce exact results for the scale of this simulation, you can use it for qualitative predictions. When γ = 1 the fringes are perfectly visible, and when γ = 0 they cannot be seen. The further you place the light source from the double slit, the closer the coherence degree will be of 1 .

This experiment is important because it's usually the easiest to set up to measure the degree of coherence of a light source. I hope these simulations have helped you to visualize how it really works.