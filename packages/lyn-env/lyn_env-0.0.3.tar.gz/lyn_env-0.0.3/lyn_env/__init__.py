from gym.envs.registration import register

register(
    id='lyn_env-v1',
    entry_point='lyn_env.envs:LynEnv',
)