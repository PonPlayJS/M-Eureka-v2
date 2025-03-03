import openai
import sys

# Configura tu clave de api de open ia
openai.api_key = "OPENIA_KEY"

def review_custom_reward(custom_reward_code, prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # Modelo de lenguaje
            messages=[
                {"role": "system", "content": "Eres un asistente experto en aprendizaje por refuerzo."},
                {"role": "user", "content": f"Revisa la siguiente función de recompensa personalizada y proporciona retroalimentación basada en los siguientes requisitos: {prompt}\n\n{custom_reward_code}"}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        print(f"Error al revisar la función de recompensa: {e}")
        sys.exit(1)
