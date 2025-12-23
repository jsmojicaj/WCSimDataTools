# WCSim Python DataTools

This repository is a Python Package containing tools to process and read the simulation data for the [WCTE experiment](https://wcte.hyperk.ca/).

## Dependencies
 - python
 - [ROOT](https://root.cern.ch/)
 - [WCSim](https://github.com/WCTE/WCSim) \
        Same ROOT version **must** be used for the compilation of WCSim and the tools provided for this package.
        The WCSim .root simulation files must have been produced with this particular version.

This package is known to work in the following platforms/software versions:
- MacOS Ventura 13.2.1
     - Python 3.10.10
     - ROOT 6.24/06
- Rocky Linux release 8.4 (Green Obsidian)
     - Python 3.7.8
     - ROOT 5.34/38
- CentOS Linux release 7.9.2009
     - Python 3.10.13
     - ROOT 6.28/07

## How To

### **Install (recomended)**
1. Clone this repository (`git clone`)
2. Move to git directory `cd WCSimDataTools`
3. Use a conda environment: `conda env create -f environment.yml -n <env-name>`
This will create a conda environment with the name of your preference `<env-name>`, this contains python 3.10 in your environment. If you want python with another different version 3.x, you may create `conda create -n <env-name> python=3.x numpy`.
After creating the environment, we will have to actívate it with `conda activate <env-name>`
 
4. Setup ROOT such that you can `import ROOT`
4.1 If running `python -c "import ROOT"` doesn’t produce any error, you can proceed to step 5.
4.2 If you cannot run `import ROOT`, you will need to install ROOT according to the version you require (It is necessary to have the conda environment activated during the installation, and which python must point to the Python executable from the conda environment. For the installation, the following CMake configuration is recommended:
```bash
cmake \ 
-DCMAKE_INSTALL_PREFIX=../root_install \ 
-DPYTHON3_EXECUTABLE=$CONDA_PREFIX/bin/python \ 
-Dpyroot=ON \ 
-Droofit=ON \ 
-Dx11=OFF \ 
-Dxrootd=OFF \ 
-Dbuiltin_xrootd=OFF \ 
-Dtbb=OFF \ 
-Dbuiltin_tbb=ON \ 
../root_src
```
**Warning:** If you use this configuration, the ROOT installation will not include a graphical interface. You will need to run `root.exe` instead of `root`.
After installing ROOT, running:
```python
python -c "import ROOT; print(ROOT.__version__)"
```
should print the ROOT version being used by Python.
**Waring:** WCSim must be recompiled using the new ROOT dependency by sourcing
```bash
source /path/to/thisroot.sh
```
It is also recommended to reinstall GEANT4 using the Python interpreter from the conda environment.


5. Install the python package in editable mode `pip install --editable .`\
    Installing in editable mode will allow you to develop package features.
6. You can remove the package using `pip uninstall wcsim-hdf5`

### **.root to .hdf5 file conversion**
After the installation, you can simply run the `root-to-hdf5`. Make sure your conda environment is activated and that ROOT, Geant4 and WCSim are sourced before running `root-to-hdf5`.
for run `root-to-hdf5` requires to provide the path to the WCSim library containing `libWCSimRoot.dylib`

> `root-to-hdf5 --wcsimlib /path/to/WCSim-build/lib /path/to/file.root -o /output/path/` 

### **reading .hdf5 files**

The `wcsimreader` package contains the tools to read the WCSim .hdf5 files. You can explore the data in the file by calling

```python 
from wcsimreader import utils
utils.explore_file(filename)
```

To read the files in a `pandas.DataFrame` instance you can use, for example for reading the table **wcsimT/Tracks**

```python 
from wcsimreader import utils
utils.read_table(filename, "wcsimT/Tracks")
```
### **Using DataFrames**

You can now load your files into pandas DataFrames using the dataframes package, which provides the following functions:


- **wcsimroot**  
- **geo**   
- **pmt**   
- **cherenkovhits** 
- **cherenkovhitstimes**
- **track**
- **trigger**
- **digihits**

An example usage is shown below:

```python
from dataframes import track, digihits
filename= "<pwd/file.h5>"
df_track = track(filename)
df_digi = digihits(filename)

print(df_track.head())
print(df_digi.head())
```
You can also use import dataframes as d and call the functions as d.trigger(filename). 

## To Do
- [ ] Add Pi0 and NCapture data
- [ ] Add tests
- [ ] Implement `conda` package
- [ ] Implement event filtering readers
- [ ] Implement event filtering writers
