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
"""
#compare robo pos x with coordinate x
#compare robo pos y with coorinate y
#pythagoras


def findGoalPoint(ourPath,roboPos,number):
    #list = []
    counter=-1
    for i in range (len(ourPath)):
        #point= ourPath[len(ourPath)-1]
        if counter<number:
            point= ourPath[i]
            #if point in list:
                #point=ourPath.pop([len(ourPath)-1])
        
            #list.append(point)
            xdiff= point['X'] - roboPos['X']
            ydiff= point['Y'] - roboPos['Y']
    
            distance=pythagoras_t(xdiff,ydiff)
            print (distance)
            counter=counter+1
    
            if(distance<1):
                ourPath.pop(i)
            else:
                return point
        else:
            sys.exit()

#def findGoalPoint(ourPath,roboPos):
    #list = []
    #for i in range (len(ourPath)):
        #point= ourPath.pop([len(ourPath)-1])
        #if point in list:
                #point=ourPath.pop()

        #list.append(point)        
       
        #xdiff= point['X'] - roboPos['X']
        #ydiff= point['Y'] - roboPos['Y']
    
        #distance=pythagoras_t(ydiff,xdiff)  
        
        #if(distance>0.7):
                #return point
    

"""Method pythagoras"""
def pythagoras_t(a,b):
    return sqrt((a**2)+(b**2))

"""Method getXYZpos"""
def getXYZpos():
    return getPose()['Pose']['Position']

def withinGoal(roboPos, ourPath):
    goal=ourPath[len(ourPath)-1]
    distanceGoal=pythagoras_t(goal['X']-roboPos['X'],goal['Y']-roboPos['Y'])
    if len(ourPath)<2:
        return True
    else:
        return False
    
    
    

#def scalor(angleDiff):
    #return 1-exp(-2*angleDiff**2)

if _name_ == '_main_':
    path = Path()
    
    #ourPath = path.loadPathAndMakeStack('Path-to-bed.json')
    
    ourPath = path.loadPathAndMakeStack('Path-around-table.json')
    number=len(ourPath)
    finalPoint=ourPath[-1]
    
    #ourPath = path.loadPathAndMakeStack('Path-from-bed.json')
    
    
    
    try:
        while(ourPath):
            
            roboPos= getXYZpos()
            
            if(withinGoal(roboPos,ourPath)==True):
                response=postSpeed(0,0)
                print ('SUCCESS')
                sys.exit()
                
            #print('Current position: ', roboPos)
            
            roboHeading = getHeading()
            
            
            #print('Current heading vector: X:{X:.3}, Y:{Y:.3}'.format(**getHeading()))
            
            carrotPoint = findGoalPoint(ourPath,roboPos,number)
            if carrotPoint==finalPoint:
                print('Final destination')
                sys.exit()
            
            #print('Current carrot point: ', carrotPoint)
            
            if(carrotPoint):
            
                roboAngle=atan2(roboHeading['Y'],roboHeading['X'])
                
                print ('Current Robotangle', roboAngle)
                
                pointAngle=atan2(carrotPoint['Y']-roboPos['Y'],carrotPoint['X']-roboPos['X'])
                
                print ('Current point angle', pointAngle)
                
                angleDiff=pointAngle-roboAngle
                
                angleDegree=angleDiff *180/pi
                
                if angleDegree >= 180: 
                    angleDiff=angleDegree-360
                if angleDegree<-180:
                    angleDiff =angleDegree+360
                  
                    
                kp=0.1
                 
                turnMagnitude= angleDiff
                
                print (turnMagnitude)
               
                
                response=postSpeed(turnMagnitude,0.5)
                
                time.sleep(1)
                
        response=postSpeed(0,0)
        
    except UnexpectedResponse as ex:
        print('Unexped response from server when sending speed commands:',ex)