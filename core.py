import base64
from openai import OpenAI
import tools

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)

# Read and encode the local image
with open("test.jpg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
data_uri = f"data:image/jpeg;base64,{encoded_string}"

completion = client.chat.completions.create(
  extra_headers={
    "HTTP-Referer": "https://www.nexusclubs.in/",
    "X-Title": "NEXUS_SIT", 
  },
  tools=tools.tools,
  tool_choice="auto",
  extra_body={},
  model="mistralai/mistral-small-3.1-24b-instruct:free",
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
)

response= completion.choices[0].message
print(response)

