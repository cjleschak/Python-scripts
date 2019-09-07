#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.3),
    on Fri Sep  6 20:31:50 2019
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
expName = 'S1_Butterfly1_Practice'  # from the Builder filename that created this script
expInfo = {'2) Subject ID': 'e.g. 000', '1) Study Prefix': 'GIV or PRO'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data_bySubject/%s/%s_%s/Practice/%s_%s_Practice_ButterflyTask_FullOutput_%s' % (expInfo['1) Study Prefix'],expInfo['1) Study Prefix'],expInfo['2) Subject ID'], expInfo['1) Study Prefix'],expInfo['2) Subject ID'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/cjleschak/Downloads/Leschak_Prosocial ButterflyTask/S1_Butterfly1_Practice.py',
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

# Initialize components for Routine "Practice_Instructions"
Practice_InstructionsClock = core.Clock()
#---------------Customizing Output --------------------
MinOutput_filename  = _thisDir + os.sep + u'data_bySubject/%s/%s_%s/Practice/%s_%s_Practice_ButterflyTask_MinOutput_%s' % (expInfo['1) Study Prefix'],expInfo['1) Study Prefix'],expInfo['2) Subject ID'], expInfo['1) Study Prefix'],expInfo['2) Subject ID'], expInfo['date'])
origin_Path         = os.path.join(_thisDir,'S1_Butterfly1_Practice.psyexp')

