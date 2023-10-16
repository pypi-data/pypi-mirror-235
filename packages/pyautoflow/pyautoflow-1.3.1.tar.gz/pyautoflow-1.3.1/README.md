# pyautoflow

This library can control your keyboard and mouse to automate everyday tasks. It can take screenshots and screen recordings for you to check back in on later. Other basic functions include power control and system information. 

## Examples
```python
# Import the four base modules
from pyautoflow import controls, inputs, info, power
from info import *

# CONTROLS
# Press the "a" key
controls.press("a")

# Press and hold the "a" key for 5 seconds
controls.press_and_hold("a", 5)

# Type the string "Hello, world!"
controls.type("Hello, world!")

# Set the cursor location to 10, 11
controls.set_cursor(10, 11)

# Set the cursor location to the current location plus 10, 11
controls.set_cursor_rel(10, 11)

# Moves the cursor location to 10, 11 over 5 seconds
controls.move_cursor(10, 11, 5)

# Moves the cursor location to the current location plus 10, 11 over 5 seconds
controls.move_cursor_rel(10, 11, 5)

# Clicks at the current location
controls.click()

# Right clicks at the current location
controls.right_click()

# Presses and holds the left mouse button until released
controls.press_mouse(0)

# Presses and holds the right mouse button until released
controls.press_mouse(1)

# Releases the left mouse button
controls.release_mouse(0)

# Releases the left mouse button
controls.release_mouse(1)

# Drags the cursor from 10, 11 to 100, 101 over 1 second
controls.drag(10, 11, 100, 101, 1)

# Resets timer
reset_timer()

# Gets the time since the last timer reset
delta = get_timer()


# INPUTS
# Takes a screenshot
screen = screenshot()

# Takes a screenshot of the area 10, 11, 100, 101
screen = screenshot_area(10, 11, 100, 101)

# Saves the given image as "foo.png"
save_img(screen, "foobar.png")

# Starts recording the screen as "bar.mp4"
start_recording("bar.mp4")

# Stops the screen recording
stop_recording()


# INFO
# Returns the CPU utilisation on each thread
utilisation = cpu.percent()

# Returns the number of CPU cores and threads
cores, threads = cpu.count()

# Returns info about the virtual RAM usage
virtual_info = ram.virtual()

# Returns info about the swap memory usage
swap_info = ram.swap()

# Returns info on all partitions detected
partition_info = disks.partitions()

# Returns info the main drive, such as the capacity used 
disk_usage = disk.usage()

# Returns a list of all processes currently running
pids = pids.pids()

# Returns a list of all of the IDs of currently running processes
ids = pids.ids()

# Returns info on the given ID
pid_id = pids.lookup(ids[1])

# Dumps all of the available info on the currently running processes to the terminal
pids.get()

# Returns info on the battery charge
battery_info = other.battery()

# Returns a list of all users on this device and some info
users = other.users()

# Returns the timestamp of the systems clock
timestamp = other.time()


# POWER
# Shutdown the computer
power.shutdown()

# Reboot the computer
power.reboot()
```

## TODO:
- Text recognition
- Microphone and camera input
- More advanced power controls