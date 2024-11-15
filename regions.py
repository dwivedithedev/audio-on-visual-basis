# Define each region with its settings

regions = [
    {
        "name": "A1",
        "x_start": 0, "y_start": 0,
        "width": 320, "height": 180,
        "zero": "./louder/1/0_alter.wav",
        "first": "./louder/1/1_alter.wav",
        "second": "./louder/1/2_alter.wav",
        "third": "./louder/1/3_alter.wav",
        "fourth": "./louder/1/4_alter.wav",
        "very_low_threshold": 1000, # 0.0
        "low_threshold": 2500, # 0.25
        "mid_threshold": 5000, # 0.5
        "high_threshold": 7500, # 0.75
        "very_high_threshold": 10000, # 1.0
        "volume": 0.25
    },
    {
        "name": "A2",
        "x_start": 0, "y_start": 180, #TODO: SET POSITIONS FOR EACH REGION.
        "width": 320, "height": 180,
        "zero": "./louder/2/0_alter.wav",
        "first": "./louder/2/1_alter.wav",
        "second": "./louder/2/2_alter.wav",
        "third": "./louder/2/3_alter.wav",
        "fourth": "./louder/2/4_alter.wav",
        "very_low_threshold": 1000, # 0.0
        "low_threshold": 2500, # 0.25
        "mid_threshold": 5000, # 0.5
        "high_threshold": 7500, # 0.75
        "very_high_threshold": 10000, # 1.0
        "volume": 0.05
    },
    {
        "name": "A3",
        "x_start": 0, "y_start": 360,
        "width": 320, "height": 180,
        "zero": "./louder/3/0_alter.wav",
        "first": "./louder/3/1_alter.wav",
        "second": "./louder/3/2_alter.wav",
        "third": "./louder/3/3_alter.wav",
        "fourth": "./louder/3/4_alter.wav",
        "very_low_threshold": 1000, # 0.0
        "low_threshold": 2500, # 0.25
        "mid_threshold": 5000, # 0.5
        "high_threshold": 7500, # 0.75
        "very_high_threshold": 10000, # 1.0
        "volume": 0.25
    },
    {
        "name": "A4",
        "x_start": 0, "y_start": 540,
        "width": 320, "height": 180,
        "zero": "./louder/4/0_alter.wav",
        "first": "./louder/4/1_alter.wav",
        "second": "./louder/4/2_alter.wav",
        "third": "./louder/4/3_alter.wav",
        "fourth": "./louder/4/4_alter.wav",
        "very_low_threshold": 1000, # 0.0
        "low_threshold": 2500, # 0.25
        "mid_threshold": 5000, # 0.5
        "high_threshold": 7500, # 0.75
        "very_high_threshold": 10000, # 1.0
        "volume": 0.05
    },
    {
        "name": "B1",
        "x_start": 320, "y_start": 0,
        "width": 320, "height": 180,
        "zero": "./louder/5/0_alter.wav",
        "first": "./louder/5/1_alter.wav",
        "second": "./louder/5/2_alter.wav",
        "third": "./louder/5/3_alter.wav",
        "fourth": "./louder/5/4_alter.wav",
        "very_low_threshold": 1000, # 0.0
        "low_threshold": 2500, # 0.25
        "mid_threshold": 5000, # 0.5
        "high_threshold": 7500, # 0.75
        "very_high_threshold": 10000, # 1.0
        "volume": 0.05
    },
    {
        "name": "B2",
        "x_start": 320, "y_start": 180,
        "width": 320, "height": 180,
        "zero": "./louder/6/0_alter.wav",
        "first":"./louder/6/0_alter.wav",
        "second": "./louder/6/1_alter.wav",
        "third": "./louder/6/1_alter.wav",
        "fourth": "./louder/6/2_alter.wav",
        "very_low_threshold": 1000, # 0.0
        "low_threshold": 2500, # 0.25
        "mid_threshold": 5000, # 0.5
        "high_threshold": 7500, # 0.75
        "very_high_threshold": 10000, # 1.0
        "volume": 0.05
    },
    {
        "name": "B3",
        "x_start": 320, "y_start": 360,
        "width": 320, "height": 180,
        "zero": "./louder/7/0_alter.wav",
        "first": "./louder/7/0_alter.wav",
        "second": "./louder/7/1_alter.wav",
        "third": "./louder/7/0_alter.wav",
        "fourth": "./louder/7/2_alter.wav",
        "very_low_threshold": 1000, # 0.0
        "low_threshold": 2500, # 0.25
        "mid_threshold": 5000, # 0.5
        "high_threshold": 7500, # 0.75
        "very_high_threshold": 10000, # 1.0
        "volume": 0.05
    },
    {
        "name": "B4",
        "x_start": 320, "y_start": 540,
        "width": 320, "height": 180,
        "zero": "./louder/8/0_alter.wav",
        "first": "./louder/8/0_alter.wav",
        "second": "./louder/8/1_alter.wav",
        "third": "./louder/8/1_alter.wav",
        "fourth": "./louder/8/2_alter.wav",
        "very_low_threshold": 1000, # 0.0
        "low_threshold": 2500, # 0.25
        "mid_threshold": 5000, # 0.5
        "high_threshold": 7500, # 0.75
        "very_high_threshold": 10000, # 1.0
        "volume": 0.05
    },
    {
        "name": "C1",
        "x_start": 640, "y_start": 0,
        "width": 320, "height": 180,
        "zero": "./louder/9/0_alter.wav",
        "first": "./louder/9/0_alter.wav",
        "second": "./louder/9/1_alter.wav",
        "third": "./louder/9/2_alter.wav",
        "fourth": "./louder/9/2_alter.wav",
        "very_low_threshold": 1000, # 0.0
        "low_threshold": 2500, # 0.25
        "mid_threshold": 5000, # 0.5
        "high_threshold": 7500, # 0.75
        "very_high_threshold": 10000, # 1.0
        "volume": 0.05
    },
    {
        "name": "C2",
        "x_start": 640, "y_start": 180,
        "width": 320, "height": 180,
        "zero": "./louder/10/0_alter.wav",
        "first": "./louder/10/0_alter.wav",
        "second": "./louder/10/1_alter.wav",
        "third": "./louder/10/0_alter.wav",
        "fourth": "./louder/10/2_alter.wav",
        "very_low_threshold": 1000, # 0.0
        "low_threshold": 2500, # 0.25
        "mid_threshold": 5000, # 0.5
        "high_threshold": 7500, # 0.75
        "very_high_threshold": 10000, # 1.0
        "volume": 1
    },
    {
        "name": "C3",
        "x_start": 640, "y_start": 360,
        "width": 320, "height": 180,
        "zero": "./louder/11/0_alter.wav",
        "first": "./louder/11/0_alter.wav",
        "second": "./louder/11/0_alter.wav",
        "third": "./louder/11/0_alter.wav",
        "fourth": "./louder/11/0_alter.wav",
        "very_low_threshold": 1000, # 0.0
        "low_threshold": 2500, # 0.25
        "mid_threshold": 5000, # 0.5
        "high_threshold": 7500, # 0.75
        "very_high_threshold": 10000, # 1.0
        "volume": 0.05
    },
    {
        "name": "C4",
        "x_start": 640, "y_start": 540,
        "width": 320, "height": 180,
        "zero": "./louder/12/0_alter.wav",
        "first": "./louder/12/0_alter.wav",
        "second": "./louder/12/0_alter.wav",
        "third": "./louder/12/0_alter.wav",
        "fourth": "./louder/12/0_alter.wav",
        "very_low_threshold": 1000, # 0.0
        "low_threshold": 2500, # 0.25
        "mid_threshold": 5000, # 0.5
        "high_threshold": 7500, # 0.75
        "very_high_threshold": 10000, # 1.0
        "volume": 0.05
    },
    {
        "name": "D1",
        "x_start": 960, "y_start": 0,
        "width": 320, "height": 180,
        "zero": "./louder/13/0_alter.wav",
        "first": "./louder/13/0_alter.wav",
        "second": "./louder/13/0_alter.wav",
        "third": "./louder/13/0_alter.wav",
        "fourth": "./louder/13/0_alter.wav",
        "very_low_threshold": 1000, # 0.0
        "low_threshold": 2500, # 0.25
        "mid_threshold": 5000, # 0.5
        "high_threshold": 7500, # 0.75
        "very_high_threshold": 10000, # 1.0
        "volume": 0.05
    },
    {
        "name": "D2",
        "x_start": 960, "y_start": 180,
        "width": 320, "height": 180,
        "zero": "./louder/14/0_alter.wav",
        "first": "./louder/14/0_alter.wav",
        "second": "./louder/14/0_alter.wav",
        "third": "./louder/14/0_alter.wav",
        "fourth": "./louder/14/0_alter.wav",
        "very_low_threshold": 1000, # 0.0
        "low_threshold": 2500, # 0.25
        "mid_threshold": 5000, # 0.5
        "high_threshold": 7500, # 0.75
        "very_high_threshold": 10000, # 1.0
        "volume": 0.05
    },
    {
        "name": "D3",
        "x_start": 960, "y_start": 360,
        "width": 320, "height": 180,
        "zero": "./louder/15/0_alter.wav",
        "first": "./louder/15/0_alter.wav",
        "second": "./louder/15/0_alter.wav",
        "third": "./louder/15/0_alter.wav",
        "fourth": "./louder/15/0_alter.wav",
        "very_low_threshold": 1000, # 0.0
        "low_threshold": 2500, # 0.25
        "mid_threshold": 5000, # 0.5
        "high_threshold": 7500, # 0.75
        "very_high_threshold": 10000, # 1.0
        "volume": 0.05
    },
    {
        "name": "D4",
        "x_start": 960, "y_start": 540,
        "width": 320, "height": 180,
        "zero": "./louder/15/0_alter.wav",
        "first": "./louder/15/0_alter.wav",
        "second": "./louder/15/0_alter.wav",
        "third": "./louder/15/0_alter.wav",
        "fourth": "./louder/15/0_alter.wav",
        "very_low_threshold": 1000, # 0.0
        "low_threshold": 2500, # 0.25
        "mid_threshold": 5000, # 0.5
        "high_threshold": 7500, # 0.75
        "very_high_threshold": 10000, # 1.0
        "volume": 0.05
    },
]