# Define each region with its settings

regions = [
    {
        "name": "top_left",
        "x_start": 0, "y_start": 0,
        "width": 200, "height": 200,
        "high_sound": "./l1/1.wav",
        "low_sound": "./l1/2.wav",
        "high_threshold": 10000, # Max - 10 aka 1.0
        "low_threshold": 1000, # Min - 1 aka 0
        "volume": 1
    },
    {
        "name": "top_right",
        "x_start": -200, "y_start": 0,
        "width": 200, "height": 200,
        "high_sound": "./l2/1.wav",
        "low_sound": "./l2/2.wav",
        "high_threshold": 10000, 
        "low_threshold": 1000,
        "volume": 0.4
    }
]