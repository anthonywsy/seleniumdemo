#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time


##################### FUNCTION ##################################

#Download the voice file
def downloadVoice (elmt):

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
	clickReplyBtn (elmt)
	fillTxt (elmt,"You said:")
	clickSendBtn (elmt)
	#clickFoldBtn (elmt)
	return

#To deal with the un-reply message
#click the send button
def clickSendBtn (elmt):
	try:
		els = elmt.find_elements_by_class_name("js_reply_OK")
		for e in els:
			eCls = e.get_attribute("class")
			if eCls == "js_reply_OK":
				print "clickSendBtn - Find send button: ",e.text
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
	try:
		els = elmt.find_elements_by_class_name("edit_area")
		for e in els:
			eCls = e.get_attribute("class")
			eCtn = e.get_attribute("contenteditable")
			if eCls == "edit_area js_editorArea" and eCtn == "true":
				print "fillTxt - Find text input area"
				e.send_keys(txt)
				#time.sleep (3)
	except NoSuchElementException:
		print "fillTxt - cannot find text input area(s)"
	return

#After click send button, click fold button
def clickFoldBtn (elmt):
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
	try:
		els = elmt.find_elements_by_class_name("icon18_common")
		for e in els:
			eCls = e.get_attribute("class")
			if eCls == "icon18_common reply_gray js_reply":
				print "clickReplyBtn - Find reply button: ",e.text
				e.click()
	except NoSuchElementException:
		print "clickReplyBtn - cannot find reply button(s)"
	return

#Reply text msg
def replyTxtMsg (elmt, txt):
	clickReplyBtn (elmt)
	fillTxt (elmt,what2reply(txt))
	clickSendBtn (elmt)
	#clickFoldBtn (elmt)
	return

#To deal with the un-reply message
def dealMsg (elmt):
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
f = open('session.txt','r')
#print f
session_id = f.readline()
#print session_id
f.close()

f = open('url.txt','r')
url = f.readline()
#print url
f.close()

driver = webdriver.Remote(command_executor=url,desired_capabilities={})
driver.session_id = session_id
driver.implicitly_wait(10)
#print driver.title

#click the MSG MGNT btn
eBtn = driver.find_element_by_xpath("//*[@id=\"menuBar\"]/dl[2]/dd[1]/a")
eBtn.click()

#Get the message_item (include replyed msgs)
eMsgs = driver.find_elements_by_class_name("message_item")

print "loop for all elements"
i = len(eMsgs)
while (i > 0):
	i = i - 1
	eClass = eMsgs[i].get_attribute("class")
	if eClass == "message_item ":
		print "Main - it's not reply yet"
		dealMsg(eMsgs[i])
		break
	elif eClass == "message_item replyed":
		print "Main - it's replyed"
	else:
		print "Main - unkown class name"

