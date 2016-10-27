# seleniumdemo
  
DESCRIPTION  
This project is the demonstration of selenium, an GUI automated testing tool.
It contains two python scripts and a Linux bash shell script.
We use these scripts to get the voice message from WeChat public account,
and convert the voice to text, then reply the text to WeChat.
  
ENVIRONMENT  
These scripts were tested at Ubuntu Desktop 16.04  
  
PRE-CONDITION  
1. Register a WeChat public account  
2. Install Selenium, refer to http://www.seleniumhq.org/  as well as Firefox/Chrominum and their WebDriver. Here is the WebDriver for Chrominum: https://sites.google.com/a/chromium.org/chromedriver/downloads  
3. Build pocketsphinx, refer to http://cmusphinx.sourceforge.net/wiki/tutorialpocketsphinx  
4. Need some other tools like ffmpeg (https://www.ffmpeg.org/) and jq (https://stedolan.github.io/jq/)  
  
GET IT WORK  
1. Get these shell scripts to local  
2. Execute the 1st python script to login WeChat public account (need to scan the QR code by mobile phone)  
3. After login, execute the 2nd python script to deal with the WeChat messages  
  
HOW IT WORKS  
1. The python script will triger the web browser to check the unreplied voice message every several seconds  
2. It will download the voice file (.mpe) from the unreplied voice message, and convert the file to .wav via ffmpeg  
3. Then use pocketsphinx to conert the .wav to .txt  
4. Finally, reply the text back to WeChat account by Selenium  
  
THANKS TO  
Thanks to sphinx. Because of this project, we don't need to pay the online speech-to-text service like Google or IBM provides.  
Thanks for the idea from anthony(at)nicodemus.club  
  
CONTACT US  
Any question please email to anthony.wsy(at)gmail.com  
  
WHY WE OPEN THIS PROJECT  
We have another similar project https://github.com/anthonywsy/pocketsphinxdemo to deal with the voice message from telegram bot.
Unfortunately, in China mainland, most of the people cannot visit telegram. That's why we use WeChat. 
And we also has no budget to rent a server to communicate with WeChat server. 
We have to use the client side -  a web based management page to deal with the message, though it's not stable.  
  
-The End-    
