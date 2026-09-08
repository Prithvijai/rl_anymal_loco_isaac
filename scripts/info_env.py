"""Script to display environment information"""


import argparse
from isaaclab.app import AppLauncher

parser = argparse.ArgumentParser(description="Information regarding the environment.")
parser.add_argument("--env-name", type=str, default=None)

args_cli = parser.parse_args()

app_launcher = AppLauncher(headless=True)
simulation_app = app_launcher.app

import isaaclab_tasks
import rl_anymal_loco_isaac.tasks
import gymnasium as gym
from isaaclab_tasks.utils import parse_env_cfg

env_cfg = parse_env_cfg(
    args_cli.env_name,
    device="cuda:0",
    num_envs=1,
)

import traceback

def main():
    print("hello world")
    for task_spec in gym.registry.values():
        # print(task_spec.id)
        if args_cli.env_name == task_spec.id:
            spec = gym.spec(task_spec.id)
            print(spec)
            
            env = gym.make(task_spec.id, cfg=env_cfg)
            print("    Environment INFO Short:",task_spec.id)
            print("Action space:", env.action_space)
            print("Observation space:", env.observation_space)
            env.close()

if __name__ == "__main__":
    try:
        # run the main function
        main()
    except Exception as e:
        raise e
    finally:
        # close the app
        simulation_app.close()
