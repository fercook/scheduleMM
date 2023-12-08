# scheduleMM
ScheduleMM allows you to schedule posts for later in MatterMost.
Requires Python. It is developed for MacOS, but the Python script can be the re-used for Linux or Windows.

In order to use the MacOS app, 

1. Download the repository.
2. There are two important files, the DMG and the Python script. Open the DMG file, and drop the scheduleMM app wherever you want (can be the Applications folder, or a special folder, as long as you can remember where it is).
3. Place the Python script also in a place where you remember.
4. In your home folder, edit your .zshrc file to add these variables to the environment:
```bash
export MATTERMOST_LOGIN=YOUR_USERNAME
export MATTERMOST_PASSWORD=YOUR_PASSWORD
export MATTERMOST_SERVER_URL=THE_URL_FOR_THE_MATTERMOST_SERVER
export MATTERMOST_TEAM_NAME=YOUR_TEAM
```
5. Find out where you have a working Python installation, and copy the path to the python executable
6. Scroll to the last step in the workflow, and replace the paths in the app with the two paths you found (for Python and for the script)
7. Save the app and close Automator

IMPORTANT: MacOS has the at command disabled by default. In order to enable it, you must activate it, and also give the atrun command permission to save files in your disk. Follow [these directions](https://unix.stackexchange.com/questions/478823/making-at-work-on-macos/478840#478840)
