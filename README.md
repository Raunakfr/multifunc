<h1>StudyGuard: A discipline enforcement system with a syllabus Parser, focus mode, voice alert
</h1>
This is a personal project I made for honing my python skills further.</br>
Basically a productivity-focused system designed to minimize distractions and enforce disciplined study sessions.</br>
This project is entirely self coded by me, only hints from ChatGPT and syntax from documentations.
<h1>
  ⭐ Key Features:
<h1>
<h2>
    1. Syllabus parser:
<h2>
    <h4>
      This can effectively parse the provided syllabus from syllabus.txt and display it in a VERY legible manner helping you stay organised.</br>
      To use your own syllabus, kindly add your syllabus to 'syllabys.txt' in the following format:</br>
      Subject 1 name, Unit I, Unit I name: Topic 1, topic 2, ... topic n, Unit II, Unit II name: Topic 1, topic 2, ...... Unit n, Unit n name, topic 1, .......... || Subject 2 name, Unit 1, Unit I name:...... So on and so forth
    <h4>
  <h2>
    2. Active app monitor:
  </h2>
  <h4>
    Disclaimer: All the data is processed on your local machine. No data is being collected or sent externally</br>
    The python script, along with acting as a parser, actively monitors what apps you have open on your PC and when focus mode is on, it closes them immediately.
  </h4>
  <h2>
    3. Active browser tab monitor:
  </h2>
  <h4>
    With the help of a separately developed browser extension, this script can even block those websites which you don't want to open during your focus/study sessions.
  </h4>
  <h2>
    4. Notification and Voice based alert
  </h2>
  <h4>
    Whenever a distraction is detected, the system triggers a notification, a voice alert, and forcefully closes the tab/app.
  </h4>
<h1>
  ⭐ Libraries used:
</h1>
<h3>
  In python script: 
<h3>
<h5>
  1. Datetime: For the timer during  focus mode.<br>
  2. Threading: VERY important. Used for waiting for user input along with monitoring the apps (two blocking actions done together).<br>
  3. Psutil: For app monitoring through process ids and names.<br>
  4. Time: For using the sleep function.<br>
</h5>
<h3>
  In extension script:
</h3>
<h5>
  1. chrome.tabs.onUpdated.addListener: Setting up listener to check for changes in tab URLs.<br>
  2. chrome.tts: Used for converting text to speech for the voice alert.<br>
  3. chrome.notifications.create: Used for creating the warning notification.<br>
</h5>
<h1>
  ⭐How to use:
</h1>
<h3>
  Step 1: Download the zip file from this repo by clicking on the green "Code<>" button.<br>
  Step 2: Place the three files, namely, 'background.js', 'manifest.json', 'icon1.png', into a separate folder, and the rest of the files into another one.<br>
  Step 3: Open your browser and go to "Chrome://extensions".<br>
  Step 4: On the top right corner, toggle 'developer mode' to on.<br>
  Step 5: On the top left, click on load unpacked and select the folder in which you have placed, 'background.js', 'manifest.json' and 'icon1.png'.<br>
  Step 6: After the extension is loaded, click on details.<br>
  Step 7: Scroll down and toggle "Allow access to file URLs" and 'Automatically allow access on these sites" (Should be on by default).<br>
  Step 8: Open python IDLE, on the top left corner, click on "File" and then "Open" and then navigate to the folder where "Syllabus tracker ++ Ext features" is located and double click to open it in the idle. After that, click on the "Run" tab and then on "Run Module" option and Voila!.<br> NOTE: If you haven't installed IDLE, kindly install it from "https://www.python.org"
</h3>
<h1>
  ⭐Future Updates
</h1>
<h3>
  In the future, I plan to do the following.<br>
</h3>
<h5>
  1. Add a better looking UI instead of the bland python terminal.<br>
  2. Fix the bug in the timer which doesn't count the time correctly in some cases.<br>
  3. Switch from file based extension toggle to Flask server.<br>
  4. Improve the code readability.<br>
  5. Improve the TTS voice.<br>
  6. Add a hands free mode using voice commands.<br>
  7. Add analytics dashboard to track distraction attempts.<br>
  8. Add an option to mark topics as done and more.<br>
</h5>
