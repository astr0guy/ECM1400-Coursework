from skimage import io
from skimage.util import img_as_ubyte
import numpy as np

def find_red_pixels(map_filename:str ,upper_threshold=100, lower_threshold=50):
    """Your documentation goes here"""

    map = io.imread(map_filename)
    output_image = np.ndarray([1140, 1053, 3], "ubyte")
    for x in range (1140):
        for y in range (1053):
            if map[x, y, 0] > upper_threshold and map[x, y, 1] < lower_threshold and map[x, y, 2] < lower_threshold:
                output_image[x, y] = 255
    io.imsave("data/map-red-pixels.jpg", output_image)

def find_cyan_pixels(map_filename:str ,upper_threshold=100, lower_threshold=50):
    """Your documentation goes here"""
    
    map = io.imread(map_filename)
    output_image = np.ndarray([1140, 1053, 3], "ubyte")
    for x in range (1140):
        for y in range (1053):
            if map[x, y, 0] < lower_threshold and map[x, y, 1] > upper_threshold and map[x, y, 2] > upper_threshold:
                output_image[x, y] = 255
    io.imsave("data/map-cyan-pixels.jpg", output_image)


def detect_connected_components(map_filename:str):
    """Your documentation goes here"""
    MARK = np.ndarray([1140, 1053], dtype=bool)
    Q = np.ndarray([0], dtype=int)
    f = open("./data/cc-output-2a.txt", "w")
    component_count = 0
    current_component = 0
    map = img_as_ubyte(io.imread(map_filename, as_gray=True))
    for y in range (1140):
        for x in range (1053):
            if map[y,x] > 210 and map[y,x] <=255 and not MARK[y,x]:
                MARK[y,x] = True
                Q = np.append(Q, [y, x])
                current_component += 1
                while len(Q) != (0):
                    neighbourhood = neighbourlist([map.shape[0], map.shape[1]], [Q[0], Q[1]])
                    Q = removefirstcoords(Q)
                    for i in neighbourhood:
                        if map[i[0], i[1]] > 210 and map[i[0], i[1]] <=255 and not MARK[i[0], i[1]]:
                            MARK[i[0], i[1]] = True
                            current_component += 1
                            Q = np.append(Q, [i[0], i[1]])
                if current_component >1:
                    f.write("Connected Component " + str(component_count + 1) + ", number of pixels = " + str(current_component) + "\n")
                    component_count += 1            
                current_component = 0             
    f.write("Total number of connected components = " + str(component_count) + "\n")
    f.close
    return MARK
    
def detect_connected_components_sorted(MARK):
    """Your documentation goes here"""
    MARK2 =  np.ndarray([1140, 1053], dtype=bool)
    Q = np.ndarray([0], dtype=int)
    f = open("./data/cc-output-2b.txt", "w")
    component_list = []
    current_component = []
    for y in range (1140):
        for x in range (1053):
            if MARK[y,x] and not MARK2[y,x]:
                MARK2 == True
                Q = np.append(Q, [y, x])
                current_component.append([y, x])
                while len(Q) != (0):
                    neighbourhood = neighbourlist([MARK.shape[0], MARK.shape[1]], [Q[0], Q[1]])
                    Q = removefirstcoords(Q)
                    for i in neighbourhood:
                        if MARK[i[0], i[1]] and not MARK2[i[0], i[1]]:
                            MARK2[i[0], i[1]] = True
                            current_component.append([i[0], i[1]])
                            Q = np.append(Q, [i[0], i[1]])
                if len(current_component) >1:
                    current_component.append(len(component_list) + 1)
                    addinorder(component_list, current_component)              
                current_component = []          
    for i in range (1, len(component_list)):
        f.write("Connected Component " + str(component_list[i-1][-1]) + ", number of pixels = " + str(len(component_list[i-1]) -2) + "\n")
    f.write("Total number of connected components = " + str(len(component_list)) + "\n")
    f.close
    MARK2 =  np.ndarray([1140, 1053], dtype=bool)
    for i in range (2):
        for j in range (len(component_list[i])-2):
            MARK2[component_list[i][j][0], component_list[i][j][1]] = True
    io.imsave("./data/cc-top-2.jpg", img_as_ubyte(MARK2))

def removefirstcoords(queue:np.ndarray):
    """This function takes a queue-like 1D array,
    if it's empty, the function returns the argument queue.
    Otherwise, the function creates another 1D array that's 2 items shorther than the argument array.
    it then copies all but the first two entries of the argument array to the new array, before returning the it."""
    if len(queue) != [0]:
        new_queue = np.ndarray([len(queue) - 2])
        for i in range (2, (len(queue))):
            new_queue[i-2] = queue[i]
    else:
        new_queue = queue
    return new_queue

def neighbourlist(shape:tuple, coordinate:list):
    neighbourhood = []
    for i in range (-1, 2):
        if  coordinate[0] + i < shape[0] - 1 and coordinate[0] + i >= 0:
            for j in range (-1, 2):
                if  (coordinate[1] + j < shape[1] - 1 and coordinate[1] + j >= 0) and not (i == 0 and j == 0):
                    neighbourhood.append([int(coordinate[0] + i), int(coordinate[1] + j)])
    return neighbourhood

def addinorder(component_list:list, component:list):
    
    for i in range (len(component_list) - 1):
        if len(component) >= len(component_list[i]):
            component_list.insert(i, component)
            return component_list
    component_list.append(component)
    return component_list