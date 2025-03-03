import time
import importlib

class Policy:
    def __init__(self, name, reward, criteria, model=None):
        self.name = name
        self.reward = reward
        self.criteria = criteria
        self.model = model  # Añadir el modelo PPO

    def run_simulation(self, env):
        observation = env.reset()
        total_reward = 0
        start_time = time.time()
        for _ in range(1000):  # Limitar el número de iteraciones
            if self.model:
                action, _states = self.model.predict(observation)
                action = int(action)
            else:
                action = env.action_space.sample()  # Política aleatoria si no hay modelo
            observation, reward, done, info = env.step(action)
            total_reward += reward
            if done:
                break
        end_time = time.time()
        env.close()
        return total_reward, end_time - start_time

def filter_policies(policies, requirements, env):
    filtered_policies = []
    for policy in policies:
        if all(requirement in policy.criteria.items() for requirement in requirements.items()):
            total_reward, duration = policy.run_simulation(env)
            if total_reward > 0:  # Filtrar las políticas que no inicien
                filtered_policies.append((policy, total_reward, duration))
    # Ordenar por recompensa total y duración
    filtered_policies.sort(key=lambda x: (-x[1], x[2]))
    return [policy for policy, _, _ in filtered_policies]

def load_policies():
    policies_module = importlib.import_module("policies")
    policies = []
    for i in range(5):
        policy_func = getattr(policies_module, f"policy_{i+1}")
        policies.append(policy_func)
    return policies
