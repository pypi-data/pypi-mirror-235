import pandas as pd
from setify import utils



def _get_server():
    # return 'https://setify-server.herokuapp.com'
    return 'http://157.230.94.79:8080'


def data(dataset):
    fpath = utils.load_data(
        _get_server() + '/' + dataset, dataset + '.h5')
    return pd.read_hdf(fpath)
