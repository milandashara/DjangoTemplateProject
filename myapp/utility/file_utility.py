'''
Created on 1 Apr 2016

@author: milanashara
'''

fileName = '/Users/milanashara/jboss-eap-6.3/standalone/log/server.log'


def getLog(fileName,num_of_last_lines):
    
    lines = []
    try:
        with open(fileName) as g:
            lines = g.readlines()
    
            return lines[-1000:]
    except IOError as io:
        return lines

def save_file(file,dir):
    try:
        import os
        if not os.path.exists(dir):
            os.makedirs(dir)
        fileNameWithPath = dir + str(file.name)
        try:
            os.remove(fileNameWithPath)
        except OSError:
            pass
        with open(fileNameWithPath, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        return True,''
    except Exception, e:
        return False,str(e)
    

            
if __name__ == '__main__':
    logs = getLog(fileName, 1000)
    print len(logs)
    