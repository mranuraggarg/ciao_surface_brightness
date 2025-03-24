"""This script extracts the radial profile of a given astronomical source, fits a 
beta plus Gaussian model to the surface brightness profile, and saves the results 
as both plots and a FITS file.
"""

import os

from ciao_contrib.runtool import dmextract
from pycrates import read_file
import matplotlib.pyplot as plt
from sherpa.astro import ui


output_file = "surface_brightness.fits"

# Only run dmextract if the output file does not already exist
if not os.path.exists(output_file):
    dmextract.punlearn()
    dmextract.infile = "data/repro/acisf01653_repro_evt2.fits[bin sky=@annuli.reg]"
    dmextract.outfile = output_file
    dmextract.opt = "generic"
    dmextract()
else:
    print(f"✅ Skipping dmextract: {output_file} already exists.")

# Load the extracted radial profile
tab = read_file(output_file)
xx = tab.get_column("rmid").values
yy = tab.get_column("sur_bri").values
ye = tab.get_column("sur_bri_err").values

# Plot raw profile
plt.errorbar(xx, yy, yerr=ye, marker="o")
plt.xscale("log")
plt.yscale("log")
plt.xlabel("R_MID (pixel)")
plt.ylabel("SUR_BRI (photons/cm**2/pixel**2/s)")
plt.title('G21.5-0.9 [Chip S3, T=120, Offsets=-1,0,1]')
plt.savefig("graphs/surface_brightness.png", dpi=600, bbox_inches='tight')


# Load data into Sherpa
ui.load_data(1, output_file, 3, ["RMID", "SUR_BRI", "SUR_BRI_ERR"])

# Define models
beta_model1 = ui.normbeta1d("beta_model1")
gauss_model = ui.gauss1d("gauss_model")
ui.set_source(beta_model1 + gauss_model)

# Set Gaussian Model Parameters
gauss_model.pos = 230
gauss_model.fwhm = 50
gauss_model.ampl = 20

# Beta Model Parameters
beta_model1.pos = 230
beta_model1.width = 100
beta_model1.index = 0.6
beta_model1.ampl = 150


# Fit the model
ui.fit()
ui.covar()  # Compute parameter uncertainties


# Plot residuals
ui.plot_fit_resid()
plt.savefig("graphs/beta_gauss_resid.png", dpi=600, bbox_inches='tight')


# Plot the fitted model
plt.figure(figsize=(6, 5))
plt.title("Beta + Gaussian Model Fit: Surface Brightness Profile")
ui.plot_fit(xlog=True, ylog=True)
plt.xlabel("R_MID (pixel)")
plt.ylabel("SUR_BRI (photons/cm**2/pixel**2/s)")
plt.savefig("graphs/beta_gauss_fit.png", dpi=600, bbox_inches='tight')
