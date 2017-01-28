OpenAI Gym Resources
----------
* [Documentation](https://gym.openai.com/docs)
* [Source code](https://github.com/openai/gym)
* [Wiki](https://github.com/openai/gym/wiki)

Steps in adding `MDPGridworld-v0` environment in Gym's `Toy Text` collection
-------------------------
OpenAI Gym also provides [instructions](https://github.com/openai/gym/wiki/Environments) on how to add a new environment. **IMPORTANT:** Ensure that the `Toy Text` environment collection is installed with your `gym` installation. 

1. Open a terminal. Type `python` and hit enter, and you should enter Python's interpreter.

    ```
    $ python
    ```

2. Execute the following commands to find the location of `gym` in your system:

    ```python
    >> import gym
    >> gym.__file__
    '/home/gabrieledcjr/Projects/gym/gym/__init__.pyc'
    >> exit()
    ```

3. After exiting python's interpreter, you can either use the file explorer GUI or use terminal commands to change to the environments directory under the `gym` directory. This environments directory is called `envs`.

    ```
    $ cd /home/gabrieledcjr/Projects/gym/gym/envs
    ```

4. Using your favorite text editor, open the file `__init__.py`. 

    ```
    $ gedit __init__.py
    ```

5. We have to register our new environment, you need add the code below the `import` line. Optionally, you can look for the `Toy Text` registration group and add the code there. Save and close after.

    ```python
    from gym.envs.registration import registry, register, make, spec

    # other registration codes ...

    # Toy Text
    # ----------------------------------------
    
    # Add this code below in envs/__init__.py
    register(
        id='MDPGridworld-v0',
        entry_point='gym.envs.toy_text:MDPGridworldEnv',
        timestep_limit=100,
    )
    ```

6. In the terminal, change directory to `toy_text`. This is where you will copy the `mdp_gridworld.py` file.

    ```
    $ cd toy_text
    $ cp <path_to_file>/mdp_gridworld.py .
    ```

7. Open the `__init__.py` file and add the code below. Save and close after. 

    ```
    $ gedit __init__.py
    ```
    ```python
    # Add this code in toy_text/__init__.py
    from gym.envs.toy_text.mdp_gridworld import MDPGridworldEnv
    ```

8. `MDPGridworld-v0` gym environment is now ready to used. 


`MDPGridworld-v0`:
--------------------
This version of the 3×4 grid world is deterministic. The set-up for this problem is based from this [blog post](https://goo.gl/GqkyzT).

* **States** or **Observation**: States are represented with scalar values in the range 0 to 11. Below is a diagram of the corresponding states.

    ```
    +---+---+---+---+
    | 0 | 1 | 2 | 3 |
    +---+---+---+---+
    | 4 | 5 | 6 | 7 |
    +---+---+---+---+
    | 8 | 9 | 10| 11|
    +---+---+---+---+

    +---+---+---+---+
    |   |   |   | G |   S - Starting state
    +---+---+---+---+   G - Goal
    |   | # |   | F |   F - Fire (very bad state)
    +---+---+---+---+   # - Wall
    | S |   |   |   |
    +---+---+---+---+
    ```

* **Actions**: Below are the scalar values for all possible actions in each non-terminal state. Agent keeps the same state when taking an action towards a wall.

    ```
    0 - North
    1 - South 
    2 - West 
    3 - East
    ```

* **Rewards**: `r(3) = +100`, `r(7) = -100`. Other states has a reward of `-3`.

* **Terminal states**: `{3, 7}` corresponds to goal (G) and fire (F) respectively, which means an episode ends when the agent reaches either states.
