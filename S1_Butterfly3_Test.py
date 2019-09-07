#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.3),
    on Fri Sep  6 20:32:54 2019
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.0.3'
expName = 'S1_Butterfly3_Test'  # from the Builder filename that created this script
expInfo = {'2) Subject ID': 'e.g. 000', '1) Study Prefix': 'GIV or PRO'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data_bySubject/%s/%s_%s/Butterfly/%s_%s_Test_ButterflyTask_FullOutput_%s' % (expInfo['1) Study Prefix'],expInfo['1) Study Prefix'],expInfo['2) Subject ID'], expInfo['1) Study Prefix'], expInfo['2) Subject ID'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/cjleschak/Downloads/Leschak_Prosocial ButterflyTask/S1_Butterfly3_Test.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1366, 768], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='norm')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
#---------Customizing Output -------------------
MinOutput_filename = _thisDir + os.sep + u'data_bySubject/%s/%s_%s/Butterfly/%s_%s_Test_ButterflyTask_MinOutput_%s' % (expInfo['1) Study Prefix'],expInfo['1) Study Prefix'],expInfo['2) Subject ID'], expInfo['1) Study Prefix'],expInfo['2) Subject ID'],expInfo['date'])
origin_Path        = _thisDir + os.sep+'S1_Butterfly3_Test.psyexp'

thisExp3         = data.ExperimentHandler(name=expName, version='',
    extraInfo    = None, runtimeInfo=None,
    originPath   = origin_Path,
    savePickle   = False, saveWideText=True, 
    dataFileName = MinOutput_filename)


#-----------Define Window & Image Sizes------------------
windowSize   = win.size
windowWidth  = windowSize[0]
windowHeight = windowSize[1]
screenRatio  = windowWidth/windowHeight

BFWidth  = .35
BFHeight = BFWidth*screenRatio
BFSize   = (BFWidth,BFHeight)

otherWidth  = 1.25
otherHeight = otherWidth*screenRatio/(4/3)
otherSize   = (otherWidth,otherHeight)

objWidth  = .5
objHeight = objWidth*screenRatio
objSize   = (objWidth,objHeight)

objBorderWidth  = .53
objBorderHeight = objBorderWidth*screenRatio
objBorderSize   = (objBorderWidth,objBorderHeight)


#-------------Define Variables Used Later-------------------

position            = ''
chosenSide          = ''
crosshairTxt        = ''
butterflyImg        = ''
conditionFile       = ''
leftFlowerImg       = ''
rightFlowerImg      = ''
butterflyFromTask   = ''
butterflySeenForWho = ''
InstructionLoopNum  = 1
durCalcd            = 9999



subID    = expInfo['2) Subject ID']
subIDnum = int(subID)
studyPrefix=expInfo['1) Study Prefix']
#---------------Setup Directories/Main Paths----------
taskLocation      = _thisDir
taskFilesPath     = _thisDir+os.sep+'TaskFiles'+os.sep+'ButterflyFiles'
instruct_Dir      = taskFilesPath+os.sep+'StimFolder'+os.sep+'OtherStims'+os.sep+'3_Test'
FlowerStim_Dir    = taskFilesPath+os.sep+'StimFolder'+os.sep+'Flowers'
ButterflyStim_Dir = taskFilesPath+os.sep+'StimFolder'+os.sep+'Butterflies'
conditionFile     = taskFilesPath+os.sep+'ConditionFiles'+os.sep+'3_Test'+os.sep+'TestCondFile.xlsx'
targetOrderCSV    = taskFilesPath+os.sep+'ConditionFiles'+os.sep+'3_Test'+os.sep+studyPrefix+'_TargetOrder.csv'
butterflyFile     = taskFilesPath+os.sep+'ConditionFiles'+os.sep+'2_Task'+os.sep+studyPrefix+'_ButterflyOrders.csv'
getReady          = instruct_Dir + os.sep+'GetReady.JPG'
endImg            = instruct_Dir + os.sep+'endImg.JPG'



