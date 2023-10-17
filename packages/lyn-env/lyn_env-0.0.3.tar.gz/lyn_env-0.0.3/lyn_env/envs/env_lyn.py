import gym
import numpy as np


class LynEnv(gym.Env):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second': 50
    }

    def __init__(self):
        self.water_level = 0.0  # 水位高度
        self.target_level = 0.5  # 目标水位高度
        self.action_space = gym.spaces.Discrete(3)  # 动作空间，例如：0表示关闭水闸，1表示打开水闸A，2表示打开水闸B
        self.observation_space = gym.spaces.Box(low=0.0, high=1.0, shape=(2,))  # 观测空间，即水位高度和流量
        self.flow_rate = 0.0  # 流量

    def reset(self):
        self.water_level = 0.0
        self.flow_rate = 0.0
        return self._get_obs()

    def step(self, action):
        assert self.action_space.contains(action), "Invalid action"

        # 更新水位高度和流量，根据动作来模拟水闸的调度效果
        if action == 0:  # 关闭水闸
            self.flow_rate = 0.0
        elif action == 1:  # 打开水闸A
            self.flow_rate = 0.2
        else:  # 打开水闸B
            self.flow_rate = -0.1

        self.water_level += self.flow_rate

        reward = self._calculate_reward()
        done = bool(abs(self.water_level - self.target_level) < 0.01)  # 判断是否达到目标水位高度
        info = {}

        return self._get_obs(), reward, done, info

    def _get_obs(self):
        return np.array([self.water_level, self.flow_rate])

    def _calculate_reward(self):
        # 计算奖励，根据水位高度与目标水位高度的差值以及流量来设定奖励值
        reward = -abs(self.water_level - self.target_level) - abs(self.flow_rate)
        return reward
