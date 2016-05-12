#-----------------------------------------------------------------
# zeus: file.py
#
# Define zeus file tools
#
# Copyright (C) 2016, Christophe Fauchard
#-----------------------------------------------------------------

class Log():
    """
    Log Class with switch capabilities
    """
    
    def __init__(self, \
                 file_name, \
                 number=10, \
                 size=1, \
                 frequence=None, \
                 ):
        
        self.file_name = file_name
        self.frequence = frequence
        self.number = number
        self.size = size

        self.fd = open(self.file_name, "a")

    def print(self, text):
        print(text, file=self.fd)

    def close(self):
        self.fd.close()

if __name__ == '__main__':
    import sys
    sys.path.insert(0, "../")
    import zeus
                
    print("version zeus: " + zeus.__version__)
    print("Running tests for file.py...")

    print("testing class Log...")

    try:
        log_file = 'file_sample1.log'
        print("create log file: " + log_file)
        log = zeus.Log(log_file)
        print("writing datas in log file")
        log.print("data")
        print("closing log file")
        log.close()

        print("Class Log passed")

    except:
        print("Class Log not passed, Unexpected error:", sys.exc_info()[0])
