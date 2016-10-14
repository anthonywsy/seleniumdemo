#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import os

##################### GLOBAL ###################################
VOICEDIR = "/home/anthony/Downloads/"
##################### FUNCTION ##################################

#delete files
def deleteFiles ():
	#cmd = "rm " + VOICEDIR + "*.mp3*"
	cmd = "mv "+VOICEDIR+"*.mp3* "+VOICEDIR+"History/"
	os.system (cmd)
	return

#read from file
def readOneLinefromFile (fileName):
	iLoop = 1
	strReturn = "Sth err at recognizing your msg, pls try again."
	while (iLoop < 10):
		if os.path.isfile(fileName):
			try:
				f = open(fileName,'r')
				strReturn = f.readline()
				print "readOneLinefromFile - : ",strReturn
				f.close()
				return strReturn
			except IOError:
				print "readOneLinefromFile - IOError."
				strReturn = "Something error at recognizing your message, please try again."
		else:
			print "readOneLinefromFile - cannot find the file to read. wait 1 sec"
		time.sleep (1)
		iLoop = iLoop + 1
	return strReturn

#get mp3 file name
def getFileName ():
	iLoop = 1
	strFileName = ""
	while ( iLoop < 10 ):
		for file in os.listdir(VOICEDIR):
			if file.endswith(".mp3"):
				if os.path.isfile(VOICEDIR+file):
					print "getFileName - find mp3 file: ",file
					strFileName = file
					return strFileName
				else:
					print "getFileName - no mp3 file"
			else:
				print "getFileName - cannot find mp3 file"
		time.sleep(1)
		iLoop = iLoop + 1
	return strFileName


#call speech2text.sh
def speech2text ():
	fileName = getFileName()
	returnTxt = ""
	if fileName == "":
		returnTxt = "Cannot recognize your voice, please try again."
		print "speech2text - "+returnTxt
	else:
		mp3File = str(VOICEDIR) + str(fileName)
		cmd = "./04_speech2text.sh " + mp3File
		#cmd = "echo \"hi~\" > "+mp3File+".wav.txt"
		print ("start to execute cmd: "+cmd)
		os.system (cmd)
		returnTxt = readOneLinefromFile(mp3File+".wav.txt")
		#returnTxt = "this is a demo text."
		print "speech2text - speech text is: ",returnTxt
	return returnTxt


#Download the voice file
def downloadVoice (elmt):
	print "downloadVoice - elmt id: "+elmt.get_attribute("id")
	try:
		els = elmt.find_elements_by_class_name("icon18_common")
		for e in els:
			eCls = e.get_attribute("class")
			if eCls == "icon18_common download_gray":
				print "downloadVoice - Find download button: ",e.text
				e.click()
	except NoSuchElementException:
		print "downloadVoice - cannot find download button(s)"
	return

#Reply voice msg
def replyVoiceMsg (elmt):
	downloadVoice (elmt)
	replyTxt = speech2text ()
	#replyTxt = "demo"
	clickReplyBtn (elmt)
	#time.sleep (1)
	fillTxt (elmt,"You said:"+replyTxt)
	#time.sleep (1)
	clickSendBtn (elmt)
	#time.sleep (1)
	#clickFoldBtn (elmt)
	deleteFiles ()
	return

#To deal with the un-reply message
#click the send button
def clickSendBtn (elmt):
	print "clickSendBtn - elmt id: "+elmt.get_attribute("id")
	try:
		els = elmt.find_elements_by_class_name("js_reply_OK")
		for e in els:
			eCls = e.get_attribute("class")
			if eCls == "js_reply_OK":
				print "clickSendBtn - Find send button: ",e.text
				#print "clickSendBtn - data-id: ",e.get_attribute("data-id")
				#print "clickSendBtn - data-fakeid: ",e.get_attribute("data-fakeid")
				#print "clickSendBtn - sleep a sec"
				#time.sleep(1)
				e.click()
	except NoSuchElementException:
		print "clickSendBtn - cannot find send button(s)"
	return

#return the reply text according to the income text
def what2reply (txt):
	print "income txt: ",txt
	if txt == "7":
		reTxt = "I don't know your command."
	else:
		reTxt = "I don't know your text message."
	return reTxt

