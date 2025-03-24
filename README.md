# Surface Brightness Profiling of A2163 using CIAO & Sherpa

This repository contains a Python-based analysis pipeline to:
- Preprocess Chandra data (CIAO)
- Extract surface brightness profiles (`dmextract`)
- Fit models using Sherpa (normalized β + Gaussian)
- Generate plots and LaTeX reports

## 🔧 Requirements
- CIAO 4.17 with Sherpa
- Python 3.10+
- Matplotlib, pycrates, ciao-contrib

## 🚀 Running the Pipeline

1. Download Chandra data for A2163 (OBSID 1653) via:
   https://cda.harvard.edu/chaser/
2. Place your event files in a `data/` folder.
3. Edit region files as needed (in `regions/`)
4. Run:

```bash
python scripts/extract_radial_profile.py
```

## 📄 Output
- Fitted parameters and uncertainty
- Publication-quality plots (log scale)
- LaTeX report (in latex_report/)

---

## 🔐 License Information

This repository is licensed under the **GNU General Public License v3.0 (GPL-3.0)** to comply with the licensing terms of key scientific packages it depends on.

### Project License

This project is licensed under the **GNU General Public License v3.0** (GPL-3.0).  
See the [LICENSE](./LICENSE) file for details.

> Zenodo DOI: [10.5281/zenodo.15074479](https://doi.org/10.5281/zenodo.15074479)

- The core analysis is built around [Sherpa](https://github.com/sherpa/sherpa), which is licensed under **GPL-3.0**.
- As a result, this repository and all associated scripts are distributed under the same license.

### External Tools & Licensing

| Tool         | License Type           | Notes                                                                 |
|--------------|------------------------|-----------------------------------------------------------------------|
| **Sherpa**   | GPL-3.0                | Requires this project to be GPL-3.0                                   |
| **CIAO**     | CXC Non-Commercial     | Free for scientific use; redistribution prohibited                    |
| **XSPEC**    | HEASARC Non-Commercial | Free for scientific use; redistribution prohibited                    |

> ⚠️ This repository does **not** include any CIAO or XSPEC binaries or source code. Users must install them separately.

- [CIAO Installation Guide](https://cxc.harvard.edu/ciao/download/)
- [XSPEC Installation Guide](https://heasarc.gsfc.nasa.gov/xanadu/xspec/)

## 🔒 Disclaimer

No Chandra data is included here. Please retrieve it from the public archive.

## 📘 Citation

If you use this repository, please cite it via:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15074479.svg)](https://doi.org/10.5281/zenodo.15074479)

Garg, A. (2025). Surface Brightness Profile Extraction for A2163 using CIAO and Python (v1.0.0). Zenodo. https://doi.org/10.5281/zenodo.15074479
