# Key-Logger
This tool is a keylogger program written in Python using the pynput library. It captures and logs keyboard input, recording each key pressed by the user. The program writes the key presses into a file (keyfile.txt), storing them as strings, including both alphanumeric characters and special keys (like "Enter", "Shift", or "Space").

Key Features:
Keyboard Event Listener: The program uses the pynput.keyboard.Listener to monitor keypress events in real-time.

Logging Keypresses: It logs each keypress into a text file by converting the key to a string and appending it to the log. This includes both characters and special keys.

Error Handling: The program tries to handle errors, such as issues with non-character keys (e.g., function keys), ensuring the logging process isn't interrupted.

Purpose:
This tool could be used for debugging keyboard input, monitoring user interaction for security purposes, or as part of research in user behavior. However, it's important to note that keyloggers can be used maliciously, so ethical and legal considerations must be taken into account when using or developing such tools.
