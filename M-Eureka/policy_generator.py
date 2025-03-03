import openai
import sys

# Configura tu clave de api de open ia
openai.api_key = "OPENIA_KEY"

def generate_policy(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # Modelo de lenguaje
            messages=[  
                {"role": "system", "content": "Eres un asistente experto en aprendizaje por refuerzo."}, # rol
                {"role": "user", "content": prompt}
            ]
        ) 
        return response['choices'][0]['message']['content']
    except Exception as e:
        print(f"Error al generar la política de recompensa: {e}")
        sys.exit(1)
