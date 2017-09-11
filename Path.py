import json

class Path:

    def __init__(self):
    # Load the path from a file and convert it into a list of coordinates
        #self.loadPathAndMakeStack('Path-to-bed.json')
        #self.vecPath = self.vectorizePath()
        pass
    
    def loadPathAndMakeStack(self, file_name):
    
        with open(file_name) as path_file:
            data = json.load(path_file)
            stack = []
            for i in range (len(data)):
                stack.append(data[i]['Pose']['Position'])
                stack.reverse
            return stack            
    
    def vectorizePath(self):
        vecArray = [{'X': p['Pose']['Position']['X'], \
                     'Y': p['Pose']['Position']['Y'], \
                     'Z': p['Pose']['Position']['Z']}\
                     for p in self.path]
        return vecArray
    

        
        
        



