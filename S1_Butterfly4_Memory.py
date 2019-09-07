#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.3),
    on Fri Sep  6 20:32:35 2019
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
expName = 'S1_Butterfly4_Memory'  # from the Builder filename that created this script
expInfo = {'2) Subject ID': 'e.g. 000', '1) Study Prefix': 'GIV or PRO'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data_bySubject/%s/%s_%s/Butterfly/%s_%s_Memory_ButterflyTask_FullOutput_%s' % (expInfo['1) Study Prefix'],expInfo['1) Study Prefix'],expInfo['2) Subject ID'], expInfo['1) Study Prefix'],expInfo['2) Subject ID'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/cjleschak/Downloads/Leschak_Prosocial ButterflyTask/S1_Butterfly4_Memory.py',
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

# Initialize components for Routine "Instruct"
InstructClock = core.Clock()
#---------Customizing Output -------------------
MinOutput_filename  = _thisDir + os.sep + u'data_bySubject/%s/%s_%s/Butterfly/%s_%s_Memory_ButterflyTask_MinOutput_%s' % (expInfo['1) Study Prefix'],expInfo['1) Study Prefix'],expInfo['2) Subject ID'], expInfo['1) Study Prefix'],expInfo['2) Subject ID'], expInfo['date'])
origin_Path         = _thisDir + os.sep+'S1_Butterfly4_Memory.psyexp'

thisExp3 = data.ExperimentHandler(name=expName, version='',
    extraInfo    = None, runtimeInfo=None,
    originPath   = origin_Path,
    savePickle   = False, saveWideText=True, 
    dataFileName = MinOutput_filename)


#------------Define Window & Image Sizes-------------------
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

objWidth  = .4
objHeight = objWidth*screenRatio
objSize   = (objWidth,objHeight)

studyPrefix    = expInfo['1) Study Prefix']
subID    = expInfo['2) Subject ID']
subIDnum = int(subID)


#-------------Specify Directories/Main Paths---------------
taskLocation      = _thisDir
taskFilesPath     = _thisDir+os.sep+'TaskFiles'+os.sep+'ButterflyFiles'
ObjectStim_Dir = taskFilesPath+os.sep+'StimFolder'+os.sep+'Objects'
instruct_Dir   = taskFilesPath+os.sep+'StimFolder'+os.sep+'OtherStims'+os.sep+'4_Memory'
memQ1          = taskFilesPath+os.sep+'StimFolder'+os.sep+'OtherStims'+os.sep+'4_Memory'+os.sep+'oldOrNew.JPG'
CSVorderFile1  = taskFilesPath+os.sep+'ConditionFiles'+os.sep+'2_Task'+os.sep+studyPrefix+'_Run1ObjectOrders.csv'
CSVorderFile2  = taskFilesPath+os.sep+'ConditionFiles'+os.sep+'2_Task'+os.sep+studyPrefix+'_Run2ObjectOrders.csv'
CSVmemTestFile = taskFilesPath+os.sep+'ConditionFiles'+os.sep+'4_Memory'+os.sep+studyPrefix+'_MemTestOrders.csv'
targetOrderCSV = taskFilesPath+os.sep+'ConditionFiles'+os.sep+'3_Test'+os.sep+studyPrefix+'_TargetOrder.csv'
endImg         = taskFilesPath+os.sep+'StimFolder'+os.sep+'OtherStims'+os.sep+'4_Memory'+os.sep+'endScreen.JPG'


#-----------------Define Variables for Later-----------------
objectOrder1       = ''
objectOrder2       = ''
corrAns            = ''
run1or2            = ''
target             = ''
position           = ''
memQ2              = ''
size               = [0,0]
trialNum           = 0
InstructionLoopNum = 1
durCalcd           = 9999




#-------Specifies all pictures files to be displayed---------#
#-----Selects 30 images possibly displayed in each run,------#
#-------and 60 new images not displayed in task runs---------#
#--------combines these in one list, and randomizes.---------#
import csv
import random
import numpy


with open(CSVmemTestFile) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for i, fullImgList in enumerate(readCSV):
        if i == subIDnum:
             break

with open(CSVorderFile1) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for i, objectOrder1 in enumerate(readCSV):
        if i == subIDnum:
             break

with open(CSVorderFile2) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for i, objectOrder2 in enumerate(readCSV):
        if i == subIDnum:
             break

objectOrder1 = [str(item).zfill(3) for item in objectOrder1]
objectOrder2 = [str(item).zfill(3) for item in objectOrder2]
fullImgList  = [str(item).zfill(3) for item in fullImgList]


