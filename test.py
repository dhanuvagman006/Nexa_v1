import cv2
import base64
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
            "url": capture_image_base64()
          }
        }
      ]
    }
  ]

print(messages)