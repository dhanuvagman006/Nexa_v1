import base64
from openai import OpenAI


client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)

#############################################TOOLS#############################################
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



def capture_image_base64():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        raise RuntimeError("Cannot open camera")
    ret, frame = cap.read()
    cap.release() 
    if not ret:
        raise RuntimeError("Failed to capture image")
    _, buffer = cv2.imencode('.jpg', frame)

    jpg_as_text = base64.b64encode(buffer).decode('utf-8')
    base64_url = f"data:image/jpeg;base64,{jpg_as_text}"
    return base64_url

msgs=[
    {"role": "system", "content": "You are a smart and superpowerfull humanoid robot."},
    
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Go straight for 10 steps, turn right by 90 degrees, move forward by 5 steps, turn left by 45 degrees."
        },
        {
          "type": "image_url",
          "image_url": {
            "url": capture_image_base64()
          }
        }
      ]
    }
  ]


def call_llm(msgs):
  completion = client.chat.completions.create(
    extra_headers={
      "HTTP-Referer": "https://www.nexusclubs.in/",
      "X-Title": "NEXUS_SIT", 
    },
    tools=tools.tools,
    tool_choice="auto",
    extra_body={
        "models": ["anthropic/claude-3.5-sonnet", "gryphe/mythomax-l2-13b"],
    },
    messages=msgs,
    model="mistralai/mistral-small-3.1-24b-instruct:free",
  )
  msgs.append(completion.choices[0].message.dict())
  return completion 

def grt_tools_response(response):
  tool_call = response.choices[0].message.tool_calls[0]
  tool_name=tool_call.function.name
  tool_args=json.loads(tool_call.function.arguments)
  tool_result=tools.TOOL_MAPPING[tool_name](**tool_args)
  return {
    "role": "tool",
    "tool_call_id": tool_call.id,
    "name": tool_name,
    "content": tool_result
  }

while True:
  resp=call_llm(messages)
  if resp.choices[0].message.tool_calls is not None:
    messages.append(grt_tools_response(resp))
  else:
    break

print(messages[-1]["content"])
