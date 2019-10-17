import numpy as np
import pickle
class Osa():
    def __init__(self):
        print('initializing the osa backend')
        self.length = 1000
        self.lambda_axis = np.linspace(-1,1,self.length)
        self._data = np.zeros(self.length)


    def gen_random_data(self):
        self._data = np.random.rand(self.length)

    @property
    def data(self):
        return self._data
    # the save and open of the Osa object is through pickle
    def save(self,file):
        pickle.dump(self,file)

    def load_from_file(self,file):
        obj = pickle.load(file)
        assert isinstance(obj,Osa)
        self._data = obj._data






