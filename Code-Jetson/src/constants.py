ALTITUDE           = 1.75  # meters above home position
ALTITUDE_FUZZINESS = 0.1  # meters around ALTITUDE to allow as error
MINIMUM_DISTANCE   = 4    # ideal meters away from person
BACKOFF_DISTANCE   = 3.6  # meters away from person to trigger backoff rule
HEARTBEAT_TIMEOUT  = 2    # seconds
YAW_RATE           = 25    # degrees per search loop
YAW_MAX_DAMP       = 5.0   # maxiumum damping value for yaw
SPEED              = 1.0    # m/s
DETECTION_THRESH   = 0.85 # Threshold at which a person is considered 'detected'
MOCK_FOV           = 70   # FOV for the mock camera in tests
MOCK_Z_MAX         = 10   # Max distance in meters for a detection
MOCK_FPS           = 60   # Mocked FPS value for detections
RADIUS_OF_EARTH    = 6378100.0  # in meters (for mock camera)