#------Determines which pics were from Friend/Self run--------
import csv
with open(targetOrderCSV) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for i, target in enumerate(readCSV):
        if i == subIDnum:
             break

with open(butterflyFile) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for i, butterflyFromTask in enumerate(readCSV):
        if i == subIDnum:
             break


#------------------Start Program Clock-------------------
TaskClock = core.Clock()
ExpOnset = TaskClock.getTime()

thisExp3.addData('trial','')
thisExp3.addData('Stimulus','instructions')
thisExp3.addData('Onset',ExpOnset)

directions = visual.ImageStim(
    win=win, name='directions',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=otherSize,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text = visual.TextStim(win=win, name='text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "cross"
crossClock = core.Clock()

text_2 = visual.TextStim(win=win, name='text_2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "flowerStim"
flowerStimClock = core.Clock()

leftFlower_img = visual.ImageStim(
    win=win, name='leftFlower_img',
    image='sin', mask=None,
    ori=0, pos=(-.4, .1), size=BFSize,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
rightFlower_img = visual.ImageStim(
    win=win, name='rightFlower_img',
    image='sin', mask=None,
    ori=0, pos=(.4, .1), size=BFSize,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
butterfly_img = visual.ImageStim(
    win=win, name='butterfly_img',
    image='sin', mask=None,
    ori=0, pos=(0, -.5), size=BFSize,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
targetReminder = visual.TextStim(win=win, name='targetReminder',
    text=None,
    font='Arial Rounded MT Bold',
    pos=(0, .7), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
responseBorder = visual.Rect(
    win=win, name='responseBorder',
    width=(0.4, 0.7)[0], height=(0.4, 0.7)[1],
    ori=0, pos=[0,0],
    lineWidth=10, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)

# Initialize components for Routine "crosshair"
crosshairClock = core.Clock()

fix1sec = visual.TextStim(win=win, name='fix1sec',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "endFix"
endFixClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);


# Initialize components for Routine "end"
endClock = core.Clock()
endImage = visual.ImageStim(
    win=win, name='endImage',
    image=endImg, mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)


# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
instructionLoop = data.TrialHandler(nReps=999, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='instructionLoop')
thisExp.addLoop(instructionLoop)  # add the loop to the experiment
thisInstructionLoop = instructionLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisInstructionLoop.rgb)
if thisInstructionLoop != None:
    for paramName in thisInstructionLoop:
        exec('{} = thisInstructionLoop[paramName]'.format(paramName))

for thisInstructionLoop in instructionLoop:
    currentLoop = instructionLoop
    # abbreviate parameter names if possible (e.g. rgb = thisInstructionLoop.rgb)
    if thisInstructionLoop != None:
        for paramName in thisInstructionLoop:
            exec('{} = thisInstructionLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Instructions"-------
    t = 0
    InstructionsClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    #-----If end of instructions is reached, but 'advance to next-----
    #----instruction button' (e.g. 'right') is being pressed, keep ---
    #---displaying last instruction image ("Do you have questions")---
    #-----Only a "5" button press will advance to the actual task.----
    if InstructionLoopNum > 6:
        InstructionLoopNum = 7
    if InstructionLoopNum < 1:
        InstructionLoopNum = 1
    
    
    #-----Select Appropriate Instruction Screen to be Displayed-------
    InstructionImgDisplayed = instruct_Dir + os.sep+'testInstruct_' + str(InstructionLoopNum) + '.JPG'
    
    
    if InstructionLoopNum == 7:
        crosshairTxt='+'
    else:
        crosshairTxt=''
    
    
    
    #-----------Get Time of Onset for each Instruction----------
    Onset = TaskClock.getTime()
    
    
    #------------Add Data to Full Output File--------------
    thisExp.addData('Stimulus','instructions')
    thisExp.addData('Onset',Onset)
    directions.setImage(InstructionImgDisplayed)
    NextInstruction = event.BuilderKeyResponse()
    text.setText(crosshairTxt)
    # keep track of which components have finished
    InstructionsComponents = [directions, NextInstruction, text]
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Instructions"-------
    while continueRoutine:
        # get current time
        t = InstructionsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *directions* updates
        if t >= 0.0 and directions.status == NOT_STARTED:
            # keep track of start time/frame for later
            directions.tStart = t
            directions.frameNStart = frameN  # exact frame index
            directions.setAutoDraw(True)
        
        # *NextInstruction* updates
        if t >= 0.0 and NextInstruction.status == NOT_STARTED:
            # keep track of start time/frame for later
            NextInstruction.tStart = t
            NextInstruction.frameNStart = frameN  # exact frame index
            NextInstruction.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(NextInstruction.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if NextInstruction.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right', '5'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if NextInstruction.keys == []:  # then this was the first keypress
                    NextInstruction.keys = theseKeys[0]  # just the first key pressed
                    NextInstruction.rt = NextInstruction.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Instructions"-------
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #---If on the last instruction slide, and "5" is pressed,---
    #--------end Instruction Loop and proceed to task.----------
    #------When "5" is pressed, start actual task clock.--------
    if InstructionLoopNum == 7 and NextInstruction.keys == '5':
        InstrOffset = TaskClock.getTime()
        instructionLoop.finished = 1
        TriggerClock = core.Clock()
        Onset = TriggerClock.getTime()
        duration2 = InstrOffset-ExpOnset
    
        thisExp.addData('Offset',InstrOffset)
        thisExp.addData('duration',duration2)
        thisExp.nextEntry()
        thisExp.addData('Stimulus','trigger')
        thisExp.addData('Onset',Onset)
    
        thisExp3.addData('Offset',InstrOffset)
        thisExp3.addData('duration',duration2)
        thisExp3.nextEntry()
        thisExp3.addData('trial','')
        thisExp3.addData('Stimulus','trigger')
        thisExp3.addData('Onset',Onset)
        thisExp3.nextEntry()
    
    
    #-------Allow forward/backward movement in instructions--------
    if NextInstruction.keys == 'left':
        InstructionLoopNum = InstructionLoopNum - 1
    elif NextInstruction.keys == 'right':
        InstructionLoopNum = InstructionLoopNum + 1
    
    
    #------------------Add Data-----------------------
    if not NextInstruction.keys == '5':
        Offset   = TaskClock.getTime()
        duration = Offset - Onset
        thisExp.addData('Offset',Offset)
        thisExp.addData('duration',duration)
    
    # check responses
    if NextInstruction.keys in ['', [], None]:  # No response was made
        NextInstruction.keys=None
    instructionLoop.addData('NextInstruction.keys',NextInstruction.keys)
    if NextInstruction.keys != None:  # we had a response
        instructionLoop.addData('NextInstruction.rt', NextInstruction.rt)
    # the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 999 repeats of 'instructionLoop'


# ------Prepare to start Routine "cross"-------
t = 0
crossClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
#----------Add Data--------------
Onset = TriggerClock.getTime()


# keep track of which components have finished
crossComponents = [text_2]
for thisComponent in crossComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "cross"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = crossClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_2.status == STARTED and t >= frameRemains:
        text_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in crossComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "cross"-------
for thisComponent in crossComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
#-----------Add Data---------------
Offset   = TriggerClock.getTime()
duration = Offset - Onset

thisExp.addData('Stimulus','+')
thisExp.addData('Onset',Onset)
thisExp.addData('Offset',Offset)
thisExp.addData('duration',duration)

thisExp3.addData('Stimulus','+')
thisExp3.addData('Onset',Onset)
thisExp3.addData('Offset',Offset)
thisExp3.addData('duration',duration)
thisExp3.nextEntry()


# set up handler to look after randomisation of conditions etc
TrialLoop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(conditionFile),
    seed=None, name='TrialLoop')
thisExp.addLoop(TrialLoop)  # add the loop to the experiment
thisTrialLoop = TrialLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialLoop.rgb)
if thisTrialLoop != None:
    for paramName in thisTrialLoop:
        exec('{} = thisTrialLoop[paramName]'.format(paramName))

for thisTrialLoop in TrialLoop:
    currentLoop = TrialLoop
    # abbreviate parameter names if possible (e.g. rgb = thisTrialLoop.rgb)
    if thisTrialLoop != None:
        for paramName in thisTrialLoop:
            exec('{} = thisTrialLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "flowerStim"-------
    t = 0
    flowerStimClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    durCalcd=9999
    
    if butterfly[0] == butterflyFromTask[1]:
        butterflySeenForWho = target[1]
    elif butterfly[0] == butterflyFromTask[2]:
        butterflySeenForWho = target[2]
    else:
        butterflySeenForWho = '??'
    
    if leftFlower == 'A1':
        leftFlowerImg  = FlowerStim_Dir + os.sep+'FlowerA1.PNG'
        rightFlowerImg = FlowerStim_Dir + os.sep+'FlowerA2.PNG'
    elif leftFlower == 'A2':
        leftFlowerImg  = FlowerStim_Dir + os.sep+'FlowerA2.PNG'
        rightFlowerImg = FlowerStim_Dir + os.sep+'FlowerA1.PNG'
    elif leftFlower == 'B1':
        leftFlowerImg  = FlowerStim_Dir + os.sep+'FlowerB1.PNG'
        rightFlowerImg = FlowerStim_Dir + os.sep+'FlowerB2.PNG'
    elif leftFlower == 'B2':
        leftFlowerImg  = FlowerStim_Dir + os.sep+'FlowerB2.PNG'
        rightFlowerImg = FlowerStim_Dir + os.sep+'FlowerB1.PNG'
    
    position     = [7,7]
    chosenSide   = ''
    butterflyImg = ButterflyStim_Dir + os.sep+'Butterfly_' + butterfly +'.JPG'
    
    
    
    #Add Data to Output
    Onset = TriggerClock.getTime()
    thisExp.addData('trial',trialNum)
    thisExp.addData('Stimulus','Butterfly_'+butterfly)
    thisExp.addData('Onset',Onset)
    
    thisExp3.addData('trial',trialNum)
    thisExp3.addData('Stimulus','Butterfly_'+butterfly)
    thisExp3.addData('Onset',Onset)
    
    leftFlower_img.setImage(leftFlowerImg)
    rightFlower_img.setImage(rightFlowerImg)
    butterfly_img.setImage(butterflyImg)
    flowerResponse = event.BuilderKeyResponse()
    # keep track of which components have finished
    flowerStimComponents = [leftFlower_img, rightFlower_img, butterfly_img, targetReminder, flowerResponse, responseBorder]
    for thisComponent in flowerStimComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "flowerStim"-------
    while continueRoutine:
        # get current time
        t = flowerStimClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if flowerResponse.keys == '1':
            chosenSide = 'L'
        elif flowerResponse.keys == '2':
            chosenSide = 'R'
        
        if chosenSide == 'L':
            position = [-.4,.1]
        elif chosenSide == 'R':
            position = [.4,.1]
        else:
            position = [7,7]
        
        if not str(flowerResponse.rt)=='[]':
            durCalcd=float(str(flowerResponse.rt)) + 1.0
        
        # *leftFlower_img* updates
        if t >= 0.0 and leftFlower_img.status == NOT_STARTED:
            # keep track of start time/frame for later
            leftFlower_img.tStart = t
            leftFlower_img.frameNStart = frameN  # exact frame index
            leftFlower_img.setAutoDraw(True)
        frameRemains = 0.0 + durCalcd- win.monitorFramePeriod * 0.75  # most of one frame period left
        if leftFlower_img.status == STARTED and t >= frameRemains:
            leftFlower_img.setAutoDraw(False)
        
        # *rightFlower_img* updates
        if t >= 0.0 and rightFlower_img.status == NOT_STARTED:
            # keep track of start time/frame for later
            rightFlower_img.tStart = t
            rightFlower_img.frameNStart = frameN  # exact frame index
            rightFlower_img.setAutoDraw(True)
        frameRemains = 0.0 + durCalcd- win.monitorFramePeriod * 0.75  # most of one frame period left
        if rightFlower_img.status == STARTED and t >= frameRemains:
            rightFlower_img.setAutoDraw(False)
        
        # *butterfly_img* updates
        if t >= 0.0 and butterfly_img.status == NOT_STARTED:
            # keep track of start time/frame for later
            butterfly_img.tStart = t
            butterfly_img.frameNStart = frameN  # exact frame index
            butterfly_img.setAutoDraw(True)
        frameRemains = 0.0 + durCalcd- win.monitorFramePeriod * 0.75  # most of one frame period left
        if butterfly_img.status == STARTED and t >= frameRemains:
            butterfly_img.setAutoDraw(False)
        
        # *targetReminder* updates
        if t >= 0.0 and targetReminder.status == NOT_STARTED:
            # keep track of start time/frame for later
            targetReminder.tStart = t
            targetReminder.frameNStart = frameN  # exact frame index
            targetReminder.setAutoDraw(True)
        frameRemains = 0.0 + durCalcd- win.monitorFramePeriod * 0.75  # most of one frame period left
        if targetReminder.status == STARTED and t >= frameRemains:
            targetReminder.setAutoDraw(False)
        
        # *flowerResponse* updates
        if t >= 0.0 and flowerResponse.status == NOT_STARTED:
            # keep track of start time/frame for later
            flowerResponse.tStart = t
            flowerResponse.frameNStart = frameN  # exact frame index
            flowerResponse.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(flowerResponse.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + durCalcd- win.monitorFramePeriod * 0.75  # most of one frame period left
        if flowerResponse.status == STARTED and t >= frameRemains:
            flowerResponse.status = FINISHED
        if flowerResponse.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if flowerResponse.keys == []:  # then this was the first keypress
                    flowerResponse.keys = theseKeys[0]  # just the first key pressed
                    flowerResponse.rt = flowerResponse.clock.getTime()
                    # was this 'correct'?
                    if (flowerResponse.keys == str(correctKey)) or (flowerResponse.keys == correctKey):
                        flowerResponse.corr = 1
                    else:
                        flowerResponse.corr = 0
        
        # *responseBorder* updates
        if t >= 0.0 and responseBorder.status == NOT_STARTED:
            # keep track of start time/frame for later
            responseBorder.tStart = t
            responseBorder.frameNStart = frameN  # exact frame index
            responseBorder.setAutoDraw(True)
        frameRemains = 0.0 + durCalcd- win.monitorFramePeriod * 0.75  # most of one frame period left
        if responseBorder.status == STARTED and t >= frameRemains:
            responseBorder.setAutoDraw(False)
        if responseBorder.status == STARTED:  # only update if drawing
            responseBorder.setPos(position, log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in flowerStimComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "flowerStim"-------
    for thisComponent in flowerStimComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #Add Data to Output
    Offset   = TriggerClock.getTime()
    duration = Offset - Onset
    
    thisExp.addData('Offset',Offset)
    thisExp.addData('duration',duration)
    thisExp.addData('butterflySeenforWho',butterflySeenForWho)
    thisExp.nextEntry()
    
    thisExp3.addData('Offset',Offset)
    thisExp3.addData('duration',duration)
    thisExp3.addData('butterflySeenforWho',butterflySeenForWho)
    thisExp3.addData('response',flowerResponse.keys)
    thisExp3.addData('response_RT',flowerResponse.rt)
    thisExp3.addData('correct (1) or incorrect (0)',flowerResponse.corr)
    
    
    # check responses
    if flowerResponse.keys in ['', [], None]:  # No response was made
        flowerResponse.keys=None
        # was no response the correct answer?!
        if str(correctKey).lower() == 'none':
           flowerResponse.corr = 1;  # correct non-response
        else:
           flowerResponse.corr = 0;  # failed to respond (incorrectly)
    # store data for TrialLoop (TrialHandler)
    TrialLoop.addData('flowerResponse.keys',flowerResponse.keys)
    TrialLoop.addData('flowerResponse.corr', flowerResponse.corr)
    if flowerResponse.keys != None:  # we had a response
        TrialLoop.addData('flowerResponse.rt', flowerResponse.rt)
    # the Routine "flowerStim" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "crosshair"-------
    t = 0
    crosshairClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    #----------Add Data--------------
    Onset = TriggerClock.getTime()
    
    # keep track of which components have finished
    crosshairComponents = [fix1sec]
    for thisComponent in crosshairComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "crosshair"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = crosshairClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *fix1sec* updates
        if t >= 0.0 and fix1sec.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix1sec.tStart = t
            fix1sec.frameNStart = frameN  # exact frame index
            fix1sec.setAutoDraw(True)
        frameRemains = 0.0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fix1sec.status == STARTED and t >= frameRemains:
            fix1sec.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in crosshairComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "crosshair"-------
    for thisComponent in crosshairComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #-----------Add Data---------------
    Offset   = TriggerClock.getTime()
    duration = Offset - Onset
    
    thisExp.addData('Stimulus','+')
    thisExp.addData('Onset',Onset)
    thisExp.addData('Offset',Offset)
    thisExp.addData('duration',duration)
    
    thisExp3.nextEntry()
    thisExp3.addData('Stimulus','+')
    thisExp3.addData('Onset',Onset)
    thisExp3.addData('Offset',Offset)
    thisExp3.addData('duration',duration)
    thisExp3.nextEntry()
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'TrialLoop'


# ------Prepare to start Routine "endFix"-------
t = 0
endFixClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
#--------------Add Data------------
Onset = TriggerClock.getTime()

thisExp.addData('Stimulus','+')
thisExp.addData('Onset',Onset)

thisExp3.addData('Stimulus','+')
thisExp3.addData('Onset',Onset)

# keep track of which components have finished
endFixComponents = [text_3]
for thisComponent in endFixComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "endFix"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endFixClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_3.status == STARTED and t >= frameRemains:
        text_3.setAutoDraw(False)
    
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endFixComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "endFix"-------
for thisComponent in endFixComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
#--------------Add Data------------
Offset   = TriggerClock.getTime()
duration = Offset - Onset

thisExp.addData('Offset',Offset)
thisExp.addData('duration',duration)
thisExp.nextEntry()

thisExp3.addData('Offset',Offset)
thisExp3.addData('duration',duration)
thisExp3.nextEntry()


# ------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
#Add Data to Output
Onset = TriggerClock.getTime()

thisExp.addData('Stimulus','EndScreen')
thisExp.addData('Onset',Onset)

# keep track of which components have finished
endComponents = [endImage]
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *endImage* updates
    if t >= 0.0 and endImage.status == NOT_STARTED:
        # keep track of start time/frame for later
        endImage.tStart = t
        endImage.frameNStart = frameN  # exact frame index
        endImage.setAutoDraw(True)
    frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if endImage.status == STARTED and t >= frameRemains:
        endImage.setAutoDraw(False)
    
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
#Add Data to Output
Offset   = TriggerClock.getTime()
duration = Offset - Onset

thisExp.addData('Offset',Offset)
thisExp.addData('duration',duration)
thisExp.nextEntry()







# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
