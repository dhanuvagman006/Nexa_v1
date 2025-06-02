import base64
from openai import OpenAI
import tools

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)


with open("test.jpg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
data_uri = f"data:image/jpeg;base64,{encoded_string}"

messages=[
    {"role": "system", "content": "You are a independent humanoid robot."},
    
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
            "url": data_uri
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
    extra_body={},
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
