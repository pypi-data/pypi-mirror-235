import gymnasium as gym
import numpy as np
from gymnasium import spaces,Env
from selenium import webdriver
from selenium.common.exceptions import MoveTargetOutOfBoundsException, NoSuchElementException
from selenium.webdriver.common.by import By
import re
from selenium.webdriver.common.action_chains import ActionBuilder
from linkedin_scraper import LinkedInDriver
from gymnasium.spaces import Dict, Box, Discrete, MultiDiscrete
import random

#https://stable-baselines3.readthedocs.io/en/master/guide/custom_env.html
#https://gymnasium.farama.org/tutorials/gymnasium_basics/environment_creation/#sphx-glr-tutorials-gymnasium-basics-environment-creation-py

def is_page_blocked(driver: LinkedInDriver):
    if re.search(r'checkpoint/challenges', driver.chrome_driver.current_url):
        return True
    try:
        name = driver.chrome_driver.find_element(By.CLASS_NAME, 'text-heading-xlarge').text
    except NoSuchElementException:
        return True
    return False

class LinkedInEnv(Env):
    def __init__(self, driver:LinkedInDriver,url_list:list[str],captcha_penalty:int,initial_x:int=100, initial_y:int=100 ):
        self.driver=driver
        self.action_space=MultiDiscrete([11,11,2])
        window_width= driver.chrome_driver.get_window_size()["width"]
        window_height=driver.chrome_driver.get_window_size()["height"]
        self.observation_space=Dict({
            "x_position":Discrete(window_width),
            "y_position":Discrete(window_height)
        })
        self.initial_x=initial_x
        self.initial_y=initial_y

        self.current_x=initial_x
        self.current_y=initial_y

        self.url_list=url_list
        self.captcha_penalty=captcha_penalty
        self.episode_scrape_list=[]
        self.count=0

    def get_obs(self):
        return {"x_position":self.current_x,"y_position":self.current_y}
    def reset(self, seed=None, options=None):
        self.driver.signin()
        self.driver.chrome_driver.get(random.choice(self.url_list))
        initial_movement_action=ActionBuilder(self.driver.chrome_driver)
        initial_movement_action.pointer_action.move_to_location(self.initial_x, self.initial_y)
        initial_movement_action.perform()
        return self.get_obs(),{}
        
    def step(self, action: dict)->tuple:
        #(observation, reward, terminated, truncated, info)
        movement_x=action[0]-5
        movement_y=action[1]-5
        self.current_x+=movement_x
        self.current_y+=movement_y

        try:
            action_builder= ActionBuilder(self.driver.chrome_driver)
            action_builder.pointer_action.move_to_location(self.current_x, self.current_y)
            action_builder.perform()
            scrape=action[2]
            terminated=False
            if scrape>0:
                reward=1
                self.count+=1
                self.driver.chrome_driver.get(random.choice(self.url_list))
                if is_page_blocked(self.driver):
                    print(f"captcha found, episode ended after {self.count} profiles visited")
                    terminated=True
                    reward=self.captcha_penalty
                    self.episode_scrape_list.append(self.count)
                    self.count=0
            else:
                reward=0
        except MoveTargetOutOfBoundsException:
            print(f"tagret out of bounds, episode ended after {self.count} profiles visited")
            terminated=True
            reward=self.captcha_penalty
            self.episode_scrape_list.append(self.count)
            self.count=0
        
        return self.get_obs(),reward, terminated, False, {}