#Fill in the text to reply
def fillTxt (elmt, txt):
	print "fillTxt - elmt id: "+elmt.get_attribute("id")
	try:
		els = elmt.find_elements_by_class_name("edit_area")
		for e in els:
			eCls = e.get_attribute("class")
			eCtn = e.get_attribute("contenteditable")
			if eCls == "edit_area js_editorArea" and eCtn == "true":
				print "fillTxt - Find text input area, input: "+txt
				#print "fillTxt - wait a sec"
				#time.sleep (1)
				e.send_keys(txt)
	except NoSuchElementException:
		print "fillTxt - cannot find text input area(s)"
	return

#After click send button, click fold button
def clickFoldBtn (elmt):
	print "clickFoldBtn - elmt id: "+elmt.get_attribute("id")
	try:
		els = elmt.find_elements_by_class_name("js_reply_pickup")
		for e in els:
			eCls = e.get_attribute("class")
			if eCls == "js_reply_pickup btn btn_default pickup":
				print "clickFoldBtn - Find fold button: ",e.text
				e.click()
	except NoSuchElementException:
		print "clickFoldBtn - cannot find fold button(s)"
	return

#click reply btn
def clickReplyBtn (elmt):
	print "clickReplyBtn - elmt id: "+elmt.get_attribute("id")
	try:
		els = elmt.find_elements_by_class_name("icon18_common")
		for e in els:
			eCls = e.get_attribute("class")
			if eCls == "icon18_common reply_gray js_reply":
				print "clickReplyBtn - Find reply button: ",e.text
				e.click()
				#print "clickReplyBtn - sleep a sec"
				#time.sleep(1)
	except NoSuchElementException:
		print "clickReplyBtn - cannot find reply button(s)"
	return

#Reply text msg
def replyTxtMsg (elmt, txt):
	print "replyTxtMsg - elmt id: "+elmt.get_attribute("id")
	clickReplyBtn (elmt)
	fillTxt (elmt,what2reply(txt))
	clickSendBtn (elmt)
	#clickFoldBtn (elmt)
	return

#To deal with the un-reply message
def dealMsg (elmt):
	print "dealMsg - elmt id: "+elmt.get_attribute("id")
	try:
		e = elmt.find_element_by_class_name("wxMsg")
		eCls = e.get_attribute("class")
		if eCls == "wxMsg ":
			print "dealMsg - This is a text msg: ",e.text
			replyTxtMsg (elmt, e.text)
		elif eCls == "wxMsg audio_primary":
			print "dealMsg - This is a voice msg."
			replyVoiceMsg (elmt)
		else:
			print "dealMsg - This is an unknow msg type."
	except NoSuchElementException:
		print "dealMsg - cannot find class wxMsg"
	return


###################### MAIN #########################

#f = open('session.txt','r')
#print f
#session_id = f.readline()
session_id = readOneLinefromFile('session.txt')
#print session_id
#f.close()

#f = open('url.txt','r')
#url = f.readline()
url = readOneLinefromFile('url.txt')
#print url
#f.close()

driver = webdriver.Remote(command_executor=url,desired_capabilities={})
driver.session_id = session_id
driver.implicitly_wait(10)
#print driver.title

iWait = 1


#click the MSG MGNT btn
try:
	eBtn = driver.find_element_by_xpath("//*[@id=\"menuBar\"]/dl[2]/dd[1]/a")
	print eBtn.text
	eBtn.click()
except NoSuchElementException:
	print "Main - cannot find menu-message button"

while (1==1):

	#Get the message_item (include replyed msgs)
	try:
		eMsgs = driver.find_elements_by_class_name("message_item")
	
	except NoSuchElementException:
		print "Main - cannot find message item(s)"
	
	print "loop for all elements"
	i = len(eMsgs)
	while (i > 0):
		i = i - 1
		eClass = eMsgs[i].get_attribute("class")
		if eClass == "message_item ":
			print "Main - it's not reply yet"
			dealMsg(eMsgs[i])
			iWait = 3
			break
		elif eClass == "message_item replyed":
			print "Main - it's replyed"
			iWait = 5
		else:
			print "Main - unkown class name"
			iWait = 7
	print "sleep for: " + str(iWait)
	time.sleep(iWait)
	driver.refresh()
