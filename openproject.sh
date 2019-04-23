#!/bin/bash
#open client
osascript -e 'tell application "Terminal" to activate' -e 'tell application "System Events" to tell process "Terminal" to keystroke "t" using command down'

osascript -e 'tell application "Terminal" to do script "cd client_select" in selected tab of the front window'
osascript -e 'tell application "Terminal" to do script "open client.py tkgui.py" in selected tab of the front window'
osascript -e 'tell application "Terminal" to do script "clear" in selected tab of the front window'
osascript -e 'tell application "Terminal" to do script "pwd" in selected tab of the front window'
osascript -e 'tell application "Terminal" to do script "ls" in selected tab of the front window'
#open server
osascript -e 'tell application "Terminal" to activate' -e 'tell application "System Events" to tell process "Terminal" to keystroke "t" using command down'
osascript -e 'tell application "Terminal" to do script "cd .." in selected tab of the front window'
osascript -e 'tell application "Terminal" to do script "cd server_select" in selected tab of the front window'
osascript -e 'tell application "Terminal" to do script "open server_select.py user.py" in selected tab of the front window'
osascript -e 'tell application "Terminal" to do script "clear" in selected tab of the front window'
osascript -e 'tell application "Terminal" to do script "pwd" in selected tab of the front window'
osascript -e 'tell application "Terminal" to do script "ls" in selected tab of the front window'
pwd
ls
