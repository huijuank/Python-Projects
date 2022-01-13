import os
import numpy as np

class dataprep():

    def __init__(self):
        pass
        
    def training_data_ID(self, size_traindata):
        """
        To store the filename of the cropped audio files in y labels.
        ID will be used to monitor the data distribution after the splitting.
        Used for unsupervised learning training models
        """
        categories = ["Tcoil","None"]
        training_data=[]
        file_dict = {}
        file_count = 0

        for category in categories:
            for root, dirs, files in os.walk(os.path.join(self.filedir, category)):
                class_num = categories.index(category)
                for file in files:
                    file_dict[file_count] = file
                    file_count += 1
                    file = os.path.join(root,file)
                    spects = self.stftnsplit(file)
                    for spec in spects:
                        try:
                            filename = os.path.split(file)
                            print(filename[1])
                            training_data.append([spec, filename[1]])
                        except Exception as e:
                            pass
                    
        plt.close('all')
        x = [] #features
        y = [] #labels  
                
        for features, label in training_data:
            x.append(features)
            y.append(label)

        unique, counts = np.unique(y,return_counts = True)
        dict(zip(unique, counts))
        x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = size_traindata, random_state = 0)
        print("x train:{0}\ny train:{1}\nx test:{2}\ny test:{3}".format(len(x_train),
                                                                        len(y_train),
                                                                        len(x_test),
                                                                        len(y_test)))
        x_train = np.array(x_train)
        y_train = np.array(y_train)
        x_test = np.array(x_test)
        y_test = np.array(y_test)
        return x_train,y_train,x_test,y_test,file_dict
