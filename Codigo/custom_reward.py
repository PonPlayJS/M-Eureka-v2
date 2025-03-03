#politica de ejemplo

def custom_reward(state):
    pole_angle = state[2]  # Ángulo del poste
    angle_penalty = abs(pole_angle)  # Penalización por desviación de la vertical
    
    reward = 1.0 - angle_penalty  # Recompensa base con penalización
    
    return max(reward, 0)  # Asegurar que la recompensa no sea negativa
