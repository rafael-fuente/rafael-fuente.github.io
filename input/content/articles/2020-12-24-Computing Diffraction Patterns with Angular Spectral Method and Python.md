Title: Computing Diffraction Patterns with the Angular Spectral Method and Python
Description: In this project we'll show how to compute the Diffraction Patterns with the Angular Spectral Method and Python.
Date: 2020-10-24 23:20
Author: Rafael de la Fuente
Tags: Optics, Diffraction, FFT
Image: https://rafael-fuente.github.io/images/incoherent-double-slit-simulations/visualization-of-the-Van-Cittert-Zernike-theorem.jpg
mathjax3: True

<!-- 16:9 aspect ratio -->
<div class="embed-responsive embed-responsive-16by9">
<iframe class="embed-responsive-item" src="https://www.youtube.com/embed/5cyzdsd6AOs?vq=hd1440" alt="Simulation of the Double Slit Experiment with Incoherent and Coherent Light" allowfullscreen></iframe>
</div>


<br /> 

In this project we will show how to numerically compute **Diffraction Patterns** with the **Angular Spectral Method**. We'll implement the method with **Python** and discuss how to simulate them both with monochromatic and polychromatic light like it's shown in the video above.


## The Angular Spectrum
---

In a previous post we have discussed how to solve the Frensel Integral with a single Fast Fourier Transform (FFT). However although this method is quite simple, it has some drawbacks:<br /> 
It is limited by the requeriment of a diffrent grid scale than the aperture figure, and by the approximation of the Fresnel and Fraunhofer regimes.<br /> 
As we will see next, the **The Angular Spectral Method** is free of these problems. It uses the same scale that the aperture figure, and it solves the wave equation exactly.

<div style="text-align:center"><img src="./images/angular-spectral-method/angular-spectral-method-single-slit-diffraction.png" alt="Angular Spectral Method Single Slit Diffraction"/></div>
<br /> 

Suppose that a monochromatic wave is incident on a transverse $(x', y')$ plane traveling with a component of propagation in the negative $z$ direction. Let the complex field across that $z = 0$ plane (Diffraction Sheet Plane) be represented by:
$$u(x', y', 0; t) = U(x', y', 0) e^{-\omega t i}$$
Our ultimate objective is to calculate the resulting field $U(x, y, -L)$ that appears
across a second, parallel plane (Screen) a distance $L$ to the right of the first plane. 

Across the $z = 0$ plane, the function $U(x, y, 0)$ has a two-dimensional Fourier transform given by:

<p class="math">
\begin{equation}
A\left(k_{x}, k_{y} ; 0\right)=\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} U(x', y', 0) e^{-(k_{x} x' + k_{y} y') i}   \mathrm{d} x' \mathrm{dy'}
\end{equation}
</p>

where $A\left(k_{x}, k_{y} ; 0\right)$ is called the **angular spectrum** of the distrubance $U(x, y, 0)$<br /> 

## Propagation of the Angular Spectrum
---

Consider now the angular spectrum of the disturbance U across a plane parallel to the
$z = 0$ plane but at a distance z from it. Let the function $A(k_{x}, k_{y}, z)$ represent the
angular spectrum of $U(x, y, z)$; that is

<p class="math">
\begin{equation}
A\left(k_{x}, k_{y} ; z\right)=\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} U(x, y, z) e^{-(k_{x} x + k_{y} y) i}   \mathrm{d} x \mathrm{dy}
\end{equation}</p>


and with its inverse transform given by:

<p class="math">
\begin{equation}
U\left(x, y , z\right)=\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} A(k_{x}, k_{y}; z) e^{(k_{x} x + k_{y} y) i}   \mathrm{d} k_{x} \mathrm{d} k_{y} 
\end{equation}
</p>


