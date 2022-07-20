Title: Visualizing the Concept of Spatial Coherence - The Double Slit Experiment with Incoherent and Coherent Light
Description: What happens when the double slit experiment is performed with incoherent light (for example with a light bulb)? And how it differs when it is performed with coherent light (for example with a laser)?
Date: 2020-10-24 23:20
Author: Rafael de la Fuente
Tags: Optics, Maxwell Equations, FDTD, Coherence
Image: https://rafael-fuente.github.io/images/incoherent-double-slit-simulations/visualization-of-the-Van-Cittert-Zernike-theorem.jpg
mathjax3: True

<!-- 16:9 aspect ratio -->
<div class="embed-responsive embed-responsive-16by9">
<iframe class="embed-responsive-item" src="https://www.youtube.com/embed/5cyzdsd6AOs?vq=hd1440" alt="Simulation of the Double Slit Experiment with Incoherent and Coherent Light" allowfullscreen></iframe>
</div>


<br /> 

What happens when the double slit experiment is performed with spatially incoherent light (for example, with a light bulb)? And how does it differ when it is performed with coherent light  (for example, with a laser)?

The surface of a spatially incoherent light source can be represented by a collection of randomly emitting electric dipoles, for example, the atoms experimenting radiative transitions in the filament of a light bulb. The light source may actually be near monochromatic like a [low pressure sodium discharge lamp](http://hyperphysics.phy-astr.gsu.edu/hbase/quantum/sodium.html) (dominated by the bright doublet known as the Sodium D-lines at 588.99 and 589.59 nanometers), but ultimately the field exiting the incoherent light source involves a small spectrum of wavelengths and randomly changing phase in time. Unlike the interference features produced by a laser light source, that can be seen, for example as a [speckle pattern](https://en.wikipedia.org/wiki/Speckle_(interference)), the interferences produced by incoherent source, are not stationary but change rapidly, so they are "averaged out" by a sensor, like an human eye responding to the time-averaged squared magnitude of the field.  

I thought that a visualization of the topic could be helpful, but I found almost zero of them in the literature. The main idea of this video is to illustrate and show the subtle details of the concept of coherence by means of three simulations of the light propagating through the double slit at different time scales: (femtoseconds, picoseconds, and microseconds) to show their differences.

The experiment demostrated in this video is a key result in statistical optics. It can also be mathematically treated with the **Van Cittert–Zernike theorem** and the concept of **mutual intensity**, that we'll discuss in the last two sections.


## How I made the simulations:
---

The simulations were done using the [finite-difference time-domain method](https://en.wikipedia.org/wiki/Finite-difference_time-domain_method) (**FDTD**) applied to **Maxwell equations**.

The incoherent light is simulated by computing the field created by oscillating dipole sources with random phases and wavelengths and randomly placed inside the light source dimensions (a rectangle). The dipoles represent the electronic transitions of the excited atoms of the light source.

The microseconds and picoseconds simulations are obtained when the field is averaged over that period of time.

You can find the **source code** of the simulations in their [GitHub repository](https://github.com/rafael-fuente/Incoherent-Light-Simulation/tree/master/double_slit_simulations)

You can change the parameters of the simulations just typing the values you want in the scripts that are indicated.

While the femtoseconds simulations only took a few minutes to be completed, the microsecond simulations [2:28](https://www.youtube.com/watch?v=5cyzdsd6AOs&t=148s) took hundreds of hours to be completed in a personal computer!

In the femtoseconds scale you can slow down the video to x0.25 in youtube settings if you find the flickering annoying. Also the video is uploaded at [HD 1440p](https://www.youtube.com/watch?v=5cyzdsd6AOs?vq=hd1440)
 to avoid the artifacts that youtube video encoder creates with the waves at lower resolutions. You can see all fine details of the waves if you watch the video at this resolution.


## Why do the interference patterns fluctuate on the picoseconds time scale?
---
<div class="object-and-details">
<div style="text-align:left"><img src="./images/incoherent-double-slit-simulations/simulation-incoherent-picoseconds.jpg" alt="simulation of the double slit experiment with incoherent light at picoseconds" loading="lazy"/></div>
  <details>
    <!-- added role=button to summary to resolve iOS funkiness -->
    <summary role="button" aria-label="static image"></summary>
    <div class="object-and-details1">
      <img src="./images/incoherent-double-slit-simulations/simulation-incoherent-picoseconds.gif" alt="simulation of the double slit experiment with incoherent light at picoseconds" loading="lazy">
    </div>
  </details>
</div>
<br /> 

Interference patterns fluctuate on picoseconds time scale because this is the order of magnitude of the [coherence time](https://en.wikipedia.org/wiki/Coherence_time) of the source. This is the minimum time to make the electric field change considerably [[1]](#references).

<p class="math">
\begin{equation}
\tau_{coh} \approx \frac{ \lambda ^2}{c \Delta \lambda}  \label{eq:1}
\end{equation}
</p>

where:

<p class="math">
$$ \Delta \lambda = \text{bandwidth of the light source}$$

$$ \lambda = \text{center wavelength}$$

$$ c = \text{speed of light}$$
</p>

In the simulation was used a wavelength of $ \lambda = 650 \text{ nm}$ and a bandwidth of $\Delta \lambda = 1 \text{ nm}$. Plugging these values in the formula \eqref{eq:1} we get a coherence time of:

<p class="math">
$$\tau_{coh} \approx 1.4 \text{ picoseconds} $$
</p>

You can see that a very narrow bandwidth $ \Delta \lambda  = 1 \text{ nm}$ is enough to make interferences fluctuate very fast. $ \lambda  = 650 \text{ nm}$ correspond to red light, and the narrow bandwidth makes almost no difference in color to the human eye.

When the intensity is averaged over a few microseconds no fluctuations can be seen. This is the reason that although the wave-like behaviour of light, we don't usually see the interferences.

## Further explanations:
---
<div class="object-and-details">
<div style="text-align:left"><img src="./images/incoherent-double-slit-simulations/simulation-incoherent-femtoseconds.jpg" alt="simulation of the double slit experiment with incoherent light at femtoseconds" loading="lazy"/></div>
  <details>
    <!-- added role=button to summary to resolve iOS funkiness -->
    <summary role="button" aria-label="static image"></summary>
    <div class="object-and-details1">
      <img src="./images/incoherent-double-slit-simulations/simulation-incoherent-femtoseconds.gif" alt="simulation of the double slit experiment with incoherent light at femtoseconds" loading="lazy">
    </div>
  </details>
</div>
<br /> 
<li>The blinking on the femtosecond time scale is because when the light is reflected on the double slit wall is due to a standing wave formed by interference from the incident and reflected waves, with an oscillation frequency equal to the frequency of the wave.</li>
<br /> 
<div class="object-and-details">
<div style="text-align:left"><img src="./images/incoherent-double-slit-simulations/simulation-incoherent-microseconds.jpg" alt="simulation of the double slit experiment with incoherent light at microseconds" loading="lazy"/></div>
  <details>
    <!-- added role=button to summary to resolve iOS funkiness -->
    <summary role="button" aria-label="static image"></summary>
    <div class="object-and-details1">
      <img src="./images/incoherent-double-slit-simulations/simulation-incoherent-microseconds.gif" alt="simulation of the double slit experiment with incoherent light at microseconds" loading="lazy">
    </div>
  </details>
</div>
<br /> 

+ In microseconds time scale [1:20](https://www.youtube.com/watch?v=5cyzdsd6AOs&t=80s) and any longer time scale, no incoherent light interference pattern should be visible as we observe in most of our daily life. But a stationary wave is still visible in the microseconds time scale near the double slit wall. However because its size is very small , you won't notice it at macroscopic scale and instead you will see a uniform pattern. (notice that the space scale of the simulations are 60 x 30 μm)

## Mathematical description of the spatial coherence
---

For incoherent light, the time variations in field amplitude are statistical in nature, and only statistical concepts can provide a satisfactory description of the field. The theory of coherence is a vast topic that will not discuss here. The reader interested in a complete treatment can consult [[1]](#references) [[3]](#references). Instead, here, we'll be limited to defining the basic concepts.

Consider the electric field $E(r, t)$ evaluated in two different points $r_1$ and $r_2$.
We define the mutual coherence function $\Gamma(r_1, r_2, \tau)$ between these two points as the time-averaged cross-correlation between the electric fields:

<p class="math">
\begin{equation}
\Gamma(r_1, r_2, \tau)= \left\langle E(r_1, t) E^{*}(r_2, t+\tau)\right\rangle = \lim _{T \rightarrow \infty} \frac{1}{2 T} \int_{-T}^{T} E(r_1,t) E^{*}(r_2,t-\tau) d t
\end{equation}
</p>

The mutual intensity is a measure of the spatial coherence of the light at the two object points, where $\tau$ is a time delay associated with the propagation. When we are observing spatially incoherent sources we should expect the mutual coherence function to be relatively small between the two observation points that are near the source, because the sources will interfere destructively as well as constructively. <br /> 

Far away from the sources, as happens when we measure the mutual coherence from a distant star, the mutual coherence function is relatively large because the sum of the observed fields is almost the same at any two points. Perfectly spatially incoherent light refers to the situation where the complex field phasors from the radiating point sources are stochastically independent, where there is no correlation between the field phasors at different points or times, leading to a mutual coherence near zero. <br />  

Furthermore, the mutual intensity it's also interesting, because beyond measuring the spatial coherence can also be used to compute the intensity along a propagation plane[[2]](#references). 

We also define the normalized coherence, that we'll use in the next section as:

<p class="math">
\begin{equation}
\gamma(\tau)=\frac{\Gamma(\tau)}{\sqrt{\Gamma(0) \Gamma(0)}}
\end{equation}
</p>

Which holds the useful propierty:

<p class="math">
\begin{equation}
0 \leq\left|\gamma(\tau)\right| \leq 1
\end{equation}
</p>

## The Van-Cittert Zernike Theorem
---

The [Van-Cittert Zernike theorem](https://en.wikipedia.org/wiki/Van_Cittert%E2%80%93Zernike_theorem), deriven originally by [[4]](#references) [[5]](#references), provides a simple way to compute the coherence $\gamma$ for the double slit experiment, by taking the Fourier transform of the intensity distribution of the light source as follows:

<p class="math">
\begin{equation}
  \gamma = \frac{\int\nolimits_{-\infty}^{\infty}  I(x') e^{i \frac{2 \pi D}{\lambda L} x'} dx'}{\int\nolimits_{-\infty}^{\infty} I(x')  dx'} \label{eq:3}
\end{equation}
</p>

Furthermore, by also using the [Fraunhofer approximation](https://en.wikipedia.org/wiki/Fraunhofer_diffraction) the irradiance patterns on the screen $I$ at the microsecond time scale can be approximated by:

<p class="math">
\begin{equation}
I ∝ \operatorname {sinc}^2{\left( \frac{𝜋 a x}{z \lambda}\right)} \left( 1 + \gamma  \cos{\left(\frac{2𝜋D}{z\lambda}  x\right)}\right) \label{eq:2}
\end{equation}
</p>

where:

<p class="math">
$$D = \text{ distance between the slits}$$

$$a = \text{ slits width}$$

$$M = \text{ width of the light source}$$

$$z = \text{ distance from the screen to the double slit}$$

$$L = \text{ distance from the light source to the double slit}$$
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



This experiment is important because it's usually the easiest to set up to measure the degree of coherence of a light source. For an experimental discussion see for example [[6]](#references). I hope these simulations have helped you to visualize how it really works.

## Bibliography
---

<div class="references" id="references"></div>

[1] Goodman J W Statistical Optics sec. 5.1 'Spatial Coherence'<br /> 

[2] Goodman J W Statistical Optics sec. 5.4 'Propagation of the mutual coherence'<br /> 

[3] M.J. Beran and G.B. Parrent, Jr. Theory of Partial Coherence. Prentice-Hall, Inc., Englewood Cliffs, NJ, 1964.<br /> 

[4] P.H. van Cittert (1934). "Die Wahrscheinliche Schwingungsverteilung in Einer von Einer Lichtquelle Direkt Oder Mittels Einer Linse Beleuchteten Ebene". Physica. 1 (1–6): 201–210.<br /> 

[5] F. Zernike (1938). "The concept of degree of coherence and its application to optical problems". Physica. 5 (8): 785–795<br /> 

[6] Brett J. Pearson, Natalie Ferris, Ruthie Strauss, Hongyi Li, and David P. Jackson, "Measurements of slit-width effects in Young’s double-slit experiment for a partially-coherent source," OSA Continuum 1, 755-763 (2018)<br /> 

