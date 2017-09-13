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
def findGoalPoint(ourPath,roboPos):
    list = []
    for i in range (len(ourPath)):
        point= ourPath[len(ourPath)-1]
        if point in list:
            point=ourPath.pop()
    
        list.append(point)
        xdiff= point['X'] - roboPos['X']
        ydiff= point['Y'] - roboPos['Y']

        distance=pythagoras_t(xdiff,ydiff)

        if(distance<0.1):
            ourPath.pop()
        else:
            return point

"""def findGoalPoint(ourPath,roboPos):
    list = []
    for i in range (len(ourPath)):
        point= ourPath.pop(len(ourPath)-1)
        if point in list:
                point=ourPath.pop()

        list.append(point)        
       
        xdiff= point['X'] - roboPos['X']
        ydiff= point['Y'] - roboPos['Y']
    
        distance=pythagoras_t(ydiff,xdiff)  
        
        if(distance>0.7):
                return point"""
    

"""Method pythagoras"""
def pythagoras_t(a,b):
    return sqrt((a**2)+(b**2))

"""Method getXYZpos"""
def getXYZpos():
    return getPose()['Pose']['Position']

if _name_ == '_main_':
    path = Path()
    
    ourPath = path.loadPathAndMakeStack('Path-to-bed.json')
    
    #ourPath = path.loadPathAndMakeStack('Path-around-table.json')
    
    #ourPath = path.loadPathAndMakeStack('Path-from-bed.json')
    
    
    
    try:
        while(ourPath):
            
            roboPos= getXYZpos()
            print('Current position: ', roboPos)
            
            roboHeading = getHeading()
            
            print('Current heading vector: X:{X:.3}, Y:{Y:.3}'.format(**getHeading()))
            
            carrotPoint = findGoalPoint(ourPath,roboPos)
            
            print('Current carrot point: ', carrotPoint)
            
            if(carrotPoint):
            
                roboAngle=atan2(roboHeading['Y'],roboHeading['X'])
                
                print ('Current Robotangle', roboAngle)
                
                pointAngle=atan2(carrotPoint['Y']-roboPos['Y'],carrotPoint['X']-roboPos['X'])
                
                print ('Current point angle', pointAngle)
                
                angleDiff=pointAngle-roboAngle
                
                if angleDiff >= pi/2 or angleDiff < -pi/2:
                    angleDiff=roboAngle-pointAngle
                else:
                    angleDiff =pointAngle- roboAngle
                    
                
                kp=0.1
                
                turnMagnitude= kp + angleDiff
                
                print turnMagnitude
                
                response=postSpeed(turnMagnitude,0.5)
                
                time.sleep(3)
                
        response=postSpeed(0,0)
        
    except UnexpectedResponse as ex:
        print('Unexped response from server when sending speed commands:',ex)