import pickle

 class dataprep():
    def __init__(self):
        pass
      
    def store_result(self,x_train,y_train,x_test,y_test,file_dict):
        """
        To store the result of training_data method as pickle files
        Returns
        -------
        None.
        """
        
        pickle_out = open("x_train.pickle", "wb")
        pickle.dump(x_train, pickle_out)
        pickle_out.close()
	
        pickle_out = open("x_test.pickle", "wb")
        pickle.dump(x_test, pickle_out)
        pickle_out.close()

        pickle_out = open("y_train.pickle", "wb")
        pickle.dump(y_train, pickle_out)
        pickle_out.close()

        pickle_out = open("y_test.pickle", "wb")
        pickle.dump(y_test, pickle_out)
        pickle_out.close()
        
        pickle_out = open("filename_dict.pickle", "wb")
        pickle.dump(file_dict, pickle_out)
        pickle_out.close()
