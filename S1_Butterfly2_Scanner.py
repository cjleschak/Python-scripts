#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.3),
    on Fri Sep  6 20:32:27 2019
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
expName = 'S1_Butterfly2_Scanner_bugFixed'  # from the Builder filename that created this script
expInfo = {'4) Friend Name': 'e.g. Anna', '2) Subject ID': 'e.g. 000', '1) Study Prefix': 'GIV or PRO', '5) Run #': '1 or 2?', '3) Target Type': 'self or friend?'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data_bySubject/%s/%s_%s/Butterfly/%s_%s_Scanner_ButterflyTask_FullOutput_%sRun%s_%s' % (expInfo['1) Study Prefix'],expInfo['1) Study Prefix'],expInfo['2) Subject ID'],expInfo['1) Study Prefix'],expInfo['2) Subject ID'],expInfo['3) Target Type'],expInfo['5) Run #'],expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/cjleschak/Downloads/Leschak_Prosocial ButterflyTask/S1_Butterfly2_Scanner.py',
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

# Initialize components for Routine "Scan_Instructions"
Scan_InstructionsClock = core.Clock()
#---------Payout Output -------------------
payout_filename = _thisDir + os.sep + u'data_bySubject/%s/%s_%s/PayoutFiles/%s_%s_ButterflyTask_Payout_%sRun%s_%s' % (expInfo['1) Study Prefix'],expInfo['1) Study Prefix'],expInfo['2) Subject ID'],expInfo['1) Study Prefix'],expInfo['2) Subject ID'],expInfo['3) Target Type'],expInfo['5) Run #'],expInfo['date'])
origin_Path        = _thisDir + os.sep+'S1_Butterfly2_Scanner.psyexp'

payoutOutput = data.ExperimentHandler(name=expName, version='',
    extraInfo    = None, runtimeInfo=None,
    originPath   = origin_Path,
    savePickle   = False, 
    saveWideText = True, dataFileName=payout_filename)

currentTrial = 1

import random
import numpy as np
totalTrials = list(range(1,61))
random.shuffle(totalTrials)
payoutTrials = totalTrials[0:15]


#---------Customizing Output -------------------
MinOutput_filename = _thisDir + os.sep + u'data_bySubject/%s/%s_%s/Butterfly/%s_%s_Scanner_ButterflyTask_MinOutput_%sRun%s_%s' % (expInfo['1) Study Prefix'],expInfo['1) Study Prefix'],expInfo['2) Subject ID'], expInfo['1) Study Prefix'],expInfo['2) Subject ID'],expInfo['3) Target Type'],expInfo['5) Run #'],expInfo['date'])
origin_Path        = _thisDir + os.sep+'S1_Butterfly2_Scanner.psyexp'

thisExp3 = data.ExperimentHandler(name=expName, version='',
    extraInfo    = None, runtimeInfo=None,
    originPath   = origin_Path,
    savePickle   = False, 
    saveWideText = True, dataFileName=MinOutput_filename)


#-----Define Window & Image Sizes---------------
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



#-----------------Get input info-------------------
studyPrefix = expInfo['1) Study Prefix']

subID    = expInfo['2) Subject ID']
subIDnum = int(subID)

targetType = expInfo['3) Target Type']
targetType = targetType.upper()

targetName = expInfo['4) Friend Name']
targetName = targetName.upper()

runNum    = expInfo['5) Run #']
runNumInt = int(runNum)
if runNum == '1':
    whoSlide       = 2
    butterflySlide = 3
    lastSlide      = 4
elif runNum == '2':
    whoSlide       = 2
    butterflySlide = 4
    lastSlide      = 5

WhoFor     = ''
if targetType == 'SELF':
    target = 'B'
    whoFor = 'YOU'
else:
    target = 'A'
    whoFor = targetName