To know how the disturbance $U(x, y, z)$ varies with z, we are going to use the [Helmholtz equation](https://en.wikipedia.org/wiki/Helmholtz_equation) \eqref{eq:3} which is obtained simply from the wave equation after separating the temporal part:

<p class="math">
\begin{equation}
\nabla^{2} U + k^{2} U=0 \quad \text{with} \quad k = \frac{2 \pi}{\lambda}
\end{equation}
</p>

Now if we plug equation \eqref{eq:2} in to the Helmholtz equation we obtain the following relationship:

<p class="math">
\begin{equation}
\frac{d^{2}}{d z^{2}} A + k_{z} A = 0  \quad \text{with} \quad k_{z} = \sqrt{k^2 - k_{x}^2 + k_{y}^2}
\end{equation}
</p>

which has the solution:

<p class="math">
\begin{equation}
A{\left(k_{x},k_{y}; z \right)} = A{\left(k_{x},k_{y}; 0 \right)} e^{- k_{z} z i}
\end{equation}
</p>

Finally, we note that the disturbance observed at $z = -L$ can be written in terms of the initial angular spectrum by inverse transforming \label{eq:2} using \label{eq:3}, giving:

<p class="math">
\begin{equation}
U\left(x, y , -L\right)=\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} A(k_{x}, k_{y}; 0) e^{k_{z} L} e^{(k_{x} x + k_{y} y) i}   \mathrm{d} k_{x} \mathrm{d} k_{y} 
\end{equation}
</p>


The simulations were done using the [finite-difference time-domain method](https://en.wikipedia.org/wiki/Finite-difference_time-domain_method) (**FDTD**) applied to **Maxwell equations**.


Finally, we comment how the irradiance patterns on the screen $I$ at the microsecond time scale can be approximated using the [Van-Cittert Zernike theorem](https://en.wikipedia.org/wiki/Van_Cittert%E2%80%93Zernike_theorem) and [Fraunhofer approximation](https://en.wikipedia.org/wiki/Fraunhofer_diffraction):

<p class="math">
\begin{equation}
I ∝ \operatorname {sinc}^2{\left( \frac{𝜋 a x}{z \lambda}\right)} \left( 1 + \gamma  \cos{\left(\frac{2𝜋D}{z\lambda}  x\right)}\right) \label{eq:2}
\end{equation}
</p>


where:

<p class="math">
$$D = \text{ distance between the slits}$$

$$a = \text{ slits width}$$

$$\gamma = \text{ degree of spatial coherence}$$  

$$M = \text{ width of the light source}$$

$$z = \text{ distance from the screen to the double slit}$$

$$L = \text{ distance from the light source to the double slit}$$
</p>

As Van-Cittert Zernike theorem states, $\gamma$ can be computed taking the Fourier Transform of the intensity distribution of the light source as follows:

<p class="math">
\begin{equation}
  \gamma = \frac{\int\nolimits_{-\infty}^{\infty}  I(x') e^{i \frac{2 \pi D}{\lambda L} x'} dx'}{\int\nolimits_{-\infty}^{\infty} I(x')  dx'} \label{eq:3}
\end{equation}
</p>

Using an uniform intensity distribution $I_0$ and a width of the light source of $M$:

<p class="math">
$$
\begin{gathered}
I(x') = \begin{cases}
 I_0 & \text{ if } x' < \left|\frac{M}{2}\right| \newline
 0 & \text{ if } x' > \left|\frac{M}{2}\right| \newline 
\end{cases}
\end{gathered}
$$
</p>

And computing the integrals \eqref{eq:3} we finally get the degree of spatial coherence:

<p class="math">
\begin{equation}
\gamma = \operatorname {sinc}{\left(\frac{𝜋 D M}{L \lambda}\right)} \label{eq:4}
\end{equation}
</p>

Although \eqref{eq:2} doesn't produce exact results for the scale of these simulations, you can use it for qualitative predictions. When $\gamma = 1$ the fringes are perfectly visible, and when $\gamma = 0$ they cannot be seen. The further you place the light source from the double slit, the closer the coherence degree will be of $1$ .

To illustrate the equation \eqref{eq:2} we have plotted it for different degrees of coherence:

<div style="text-align:center"><img src="./images/incoherent-double-slit-simulations/Van-Cittert-Zernike-Theorem-coherence.png" alt="Van Cittert-Zernike theorem coherence"/></div>
<br /> 



This experiment is important because it's usually the easiest to set up to measure the degree of coherence of a light source. For an experimental discussion see for example [[2]](#references). I hope these simulations have helped you to visualize how it really works.

## Bibliography
---

<div class="references" id="references"></div>

[1] Goodman J W Statistical Optics sec. 5.1<br /> 

[2] Brett J. Pearson, Natalie Ferris, Ruthie Strauss, Hongyi Li, and David P. Jackson, "Measurements of slit-width effects in Young’s double-slit experiment for a partially-coherent source," OSA Continuum 1, 755-763 (2018)

