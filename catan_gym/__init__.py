from gym.envs.registration import register

register(
    id='catan-v0',
    entry_point='catan_gym.envs:CatanEnv',
)
