import numpy as np
import sys
import pandas as pd
import time

# create a dynamic map later on, 
# thought is to use numpy to genereate one, but that's later

base_map = np.array([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
])

alphabets = {
    " ":[
        [" "," "," "," "," "," "],
        [" "," "," "," "," "," "],
        [" "," "," "," "," "," "],
        [" "," "," "," "," "," "],
        [" "," "," "," "," "," "],
        [" "," "," "," "," "," "],
    ],
    "a":np.array([
    [1 , 1 , 1 , 1 , 1 , " "],
    [1 ," ", " ", " ", 1 , " "],
    [1 , 1 , 1 , 1 , 1 , " "],
    [1 , " ", " ", " ", 1 , " "],
    [1 , " ", " ", " ", 1 , " "]
]), "b":np.array([
    [1 , 1 , 1 , 1 , " ", " "],
    [1 , " ", " ", " ", 1 , " "],
    [1 , 1 , 1 , 1 , " ", " "],
    [1 , " ", " ", " ", 1 , " "],
    [1 , 1 , 1 , 1 , " ", " "]
]), "c":np.array([
    [1 , 1 , 1 , 1 , 1 , " "],
    [1 , " ", " ", " ", " ", " "],
    [1 , " ", " ", " ", " ", " "],
    [1 , " ", " ", " ", " ", " "],
    [1 , 1 , 1 , 1 , 1 , " "]
]), "d":np.array([
    [1 , 1 , 1 , 1 , " ", " "],
    [1 , " ", " ", " ", 1 , " "],
    [1 , " ", " ", " ", 1 , " "],
    [1 , " ", " ", " ", 1 , " "],
    [1 , 1 , 1 , 1 , " ", " "]
]), "e":np.array([
    [1 , 1 , 1 , 1 , 1 , " "],
    [1 , " ", " ", " ", " ", " "],
    [1 , 1 , 1 , 1 , 1 , " "],
    [1 , " ", " ", " ", " " , " "],
    [1 , 1 , 1 , 1 , 1 , " "]
]), "f":np.array([
    [1 , 1 , 1 , 1 , 1 , " "],
    [1 , " ", " ", " ", " ", " "],
    [1 , 1 , 1 , 1 , 1 , " "],
    [1 , " ", " ", " ", " ", " "],
    [1 , " ", " ", " ", " ", " "]
]), "g":np.array([
    [1 , 1 , 1 , 1 , 1 , " "],
    [1 , " ", " ", " ", " ", " "],
    [1 , " ", " ", 1 , 1 , " "],
    [1 , " ", " ", " ", 1 , " "],
    [1 , 1 , 1 , 1 , 1 , " "]
]), 


}


# steps
# get sentence
# add extra spacing at end of sentence
# get corresponding map of each leter 
# add all together on a seperate matrix which is the platform
# output all of it
# output column by column
# replace ncoming column with outgoing column
# this should show a scrolling effect


class Scroller:
    def __init__(self, sentence:str):
        self.sentence =  sentence + " "
        self.platform_size = ()
        self.df = pd.DataFrame(alphabets[" "], columns=["", "","", "", "", ""])
    
    def count_spaces(self):
        """
        Returns dictionary of spaces
        """
        return self.sentence.count(" ")
    
    def scroll(self,speed):
        text = self.create_platform()
        while True:
            print(text, end="\r")
            # print("////////////////", end="\r")
            
            time.sleep(speed)
            # get all the first items in the list and move them to the back.
            first_items = ""
            second_items = ""

            # print(text[1])
            # text = text[1:] + text[0]
    
    def _get_corr_map_(self):
        columns = ["" for i in range(6)]
        for i in self.sentence:
            # self.df = pd.concat(pd.DataFrame(alphabets[i]),on=0 ,how="right")
            self.df = pd .concat([self.df, pd.DataFrame(alphabets[i], columns=columns)], axis=1, ignore_index=True)
        # print(self.df.columns)
        return self.df