#------Determines which pics were from Friend/Self run--------
import csv
with open(targetOrderCSV) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for i, target in enumerate(readCSV):
        if i == subIDnum:
             break


#-----------------Start Program Clock-------------------
TaskClock = core.Clock()
ExpOnset = TaskClock.getTime()

thisExp3.addData('trial','')
thisExp3.addData('Stimulus','instructions')
thisExp3.addData('Onset',ExpOnset)
Instruction = visual.ImageStim(
    win=win, name='Instruction',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=otherSize,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "oldOrNew"
oldOrNewClock = core.Clock()

oldOrNewImg = visual.ImageStim(
    win=win, name='oldOrNewImg',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=otherSize,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Object = visual.ImageStim(
    win=win, name='Object',
    image='sin', mask=None,
    ori=0, pos=(0, .1), size=objSize,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
oldNewBox = visual.Rect(
    win=win, name='oldNewBox',
    width=(0.26, 0.45)[0], height=(0.26, 0.45)[1],
    ori=0, pos=[0,0],
    lineWidth=6, lineColor=[1.000,1.000,1.000], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)

# Initialize components for Routine "Confidence"
ConfidenceClock = core.Clock()

confidenceImg = visual.ImageStim(
    win=win, name='confidenceImg',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=otherSize,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Object2 = visual.ImageStim(
    win=win, name='Object2',
    image='sin', mask=None,
    ori=0, pos=(0, .1), size=objSize,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
confBox = visual.Rect(
    win=win, name='confBox',
    width=(0.28, 0.45)[0], height=(0.28, 0.45)[1],
    ori=0, pos=[0,0],
    lineWidth=6, lineColor=[1.000,1.000,1.000], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)

# Initialize components for Routine "fixEnd"
fixEndClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);


# Initialize components for Routine "End"
EndClock = core.Clock()
endScreen = visual.ImageStim(
    win=win, name='endScreen',
    image=endImg, mask=None,
    ori=0, pos=(0, 0), size=otherSize,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)


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
    
    # ------Prepare to start Routine "Instruct"-------
    t = 0
    InstructClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    #-----If end of instructions is reached, but 'advance to next-----
    #----instruction button' (e.g. 'right') is being pressed, keep ---
    #---displaying last instruction image ("Do you have questions")---
    #-----Only a "5" button press will advance to the actual task.----
    if InstructionLoopNum > 14:
        InstructionLoopNum = 15
    if InstructionLoopNum < 1:
        InstructionLoopNum = 1
    
    
    #-----If 'left' button is pressed to go back in instructions------
    #--------call up appropriate instruction to be displayed.---------
    instructionImgDisplayed = instruct_Dir + os.sep+'memInstruct_' + str(InstructionLoopNum) + '.JPG'
    
    
    #-----------Get Time of Onset for each Instruction----------
    Onset = TaskClock.getTime()
    
    #-----------------Add Data---------------------
    thisExp.addData('Stimulus','instructions')
    thisExp.addData('Onset',Onset)
    Instruction.setImage(instructionImgDisplayed)
    nextInstruction = event.BuilderKeyResponse()
    # keep track of which components have finished
    InstructComponents = [Instruction, nextInstruction]
    for thisComponent in InstructComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Instruct"-------
    while continueRoutine:
        # get current time
        t = InstructClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *Instruction* updates
        if t >= 0.0 and Instruction.status == NOT_STARTED:
            # keep track of start time/frame for later
            Instruction.tStart = t
            Instruction.frameNStart = frameN  # exact frame index
            Instruction.setAutoDraw(True)
        
        # *nextInstruction* updates
        if t >= 0.0 and nextInstruction.status == NOT_STARTED:
            # keep track of start time/frame for later
            nextInstruction.tStart = t
            nextInstruction.frameNStart = frameN  # exact frame index
            nextInstruction.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(nextInstruction.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if nextInstruction.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right', '5'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if nextInstruction.keys == []:  # then this was the first keypress
                    nextInstruction.keys = theseKeys[0]  # just the first key pressed
                    nextInstruction.rt = nextInstruction.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstructComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Instruct"-------
    for thisComponent in InstructComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #---If on the last instruction slide, and "5" is pressed,---
    #--------end Instruction Loop and proceed to task.----------
    #------When "5" is pressed, start actual task clock.--------
    if InstructionLoopNum > 14 and nextInstruction.keys == '5':
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
    
    
    
    #---Allow backward and forward movement within instruction loop.----
    if nextInstruction.keys == 'left':
        InstructionLoopNum = InstructionLoopNum - 1
    elif nextInstruction.keys == 'right':
        InstructionLoopNum = InstructionLoopNum + 1
    
    
    #------------------Add Data-----------------------
    if not nextInstruction.keys == '5':
        Offset   = TaskClock.getTime()
        duration = Offset - Onset
        thisExp.addData('Offset',Offset)
        thisExp.addData('duration',duration)
    # check responses
    if nextInstruction.keys in ['', [], None]:  # No response was made
        nextInstruction.keys=None
    instructionLoop.addData('nextInstruction.keys',nextInstruction.keys)
    if nextInstruction.keys != None:  # we had a response
        instructionLoop.addData('nextInstruction.rt', nextInstruction.rt)
    # the Routine "Instruct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1000 repeats of 'instructionLoop'


# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=120, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "oldOrNew"-------
    t = 0
    oldOrNewClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    durCalcd = 9999
    position = [7,7]
    
    #---------Select current picture to display----------
    currentImg = ObjectStim_Dir + os.sep + fullImgList[trialNum] + '.JPG'
    ImgName    = fullImgList[trialNum] + '.JPG'
    
    
    #------Records whether selected picture was seen-------
    #--------------before & in which run-------------------
    if fullImgList[trialNum] in objectOrder1:
        corrAns = '1'
        run1or2 = '1'
        seenFor = target[1]
    elif fullImgList[trialNum] in objectOrder2:
        corrAns = '1'
        run1or2 = '2'
        seenFor = target[2]
    else:
        corrAns = '2'
        run1or2 = '0'
        seenFor = ''
    
    
    
    #-----------Save Onset of Old/New question------------
    Onset1 = TriggerClock.getTime()
    
    oldOrNewImg.setImage(memQ1)
    Object.setImage(currentImg)
    oldNew_resp = event.BuilderKeyResponse()
    # keep track of which components have finished
    oldOrNewComponents = [oldOrNewImg, Object, oldNew_resp, oldNewBox]
    for thisComponent in oldOrNewComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "oldOrNew"-------
    while continueRoutine:
        # get current time
        t = oldOrNewClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if oldNew_resp.keys == '1':
            position = [-.345,-.52]
        elif oldNew_resp.keys == '2':
            position = [.35,-.52]
        else:
            position = [7,7]
        
        
        if not str(oldNew_resp.rt) == '[]':
            durCalcd=float(str(oldNew_resp.rt)) + .5
        
        # *oldOrNewImg* updates
        if t >= 0.0 and oldOrNewImg.status == NOT_STARTED:
            # keep track of start time/frame for later
            oldOrNewImg.tStart = t
            oldOrNewImg.frameNStart = frameN  # exact frame index
            oldOrNewImg.setAutoDraw(True)
        frameRemains = 0.0 + durCalcd- win.monitorFramePeriod * 0.75  # most of one frame period left
        if oldOrNewImg.status == STARTED and t >= frameRemains:
            oldOrNewImg.setAutoDraw(False)
        
        # *Object* updates
        if t >= 0.0 and Object.status == NOT_STARTED:
            # keep track of start time/frame for later
            Object.tStart = t
            Object.frameNStart = frameN  # exact frame index
            Object.setAutoDraw(True)
        frameRemains = 0.0 + durCalcd- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Object.status == STARTED and t >= frameRemains:
            Object.setAutoDraw(False)
        
        # *oldNew_resp* updates
        if t >= 0.0 and oldNew_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            oldNew_resp.tStart = t
            oldNew_resp.frameNStart = frameN  # exact frame index
            oldNew_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(oldNew_resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + durCalcd- win.monitorFramePeriod * 0.75  # most of one frame period left
        if oldNew_resp.status == STARTED and t >= frameRemains:
            oldNew_resp.status = FINISHED
        if oldNew_resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if oldNew_resp.keys == []:  # then this was the first keypress
                    oldNew_resp.keys = theseKeys[0]  # just the first key pressed
                    oldNew_resp.rt = oldNew_resp.clock.getTime()
        
        # *oldNewBox* updates
        if t >= 0.0 and oldNewBox.status == NOT_STARTED:
            # keep track of start time/frame for later
            oldNewBox.tStart = t
            oldNewBox.frameNStart = frameN  # exact frame index
            oldNewBox.setAutoDraw(True)
        frameRemains = 0.0 + durCalcd- win.monitorFramePeriod * 0.75  # most of one frame period left
        if oldNewBox.status == STARTED and t >= frameRemains:
            oldNewBox.setAutoDraw(False)
        if oldNewBox.status == STARTED:  # only update if drawing
            oldNewBox.setPos(position, log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in oldOrNewComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "oldOrNew"-------
    for thisComponent in oldOrNewComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #----Save offset of old/new question & calculate duration----
    Offset1   = TriggerClock.getTime()
    duration1 = Offset - Onset
    
    
    #-----Did they correctly identify the image as old/new?-----
    if corrAns == oldNew_resp.keys:
        CorrectorIncorrect = '1'
    else:
        CorrectorIncorrect = '0'
    
    
    #------------Add Data to Full Output File------------
    thisExp.addData('Stimulus','Is this image old (1) or new (2)?')
    thisExp.addData('Onset',Onset1)
    thisExp.addData('oldNew_correctAnswer', corrAns)
    thisExp.addData('seenWhen?',run1or2)
    thisExp.addData('seenFor?',seenFor)
    thisExp.addData('ImageFile', ImgName)
    thisExp.addData('ImageNum', fullImgList[trialNum])
    thisExp.addData('Offset',Offset1)
    thisExp.addData('duration',duration1)
    thisExp.addData('Correct (1) or Incorrect (0) Response?', CorrectorIncorrect)
    thisExp.addData('oldNew_resp.keys',oldNew_resp.keys)
    thisExp.addData('oldNew_resp.rt',oldNew_resp.rt)
    thisExp.nextEntry()
    
    # check responses
    if oldNew_resp.keys in ['', [], None]:  # No response was made
        oldNew_resp.keys=None
    trials.addData('oldNew_resp.keys',oldNew_resp.keys)
    if oldNew_resp.keys != None:  # we had a response
        trials.addData('oldNew_resp.rt', oldNew_resp.rt)
    # the Routine "oldOrNew" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Confidence"-------
    t = 0
    ConfidenceClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    durCalcd=9999
    position=[7,7]
    
    #-----Select appropriate confidence image to display----------
    #---------------based on old/new response---------
    if oldNew_resp.keys=='1':
        memQ2 = instruct_Dir+os.sep+'confidentOld.JPG'
    elif oldNew_resp.keys=='2':
        memQ2 = instruct_Dir+os.sep+'confidentNew.JPG'
    
    
    #-----------Save Onset of Old/New question------------
    Onset2 = TriggerClock.getTime()
    
    confidenceImg.setImage(memQ2)
    Object2.setImage(currentImg)
    confidence_resp = event.BuilderKeyResponse()
    # keep track of which components have finished
    ConfidenceComponents = [confidenceImg, Object2, confidence_resp, confBox]
    for thisComponent in ConfidenceComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Confidence"-------
    while continueRoutine:
        # get current time
        t = ConfidenceClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if confidence_resp.keys == '1':
            position=[-.465,-.54]
        elif confidence_resp.keys == '2':
            position = [-.155,-.54]
        elif confidence_resp.keys == '3':
            position = [.16,-.54]
        elif confidence_resp.keys == '4':
            position = [.47,-.54]
        else:
            position=[7,7]
        
        
        if not str(confidence_resp.rt)=='[]':
            durCalcd=float(str(confidence_resp.rt)) + .5
        
        # *confidenceImg* updates
        if t >= 0.0 and confidenceImg.status == NOT_STARTED:
            # keep track of start time/frame for later
            confidenceImg.tStart = t
            confidenceImg.frameNStart = frameN  # exact frame index
            confidenceImg.setAutoDraw(True)
        frameRemains = 0.0 + durCalcd- win.monitorFramePeriod * 0.75  # most of one frame period left
        if confidenceImg.status == STARTED and t >= frameRemains:
            confidenceImg.setAutoDraw(False)
        
        # *Object2* updates
        if t >= 0.0 and Object2.status == NOT_STARTED:
            # keep track of start time/frame for later
            Object2.tStart = t
            Object2.frameNStart = frameN  # exact frame index
            Object2.setAutoDraw(True)
        frameRemains = 0.0 + durCalcd- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Object2.status == STARTED and t >= frameRemains:
            Object2.setAutoDraw(False)
        
        # *confidence_resp* updates
        if t >= 0.0 and confidence_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            confidence_resp.tStart = t
            confidence_resp.frameNStart = frameN  # exact frame index
            confidence_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(confidence_resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + durCalcd- win.monitorFramePeriod * 0.75  # most of one frame period left
        if confidence_resp.status == STARTED and t >= frameRemains:
            confidence_resp.status = FINISHED
        if confidence_resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2', '3', '4'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if confidence_resp.keys == []:  # then this was the first keypress
                    confidence_resp.keys = theseKeys[0]  # just the first key pressed
                    confidence_resp.rt = confidence_resp.clock.getTime()
        
        # *confBox* updates
        if t >= 0.0 and confBox.status == NOT_STARTED:
            # keep track of start time/frame for later
            confBox.tStart = t
            confBox.frameNStart = frameN  # exact frame index
            confBox.setAutoDraw(True)
        frameRemains = 0.0 + durCalcd- win.monitorFramePeriod * 0.75  # most of one frame period left
        if confBox.status == STARTED and t >= frameRemains:
            confBox.setAutoDraw(False)
        if confBox.status == STARTED:  # only update if drawing
            confBox.setPos(position, log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ConfidenceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Confidence"-------
    for thisComponent in ConfidenceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #----Save offset of old/new question & calculate duration----
    Offset2 = TriggerClock.getTime()
    duration2 = Offset - Onset
    
    
    #---------Add Data to Full Output File-------------
    thisExp.addData('ImageFile', ImgName)
    thisExp.addData('ImageNum', fullImgList[trialNum])
    thisExp.addData('oldNew_correctAnswer', corrAns)
    thisExp.addData('seenWhen?',run1or2)
    thisExp.addData('seenFor?',seenFor)
    thisExp.addData('Stimulus','How confident are you? (1) Completely sure -> (4) Just guessing')
    thisExp.addData('Onset',Onset2)
    thisExp.addData('Offset',Offset2)
    thisExp.addData('duration',duration2)
    thisExp.addData('confidence_resp.keys',confidence_resp.keys)
    thisExp.addData('confidence_resp.rt',confidence_resp.rt)
    thisExp.addData('oldNew_resp.keys','')
    thisExp.addData('oldNew_resp.rt','')
    
    
    #--------Add Data to Minimal Output File------------
    duration3=Offset2-Onset1
    thisExp3.addData('trial',trialNum)
    thisExp3.addData('Stimulus',ImgName)
    thisExp3.addData('Onset',Onset1)
    thisExp3.addData('Offset',Offset2)
    thisExp3.addData('duration',duration3)
    thisExp3.addData('oldNew_correctAnswer', corrAns)
    thisExp3.addData('seenWhen?',run1or2)
    thisExp3.addData('seenFor?',seenFor)
    thisExp3.addData('Correct (1) or Incorrect (0) Response for Old/New?', CorrectorIncorrect)
    thisExp3.addData('Is this image old (1) or new (2)?',oldNew_resp.keys)
    thisExp3.addData('oldNew_RT',oldNew_resp.rt)
    thisExp3.addData('How confident are you? (1) Completely sure -> (4) Just guessing',confidence_resp.keys)
    thisExp3.addData('Confidence_RT',confidence_resp.rt)
    thisExp3.nextEntry()
    
    
    #------------End Loop After 120 trials--------------
    trialNum = trialNum + 1
    if trialNum == 120:
        trials.Finished = 1
    # check responses
    if confidence_resp.keys in ['', [], None]:  # No response was made
        confidence_resp.keys=None
    trials.addData('confidence_resp.keys',confidence_resp.keys)
    if confidence_resp.keys != None:  # we had a response
        trials.addData('confidence_resp.rt', confidence_resp.rt)
    # the Routine "Confidence" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 120 repeats of 'trials'


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
    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
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


# ------Prepare to start Routine "End"-------
t = 0
EndClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
#Add Data to Output
Onset = TriggerClock.getTime()

thisExp.addData('Stimulus','EndScreen')
thisExp.addData('Onset',Onset)
# keep track of which components have finished
EndComponents = [endScreen]
for thisComponent in EndComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "End"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EndClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *endScreen* updates
    if t >= 0.0 and endScreen.status == NOT_STARTED:
        # keep track of start time/frame for later
        endScreen.tStart = t
        endScreen.frameNStart = frameN  # exact frame index
        endScreen.setAutoDraw(True)
    frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if endScreen.status == STARTED and t >= frameRemains:
        endScreen.setAutoDraw(False)
    
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
#Add Data to Output
Offset   = TriggerClock.getTime()
duration = Offset - Onset

#-----------Add Data to Full Output File-------------
thisExp.addData('Stimulus','End Screen')
thisExp.addData('Onset',Onset)
thisExp.addData('Offset',Offset)
thisExp.addData('duration',duration)





# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
