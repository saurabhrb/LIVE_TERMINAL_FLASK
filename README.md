# LIVE_TERMINAL_FLASK
Features:
- live stream of console over Flask server using websockets
- user input is also handled
- 'python'\command wont work, but 'python your_file.py arg1 arg2' will work
- adds a custom host "my_flask_liveterminal.com" to hosts file, which needs admin access for the first time run

Bugs:
- python 2.7:
  - raw_input('text') blocks the stdout read becoz of which 
    'text' gets displayed after the user input
- requirements only mentioned for Windows, still needs proper testing f all commands on MAC and Linux 

Working example:
- https://youtu.be/-x8RYNSLkbY
