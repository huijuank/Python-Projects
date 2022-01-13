@call "C:/Users/<username>/Anaconda3/Scripts/activate.bat"
@call conda env remove -n <envname>
@call conda create -n <envname> python=3.8 spyder -y
@call conda activate <envname>
@call conda install pandas -y
@call conda install opencv -y
@call conda install matplotlib -y
@call conda install pillow -y
@call conda install -c conda-forge pyvisa -y
@call conda install -c conda-forge librosa -y
@call conda install -c conda-forge pysimplegui -y
@echo Installation completed.
pause
