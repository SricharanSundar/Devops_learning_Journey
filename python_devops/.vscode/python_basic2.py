import sys  # Import the sys module to access system-specific parameters and functions
import platform
import platform
print(platform.python_version_tuple())

print(platform.python_version())
# Print the Python version to the console
print("Python version")

# Use the sys.version attribute to get the Python version and print it
print(sys.version)

# Print information about the Python version
print("Version info.")

# Use the sys.version_info attribute to get detailed version information and print it
print(sys.version_info)

'''
Output:

('3', '11', '9')
3.11.9
Python version
3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)]
Version info.
sys.version_info(major=3, minor=11, micro=9, releaselevel='final', serial=0)
'''