# settings.py

# Configuration settings for eye movement monitoring

# Dimensions of the bounding box for eye movement detection
BOUNDS_X = 100  # X-coordinate of the top-left corner of the bounding box
BOUNDS_Y = 100  # Y-coordinate of the top-left corner of the bounding box
BOUNDS_WIDTH = 400  # Width of the bounding box
BOUNDS_HEIGHT = 200  # Height of the bounding box

# Sensitivity thresholds for eye movement detection
SENSITIVITY_THRESHOLD_X = 0.05  # Sensitivity for horizontal movement
SENSITIVITY_THRESHOLD_Y = 0.05  # Sensitivity for vertical movement

# Other parameters
MONITORING_INTERVAL = 1  # Time in seconds between monitoring checks
ENABLE_ALERTS = True  # Flag to enable or disable alerts for eye movement detection