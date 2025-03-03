import tkinter as tk
from tkinter import messagebox
from stable_baselines3 import PPO
import os
import sys
import subprocess
sys.path.append("/home/user/MINI-E/Codigo")

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Eureka!")
        self.master.resizable(width=True, height=True)
        self.master.geometry("400x400")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.welcome = tk.Label(self, text="Generador y Revisor de Políticas de Recompensa")
        self.welcome.pack(pady=10)
        
        self.input_prompt = tk.Label(self, text="Introduce tu prompt:")
        self.input_prompt.pack(pady=10)

        self.prompt = tk.Text(self, height=5, width=50)
        self.prompt.pack(pady=10)

        self.custom_reward_label = tk.Label(self, text="Introduce tu función de recompensa personalizada:")
        self.custom_reward_label.pack(pady=10)

        self.custom_reward = tk.Text(self, height=10, width=50)
        self.custom_reward.pack(pady=10)

        self.generate_button = tk.Button(self, text="Generar política de recompensa", command=self.generate_policy)
        self.generate_button.pack(pady=10)

        self.filter_button = tk.Button(self, text="Filtrar políticas", command=self.filter_policies)
        self.filter_button.pack(pady=10)

        self.review_button = tk.Button(self, text="Revisar función de recompensa", command=self.review_reward)
        self.review_button.pack(pady=10)

        self.output_label = tk.Label(self, text="Salida:")
        self.output_label.pack(pady=10)

        self.output_text = tk.Text(self, height=10, width=50)
        self.output_text.pack(pady=10)

        self.console_output_label = tk.Label(self, text="Salida de la consola:")
        self.console_output_label.pack(pady=10)

        self.console_output_text = tk.Text(self, height=10, width=50)
        self.console_output_text.pack(pady=10)

    def run_command(self, command):
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdout, stderr = process.communicate()
        self.console_output_text.delete("1.0", tk.END)
        self.console_output_text.insert(tk.END, stdout.decode())
        if stderr:
            self.console_output_text.insert(tk.END, "\n[ERROR]\n" + stderr.decode())

    def generate_policy(self):
        prompt_text = self.prompt.get("1.0", tk.END).strip()
        if prompt_text:
            if self.check_openai_api():
                from policy_generator import generate_policy
                policy_text = generate_policy(prompt_text)
                from policy_filter import Policy
                self.policies = [
                    Policy("Policy1", 100, {"speed": "fast", "accuracy": "high"}),
                    Policy("Policy2", 80, {"speed": "medium", "accuracy": "medium"}),
                    Policy("Policy3", 90, {"speed": "fast", "accuracy": "medium"}),
                ]
                self.requirements = {"speed": "fast", "accuracy": "high"}
                from int_gym import CustomEnv
                self.env = CustomEnv()
                model_path = "/home/user/MINI-E/models/ppo_custom_cartpole"
                if os.path.exists(model_path):
                    self.model = PPO.load(model_path)
                else:
                    messagebox.showwarning("Advertencia", f"No se encontró el modelo en la ruta: {model_path}")
                    return
                for policy in self.policies:
                    policy.model = self.model
                messagebox.showinfo("Política generada", "Política de recompensa generada con éxito.")
            else:
                messagebox.showwarning("Advertencia", "No se encontró la API de OpenAI.")
        else:
            messagebox.showwarning("Advertencia", "El prompt no puede estar vacío.")
        self.run_command("python /home/user/MINI-E/Codigo/policy_generator.py")

    def filter_policies(self):
        if hasattr(self, 'policies') and hasattr(self, 'requirements') and hasattr(self, 'env'):
            from policy_filter import filter_policies, load_policies
            self.policies = load_policies()
            filtered_policies = filter_policies(self.policies, self.requirements, self.env)
            if filtered_policies:
                policy_names = "\n".join([policy.name for policy in filtered_policies])
                messagebox.showinfo("Políticas de recompensa filtradas", policy_names)
            else:
                messagebox.showinfo("Políticas de recompensa filtradas", "No se encontraron políticas que cumplan con los requisitos.")
        else:
            messagebox.showwarning("Advertencia", "Primero debe generar las políticas de recompensa.")
        self.run_command("python /home/user/MINI-E/Codigo/policy_filter.py")

    def review_reward(self):
        custom_reward_code = self.custom_reward.get("1.0", tk.END).strip()
        prompt_text = self.prompt.get("1.0", tk.END).strip()
        if custom_reward_code and prompt_text:
            if self.check_openai_api():
                from review_reward import review_custom_reward
                review_text = review_custom_reward(custom_reward_code, prompt_text)
                self.output_text.delete("1.0", tk.END)
                self.output_text.insert(tk.END, review_text)
            else:
                messagebox.showwarning("Advertencia", "No se encontró la API de OpenAI.")
        else:
            messagebox.showwarning("Advertencia", "El prompt y la función de recompensa no pueden estar vacíos.")
        self.run_command("python /home/user/MINI-E/Codigo/review_reward.py")

    def check_openai_api(self):
        try:
            import openai
            return True
        except ImportError:
            return False

if __name__ == "__main__":
    root = tk.Tk()
    app = App(master=root)
    app.mainloop()
