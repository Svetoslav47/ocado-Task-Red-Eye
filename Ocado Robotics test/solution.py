#!/usr/bin/env python3

from typing import (
    List,
    Tuple,
    Union
)

from utils.image import (
    ImageType,
    PackedImage,
    StrideImage,
)

import numpy as np

from utils.function_tracer import FunctionTracer

from utils.eye_pattern import eyePatterns

def compute_solution(images: List[Union[PackedImage, StrideImage]]):
    ft = FunctionTracer("compute_solution", "seconds")

    for image in images:
        
        npImage = np.zeros((image.resolution.height, image.resolution.width, 3))

        for y in range(0, image.resolution.height):
            for x in range(0, image.resolution.width):
                npImage[y][x] = [image.pixels[y*image.resolution.height + x].red, image.pixels[y*image.resolution.height + x].green, image.pixels[y*image.resolution.height + x].blue]
                
        #we go trough every row in increments of 5, we will for sure find a wall
        for col in range(0, image.resolution.height):
            for row in range(0, image.resolution.width, 5):
                if(npImage[col][row][0] >= 200):
                    #finding the exact place of the square
                    top_left = (col, row)

                    if row < 4:
                        for i in range(0, row):
                            if npImage[col][row - i][0]> 199:
                                top_left = (col, row-i)
                    else:
                        #we go only to the left, garanteed we are at the top 
                        for i in range(0, 5): #left
                            if npImage[col][row - i][0] > 199:
                                top_left = (col, row-i)
                    
                    #finding the pattern
                    current_pattern = -1
                    for patternNum, pattern in enumerate(eyePatterns):
                        if top_left[0] + 4 >= image.resolution.height:
                            break

                        if top_left[1] + 4 >= image.resolution.width:
                            break

                        if current_pattern != -1:
                            break
                        does_pattern_work = True
                        for x in range(0, 5):
                            for y in range(0, 5):
                                if (npImage[top_left[0] + y][top_left[1] + x][0] < 200) and (pattern[y][x] != ' '):
                                    does_pattern_work = False
                        if does_pattern_work == True:
                            current_pattern = patternNum


                    if current_pattern != -1:
                        for x in range(0, 5):
                            for y in range(0, 5):
                                if (npImage[top_left[0] + y][top_left[1] + x][0] >= 200) and (eyePatterns[current_pattern][y][x] != ' '):
                                    npImage[top_left[0] + y][top_left[1] + x][0] -= 150
                                    image.pixels[(top_left[0] + y)*image.resolution.height + (top_left[1] + x)].red -= 150

        # npImage = npImage.reshape((image.resolution.height * image.resolution.width, 3))
        # for x in range(0, image.resolution.height * image.resolution.width):
        #     image.pixels[x].red = npImage[x][0]
        #     image.pixels[x].blue = npImage[x][2]
        #     image.pixels[x].green = npImage[x][1]
    #TODO fill solution
    del ft