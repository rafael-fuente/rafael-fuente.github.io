Title: Visual Explanation of the Van-Cittert Zernike Theorem - The Double Slit Experiment with Incoherent and Coherent Light
Date: 2020-10-24 23:20
Author: Rafael de la Fuente
Tags: Optics, Maxwell Equations, FDTD, Coherence

<!-- 16:9 aspect ratio -->
<div class="embed-responsive embed-responsive-16by9">
<iframe class="embed-responsive-item" src="https://www.youtube.com/embed/5cyzdsd6AOs?vq=hd1440" alt="Simulation of the Double Slit Experiment with Incoherent and Coherent Light" allowfullscreen></iframe>
</div>


<br /> 

What happens when the **double slit experiment** is performed with **incoherent light** (for example with a light bulb)? And how it differs when it is performed with **coherent light**  (for example with a laser)?

The main idea of these simulations is to answer this question, simulating the light propagating through the double slit at different time scales: (femtoseconds, picoseconds and microseconds) to show their differences.

The topics shown in this video are discussed in Statistical Optics Books and usually treated with the **Van Cittert–Zernike theorem** (we'll discuss it later), but what happens it's that they are a bit mathematically obscure.

I thought that a visualization of the topic could be helpful, but I found almost zero of them both in the internet and in the literature, so this is the reason I made these simulations, to help to better understand this important topic in Optics ([Coherence](https://en.wikipedia.org/wiki/Coherence_(physics))).


## How I made the simulations:
---

The simulations were done using the [finite-difference time-domain method](https://en.wikipedia.org/wiki/Finite-difference_time-domain_method) (**FDTD**) applied to **Maxwell equations**.

The incoherent light is simulated computing the field created by oscillating dipoles sources with random phases and wavelengths and randomly placed inside the light source dimensions (a rectangle). The dipoles represent the electronic transitions of the excited atoms of the light source.

The microseconds and picoseconds simulations are obtained when the field is averaged over that period of time.

You can find the **source code** of the simulations in their [GitHub repository](https://github.com/rafael-fuente/Incoherent-Light-Simulation/tree/master/double_slit_simulations)

You can change the parameters of the simulations just typing the values you want in the scripts that are indicated.

While the femtoseconds simulations only took a few minutes to be completed, the microsecond simulations [2:28](https://www.youtube.com/watch?v=5cyzdsd6AOs&t=148s) took hundreds of hours to be completed in a personal computer!

In the femtoseconds scale you can slow down the video to x0.25 in youtube settings if you find the flickering annoying. Also the video is uploaded at [HD 1440p](https://www.youtube.com/watch?v=5cyzdsd6AOs?vq=hd1440)
 to avoid the artifacts that youtube video encoder creates with the waves at lower resolutions. You can see all fine details of the waves if you watch the video at this resolution.


## Why does the interference patterns fluctuate on the picoseconds time scale?
---
<div class="object-and-details">
<div style="text-align:left"><img src="./images/incoherent-double-slit-simulations/simulation-incoherent-picoseconds.jpg" alt="simulation of the double slit experiment with incoherent light picoseconds" loading="lazy"/></div>
  <details>
    <!-- added role=button to summary to resolve iOS funkiness -->
    <summary role="button" aria-label="static image"></summary>
    <div class="object-and-details1">
      <img src="./images/incoherent-double-slit-simulations/simulation-incoherent-picoseconds.gif" alt="simulation of the double slit experiment with incoherent light picoseconds" loading="lazy">
    </div>
  </details>
</div>
<br /> 

Interference patterns fluctuate on picoseconds time scale because this is the order of magnitude of the [coherence time](https://en.wikipedia.org/wiki/Coherence_time) of the source. This is the minimum time to make the electric field change considerably [[1]](#references).

\begin{equation}
\tau_{coh} \approx \frac{λ^2}{c Δλ}  \label{eq:1}
\end{equation}

where:

$$ Δλ = \text{bandwidth of the light source}$$

$$ λ = \text{center wavelength}$$

$$ c = \text{speed of light}$$


In the simulation was used a wavelength of $λ = 650 \text{ nm}$ and a bandwidth of $Δλ = 1 \text{ nm}$. Plugging these values in the formula \eqref{eq:1} we get a coherence time of:

$$\tau_{coh} \approx 1.4 \text{ picoseconds} $$

You can see that a very narrow bandwidth $Δλ = 1 \text{ nm}$ is enough to make interferences fluctuate very fast. $λ = 650 \text{ nm}$ correspond to red light, and the narrow bandwidth makes almost no difference in color to the human eye.

When the intensity is averaged over a few microseconds no fluctuations can be seen. This is the reason that although the wave-like behaviour of light, we don't usually see the interferences.

## More explanations:
---
<div class="object-and-details">
<div style="text-align:left"><img src="./images/incoherent-double-slit-simulations/simulation-incoherent-femtoseconds.jpg" alt="simulation of the double slit experiment with incoherent light femtoseconds" loading="lazy"/></div>
  <details>
    <!-- added role=button to summary to resolve iOS funkiness -->
    <summary role="button" aria-label="static image"></summary>
    <div class="object-and-details1">
      <img src="./images/incoherent-double-slit-simulations/simulation-incoherent-femtoseconds.gif" alt="simulation of the double slit experiment with incoherent light femtoseconds" loading="lazy">
    </div>
  </details>
</div>

+ The blinking on the femtosecond time scale is because when the light is reflected on the double slit wall is due to a standing wave formed by interference from the incident and reflected waves, with an oscillation frequency equal to the frequency of the wave.

<div class="object-and-details">
<div style="text-align:left"><img src="./images/incoherent-double-slit-simulations/simulation-incoherent-microseconds.jpg" alt="simulation of the double slit experiment with incoherent light microseconds" loading="lazy"/></div>
  <details>
    <!-- added role=button to summary to resolve iOS funkiness -->
    <summary role="button" aria-label="static image"></summary>
    <div class="object-and-details1">
      <img src="./images/incoherent-double-slit-simulations/simulation-incoherent-microseconds.gif" alt="simulation of the double slit experiment with incoherent light microseconds" loading="lazy">
    </div>
  </details>
</div>
<br /> 

+ In microseconds time scale [1:20](https://www.youtube.com/watch?v=5cyzdsd6AOs&t=80s) and any longer time scale, no incoherent light interference pattern should be visible as we observe in most of our daily life. But a stationary wave is still visible in the microseconds time scale near the double slit wall. However because its size is very small , you won't notice it at macroscopic scale and instead you will see a uniform pattern. (notice that the space scale of the simulations are 60 x 30 μm)

## The Van-Cittert Zernike Theorem
---

Finally, we comment how the irradiance patterns on the screen $I$ at the microsecond time scale can be approximated using the [Van-Cittert Zernike theorem](https://en.wikipedia.org/wiki/Van_Cittert%E2%80%93Zernike_theorem) and [Fraunhofer approximation](https://en.wikipedia.org/wiki/Fraunhofer_diffraction):

\begin{equation}
I ∝ \operatorname {sinc}^2{\left( \frac{𝜋 a x}{z λ}\right)} \left( 1 + γ  \cos{\left(\frac{2𝜋D}{zλ}  x\right)}\right) \label{eq:2}
\end{equation}

where:


$$D = \text{ distance between the slits}$$

$$a = \text{ slits width}$$

$$γ = \text{ degree of spatial coherence}$$  

$$M = \text{ width of the light source}$$

$$z = \text{ distance from the screen to the double slit}$$

$$L = \text{ distance from the light source to the double slit}$$

<br /> 

As Van-Cittert Zernike theorem states, $γ$ can be computed taking the Fourier Transform of the intensity distribution of the light source as follows:

\begin{equation}
  γ = \frac{\int\nolimits_{-\infty}^{\infty}  I(x') e^{i \frac{2 \pi D}{\lambda L} x'} dx'}{\int\nolimits_{-\infty}^{\infty} I(x')  dx'} \label{eq:3}
\end{equation}

Using an uniform intensity distribution $I_0$ and a width of the light source of $M$:

$$
\begin{gathered}
I(x') = \begin{cases}
 I_0 & \text{ if } x' < \left|\frac{M}{2}\right| \newline
 0 & \text{ if } x' > \left|\frac{M}{2}\right| \newline 
\end{cases}
\end{gathered}
$$

And computing the integrals \eqref{eq:3} we finally get the degree of spatial coherence:

\begin{equation}
γ = \operatorname {sinc}{\left(\frac{𝜋 D M}{L λ}\right)} \label{eq:4}
\end{equation}

Although \eqref{eq:2} doesn't produce exact results for the scale of these simulations, you can use it for qualitative predictions. When $γ = 1$ the fringes are perfectly visible, and when $γ = 0$ they cannot be seen. The further you place the light source from the double slit, the closer the coherence degree will be of $1$ .

To illustrate the equation \eqref{eq:2} we have plotted it for different degrees of coherence:

<div style="text-align:center"><img src="./images/incoherent-double-slit-simulations/Van-Cittert-Zernike-Theorem-coherence.png" alt="simulation of the double slit experiment with incoherent light microseconds"/></div>
<br /> 



This experiment is important because it's usually the easiest to set up to measure the degree of coherence of a light source. For an experimental discussion see for example [[2]](#references). I hope these simulations have helped you to visualize how it really works.

## Bibliography
---

<div class="references" id="references"></div>

[1] Goodman J W Statistical Optics sec. 5.1<br /> 

[2] Brett J. Pearson, Natalie Ferris, Ruthie Strauss, Hongyi Li, and David P. Jackson, "Measurements of slit-width effects in Young’s double-slit experiment for a partially-coherent source," OSA Continuum 1, 755-763 (2018)

