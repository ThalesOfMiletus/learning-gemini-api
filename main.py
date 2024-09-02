import google.generativeai as genai
from apikey import APIKEYGEMINI

API_KEY = APIKEYGEMINI

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-pro')

dor_usuario = input("Qual é a sua dor? \n")

prompt = (
    "Você é um assistente médico virtual especializado em aconselhar sobre problemas de saúde. "
    "Com base no relato do paciente, forneça a especialidade médica mais adequada: "
    f"'{dor_usuario}'"
)
response = model.generate_content(prompt)
print(response.text)