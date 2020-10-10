Title: Solving the Diffraction Integral with the Fast Fourier Transform (FFT) and Python
date: 2019-10-08 18:50
Author: Rafael de la Fuente
Tags: Schrödinger Equation, Diffraction, Double Slit Experiment, FFT

In this project we will show how to numerically computing the Diffraction Fresnel Integral with the Fast Fourier Transform (FFT). We'll implement the method with Python and we will apply it to the study of the diffraction patterns obtained by the particle beams in the double slit experiment, showing the dependence of the phenomenon with respect to the separation of the slits.

## Theoretical foundation
---

Consider a particle traveling with a well-defined momentum: 

\begin{equation}
 \mathbf {p} = p_ {0} \mathbf {u_ {z}} \quad  \text{  in the region  }\quad  z < 0
\end{equation}

Its wave function is:

\begin{equation}
\Psi{(\mathbf{r},t)} = \Psi_{0} e^{i (k z - w t)},\quad \text{   with   } \quad
\begin{gathered}
\begin{cases}
 k = \frac{p_{0}}{\hbar} \newline
 w = \frac{p_{0}^{2}}{2 m \hbar} \newline
\end{cases}
\end{gathered}
\end{equation}

A plate is now placed at $ z = 0 $ with an opening $ S '$. According to the Huygen-Fresnel principle, the wave in the plane $ z = L $ it's given by the Fresnel integral:

\begin{equation}
  \Psi{(\mathbf{r},t)} = C \int\nolimits_{S'}^{} \frac{e^{i k \left|{r - r'}\right|}}{\left|{r - r'}\right|} cos{\theta}\,  d^{2}r',
\quad \text{   with   } \quad  \hspace{2mm}
  C =  \frac{k \Psi_{0} e^{- i t w}}{2 \pi i}
\end{equation}

This approximation is valid if $ L >> \lambda $

Next we are going to simplify the integral using the Fresnel approximation.
This consists of considering $ \theta \approx 0 $ and using the approximation in the exponential:

\begin{equation}
|{r - r'}| \approx z +\frac{(x - x')^{2} + (y - y')^{2}}{2 z}
\end{equation}

Which it is valid if $((x - x')^{2} + (y - y')^{2})^{2} << 8 \lambda  L^{3}$

In the case of the denominator we do:

\begin{equation}
|{r - r'}| \approx L
\end{equation}

And the Fresnel integral becomes:

\begin{equation}
\begin{gathered}
\Psi{(\mathbf{r},t)} = R \int\nolimits_{-\infty}^{\infty}\int\nolimits_{-\infty}^{\infty} f{(x', y')}  e^{\frac{i k}{2 z} ({x'}^{2} + {y'}^{2})} e^{ -\frac{i k x}{z}x' -\frac{i k y}{z}y'} \,  dx'dy',
  \hspace{3mm} with \hspace{3mm}
  R =  \frac{k \Psi_{0} e^{ i(k z - t w)}}{2 \pi i z} e^{ i k\frac{x^{2} + y^{2}}{2 z}} \newline
f(x', y') = \begin{cases}
 1 & \text{ if } (x' , y') \in S'\newline
 0 & \text{ if } (x' , y') \notin S'\newline 
\end{cases}
\end{gathered}
\end{equation}

Finally we observe that this integral can be expressed as a Fourier transform:

\begin{equation}
\begin{gathered}
 \Psi{(\mathbf{r},t)} =R   \hspace{2mm}\mathcal{F}\{f{(x', y')}  e^{\frac{i k}{2 z} ({x'}^{2} + {y'}^{2})}\} \newline
\mathcal{F} \{f{(x', y')}  e^{\frac{i k}{2 z} ({x'}^{2} + {y'}^{2})}\} = \int\nolimits_{-\infty}^{\infty}\int\nolimits_{-\infty}^{\infty} f{(x', y')}  e^{\frac{i k}{2 z} ({x'}^{2} + {y'}^{2})} e^{ -\frac{i k x}{z}x' -\frac{i k y}{z}y'} \,  dx'dy'
\end{gathered}
\end{equation}


To estimate the diffraction pattern, we use the region $(x', y') \in [-L_{x},L_{x}] \times [-L_{y},L_{y}]$ dividing each axis in $N_{x}$ and $N_{y}$ points respectively:

<p>\begin{equation}
\begin{gathered}
x_{n_{x}}^{\prime}= \left\{ -L_{x}+n_{x} \frac{2 L_{x}}{N_{x}}: 0 \leq n_{x} \leq N_{x}-1 \right\} \newline
y_{n_{y}}^{\prime}= \left\{ -L_{y}+n_{y} \frac{2 L_{y}}{N_{y}}: 0 \leq n_{y} \leq N_{y}-1 \right\}
\end{gathered}
\end{equation}</p>

And we define the Discrete Fourier Transform (DFT) of the set of points, which we will compute efficiently using the Fast Fourier Transform (FFT) algorithm:

<p>\begin{equation}
\begin{gathered}
  G(\mu_{x}, \mu_{y}) = \sum _{n_{x}=0}^{N_{x}-1}\sum _{n_{y}=0}^{N_{y}-1}g(x'_{n_{x}},y'_{n_{y}})e^{-{i2\pi \mu_{x}{\frac {n_{x}}{N_{x}}} -{i2\pi \mu_{y}{\frac {n_{y}}{N_{y}}}}}},
\end{gathered}
\end{equation}</p>

With the points of the screen located at $z = L$:

\begin{equation}
\begin{gathered}
x_{\mu_{x}}  = \frac{(\mu_{x} - N_{x}/2) L \lambda}{2 L_{x}} \newline
y_{\mu_{y}}  =\frac{(\mu_{y} - N_{y}/2) L \lambda}{2 L_{y}}
\end{gathered}
\end{equation}

Post in progress 