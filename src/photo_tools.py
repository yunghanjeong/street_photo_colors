# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 11:51:23 2020

@author: Yung
"""
# for local files and online data
import os
import json
import io

# for reddit api
import pandas as pd
import praw
from urllib.request import urlopen

# for color analysis
from colorthief import ColorThief
import webcolors

import numpy as np


class reddit_tools():
    """
    This is for initializing the reddit API, PRAW
    """
    def __init__(self, agent:str):
        api_id, api_secret = self.get_keys()
        self.reddit = praw.Reddit(client_id=api_id,
                     client_secret=api_secret,
                     user_agent=agent)
        
    #this function grabs api keys and returns them
    def get_keys(self):
        f = open("api_secret.json") #you many need to change this file path
        api_data = json.load(f)
    
        #return api keys 
        return api_data["id"], api_data["secret"]
    
    #accepts subreddit, top time limit, and post number limit
    #outputs data frame of post name and url
    def get_top_posts(self, subreddit:str, time:str = "week", limit:int = 10):
        """

        Parameters
        ----------
        subreddit : str
            DESCRIPTION.
        time : str, optional
           (all, day, hour, month, week, year). The default is "week".
        limit : int, optional
            number of posts. The default is 10.

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        #get posts
        posts = self.reddit.subreddit(subreddit).top(time, limit=limit)
        submission_url = []
        submission_title = []
        
        #obtain post data
        for post in posts:
            submission_url.append(post.url)
            submission_title.append(post.title)
        
        return pd.DataFrame({"title":submission_title, "url":submission_url})
    
class palette_tools():
    """
    This is for getting palettes with colorthief
    """
    def __int__(self):
        pass
    
    def get_url_binary(self, url):
        """
        grabs the binary data from post in url
        """
        post_url = urlopen(url)
        post_bin = io.BytesIO(post_url.read())
        return post_bin
    
    def get_palette(self, url:str, count:int = 10, qual:int = 10):
        """

        Parameters
        ----------
        url : str
            URL in string
        count : int, optional
            # of rgb values in pallet. The default is 6.
        qual: int, optional
            sets the quality of get_palette, larger it is faster it runs
            and more likely to miss colors

        Returns
        -------
        List of rgb tuples, # of tuples defined by count variable sort by values with close rgb values

        """
        post = self.get_url_binary(url)
        ct = ColorThief(post)
        rgb_list = ct.get_palette(color_count=count, quality=qual)
        return rgb_list
    
    #sorts palette from least grey to most grey
    def palette_sort(self, palette):
        palette.sort(key = lambda x: np.sqrt((x[0] - x[1])**2 + (x[1] - x[2])**2 + (x[0] - x[2])**2))
        return palette
        
    def rgb_hex_list(self, rgb_list:list):
        return [webcolors.rgb_to_hex(color) for color in rgb_list]
    
    
        
        