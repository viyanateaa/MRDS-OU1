"""
MRDS Assigment 1 
Emelie Andersson
Viyan Ateaa

"""

import json, time 
from math import *
from givenCode import *
from path import *
import sys



"""
Method findGoalPoint
Find the point to aim for
Takes the path and current position of the robot 
as arguments
"""

def findGoalPoint(ourPath,roboPos):

    for i in range (len(ourPath)):
     
            point= ourPath[i]
            
            xdiff= point['X'] - roboPos['X']
            ydiff= point['Y'] - roboPos['Y']
    
            distance=pythagoras_t(xdiff,ydiff)

            if(distance<1):
                ourPath.pop(i)
            else:
                return point
    

"""
Method pythagoras
Calculates the hypothenus beween the 
point A and B
"""
def pythagoras_t(a,b):
    return sqrt((a**2)+(b**2))


"""
Method getXYZpos
Return the robot's current position in a 
XYZ-coordinate system
"""
def getXYZpos():
    return getPose()['Pose']['Position']


"""
Main function
Runs the methods and the follow-the-carrot
algorithm
"""
if __name__ == '__main__':
    path = Path()
    
    """The different paths"""
    #ourPath = path.loadPathAndMakeStack('Path-to-bed.json')
    
    ourPath = path.loadPathAndMakeStack('Path-around-table.json')
    
    lenPath= len(ourPath)
    counter=1
    
    #ourPath = path.loadPathAndMakeStack('Path-from-bed.json')
    
    lastPoint = path.findLastPoint('Path-around-table.json')
    
    try:
        while (len(ourPath)>2):
            print ('Path lenght: ')
            print (len(ourPath))
            
            roboPos= getXYZpos()
            
            if(roboPos==lastPoint):
                response=postSpeed(0,0)
                print ('GOAL REACHED')
                sys.exit(0)
                
         
            print('Current position: ', roboPos)
            
            roboHeading = getHeading()
            
            print('Current heading vector: X:{X:.3}, Y:{Y:.3}'.format(**getHeading()))
            
            carrotPoint = findGoalPoint(ourPath,roboPos)
           
            
            if(carrotPoint):
            
                roboAngle=atan2(roboHeading['Y'],roboHeading['X'])
                
                
                pointAngle=atan2(carrotPoint['Y']-roboPos['Y'],carrotPoint['X']-roboPos['X'])
                
                
                angleDiff=pointAngle-roboAngle
                
                angleDegree=angleDiff *180/pi
                
                if angleDegree >= 180: 
                    angleDiff=angleDegree-360
                if angleDegree<-180:
                    angleDiff =angleDegree+360
                #if angleDiff >=pi:
                    #angleDiff=angleDiff-2*pi
                #if angleDiff <-pi:
                    #angleDiff=angleDiff+2*pi
                
                 
                turnMagnitude= angleDiff
                
                
                response=postSpeed(turnMagnitude,0.5)
                
                time.sleep(1)
                
        response=postSpeed(0,0)
        
    except UnexpectedResponse as ex:
        print('Unexped response from server when sending speed commands:',ex)
            
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
                    
    
    
    
    
    

    



