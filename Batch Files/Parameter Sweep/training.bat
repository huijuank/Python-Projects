@echo Activating python environment...
@Call "C:/Users/<user>/Anaconda3/Scripts/activate.bat"
@call conda activate<envname>
@echo Activating <envname> environment...
@echo Starting parameter sweep for ML model
@python sweepParameter.py
@echo Training completed.
@pause
