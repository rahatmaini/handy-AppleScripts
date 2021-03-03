tell application "System Events"
	set listOfProcesses to (name of every process where background only is false)
end tell

set whiteList to {"Finder", "BetterTouchTool"}

repeat with processName in listOfProcesses
	tell application "System Events"
		if not (exists (window 1 of process processName)) then
			if processName is not in whiteList then
				set appToQuit to processName as string
				set appToQuit to appToQuit & "\"'"
				do shell script "osascript -e 'quit app \"" & appToQuit
			end if
		end if
	end tell
end repeat