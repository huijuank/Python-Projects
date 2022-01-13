# Python-Projects

In this repo, I collated some of the past Python projects I have done.

## OpenCV

### Project: Internship

#### `overlayCameraHeatmap.py`
##### _Libraries used: OpenCV on Python_

In this code, I created a class to implement the overlay of a camera image and a heatmap graph. 

This is useful in a case whereby one have collated experimental data of a specific device, and would like to have a better visualisation of the data with respect to the device. By overlaying the heatmap graph onto a camera image of the device, one can directly infer which parts of the device correlates to specific parts of the heatmap graph.

## Matplotlib

### Project: Internship

#### `plotLogNormalize.py`
##### _Libraries used: Matplotlib, Numpy, PySimpleGUI_

In this code, I created a function which loads CSV files and plot the data. There is the option to:
1. normalize the data
2. convert the data to logarithmic scale

This is useful for processing of given data to assist in data analysis works.

There is a line of code which is has a command for some output in PySimpleGUI, as this is one of the post processing features which I have added on to an application used in my internship. 

## Batch Files

### Project: Internship

#### `installer.bat`
This is an example of how to implement batch files on Windows to automate the creation of a virtual environment on Anaconda, and install the required libraries.

#### `runPythonFile.bat`
This is an example of how to implement batch files on Windows to automate the running of a python file.

#### Parameter Sweep
This is an example of how to automate a paramter sweep for machine learning training. The folder consists 4 files.
1. sweepParameter.py: allows you to define the paramters to sweep.
2. sweepParameter.bat: called by sweepParameter.py to run 1 iteration of training for a given set of parameter values.
3. baseline.yaml: saves the list of paramters and their respective values for the training.
4. training.bat: the file to run the automatic paramter sweep after defining the rangle of parameter values to sweep in sweepParameter.py.
