from pathlib import Path

def add_image_sitemap_from_links(img_sitemaps):

	for link, sitemap_string in img_sitemaps.items():

		f= open("sitemap.xml", "rt")
		sitemap = f.read()

		article_url = link
		st = "<loc>"+article_url+"</loc>"
		l = len(st)
		i = sitemap.index(st) + l + 104
		edited_sitemap = sitemap[:i] + sitemap_string + "\n" + sitemap[i:]
		f.close()


		f= open("sitemap.xml", "w")
		f.write(edited_sitemap)
		f.close()

def load_sitemap_string(name):
	f= open(name, "rt")
	img_sitemap_string = f.read()
	f.close()
	return img_sitemap_string

#img_sitemaps = {"https://rafael-fuente.github.io/visual-explanation-of-the-van-cittert-zernike-theorem-the-double-slit-experiment-with-incoherent-and-coherent-light.html": load_sitemap_string("incoherent-double-slit-simulations.txt")}
img_sitemaps = {}
img_sitemaps["https://rafael-fuente.github.io/visual-explanation-of-the-van-cittert-zernike-theorem-the-double-slit-experiment-with-incoherent-and-coherent-light.html"] = load_sitemap_string(Path("images/incoherent-double-slit-simulations/sitemap.txt"))
img_sitemaps["https://rafael-fuente.github.io/solving-the-diffraction-integral-with-the-fast-fourier-transform-fft-and-python.html"] = load_sitemap_string(Path("images/fft-diffraction-integral/sitemap.txt"))
img_sitemaps["https://rafael-fuente.github.io/simulating-diffraction-patterns-with-the-angular-spectrum-method-and-python.html"] = load_sitemap_string(Path("images/angular-spectral-method/sitemap.txt"))
img_sitemaps["https://rafael-fuente.github.io/simulating-light-diffraction-with-lenses-visualizing-fourier-optics.html"] = load_sitemap_string(Path("images/visualizing-fourier-optics/sitemap.txt"))

add_image_sitemap_from_links(img_sitemaps)