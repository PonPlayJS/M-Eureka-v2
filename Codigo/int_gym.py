import gym
from gym import spaces
import numpy as np
from custom_reward import custom_reward  # Importa una función de recompensa personalizada desde el archivo custom_reward.py

class CustomEnv(gym.Env):
    def __init__(self):
        super(CustomEnv, self).__init__()
        self.env = gym.make("CartPole-v1", render_mode="rgb_array")
        
        # Definir los espacios de observación y acción
        self.observation_space = gym.spaces.Box(
            low=-np.inf, high=np.inf, shape=(4,), dtype=np.float32
        )
        self.action_space = gym.spaces.Discrete(2)
        
    def step(self, action):
        # Realiza un paso en el entorno con la acción proporcionada. Recibe la observación, la recompensa, el estado de finalización y la información adicional del entorno base.
        obs, reward, terminated, truncated, info = self.env.step(action)
        done = terminated or truncated
        
        # Usa la función de recompensa personalizada
        reward = custom_reward(obs)

        return np.array(obs, dtype=np.float32), reward, done, info

    def reset(self):
        obs, _ = self.env.reset()  # Manejar la tupla devuelta por reset()
        return np.array(obs, dtype=np.float32)

    def render(self, mode="rgb_array"):
        return self.env.render()

    def close(self):
        self.env.close()
