import google.generativeai as genai

API_KEY = "PASTE_AI_STUDIO_KEY_HERE"  # no quotes inside the key

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

response = model.generate_content("Say hello in one sentence")
print(response.text)
