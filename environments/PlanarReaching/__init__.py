import sys

from gym.envs.registration import register

default_max_episode_steps = 1e5

register(
    id="PlanarReaching-v0",
    entry_point="environments.PlanarReaching.PlanarReaching:PlanarReaching",
    max_episode_steps=default_max_episode_steps,
)
