"""
MRDS Assigment 1 
Emelie Andersson
Viyan Ateaa

"""

import json, time, sys
from math import *
from givenCode import *
from path import *




"""
Method findGoalPoint
Find the point to aim for
Takes the path and current position of the robot 
as arguments
"""

def findGoalPoint(ourPath,roboPos):
    counter=0       
    while ourPath:
        point= ourPath[counter]
        distance=distanceCalc(point,roboPos)
        
        if(distance<1):
            ourPath.pop(counter)
        else:
            return point
        counter+=1
    return None
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
Method distanceCalc
Returns the distance between two points"""
def distanceCalc(pointA, pointB):
    xdiff= pointA['X'] - pointB['X']
    ydiff= pointA['Y'] - pointB['Y']

    return pythagoras_t(xdiff,ydiff)    

def main():
    if(len(sys.argv)>1):
        file_name=sys.argv[1]
    else:
        file_name='Path-to-bed.json'
    return file_name    
"""
Main function
Runs the methods and the follow-the-carrot
algorithm
"""

if _name_ == '_main_':
    starttime = time.time()
    
    file_name=main()
    
    path = Path()
    
    ourPath = path.loadPathAndMakeStack(file_name)

    try:
        while (ourPath):
            
            roboPos= getXYZpos()
         
            print('Current position: ', roboPos)
            
            roboHeading = getHeading()
            
            print('Current heading vector: X:{X:.3}, Y:{Y:.3}'.format(**getHeading()))
            
            carrotPoint = findGoalPoint(ourPath,roboPos)
           
            
            if(carrotPoint!=None):
            
                roboAngle=atan2(roboHeading['Y'],roboHeading['X'])
                    
                    
                pointAngle=atan2(carrotPoint['Y']-roboPos['Y'],carrotPoint['X']-roboPos['X'])
                    
                    
                angleDiff=pointAngle-roboAngle
                    
                #Degrees
                angleDegree=angleDiff *180/pi
                    
                if angleDegree >= 180: 
                    angleDiff=(angleDegree-360)*(pi/180)
                if angleDegree<-180:
                    angleDiff =(angleDegree+360)*(pi/180)
                    
                turnMagnitude = angleDiff
                    
                    
                response=postSpeed(turnMagnitude,0.7)
                    
        
    except UnexpectedResponse as ex:
        print('Unexped response from server when sending speed commands:',ex)
        
    except IndexError as ex:
        response=postSpeed(0,0)
        endtime = time.time()
        runtime = endtime - starttime
        print ('GOAL')
        print ('The robot finished the path in:', runtime, 'seconds')