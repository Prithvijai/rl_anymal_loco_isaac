# Locomotion using RL for Quadpedal robot in Isaac Lab

## Overview

This project demonstrates the use of Reinforcement Learning (RL) for locomotion control of a quadpedal robot in the Isaac Lab simulation environment. 

problem: veleocity tracking, so RL algorithm tries to learn low level control to stand and walk. 

## Video Demo (before training)



<video src="https://github.com/user-attachments/assets/63ef3e99-f12d-4a48-8e76-dd26b4922569" width="200" controls></video>

This video shows the quadpedal robot learning to walk step 0 of training.


## Installation

```bash 
source isaaclab_env/bin/activate

```
- Verify that the extension is correctly installed by:

    - Listing the available tasks:

        Note: It the task name changes, it may be necessary to update the search pattern `"Template-"`
        (in the `scripts/list_envs.py` file) so that it can be listed.

        ```bash
        python scripts/list_envs.py
        ```

## Running a task:

```bash
python scripts/skrl/train.py --task=Template-baseline-Isaac-Velocity-Rough-Anymal-D-v0 --num_envs 1 --max_iterations 5 --video
```

Baseline training with PPO

```bash
python scripts/skrl/train.py \
  --task Template-baseline-Isaac-Velocity-Rough-Anymal-D-v0 \
  --algorithm PPO \
  --num_envs 512 \
  --max_iterations 1500 \
  --seed 42 \
  --device cuda:0 \
  --headless \
  --video \
  --video_interval 6000 \
  --video_length 300

```

## Playing the task:

```bash
python scripts/skrl/play.py   --task Template-baseline-Isaac-Velocity-Rough-Anymal-D-Play-v0   --checkpoint ./logs/skrl/anymal_d_rough/2026-09-04_14-55-13_ppo_torch/checkpoints/agent_120.pt   --num_envs 1   --real-time

```

Baseline PPO playing

<video src="https://github.com/user-attachments/assets/dbf85ac1-ed95-4948-ac51-e8ef33418968" width="200" controls></video>
```bash
python scripts/skrl/play.py   --task Template-baseline-Isaac-Velocity-Rough-Anymal-D-Play-v0   --checkpoint "./logs/skrl/anymal_d_rough/2026-09-06_14-59-27_ppo_torch/checkpoints/agent_36000.pt"   --num_envs 1   --video   --video_length 500   --headless

```


## Code formatting

We have a pre-commit template to automatically format your code.
To install pre-commit:

```bash
pip install pre-commit
```

Then you can run pre-commit with:

```bash
pre-commit run --all-files
```

## Troubleshooting

### Pylance Missing Indexing of Extensions

In some VsCode versions, the indexing of part of the extensions is missing.
In this case, add the path to your extension in `.vscode/settings.json` under the key `"python.analysis.extraPaths"`.

```json
{
    "python.analysis.extraPaths": [
        "<path-to-ext-repo>/source/rl_anymal_loco_isaac"
    ]
}
```

### Pylance Crash

If you encounter a crash in `pylance`, it is probable that too many files are indexed and you run out of memory.
A possible solution is to exclude some of omniverse packages that are not used in your project.
To do so, modify `.vscode/settings.json` and comment out packages under the key `"python.analysis.extraPaths"`
Some examples of packages that can likely be excluded are:

```json
"<path-to-isaac-sim>/extscache/omni.anim.*"         // Animation packages
"<path-to-isaac-sim>/extscache/omni.kit.*"          // Kit UI tools
"<path-to-isaac-sim>/extscache/omni.graph.*"        // Graph UI tools
"<path-to-isaac-sim>/extscache/omni.services.*"     // Services tools
...
```