#--------------Define variables used later-------------
leftFlowerImg      = ''
rightFlowerImg     = ''
whichFlowerLeft    = ''
whichFlowerRight   = ''
chosenSide         = ''
butterflyImg       = ''
whichButterfly     = ''
whoForTxt          = ''
objectList         = ''
objectOrder        = ''
position           = ''
select             = ''
currentObj         = ''
stim               = ''
selectionTotal     = 0
trialNum           = 0
runningTotal       = 0
InstructionLoopNum = 1
favSelected        = 0


#---------------Setup Directories/Main Paths----------
taskLocation      = _thisDir
taskFilesPath     = _thisDir+os.sep+'TaskFiles'+os.sep+'ButterflyFiles'
ObjectStim_Dir    = taskFilesPath+os.sep+'StimFolder'+os.sep+'Objects'
FlowerStim_Dir    = taskFilesPath+os.sep+'StimFolder'+os.sep+'Flowers'
ButterflyStim_Dir = taskFilesPath+os.sep+'StimFolder'+os.sep+'Butterflies'
instruct_Dir      = taskFilesPath+os.sep+'StimFolder'+os.sep+'OtherStims'+os.sep+'2_Task'+os.sep+'Round' + runNum
conditionFile     = taskFilesPath+os.sep+'ConditionFiles'+os.sep+'2_Task'+os.sep+'CondFile_Run'+runNum+'.xlsx'
CSVorderFile      = taskFilesPath+os.sep+'ConditionFiles'+os.sep+'2_Task'+os.sep+studyPrefix+'_Run' + runNum + 'ObjectOrders.csv'
butterflyFile     = taskFilesPath+os.sep+'ConditionFiles'+os.sep+'2_Task'+os.sep+studyPrefix+'_ButterflyOrders.csv'
playingForImg     = instruct_Dir +os.sep+'playingFor.JPG'
endImg            = instruct_Dir +os.sep+'End.JPG'


#----------Specifies which objects to use for this run.--------
import csv
with open(CSVorderFile) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for i, objectOrder in enumerate(readCSV):
        if i == subIDnum:
             break
objectOrder = [str(item).zfill(3) for item in objectOrder]

with open(butterflyFile) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for i, butterfly in enumerate(readCSV):
        if i == subIDnum:
             break
currentButterfly   = butterfly[runNumInt]


#-----------Start Program Clock-------------
TaskClock = core.Clock()
ExpOnset = TaskClock.getTime()

