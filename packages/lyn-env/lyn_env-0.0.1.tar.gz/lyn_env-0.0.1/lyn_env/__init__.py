from gym.envs.registration import register

register(
    id='lyn_env-v0',
    entry_point='lyn_env.envs:LynEnv',
)