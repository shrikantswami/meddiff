import os


class Path:
    def __init__(self, path_string):
        try:
            os.chdir(path_string)
        except:
            print('given path dosen"t exists')

    def cd(self, path_string):
        try:
            os.chdir(path_string)
        except :
            print('in valid path'+str(path_string))

    def current_path(self):
        return os.path.dirname(os.path.abspath(__file__))


folder = '/home/shrikant/Desktop/office/meddiff/Problem5'
path = Path(folder)
path.cd('../')
print(path.current_path())