thisExp3.addData('trial','')
thisExp3.addData('Stimulus','instructions')
thisExp3.addData('Onset',ExpOnset)
instructionImg = visual.ImageStim(
    win=win, name='instructionImg',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=otherSize,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
PlayingforWho = visual.TextStim(win=win, name='PlayingforWho',
    text='default text',
    font='Arial Rounded MT Bold',
    pos=(0, -.05), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "crosshair"
crosshairClock = core.Clock()

fix2sec = visual.TextStim(win=win, name='fix2sec',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "PlayingFor"
PlayingForClock = core.Clock()

playinForwho = visual.ImageStim(
    win=win, name='playinForwho',
    image=playingForImg, mask=None,
    ori=0, pos=(0, 0), size=otherSize,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
targetNameTxt = visual.TextStim(win=win, name='targetNameTxt',
    text=whoFor,
    font='Arial Rounded MT Bold',
    pos=(0, -.2), height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "crosshair"
crosshairClock = core.Clock()

fix2sec = visual.TextStim(win=win, name='fix2sec',
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
    text=whoFor,
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

# Initialize components for Routine "fixation2"
fixation2Clock = core.Clock()

fixation2secs = visual.TextStim(win=win, name='fixation2secs',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()

Feedback = visual.TextStim(win=win, name='Feedback',
    text='default text',
    font='Arial Rounded MT Bold',
    pos=(0, .7), height=0.26, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
objectBorder = visual.Rect(
    win=win, name='objectBorder',
    width=objBorderSize[0], height=objBorderSize[1],
    ori=0, pos=(0, -.05),
    lineWidth=10, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
objectImg = visual.ImageStim(
    win=win, name='objectImg',
    image='sin', mask=None,
    ori=0, pos=(0, -.05), size=objSize,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "fixation"
fixationClock = core.Clock()

fixationTxt = visual.TextStim(win=win, name='fixationTxt',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "fixEnd"
fixEndClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);


# Initialize components for Routine "end"
endClock = core.Clock()
EndingScreen = visual.ImageStim(
    win=win, name='EndingScreen',
    image=endImg, mask=None,
    ori=0, pos=(0, 0), size=otherSize,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
instructionLoop = data.TrialHandler(nReps=1000, method='random', 
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
    
    # ------Prepare to start Routine "Scan_Instructions"-------
    t = 0
    Scan_InstructionsClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    #-----If end of instructions is reached, but 'advance to next-----
    #----instruction button' (e.g. 'right') is being pressed, keep ---
    #---displaying last instruction image ("Do you have questions")---
    #-----Only a "5" button press will advance to the actual task.----
    if InstructionLoopNum > lastSlide:
        InstructionLoopNum = lastSlide
    elif InstructionLoopNum < 1:
        InstructionLoopNum = 1
    
    if InstructionLoopNum == whoSlide:
        whoForTxt = whoFor
    else:
        whoForTxt = ''
    
    
    if InstructionLoopNum == butterflySlide:
        InstructionImgDisplayed = instruct_Dir + os.sep+'instruction_' + str(butterflySlide) + currentButterfly + '.JPG'
    else:
        InstructionImgDisplayed = instruct_Dir + os.sep+'instruction_' + str(InstructionLoopNum) + '.JPG'
    
    
    
    #-----------Get Time of Onset for each Instruction----------
    Onset = TaskClock.getTime()
    
    
    #------------Add Data to Full Output File--------------
    thisExp.addData('Stimulus','instructions')
    thisExp.addData('Onset',Onset)
    instructionImg.setImage(InstructionImgDisplayed)
    PlayingforWho.setText(whoForTxt)
    NextInstruction2 = event.BuilderKeyResponse()
    # keep track of which components have finished
    Scan_InstructionsComponents = [instructionImg, PlayingforWho, NextInstruction2]
    for thisComponent in Scan_InstructionsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Scan_Instructions"-------
    while continueRoutine:
        # get current time
        t = Scan_InstructionsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *instructionImg* updates
        if t >= 0.0 and instructionImg.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructionImg.tStart = t
            instructionImg.frameNStart = frameN  # exact frame index
            instructionImg.setAutoDraw(True)
        
        # *PlayingforWho* updates
        if t >= 0.0 and PlayingforWho.status == NOT_STARTED:
            # keep track of start time/frame for later
            PlayingforWho.tStart = t
            PlayingforWho.frameNStart = frameN  # exact frame index
            PlayingforWho.setAutoDraw(True)
        
        # *NextInstruction2* updates
        if t >= 0.0 and NextInstruction2.status == NOT_STARTED:
            # keep track of start time/frame for later
            NextInstruction2.tStart = t
            NextInstruction2.frameNStart = frameN  # exact frame index
            NextInstruction2.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(NextInstruction2.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if NextInstruction2.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right', '5'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if NextInstruction2.keys == []:  # then this was the first keypress
                    NextInstruction2.keys = theseKeys[0]  # just the first key pressed
                    NextInstruction2.rt = NextInstruction2.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Scan_InstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Scan_Instructions"-------
    for thisComponent in Scan_InstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #---If on the last instruction slide, and "5" is pressed,---
    #--------end Instruction Loop and proceed to task.----------
    #------When "5" is pressed, start actual task clock.--------
    if InstructionLoopNum > lastSlide - 1 and NextInstruction2.keys == '5':
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
    if NextInstruction2.keys == 'left':
        InstructionLoopNum = InstructionLoopNum - 1
    elif NextInstruction2.keys == 'right':
        InstructionLoopNum = InstructionLoopNum + 1
    
    
    #-------------Add Data-------------------
    if not NextInstruction2.keys == '5':
        Offset   = TaskClock.getTime()
        duration = Offset - Onset
        thisExp.addData('Offset',Offset)
        thisExp.addData('duration',duration)
    
    
    # check responses
    if NextInstruction2.keys in ['', [], None]:  # No response was made
        NextInstruction2.keys=None
    instructionLoop.addData('NextInstruction2.keys',NextInstruction2.keys)
    if NextInstruction2.keys != None:  # we had a response
        instructionLoop.addData('NextInstruction2.rt', NextInstruction2.rt)
    # the Routine "Scan_Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1000 repeats of 'instructionLoop'


# ------Prepare to start Routine "crosshair"-------
t = 0
crosshairClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
#---------Add Data--------------
Onset = TriggerClock.getTime()

thisExp.addData('Stimulus','+')
thisExp.addData('Onset',Onset)
thisExp.addData('flowerResponse.keys','')
thisExp.addData('flowerResponse.corr','')
thisExp.addData('flowerResponse.rt','')

thisExp3.addData('trial','')
thisExp3.addData('Stimulus','+')
thisExp3.addData('Onset',Onset)

# keep track of which components have finished
crosshairComponents = [fix2sec]
for thisComponent in crosshairComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "crosshair"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = crosshairClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *fix2sec* updates
    if t >= 0.0 and fix2sec.status == NOT_STARTED:
        # keep track of start time/frame for later
        fix2sec.tStart = t
        fix2sec.frameNStart = frameN  # exact frame index
        fix2sec.setAutoDraw(True)
    frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if fix2sec.status == STARTED and t >= frameRemains:
        fix2sec.setAutoDraw(False)
    
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
#---------Add Data--------------
Offset   = TriggerClock.getTime()
duration = Offset - Onset

thisExp.addData('Offset',Offset)
thisExp.addData('duration',duration)
thisExp.nextEntry()

thisExp3.addData('Offset',Offset)
thisExp3.addData('duration',duration)
thisExp3.nextEntry()

trialNum = 0

# ------Prepare to start Routine "PlayingFor"-------
t = 0
PlayingForClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
#---------Add Data--------------
Onset = TriggerClock.getTime()

thisExp.addData('Stimulus','PlayingFor')
thisExp.addData('Onset',Onset)

thisExp3.addData('trial','')
thisExp3.addData('Stimulus','PlayingFor')
thisExp3.addData('Onset',Onset)

targetNameTxt.setHeight(0.3)
# keep track of which components have finished
PlayingForComponents = [playinForwho, targetNameTxt]
for thisComponent in PlayingForComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "PlayingFor"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = PlayingForClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *playinForwho* updates
    if t >= 0.0 and playinForwho.status == NOT_STARTED:
        # keep track of start time/frame for later
        playinForwho.tStart = t
        playinForwho.frameNStart = frameN  # exact frame index
        playinForwho.setAutoDraw(True)
    frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
    if playinForwho.status == STARTED and t >= frameRemains:
        playinForwho.setAutoDraw(False)
    
    # *targetNameTxt* updates
    if t >= 0.0 and targetNameTxt.status == NOT_STARTED:
        # keep track of start time/frame for later
        targetNameTxt.tStart = t
        targetNameTxt.frameNStart = frameN  # exact frame index
        targetNameTxt.setAutoDraw(True)
    frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
    if targetNameTxt.status == STARTED and t >= frameRemains:
        targetNameTxt.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PlayingForComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "PlayingFor"-------
for thisComponent in PlayingForComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
#---------Add Data--------------
Offset   = TriggerClock.getTime()
duration = Offset - Onset


thisExp.addData('Offset',Offset)
thisExp.addData('duration',duration)
thisExp.nextEntry()

thisExp3.addData('Offset',Offset)
thisExp3.addData('duration',duration)
thisExp3.nextEntry()


# ------Prepare to start Routine "crosshair"-------
t = 0
crosshairClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
#---------Add Data--------------
Onset = TriggerClock.getTime()

thisExp.addData('Stimulus','+')
thisExp.addData('Onset',Onset)
thisExp.addData('flowerResponse.keys','')
thisExp.addData('flowerResponse.corr','')
thisExp.addData('flowerResponse.rt','')

thisExp3.addData('trial','')
thisExp3.addData('Stimulus','+')
thisExp3.addData('Onset',Onset)

# keep track of which components have finished
crosshairComponents = [fix2sec]
for thisComponent in crosshairComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "crosshair"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = crosshairClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *fix2sec* updates
    if t >= 0.0 and fix2sec.status == NOT_STARTED:
        # keep track of start time/frame for later
        fix2sec.tStart = t
        fix2sec.frameNStart = frameN  # exact frame index
        fix2sec.setAutoDraw(True)
    frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if fix2sec.status == STARTED and t >= frameRemains:
        fix2sec.setAutoDraw(False)
    
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
#---------Add Data--------------
Offset   = TriggerClock.getTime()
duration = Offset - Onset

thisExp.addData('Offset',Offset)
thisExp.addData('duration',duration)
thisExp.nextEntry()

thisExp3.addData('Offset',Offset)
thisExp3.addData('duration',duration)
thisExp3.nextEntry()

trialNum = 0

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
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    
    #-Specify position (left/right) for the two flowers/specify butterfly-------
    
    leftFlowerImg   = FlowerStim_Dir + os.sep+'Flower'+currentButterfly+str(leftFlower)+'.PNG'
    whichFlowerLeft = 'Flower'+currentButterfly+str(leftFlower)+'.PNG'
    rightFlowerImg  = FlowerStim_Dir + os.sep+'Flower'+currentButterfly+str(rightFlower)+'.PNG'
    whichFlowerRight= 'Flower'+currentButterfly+str(rightFlower)+'.PNG'
    favFlowerImg    = 'Flower'+currentButterfly+str(favFlower)+'.PNG'
    correctFlowerImg= 'Flower'+currentButterfly+str(correctFlower)+'.PNG'
    
    butterflyImg   = ButterflyStim_Dir + os.sep+'Butterfly_' + currentButterfly + str(butterfly) +'.JPG'
    whichButterfly = 'Butterfly_' + currentButterfly + str(butterfly) +'.JPG'
    
    
    #----Clear Selected Side each Repeat-------
    chosenSide = ''
    position   = [7,7]
    
    
    #-----------Add Data------------
    Onset = TriggerClock.getTime()
    
    thisExp.addData('Stimulus','butterfly')
    thisExp.addData('Onset',Onset)
    
    thisExp3.addData('trial',trialNum)
    thisExp3.addData('Stimulus','butterfly')
    thisExp3.addData('whichButterfly?',whichButterfly)
    thisExp3.addData('WhichFlowerLeft? (1)',whichFlowerLeft)
    thisExp3.addData('WhichFlowerRight? (2)',whichFlowerRight)
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
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = flowerStimClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        #----Determine which key was pressed-------
        if flowerResponse.keys == '1':
            chosenSide = 'L'
        elif flowerResponse.keys == '2':
            chosenSide = 'R'
        
        #----Determine location of response box-------
        if chosenSide == 'L':
            position = [-.4,.1]
        elif chosenSide == 'R':
            position = [.4,.1]
        else:
            position = [7,7]
        
        # *leftFlower_img* updates
        if t >= 0.0 and leftFlower_img.status == NOT_STARTED:
            # keep track of start time/frame for later
            leftFlower_img.tStart = t
            leftFlower_img.frameNStart = frameN  # exact frame index
            leftFlower_img.setAutoDraw(True)
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if leftFlower_img.status == STARTED and t >= frameRemains:
            leftFlower_img.setAutoDraw(False)
        
        # *rightFlower_img* updates
        if t >= 0.0 and rightFlower_img.status == NOT_STARTED:
            # keep track of start time/frame for later
            rightFlower_img.tStart = t
            rightFlower_img.frameNStart = frameN  # exact frame index
            rightFlower_img.setAutoDraw(True)
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if rightFlower_img.status == STARTED and t >= frameRemains:
            rightFlower_img.setAutoDraw(False)
        
        # *butterfly_img* updates
        if t >= 0.0 and butterfly_img.status == NOT_STARTED:
            # keep track of start time/frame for later
            butterfly_img.tStart = t
            butterfly_img.frameNStart = frameN  # exact frame index
            butterfly_img.setAutoDraw(True)
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if butterfly_img.status == STARTED and t >= frameRemains:
            butterfly_img.setAutoDraw(False)
        
        # *targetReminder* updates
        if t >= 0.0 and targetReminder.status == NOT_STARTED:
            # keep track of start time/frame for later
            targetReminder.tStart = t
            targetReminder.frameNStart = frameN  # exact frame index
            targetReminder.setAutoDraw(True)
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
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
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
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
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
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
    #The favorite flower was selected by sub
    if str(favFlowerKey)==flowerResponse.keys:
        favSelected=1
    else:
        favSelected=0
    #The favorite flower was not selected by sub
    
    #---------Add Data---------------
    Offset   = TriggerClock.getTime()
    duration = Offset - Onset
    
    thisExp.addData('Offset',Offset)
    thisExp.addData('duration',duration)
    thisExp.addData('flowerResponse.keys',flowerResponse.keys)
    thisExp.addData('flowerResponse.corr',flowerResponse.corr)
    thisExp.addData('flowerResponse.rt',flowerResponse.rt)
    thisExp.addData('Favorite Flower',favFlowerImg)
    thisExp3.addData('Correct Flower',correctFlowerImg)
    thisExp3.addData('Correct Flower Key',correctKey)
    thisExp3.addData('Favorite Flower',favFlowerImg)
    thisExp3.addData('Favorite Flower Key',favFlowerKey)
    thisExp3.addData('Correct (1)/Incorrect (0)? (for that trial)',flowerResponse.corr)
    thisExp3.addData('Favorite Flower (1) selected or not (0)?',favSelected)
    thisExp.nextEntry()
    
    thisExp3.addData('Offset',Offset)
    thisExp3.addData('duration',duration)
    thisExp3.addData('Correct Flower',correctFlowerImg)
    thisExp3.addData('Correct Flower Key',correctKey)
    thisExp3.addData('Favorite Flower',favFlowerImg)
    thisExp3.addData('Favorite Flower Key',favFlowerKey)
    thisExp3.addData('Subject''s Key Press',flowerResponse.keys)
    thisExp3.addData('Correct (1)/Incorrect (0)? (for that trial)',flowerResponse.corr)
    thisExp3.addData('Favorite Flower (1) selected or not (0)?',favSelected)
    thisExp3.addData('Flower Response RT',flowerResponse.rt)
    thisExp3.nextEntry()
    
    
    #--------------
    
    #if the current trial is one of the selected trials,
    #add the current trial to the payout sheet
    #add the correct/incorrect for current trial to the payout sheet
    #if correct on current trial, add 1 to running total
    #add running total to payout sheet
    if currentTrial in payoutTrials:
        payoutOutput.addData('Selected Trials',currentTrial)
        payoutOutput.addData('Correct (1)/Incorrect (0)', flowerResponse.corr)
        if flowerResponse.corr == 1:
            runningTotal = runningTotal + 1
        else:
            runningTotal = runningTotal + 0
        payoutOutput.addData('Running Total',runningTotal)
        payoutOutput.nextEntry()
    
    
    
    currentTrial=currentTrial+1
    
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
    
    # ------Prepare to start Routine "fixation2"-------
    t = 0
    fixation2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    #------------------Add Data-----------------------
    Onset = TriggerClock.getTime()
    
    thisExp.addData('Stimulus','+')
    thisExp.addData('Onset',Onset)
    thisExp.addData('flowerResponse.keys','')
    thisExp.addData('flowerResponse.corr','')
    thisExp.addData('flowerResponse.rt','')
    
    thisExp3.addData('trial',trialNum)
    thisExp3.addData('Stimulus','+')
    thisExp3.addData('Onset',Onset)
    thisExp3.addData('trial',trialNum)
    
    # keep track of which components have finished
    fixation2Components = [fixation2secs]
    for thisComponent in fixation2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "fixation2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixation2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *fixation2secs* updates
        if t >= 0.0 and fixation2secs.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation2secs.tStart = t
            fixation2secs.frameNStart = frameN  # exact frame index
            fixation2secs.setAutoDraw(True)
        frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation2secs.status == STARTED and t >= frameRemains:
            fixation2secs.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixation2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation2"-------
    for thisComponent in fixation2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #------------------Add Data-----------------------
    Offset   = TriggerClock.getTime()
    duration = Offset - Onset
    
    thisExp.addData('Offset',Offset)
    thisExp.addData('duration',duration)
    thisExp.nextEntry()
    
    thisExp3.addData('Offset',Offset)
    thisExp3.addData('duration',duration)
    thisExp3.nextEntry()
    
    
    # ------Prepare to start Routine "feedback"-------
    t = 0
    feedbackClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    #-------Select current object---------
    currentObj = objectOrder[trialNum]
    currentObjFile = currentObj + '.JPG'
    
    Onset = TriggerClock.getTime()
    
    
    #------Determine feedback------------
    if not flowerResponse.keys:
        feedbackMsg     = 'OUT OF TIME'
        feedbackColor   = [1,-1,-1]
        borderColor     = [-1,-1,-1]
        objectImgPath   = ObjectStim_Dir +os.sep+'0 .JPG'
        objectDisplayed = ''
    elif flowerResponse.corr:
        feedbackMsg     = 'CORRECT'
        feedbackColor   = [-1.000,0.380,-0.412]
        borderColor     = [-1.000,0.380,-0.412]
        objectImgPath   = ObjectStim_Dir +os.sep + currentObj + '.JPG'
        objectDisplayed = currentObj + '.JPG'
    else:
        feedbackMsg     = 'INCORRECT'
        feedbackColor   = [1,-1,-1]
        borderColor     = [1,-1,-1]
        objectImgPath   = ObjectStim_Dir +os.sep + currentObj + '.JPG'
        objectDisplayed = currentObj + '.JPG'
    
    
    #--------Add Data--------------
    thisExp.addData('Stimulus','object/feedback')
    thisExp.addData('Onset',Onset)
    thisExp.addData('ObjectDisplayed',objectDisplayed)
    thisExp.addData('SelectedObject',currentObjFile)
    
    thisExp3.addData('trial',trialNum)
    thisExp3.addData('Stimulus','object/feedback')
    thisExp3.addData('Onset',Onset)
    thisExp3.addData('ObjectDisplayed',objectDisplayed)
    thisExp3.addData('SelectedObject',currentObjFile)
    
    Feedback.setColor(feedbackColor, colorSpace='rgb')
    Feedback.setText(feedbackMsg)
    objectBorder.setFillColor(borderColor)
    objectBorder.setLineColor(borderColor)
    objectImg.setImage(objectImgPath)
    # keep track of which components have finished
    feedbackComponents = [Feedback, objectBorder, objectImg]
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *Feedback* updates
        if t >= 0.0 and Feedback.status == NOT_STARTED:
            # keep track of start time/frame for later
            Feedback.tStart = t
            Feedback.frameNStart = frameN  # exact frame index
            Feedback.setAutoDraw(True)
        frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Feedback.status == STARTED and t >= frameRemains:
            Feedback.setAutoDraw(False)
        
        # *objectBorder* updates
        if t >= 0.0 and objectBorder.status == NOT_STARTED:
            # keep track of start time/frame for later
            objectBorder.tStart = t
            objectBorder.frameNStart = frameN  # exact frame index
            objectBorder.setAutoDraw(True)
        frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if objectBorder.status == STARTED and t >= frameRemains:
            objectBorder.setAutoDraw(False)
        
        # *objectImg* updates
        if t >= 0.0 and objectImg.status == NOT_STARTED:
            # keep track of start time/frame for later
            objectImg.tStart = t
            objectImg.frameNStart = frameN  # exact frame index
            objectImg.setAutoDraw(True)
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if objectImg.status == STARTED and t >= frameRemains:
            objectImg.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #------------Add Data------------------
    #thisExp.addData('SelectedTrial?',select)
    #thisExp.addData('RunningPayout',selectionTotal)
    
    Offset = TriggerClock.getTime()
    duration = Offset - Onset
    
    thisExp.addData('Offset',Offset)
    thisExp.addData('duration',duration)
    thisExp.nextEntry()
    
    thisExp3.addData('Offset',Offset)
    thisExp3.addData('duration',duration)
    thisExp3.nextEntry()
    
    
    # ------Prepare to start Routine "fixation"-------
    t = 0
    fixationClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    #-----------Add Data---------------
    Onset = TriggerClock.getTime()
    
    thisExp.addData('Stimulus','+')
    thisExp.addData('Onset',Onset)
    
    thisExp3.addData('trial',trialNum)
    thisExp3.addData('Stimulus','+')
    thisExp3.addData('Onset',Onset)
    
    # keep track of which components have finished
    fixationComponents = [fixationTxt]
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "fixation"-------
    while continueRoutine:
        # get current time
        t = fixationClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *fixationTxt* updates
        if t >= 0.0 and fixationTxt.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixationTxt.tStart = t
            fixationTxt.frameNStart = frameN  # exact frame index
            fixationTxt.setAutoDraw(True)
        frameRemains = 0.0 + jitter- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixationTxt.status == STARTED and t >= frameRemains:
            fixationTxt.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation"-------
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Offset   = TriggerClock.getTime()
    duration = Offset - Onset
    
    #---------Add Data-------------
    thisExp.addData('Offset',Offset)
    thisExp.addData('duration',duration)
    
    thisExp3.addData('Offset',Offset)
    thisExp3.addData('duration',duration)
    thisExp3.nextEntry()
    
    
    #---------Next Trial-------------
    trialNum = trialNum + 1
    
    if trialNum == 60:
        TrialLoop.finished = 1
    
    
    # the Routine "fixation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'TrialLoop'


# ------Prepare to start Routine "fixEnd"-------
t = 0
fixEndClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(10.000000)
# update component parameters for each repeat
#--------------Add Data------------
Onset = TriggerClock.getTime()

thisExp.addData('Stimulus','+')
thisExp.addData('Onset',Onset)

thisExp3.addData('Stimulus','+')
thisExp3.addData('Onset',Onset)


# keep track of which components have finished
fixEndComponents = [text]
for thisComponent in fixEndComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "fixEnd"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixEndClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    frameRemains = 0.0 + 10- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text.status == STARTED and t >= frameRemains:
        text.setAutoDraw(False)
    
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixEndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fixEnd"-------
for thisComponent in fixEndComponents:
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
# keep track of which components have finished
endComponents = [EndingScreen]
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *EndingScreen* updates
    if t >= 0.0 and EndingScreen.status == NOT_STARTED:
        # keep track of start time/frame for later
        EndingScreen.tStart = t
        EndingScreen.frameNStart = frameN  # exact frame index
        EndingScreen.setAutoDraw(True)
    frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if EndingScreen.status == STARTED and t >= frameRemains:
        EndingScreen.setAutoDraw(False)
    
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









# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
