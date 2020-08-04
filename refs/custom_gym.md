Create new environments
See the main page of the repository:

https://github.com/openai/gym/blob/master/docs/creating-environments.md

The steps are:

Create a new repository with a PIP-package structure
It should look like this

```
gym-foo/
  README.md
  setup.py
  gym_foo/
    __init__.py
    envs/
      __init__.py
      foo_env.py
      foo_extrahard_env.py
```

For the contents of it, follow the link above. Details which are not mentioned there are especially how some functions in foo_env.py should look like. Looking at examples and at `gym.openai.com/docs/` helps. Here is an example:

```
class FooEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        pass

    def _step(self, action):
        """

        Parameters
        ----------
        action :

        Returns
        -------
        ob, reward, episode_over, info : tuple
            ob (object) :
                an environment-specific object representing your observation of
                the environment.
            reward (float) :
                amount of reward achieved by the previous action. The scale
                varies between environments, but the goal is always to increase
                your total reward.
            episode_over (bool) :
                whether it's time to reset the environment again. Most (but not
                all) tasks are divided up into well-defined episodes, and done
                being True indicates the episode has terminated. (For example,
                perhaps the pole tipped too far, or you lost your last life.)
            info (dict) :
                 diagnostic information useful for debugging. It can sometimes
                 be useful for learning (for example, it might contain the raw
                 probabilities behind the environment's last state change).
                 However, official evaluations of your agent are not allowed to
                 use this for learning.
        """
        self._take_action(action)
        self.status = self.env.step()
        reward = self._get_reward()
        ob = self.env.getState()
        episode_over = self.status != hfo_py.IN_GAME
        return ob, reward, episode_over, {}

    def _reset(self):
        pass

    def _render(self, mode='human', close=False):
        pass

    def _take_action(self, action):
        pass

    def _get_reward(self):
        """ Reward is given for XY. """
        if self.status == FOOBAR:
            return 1
        elif self.status == ABC:
            return self.somestate ** 2
        else:
            return 0
```
Use your environment
```
import gym
import gym_foo
env = gym.make('MyEnv-v0')
```
Examples
https://github.com/MartinThoma/banana-gym
https://github.com/openai/gym-soccer
https://github.com/openai/gym-wikinav
https://github.com/alibaba/gym-starcraft
https://github.com/endgameinc/gym-malware
https://github.com/hackthemarket/gym-trading
https://github.com/tambetm/gym-minecraft
https://github.com/ppaquette/gym-doom
https://github.com/ppaquette/gym-super-mario
https://github.com/tuzzer/gym-maze
