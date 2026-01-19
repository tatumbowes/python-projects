"""Functions used in preparing Guido's gorgeous lasagna."""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2 #minutes per layer

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining."""
    return EXPECTED_BAKE_TIME - elapsed_bake_time
    
def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time based on number of layers."""
    return number_of_layers * PREPARATION_TIME  

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate total elapsed time (prep + bake)."""
    prep_time = preparation_time_in_minutes(number_of_layers)
    return prep_time + elapsed_bake_time
