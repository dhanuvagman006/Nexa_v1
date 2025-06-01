tools=[
    {
        "type": "function",
        "function": {
            "name": "turn_right",
            "description": "Turn right by given number of degrees",
            "parameters": {
                "type": "object",
                "properties": {
                    "degrees": {
                        "type": "integer",
                        "description": "Number of degrees to turn right"
                    }
                },
                "required": ["degrees"]
            }
        }
    },{
        "type": "function",
        "function": {
            "name": "turn_left",
            "description": "Turn left by given number of degrees",
            "parameters": {
                "type": "object",
                "properties": {
                    "degrees": {
                        "type": "integer",
                        "description": "Number of degrees to turn left"
                    }
                },
                "required": ["degrees"]
            }
        }
    }, {
        "type": "function",
        "function": {
            "name": "move_forward",
            "description": "Move forward by given number of steps",
            "parameters": {
                "type": "object",
                "properties": {
                    "steps": {
                        "type": "integer",
                        "description": "Number of steps to move forward"
                    }
                },
                "required": ["steps"]
            }
        }
    }, {
        "type": "function",
        "function": {
            "name": "move_backward",
            "description": "Move backward by given number of steps",
            "parameters": {
                "type": "object",
                "properties": {
                    "steps": {
                        "type": "integer",
                        "description": "Number of steps to move backward"
                    }
                },
                "required": ["steps"]
            }
        }
    }
]



def turn_right(deg):
    """
    Function to turn right by 90 degrees.
    This function can be called by the AI model when it decides to turn right.
    """
    return(f"Turning right by {deg} degrees.")
    
def turn_left(deg):
    """
    Function to turn left by 90 degrees.
    This function can be called by the AI model when it decides to turn left.
    """
    return(f"Turning left by {deg} degrees.")
    # Add any additional logic for turning left here

def move_forward(steps):
    """
    Function to move forward.
    This function can be called by the AI model when it decides to move forward.
    """
    return(f"Moving forward by {steps}.")
    # Add any additional logic for moving forward here

def move_backward(steps):
    """
    Function to move backward.
    This function can be called by the AI model when it decides to move backward.
    """
    return(f"Moving backward by {steps}.")
    # Add any additional logic for moving backward here

TOOL_MAPPING={
    "turn_right": turn_right,
    "turn_left": turn_left,
    "move_forward": move_forward,
    "move_backward": move_backward
}