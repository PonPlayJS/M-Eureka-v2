import time
from filter import Policy  # Importar la clase Policy

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
