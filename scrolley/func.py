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
        ["*","*","*","*","*","*"],
        ["*","*","*","*","*","*"],
        ["*","*","*","*","*","*"],
        ["*","*","*","*","*","*"],
        ["*","*","*","*","*","*"],
        
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
        self.platform = self.df
    
    def __create_platform__(self):
        shape = self.df.shape
        rows = shape[0]
        platform = [["*" for x in range(30)] for i in range(rows)] # 45 is the length of the platform
        self.platform = pd.DataFrame(platform)
    
    def count_spaces(self):
        """
        Returns dictionary of spaces
        """
        return self.sentence.count(" ")
    
    def scroll(self,speed):
        self._get_corr_map_()
        self.__create_platform__()
        x = 1
        columns = self.platform.columns
        while True:
            # print(columns)
            print(self.platform, end="\r")
            print("\033c", end='')
            self.platform.pop(columns[0])
            columns.drop(columns[0])
            time.sleep(speed)
            try:
                self.platform = pd.concat([self.platform, self.df[x]], ignore_index=True, axis=1)
            except KeyError:
                x = 1
                columns = self.platform.columns
                self.platform = pd.concat([self.platform, self.df[x]], ignore_index=True, axis=1)
            x += 1

        
        # columns = self.df.columns
        # x = 1
        # start = pd.concat([self.platform, self.df[x]], ignore_index=True, axis=1)
        # while x < len(columns):
        #     print(start, end="\r")
        #     start = pd.concat([start, self.df[x]], ignore_index=True, axis=1)
        #     # print("////////////////", end="\r")
            
        #     time.sleep(speed)

        # remove first of string and put in place of last
        
    def _get_corr_map_(self):
        columns = ["" for i in range(6)]
        for i in self.sentence:
            # self.df = pd.concat(pd.DataFrame(alphabets[i]),on=0 ,how="right")
            self.df = pd.concat([self.df, pd.DataFrame(alphabets[i], columns=columns )], axis=1, ignore_index=True)
        # return self.df
        # print(self.df)
