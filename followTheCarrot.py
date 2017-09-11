"""
MRDS Assigment 1 
Emelie Andersson
Viyan Ateaa

"""

import json, time 
from math import sin,cos,pi,atan2,sqrt
from givenCode import *
from path import *



"""
Method findGoalPoint
Find the point to aim for
"""
#compare robo pos x with coordinate x
#compare robo pos y with coorinate y
#pythagoras

#if distance > lookAhedDistance got there
def findGoalPoint(ourPath):
    for i in range (len(ourPath)):
        point= ourPath.pop(len(ourPath)-1)
        
        xdiff= point['X'] - roboPos['X']
        ydiff= point['Y'] - roboPos['Y']

        distance=pythagoras_t(xdiff,ydiff)

        if(distance>5):
            return point;
        else:
            ourPath.pop

"""
Method diff_points
Calcs the difference between points
"""

"""
Method diff_angels
Calcs the the difference between angles
"""

"""
Method diff_roboPosAngle
Find out what the angle is between noth and robot vector
"""

"""Method pythagoras"""
def pythagoras_t(a,b):
    return sqrt((a**2)+(b**2))

"""Method getXYZpos"""
def getXYZpos():
    return getPose()['Pose']['Position']

if __name__ == '__main__':
    path = Path()
    
    ourPath = path.loadPathAndMakeStack('Path-to-bed.json')
    print len(ourPath)
    
    try:
        while(ourPath):
            
            roboPos= getXYZpos()
            
            roboHeading = getHeading()
            
            carrotPoint = findGoalPoint(ourPath)
            
            if(carrotPoint):
            
                roboAngle=atan2(roboHeading['X'],roboHeading['Y'])
                
                
                pointAngle=atan2(carrotPoint['Y']-roboPos['Y'],carrotPoint['X']-roboPos['X'])
                
                angleDiff= pointAngle-roboAngle
                
                kp=0.5
                
                turnMagnitude= kp + angleDiff
                print turnMagnitude
                
                response=postSpeed(turnMagnitude,0.5)
                
                time.sleep(3)
                
        response=postSpeed(0,0)
    except UnexpectedResponse as ex:
        print('Unexped response from server when sending speed commands:',ex)
            
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
                    
    
    
    
    
    

    



