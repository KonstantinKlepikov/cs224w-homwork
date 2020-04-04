import shelve
import os
from .core_paths import DUMP_PATH

class DataDump:
    """
    Class provide method constructor for serialise data
    """
    def __init__(self, dump_list, path):

        self.dump_list = dump_list
        self.path = path
        self.ospath= os.path.realpath(DUMP_PATH + path)

class ShelveDump(DataDump):
    """
    Class provide methods for save and load data with shelve
    """
    def save(self):
        with shelve.open(self.ospath) as s:
            for k, v in enumerate(self.dump_list):
                try:
                    s[str(k)] = v
                    print('Object {0} is dumped to "{1}" objects'.format(k, self.path))
                except TypeError:
                    print('Object {} not dumped - an error occurred'.format(k))

    def load(self):
        dict_of_objects = {}
        with shelve.open(self.ospath) as o:
            for k, v in o.items():
                dict_of_objects[k] = v
            return dict_of_objects.values()


def dumper(dump_list=None, path='default', method='shelve', task=None):
    """
    Save and open data with serialise tools. 
    Now available:
    - shelve
    
    Parameters
    ----------
    :param dump_list: 
    List or tuple with objects for saving
        list, tuple
    
    :param path: 
    Current path name to folder with data
        string, default 'default'

    :param method: 
    Method of serialisation
        string, default 'shelve'

    :param task: 
    Type of operation. 's' for saving, 'o' for opening
        string, default None
    """
    if method == 'shelve':
        dumped = ShelveDump(dump_list, path)
    else:
        print('Wrong method')

    if task == 's':
        try: 
            dumped.save()
        except NameError:
            print("Objects can't be saved")
    elif task == 'o':
        try: 
            return dumped.load()
        except NameError:
            print("Objects can't be extracted")
    else:
        print("No one object are dumped. Set task 'o' for opening or set task 's' for saving.")