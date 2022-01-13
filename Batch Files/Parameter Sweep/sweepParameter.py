import yaml
import subprocess

def automate():
    epoch_val = list(range(10, 30, 10))
    batchsize_val = [512,256]
    
    with open("baseline.yaml") as stream:
        param = yaml.safe_load(stream)

    for epoch in epoch_val:
        for batchsize in batchsize_val:
            param["fit"]["epochs"] = epoch
            param["fit"]["batch_size"] = batchsize
            param["result_file"] = "result_epoch{epoch}_bs{batchsize}.csv".format(epoch=epoch,
                                                                               batchsize=batchsize)
            with open("baseline.yaml", "w") as stream:
                yaml.dump(param, stream)
            print("Starting run for epoch = {epoch}, batch size = {batchsize}".format(epoch=epoch,
                                                                                       batchsize = batchsize))
            subprocess.call([r'C:\Users\<file dir>\sweepParameter.bat'])
                
automate()
