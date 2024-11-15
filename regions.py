# Define each region with its settings

regions = [
    {
        "name": "TOP_LEFT",
        "x_start": 0, "y_start": 0,
        "width": 500, "height": 500,
        "zero": "./1/0.wav",
        "first": "./1/1.wav",
        "second": "./1/2.wav",
        "third": "./1/3.wav",
        "fourth": "./1/4.wav",
        "very_low_threshold": 1000, # 0.0
        "low_threshold": 2500, # 0.25
        "mid_threshold": 5000, # 0.5
        "high_threshold": 7500, # 0.75
        "very_high_threshold": 10000, # 1.0
        "volume": 1
    },
    {
        "name": "BOTTOM_LEFT",
        "x_start": 0, "y_start": 500, #TODO: SET POSITIONS FOR EACH REGION.
        "width": 500, "height": 500,
        "zero": "./2/0.wav",
        "first": "./2/1.wav",
        "second": "./2/2.wav",
        "third": "./2/3.wav",
        "fourth": "./2/4.wav",
        "very_low_threshold": 1000, # 0.0
        "low_threshold": 2500, # 0.25
        "mid_threshold": 5000, # 0.5
        "high_threshold": 7500, # 0.75
        "very_high_threshold": 10000, # 1.0
        "volume": 1
    },
    {
        "name": "TOP_RIGHT",
        "x_start": 500, "y_start": 0,
        "width": 500, "height": 500,
        "zero": "./3/0.wav",
        "first": "./3/1.wav",
        "second": "./3/2.wav",
        "third": "./3/3.wav",
        "fourth": "./3/4.wav",
        "very_low_threshold": 1000, # 0.0
        "low_threshold": 2500, # 0.25
        "mid_threshold": 5000, # 0.5
        "high_threshold": 7500, # 0.75
        "very_high_threshold": 10000, # 1.0
        "volume": 1
    },
    {
        "name": "BOTTOM_RIGHT",
        "x_start": 500, "y_start": 500,
        "width": 500, "height": 500,
        "zero": "./4/0.wav",
        "first": "./4/1.wav",
        "second": "./4/2.wav",
        "third": "./4/3.wav",
        "fourth": "./4/4.wav",
        "very_low_threshold": 1000, # 0.0
        "low_threshold": 2500, # 0.25
        "mid_threshold": 5000, # 0.5
        "high_threshold": 7500, # 0.75
        "very_high_threshold": 10000, # 1.0
        "volume": 1
    },
    # {
    #     "name": "five_stem_region_five",
    #     "x_start": 0, "y_start": 0,
    #     "width": 500, "height": 500,
    #     "zero": "./5/0.wav",
    #     "first": "./5/1.wav",
    #     "second": "./5/2.wav",
    #     "third": "./5/3.wav",
    #     "fourth": "./5/4.wav",
    #     "very_low_threshold": 1000, # 0.0
    #     "low_threshold": 2500, # 0.25
    #     "mid_threshold": 5000, # 0.5
    #     "high_threshold": 7500, # 0.75
    #     "very_high_threshold": 10000, # 1.0
    #     "volume": 1
    # },
    # {
    #     "name": "three_stem_region_one",
    #     "x_start": 0, "y_start": 0,
    #     "width": 500, "height": 500,
    #     "zero": "./6/0.wav",
    #     "second": "./6/1.wav",
    #     "fourth": "./6/2.wav",
    #     "very_low_threshold": 1000, # 0.0
    #     "low_threshold": 2500, # 0.25
    #     "mid_threshold": 5000, # 0.5
    #     "high_threshold": 7500, # 0.75
    #     "very_high_threshold": 10000, # 1.0
    #     "volume": 1
    # },
    # {
    #     "name": "three_stem_region_two",
    #     "x_start": 0, "y_start": 0,
    #     "width": 500, "height": 500,
    #     "zero": "./7/0.wav",
    #     "second": "./7/1.wav",
    #     "fourth": "./7/2.wav",
    #     "very_low_threshold": 1000, # 0.0
    #     "low_threshold": 2500, # 0.25
    #     "mid_threshold": 5000, # 0.5
    #     "high_threshold": 7500, # 0.75
    #     "very_high_threshold": 10000, # 1.0
    #     "volume": 1
    # },
    # {
    #     "name": "three_stem_region_three",
    #     "x_start": 0, "y_start": 0,
    #     "width": 500, "height": 500,
    #     "zero": "./8/0.wav",
    #     "second": "./8/1.wav",
    #     "fourth": "./8/2.wav",
    #     "very_low_threshold": 1000, # 0.0
    #     "low_threshold": 2500, # 0.25
    #     "mid_threshold": 5000, # 0.5
    #     "high_threshold": 7500, # 0.75
    #     "very_high_threshold": 10000, # 1.0
    #     "volume": 1
    # },
    # {
    #     "name": "three_stem_region_four",
    #     "x_start": 0, "y_start": 0,
    #     "width": 500, "height": 500,
    #     "zero": "./9/0.wav",
    #     "second": "./9/1.wav",
    #     "fourth": "./9/2.wav",
    #     "very_low_threshold": 1000, # 0.0
    #     "low_threshold": 2500, # 0.25
    #     "mid_threshold": 5000, # 0.5
    #     "high_threshold": 7500, # 0.75
    #     "very_high_threshold": 10000, # 1.0
    #     "volume": 1
    # },
    # {
    #     "name": "three_stem_region_five",
    #     "x_start": 0, "y_start": 0,
    #     "width": 500, "height": 500,
    #     "zero": "./10/0.wav",
    #     "second": "./10/1.wav",
    #     "fourth": "./10/2.wav",
    #     "very_low_threshold": 1000, # 0.0
    #     "low_threshold": 2500, # 0.25
    #     "mid_threshold": 5000, # 0.5
    #     "high_threshold": 7500, # 0.75
    #     "very_high_threshold": 10000, # 1.0
    #     "volume": 1
    # },
    # {
    #     "name": "one_stem_region_one",
    #     "x_start": 0, "y_start": 0,
    #     "width": 500, "height": 500,
    #     "zero": "./11/0.wav",
    #     "very_low_threshold": 1000, # 0.0
    #     "low_threshold": 2500, # 0.25
    #     "mid_threshold": 5000, # 0.5
    #     "high_threshold": 7500, # 0.75
    #     "very_high_threshold": 10000, # 1.0
    #     "volume": 1
    # },
    # {
    #     "name": "one_stem_region_two",
    #     "x_start": 0, "y_start": 0,
    #     "width": 500, "height": 500,
    #     "first": "./12/0.wav",
    #     "very_low_threshold": 1000, # 0.0
    #     "low_threshold": 2500, # 0.25
    #     "mid_threshold": 5000, # 0.5
    #     "high_threshold": 7500, # 0.75
    #     "very_high_threshold": 10000, # 1.0
    #     "volume": 1
    # },
    # {
    #     "name": "one_stem_region_three",
    #     "x_start": 0, "y_start": 0,
    #     "width": 500, "height": 500,
    #     "second": "./12/0.wav",
    #     "very_low_threshold": 1000, # 0.0
    #     "low_threshold": 2500, # 0.25
    #     "mid_threshold": 5000, # 0.5
    #     "high_threshold": 7500, # 0.75
    #     "very_high_threshold": 10000, # 1.0
    #     "volume": 1
    # },
    # {
    #     "name": "one_stem_region_four",
    #     "x_start": 0, "y_start": 0,
    #     "width": 500, "height": 500,
    #     "third": "./12/0.wav",
    #     "very_low_threshold": 1000, # 0.0
    #     "low_threshold": 2500, # 0.25
    #     "mid_threshold": 5000, # 0.5
    #     "high_threshold": 7500, # 0.75
    #     "very_high_threshold": 10000, # 1.0
    #     "volume": 1
    # },
    # {
    #     "name": "one_stem_region_five",
    #     "x_start": 0, "y_start": 0,
    #     "width": 500, "height": 500,
    #     "fourth": "./12/0.wav",
    #     "very_low_threshold": 1000, # 0.0
    #     "low_threshold": 2500, # 0.25
    #     "mid_threshold": 5000, # 0.5
    #     "high_threshold": 7500, # 0.75
    #     "very_high_threshold": 10000, # 1.0
    #     "volume": 1
    # },
]