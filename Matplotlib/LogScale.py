import matplotlib.pyplot as plt
import numpy as np
import PySimpleGUI as sg

def plotData(files,arrays,log,logval,norm):
    #For plotting of loaded csv data
    for index,array in enumerate(arrays):
        plt.imshow(array,interpolation='bicubic',origin='lower',cmap='jet')
        plt.xlabel('Steps')
        plt.ylabel('Steps')
        plt.subplots_adjust(left = 0.2,bottom=0.125,right=0.75,top=0.95)
        
        
        if log == True:
            if logval == 'ln':
                if norm == True:
                    plt.title("normalized plot, log scale",pad=20)
                    plt.colorbar(label = 'log Voltage(log V)')
                   # plt.savefig("heatmap_norm_log_r.png")
                    plt.show(block=False)
                else:
                    plt.title("plot, log scale",pad=20)
                    plt.colorbar(label = 'log Voltage(log V)')
                    #plt.savefig("heatmap_log_r.png")
                    plt.show(block=False)
            if logval == 'log10':
                if norm == True:
                    plt.title("normalized plot, log10 scale",pad=20)
                    plt.colorbar(label = 'log Voltage(log V)')
                   # plt.savefig("heatmap_norm_log_r.png")
                    plt.show(block=False)
                else:
                    plt.title("plot, log10 scale",pad=20)
                    plt.colorbar(label = 'log Voltage(log V)')
                    #plt.savefig("heatmap_log_r.png")
                    plt.show(block=False)
            
        elif log == False:
            if norm == True:
                plt.title("normalized plot",pad=20)
                plt.colorbar(label = 'Voltage(V)')
                #plt.savefig("heatmap_norm_nolog_r.png")
                plt.show(block=False)
            else:
                plt.title("plot",pad=20)
                plt.colorbar(label = 'Voltage(V)')
                #plt.savefig("heatmap_nolog_r.png")
                plt.show(block=False)
        return arrays
    
    
    
def readCSVtoarray(file):
     array = np.loadtxt(open(file, "rb"), delimiter=",")
     return array
 
    
def normalizeData(arrays,log):
    for array in arrays:
        if log == True:
            maxVal = np.amin(array)
            maxVal *= -1
        else:
            maxVal = np.amax(array)
        for x,row in enumerate(array):
            for y,val in enumerate(row):
                array[x,y] = val/maxVal
    return arrays
    
files = sg.popup_get_file('Load Data','Load Data',file_types=(("CSV",".csv")),multiple_files=True)
if files is not None:
    files = files.split(',')
    temp_arrays = []
    for file in files:
        if file[-4:] == '.csv':
            temp_arrays.append(readCSVtoarray(file))
    print('{} files have been loaded!'.format(len(temp_arrays)))    
    
temp_arrays_log = list(np.log(temp_arrays))
temp_arrays_log10 = list(np.log10(temp_arrays))
no_log = plotData(files,temp_arrays,False,None,False)
log = plotData(files,temp_arrays_log,True,"ln",False)
log10 = plotData(files,temp_arrays_log10,True,'log10',False)

temp_arrays_norm = normalizeData(temp_arrays,False)
#norm_no_log = plotData(files,temp_arrays,False,True)
temp_arrays_norm_log = normalizeData(temp_arrays_log,True)
#norm_log = plotData(files,temp_arrays_log,True,True)