thisExp3 = data.ExperimentHandler(name=expName, version='', extraInfo = None, runtimeInfo=None,
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


#-----Define Variables Used Later--------------
leftFlowerImg   = ''
rightFlowerImg  = ''
chosenSide      = ''
position        = ''
currentObj      = ''
crosshairTxt    = ''
trialNum        = ''
currentObjFile  = ''
InstructionImgDisplayed = ''
InstructionLoopNum      = 1
NumOfInstructSlides = 28

#--------------Define Directories/Main Paths--------------------
taskLocation    = _thisDir
taskFilesPath   = os.path.join(_thisDir,'TaskFiles','ButterflyFiles')
ObjectStim_Dir  = os.path.join(taskFilesPath,'StimFolder','Objects')
FlowerStim_Dir  = os.path.join(taskFilesPath,'StimFolder','Flowers')
instruct_Dir    = os.path.join(taskFilesPath,'StimFolder','OtherStims','1_Practice')
butterflyImg    = os.path.join(taskFilesPath,'StimFolder','Butterflies','practice_Butterfly.JPG')
conditionFile   = os.path.join(taskFilesPath,'ConditionFiles','1_Practice','PracticeCondFile.xlsx')
practiceTrigger = os.path.join(instruct_Dir,'practiceTrigger.JPG')
endImg          = os.path.join(instruct_Dir,'PracticeEnd.JPG')
playingForImg   = os.path.join(instruct_Dir,'playingFor.JPG')
whichButterfly  = 'practice_Butterfly.JPG'


#------------------Start Program Clock-------------------
PracticeClock = core.Clock()
ExpOnset = PracticeClock.getTime()

thisExp3.addData('trial','')
thisExp3.addData('Stimulus','instructions')
thisExp3.addData('Onset',ExpOnset)
InstructionScreens = visual.ImageStim(
    win=win, name='InstructionScreens',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=otherSize,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
crossTxt = visual.TextStim(win=win, name='crossTxt',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "crosshair3"
crosshair3Clock = core.Clock()

text = visual.TextStim(win=win, name='text',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "PlayingFor"
PlayingForClock = core.Clock()

playinFor = visual.ImageStim(
    win=win, name='playinFor',
    image=playingForImg, mask=None,
    ori=0, pos=(0,0), size=otherSize,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
targetNameTxt = visual.TextStim(win=win, name='targetNameTxt',
    text='YOU',
    font='Arial Rounded MT Bold',
    pos=(0, -.2), height=0.25, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "crosshair"
crosshairClock = core.Clock()

fix2sec2 = visual.TextStim(win=win, name='fix2sec2',
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
    image=butterflyImg, mask=None,
    ori=0, pos=(0, -.6), size=BFSize,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
targetReminder = visual.TextStim(win=win, name='targetReminder',
    text='YOU',
    font='Arial Rounded MT Bold',
    pos=(0, .75), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
responseBorder = visual.Rect(
    win=win, name='responseBorder',
    width=(0.5, 0.8)[0], height=(0.5, 0.8)[1],
    ori=0, pos=[0,0],
    lineWidth=10, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)

# Initialize components for Routine "crosshair2"
crosshair2Clock = core.Clock()

fix2secs = visual.TextStim(win=win, name='fix2secs',
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
    pos=(0, .7), height=0.24, wrapWidth=None, ori=0, 
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
text_2 = visual.TextStim(win=win, name='text_2',
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


# Initialize components for Routine "loop"
loopClock = core.Clock()
afterLoopNum=1
keys2=''
afterPracImgDisplayed3=''
currentAfterImg=''
image = visual.ImageStim(
    win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=otherSize,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
instructionLoop = data.TrialHandler(nReps=1000, method='sequential', 
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
    
    # ------Prepare to start Routine "Practice_Instructions"-------
    t = 0
    Practice_InstructionsClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    #-----If end of instructions is reached, but 'advance to next-----
    #----instruction button' (e.g. 'right') is being pressed, keep ---
    #---displaying last instruction image ("Do you have questions")---
    #-----Only a "5" button press will advance to the actual task.----
    if InstructionLoopNum > NumOfInstructSlides-1:
        InstructionLoopNum = NumOfInstructSlides
    if InstructionLoopNum < 1:
        InstructionLoopNum = 1
    
    
    #-----Select Appropriate Instruction Screen to be Displayed-------
    InstructionImgDisplayed = os.path.join(instruct_Dir,'pracInstruct_' + str(InstructionLoopNum) + '.JPG')
    
    
    if InstructionLoopNum == NumOfInstructSlides:
        crosshairTxt='+'
    else:
        crosshairTxt=''
    
    
    
    #-----------Get Time of Onset for each Instruction----------
    Onset = PracticeClock.getTime()
    
    
    #------------Add Data to Full Output File--------------
    thisExp.addData('Stimulus','instructions')
    thisExp.addData('Onset',Onset)
    InstructionScreens.setImage(InstructionImgDisplayed)
    NextInstruction = event.BuilderKeyResponse()
    crossTxt.setText(crosshairTxt)
    # keep track of which components have finished
    Practice_InstructionsComponents = [InstructionScreens, NextInstruction, crossTxt]
    for thisComponent in Practice_InstructionsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Practice_Instructions"-------
    while continueRoutine:
        # get current time
        t = Practice_InstructionsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *InstructionScreens* updates
        if t >= 0.0 and InstructionScreens.status == NOT_STARTED:
            # keep track of start time/frame for later
            InstructionScreens.tStart = t
            InstructionScreens.frameNStart = frameN  # exact frame index
            InstructionScreens.setAutoDraw(True)
        
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
        
        # *crossTxt* updates
        if t >= 0.0 and crossTxt.status == NOT_STARTED:
            # keep track of start time/frame for later
            crossTxt.tStart = t
            crossTxt.frameNStart = frameN  # exact frame index
            crossTxt.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Practice_InstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Practice_Instructions"-------
    for thisComponent in Practice_InstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #---If on the last instruction slide, and "5" is pressed,---
    #--------end Instruction Loop and proceed to task.----------
    #------When "5" is pressed, start actual task clock.--------
    if InstructionLoopNum == NumOfInstructSlides and NextInstruction.keys == '5':
        InstrOffset = PracticeClock.getTime()
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
    
    
    
    #-------Allow forward/backward movement in instructions--------
    if NextInstruction.keys == 'left':
        InstructionLoopNum = InstructionLoopNum - 1
    elif NextInstruction.keys == 'right':
        InstructionLoopNum = InstructionLoopNum + 1
    
    
    
    #------------------Add Data-----------------------
    if not NextInstruction.keys == '5':
        Offset = PracticeClock.getTime()
        duration = Offset - Onset
        thisExp.addData('Offset',Offset)
        thisExp.addData('duration',duration)
    
    
    # check responses
    if NextInstruction.keys in ['', [], None]:  # No response was made
        NextInstruction.keys=None
    instructionLoop.addData('NextInstruction.keys',NextInstruction.keys)
    if NextInstruction.keys != None:  # we had a response
        instructionLoop.addData('NextInstruction.rt', NextInstruction.rt)
    # the Routine "Practice_Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1000 repeats of 'instructionLoop'


# ------Prepare to start Routine "crosshair3"-------
t = 0
crosshair3Clock.reset()  # clock
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

thisExp3.nextEntry()
thisExp3.addData('trial','')
thisExp3.addData('Stimulus','+')
thisExp3.addData('Onset',Onset)
# keep track of which components have finished
crosshair3Components = [text]
for thisComponent in crosshair3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "crosshair3"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = crosshair3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text.status == STARTED and t >= frameRemains:
        text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in crosshair3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "crosshair3"-------
for thisComponent in crosshair3Components:
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

# keep track of which components have finished
PlayingForComponents = [playinFor, targetNameTxt]
for thisComponent in PlayingForComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "PlayingFor"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = PlayingForClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *playinFor* updates
    if t >= 0.0 and playinFor.status == NOT_STARTED:
        # keep track of start time/frame for later
        playinFor.tStart = t
        playinFor.frameNStart = frameN  # exact frame index
        playinFor.setAutoDraw(True)
    frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
    if playinFor.status == STARTED and t >= frameRemains:
        playinFor.setAutoDraw(False)
    
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
crosshairComponents = [fix2sec2]
for thisComponent in crosshairComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "crosshair"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = crosshairClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *fix2sec2* updates
    if t >= 0.0 and fix2sec2.status == NOT_STARTED:
        # keep track of start time/frame for later
        fix2sec2.tStart = t
        fix2sec2.frameNStart = frameN  # exact frame index
        fix2sec2.setAutoDraw(True)
    frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if fix2sec2.status == STARTED and t >= frameRemains:
        fix2sec2.setAutoDraw(False)
    
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
    if leftFlower == 1:
        leftFlowerImg    = os.path.join(FlowerStim_Dir,'FlowerP1.JPG')
        whichFlowerLeft  = 'FlowerP1.JPG'
        rightFlowerImg   = os.path.join(FlowerStim_Dir,'FlowerP2.JPG')
        whichFlowerRight = 'FlowerP2.JPG'
    elif leftFlower == 2:
        leftFlowerImg    = os.path.join(FlowerStim_Dir,'FlowerP2.JPG')
        whichFlowerLeft  = 'FlowerP2.JPG'
        rightFlowerImg   = os.path.join(FlowerStim_Dir,'FlowerP1.JPG')
        whichFlowerRight = 'FlowerP1.JPG'
    
    position   = [7,7]
    chosenSide =''
    
    
    Onset = TriggerClock.getTime()
    
    #-----------Add Data------------
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
        if flowerResponse.keys   == '1':
            chosenSide = 'L'
        elif flowerResponse.keys == '2':
            chosenSide = 'R'
        
        #----Determine location of response box-------
        if chosenSide   == 'L':
            position     = [-.4,.1]
        elif chosenSide == 'R':
            position     = [.4,.1]
        else:
            position     = [7,7]
        
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
    #---------Add Data---------------
    Offset   = TriggerClock.getTime()
    duration = Offset - Onset
    
    thisExp.addData('Offset',Offset)
    thisExp.addData('duration',duration)
    thisExp.addData('flowerResponse.keys',flowerResponse.keys)
    thisExp.addData('flowerResponse.corr',flowerResponse.corr)
    thisExp.addData('flowerResponse.rt',flowerResponse.rt)
    thisExp.nextEntry()
    
    thisExp3.addData('Offset',Offset)
    thisExp3.addData('duration',duration)
    thisExp3.addData('Flower Selected?',flowerResponse.keys)
    thisExp3.addData('Correct Flower',correctFlower)
    thisExp3.addData('Correct(1)/Incorrect(0)?',flowerResponse.corr)
    thisExp3.addData('Flower Response RT',flowerResponse.rt)
    thisExp3.nextEntry()
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
    
    # ------Prepare to start Routine "crosshair2"-------
    t = 0
    crosshair2Clock.reset()  # clock
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
    
    thisExp3.addData('trial',trialNum)
    thisExp3.addData('Stimulus','+')
    thisExp3.addData('Onset',Onset)
    thisExp3.addData('trial',trialNum)
    
    
    
    # keep track of which components have finished
    crosshair2Components = [fix2secs]
    for thisComponent in crosshair2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "crosshair2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = crosshair2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *fix2secs* updates
        if t >= 0.0 and fix2secs.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix2secs.tStart = t
            fix2secs.frameNStart = frameN  # exact frame index
            fix2secs.setAutoDraw(True)
        frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fix2secs.status == STARTED and t >= frameRemains:
            fix2secs.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in crosshair2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "crosshair2"-------
    for thisComponent in crosshair2Components:
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
    
    
    # ------Prepare to start Routine "feedback"-------
    t = 0
    feedbackClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    #-------Select current object---------
    currentObj     = str(trialNum + 239)
    currentObjFile = currentObj + '.JPG'
    
    Onset = TriggerClock.getTime()
    
    
    #------Determine feedback------------
    if not flowerResponse.keys:
        feedbackMsg     = 'OUT OF TIME'
        feedbackColor   = [1,-1,-1]
        borderColor     = [-1,-1,-1]
        objectImgPath   = os.path.join(ObjectStim_Dir,'0 .JPG')
        objectDisplayed = ''
    elif flowerResponse.corr:
        feedbackMsg     = 'CORRECT'
        feedbackColor   = [-1.000,0.380,-0.412]
        borderColor     = [-1.000,0.380,-0.412]
        objectImgPath   = os.path.join(ObjectStim_Dir,currentObj + '.JPG')
        objectDisplayed = currentObj + '.JPG'
    else:
        feedbackMsg     = 'INCORRECT'
        feedbackColor   = [1,-1,-1]
        borderColor     = [1,-1,-1]
        objectImgPath   = os.path.join(ObjectStim_Dir,currentObj + '.JPG')
        objectDisplayed = currentObj + '.JPG'
    
    
    
    #----------------------Add Data-------------------------
    thisExp.addData('Stimulus','object/feedback')
    thisExp.addData('Onset',Onset)
    thisExp.addData('ObjectDisplayed',objectDisplayed)
    thisExp.addData('SelectedObject',currentObjFile)
    
    thisExp3.addData('trial',trialNum)
    thisExp3.addData('Stimulus','object/feedback')
    thisExp3.addData('Onset',Onset)
    thisExp3.addData('ObjectDisplayed?',objectDisplayed)
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
    Offset   = TriggerClock.getTime()
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
    
    #-----------Add Data---------------
    thisExp.addData('Offset',Offset)
    thisExp.addData('duration',duration)
    
    thisExp3.addData('Offset',Offset)
    thisExp3.addData('duration',duration)
    thisExp3.nextEntry()
    
    #----------Next Trial-------------
    trialNum = trialNum + 1
    # the Routine "fixation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'TrialLoop'


# ------Prepare to start Routine "fixEnd"-------
t = 0
fixEndClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
#--------------Add Data------------
Onset = TriggerClock.getTime()


thisExp.addData('Stimulus','+')
thisExp.addData('Onset',Onset)

thisExp3.addData('Stimulus','+')
thisExp3.addData('Onset',Onset)
# keep track of which components have finished
fixEndComponents = [text_2]
for thisComponent in fixEndComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "fixEnd"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixEndClock.getTime()
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
# update component parameters for each repeat
#---------Add Data--------------
Onset = TriggerClock.getTime()


thisExp.addData('Stimulus','End Screen')
thisExp.addData('Onset',Onset)


key_resp_3 = event.BuilderKeyResponse()
# keep track of which components have finished
endComponents = [EndingScreen, key_resp_3]
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "end"-------
while continueRoutine:
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
    
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['right'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            if key_resp_3.keys == []:  # then this was the first keypress
                key_resp_3.keys = theseKeys[0]  # just the first key pressed
                key_resp_3.rt = key_resp_3.clock.getTime()
                # a response ends the routine
                continueRoutine = False
    
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
#--------------Add Data------------
Offset   = TriggerClock.getTime()
duration = Offset - Onset





# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys=None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
afterPracLoop = data.TrialHandler(nReps=1000, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='afterPracLoop')
thisExp.addLoop(afterPracLoop)  # add the loop to the experiment
thisAfterPracLoop = afterPracLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisAfterPracLoop.rgb)
if thisAfterPracLoop != None:
    for paramName in thisAfterPracLoop:
        exec('{} = thisAfterPracLoop[paramName]'.format(paramName))

for thisAfterPracLoop in afterPracLoop:
    currentLoop = afterPracLoop
    # abbreviate parameter names if possible (e.g. rgb = thisAfterPracLoop.rgb)
    if thisAfterPracLoop != None:
        for paramName in thisAfterPracLoop:
            exec('{} = thisAfterPracLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "loop"-------
    t = 0
    loopClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    trialNum=0
    #-----If end of instructions is reached, but 'advance to next-----
    #----instruction button' (e.g. 'right') is being pressed, keep ---
    #---displaying last instruction image ("Do you have questions")---
    if afterLoopNum > 5:
        afterLoopNum = 5
    if afterLoopNum < 1:
        afterLoopNum = 1
    
    
    
    
    #-----Select Appropriate Instruction Screen to be Displayed-------
    if afterLoopNum==3:
        afterPracImgDisplayed=afterPracImgDisplayed3
    else:
        afterPracImgDisplayed = os.path.join(instruct_Dir,'afterPrac_' + str(afterLoopNum) + '.JPG')
    
    currentAfterImg='afterPrac_'+str(afterLoopNum)+'.JPG'
    
    #-----------Get Time of Onset for each Stim-----------
    Onset = PracticeClock.getTime()
    
    
    #------------Add Data to Full Output File--------------
    thisExp.addData('Stimulus',currentAfterImg)
    thisExp.addData('Onset',Onset)
    
    thisExp3.addData('trial','')
    thisExp3.addData('Stimulus',currentAfterImg)
    thisExp3.addData('Onset',Onset)
    
    image.setImage(afterPracImgDisplayed)
    key_resp_2 = event.BuilderKeyResponse()
    # keep track of which components have finished
    loopComponents = [image, key_resp_2]
    for thisComponent in loopComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "loop"-------
    while continueRoutine:
        # get current time
        t = loopClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *image* updates
        if t >= 0.0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        
        # *key_resp_2* updates
        if t >= 0.0 and key_resp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_2.tStart = t
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right', '1', '2', '3'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if key_resp_2.keys == []:  # then this was the first keypress
                    key_resp_2.keys = theseKeys[0]  # just the first key pressed
                    key_resp_2.rt = key_resp_2.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in loopComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "loop"-------
    for thisComponent in loopComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #-------Allow forward/backward movement in instructions--------
    if afterLoopNum==1:
        if key_resp_2.keys == 'left' or key_resp_2.keys == 'right':
            afterLoopNum = 1
        elif key_resp_2.keys == '1' or key_resp_2.keys == '2' or key_resp_2.keys=='3':
            afterLoopNum = afterLoopNum+1
    elif afterLoopNum==2:
        if key_resp_2.keys == 'left':
            afterLoopNum = afterLoopNum- 1
        elif key_resp_2.keys == 'right':
            afterLoopNum = afterLoopNum
        elif key_resp_2.keys == '1':
            afterLoopNum = afterLoopNum+1
            afterPracImgDisplayed3 = os.path.join(instruct_Dir,'afterPrac_' + str(afterLoopNum) + '_1.JPG')
        elif key_resp_2.keys == '2':
            afterLoopNum = afterLoopNum+1
            afterPracImgDisplayed3 = os.path.join(instruct_Dir,'afterPrac_' + str(afterLoopNum) + '_2.JPG')
    else:
        if key_resp_2.keys == 'left':
            afterLoopNum = afterLoopNum- 1
        elif key_resp_2.keys == 'right':
            afterLoopNum = afterLoopNum+ 1
    
    
    
    Offset   = TriggerClock.getTime()
    duration = Offset - Onset
    
    #-----------Add Data---------------
    thisExp.addData('Offset',Offset)
    thisExp.addData('duration',duration)
    
    thisExp3.addData('Offset',Offset)
    thisExp3.addData('duration',duration)
    
    if afterLoopNum-1==1:
        thisExp3.addData('Did you figure out the favorite? (1) Yes (2) Not sure (3) No idea',key_resp_2.keys)
    if afterLoopNum-1==2:
        thisExp3.addData('Which was the favorite? (1) blue (2) orange',key_resp_2.keys)
    
    thisExp3.nextEntry()
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys=None
    afterPracLoop.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        afterPracLoop.addData('key_resp_2.rt', key_resp_2.rt)
    # the Routine "loop" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1000 repeats of 'afterPracLoop'












# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
