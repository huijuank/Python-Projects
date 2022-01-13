@call "C:/Users/<user>/Anaconda3/Scripts/activate.bat"
@call conda activate <envname>
@echo Run training.
@python 00_train.py -d
@echo Run testing.
@python 01_test.py -d
