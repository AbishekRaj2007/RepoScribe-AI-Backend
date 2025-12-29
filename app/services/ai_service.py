import google.generativeai as genai

genai.configure(api_key="PASTE_AI_STUDIO_KEY_HERE")

model = genai.GenerativeModel("gemini-1.5-flash")
print(model.generate_content("Say hello in one sentence").text)
