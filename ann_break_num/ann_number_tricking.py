"""
Author: Philip Wen Wei Ooi (32495978)

Inspired from the human brain, artificial neural networks (ANNs) are a 
type of computer vision model to classify images into certain categories.
In particular, in this assignment we will consider ANNs for the taks of
recognising handwritten digits (0 to 9) from black-and-white images with a
resolution of 28x28 pixels. In Part 1 of this assignment you will create
functions that compute an ANN output for a given input, and in Part 2 you
will write functions to "attack" an ANN. That is, to try to generate inputs
that will fool the network to make a wrong classification.

Part 1 is due at the end of Week 6 and Part 2 is due at the end of week 11.

For more information see the function documentation below and the
assignment sheet.
"""
#importing scripts 
import os 

#Part 1 coding solutions were provided by the FIT1045 Algorithms and programming in python team. 
def linear(x, w, b): # 1 Mark
    return sum(w[j]*x[j] for j in range(len(w))) + b

def linear_layer(x, w, b): # 1 Mark
    return [linear(x, w[i], b[i]) for i in range(len(w))]

def inner_layer(x, w, b): # 1 Mark
    return [max(linear(x, w[i], b[i]), 0.0) for i in range(len(w))]

def inference(x, w, b): # 2 Marks
    num_layers = len(w)
   
    for l in range(num_layers-1):
        x = inner_layer(x, w[l], b[l])
        
    return linear_layer(x, w[num_layers-1], b[num_layers-1])

def read_weights(file_name): # 1 Mark
    weights_file = open(file_name,"r")
    w = []
    for line in weights_file:
        if "#" == line[0]:
            w.append([])
        else:
            w[-1].append([float(w_ij) for w_ij in line.strip().split(",")])
    
    return w

def read_biases(file_name): # 1 Mark
    biases_file = open(file_name,"r")
    b = []
    for line in biases_file:
        if not "#" == line[0]:
            b.append([float(b_j) for b_j in line.strip().split(",")])
    
    return b
def read_image(file_name): # 1 Mark
    image_file = open(file_name,"r")
    x = []
    for line in image_file:
        for x_i in line.strip():
            x.append(int(x_i))
            
    return x


def argmax(x): # 1 Mark
    num_inputs = len(x)
    max_index = 0
    
    for i in range(1,num_inputs):
        if x[max_index] < x[i]:
            max_index = i
            
    return  max_index


def predict_number(image_file_name, weights_file_name, biases_file_name): # 1 Mark
    x = read_image(image_file_name)
    w = read_weights(weights_file_name)
    b = read_biases(biases_file_name)

    y = inference(x, w, b)
    return argmax(y)


#ASSIGNMENT PART 2 BEGINS HERE  

def flip_pixel(x):
    """
    Computation:
    This funciton is used to flip a detected 1 to a 0 and vice versa. 

    Input: A single digit of either 1 or 0 
    Output: The opposite digit of the input digit. 0 will return a 1 and 1 will return a 0.

    For example:
    >>> x = 1
    >>> flip_pixel(x)
    0
    >>> x = 0
    >>> flip_pixel(x)
    1

    Specific problems:
    The specific problem here was to flip the input correctly to its opposite value of either 0 or 1 

    Programming techniques:
    An if-else statement was used here to detect the input and flip the pixel. If 1 was an input, the opposite 0 was an output, else return a 1. 
    """
    if x == 1: # if x in imputted
        return 0 #return a 0
    else: #otherwise, we can assume that a 0 has been imputted
        return 1 #thus return a 1 

def modified_list(i,x):
    """
    Computation:
    This function is used to flip a pixel at a given index input (i) in the selected list input(x). When an index is given, it will traverse the list to the given index
    and perform the flip_pixel() function at that specific index location changing a 1 to a 0 and vice versa. 

    Input: The index location where the flip is to occur(i) and the list where the index should point to(x)
    Output: a list with the pixel at index(i) that has been flipped

    For example:
    >>> x = [1, 0, 1, 1, 0, 0, 0]
    >>> i = 2
    >>> modified_list(i,x)
    [1, 0, 0, 1, 0, 0, 0]
    
    >>> x = [1, 0, 1, 1, 0, 0, 0]
    >>> i = 3
    >>> modified_list(i,x)
    [1, 0, 1, 0, 0, 0, 0]

    Specific probelms:
    The problems encountered in this function was to be able to locate the specific index that was needed for a flip

    Programming techniques:
    In this function I used an index with x as the list and i as the index then I inputted the number at that location 
    into the flip pixel function which flipped it. Then made the number at that location be the new number, overriding 
    the old number that was stored at the location of x[i]
    """
    x[i] = flip_pixel(x[i]) #flip the pixel at that location and override the value in x[i]
    return x #return the list


def compute_difference(x1,x2):
    """
    Computation:
    This function is used to count the number of differences in pixels between two different lists. 

    Input: two lists of 0s and 1s 
    Output: the number of differences between the two different lists

    For example:
    >>> x1 = [1, 0, 1, 1, 0, 0, 0]
    >>> x2 = [1, 1, 1, 0, 0, 0, 1]
    >>> x3 = [1, 0, 1, 1, 0, 0, 0]
    >>> compute_difference(x1,x2)
    3
    >>> compute_difference(x1,x3)
    0

    Specific problems:
    The problems encountered in the creation of this function is iterating through the whole list and checking 
    if the two numbers at the same index in a list are identical. If the numbers are not, a difference counter 
    must be incremented to keep track of the differences

    Programming techniques:
    To achieve a traversal of the lists a for loop was used with i being used as the index. Each pair of numbers 
    were found using the same index which allows you to take two numbers from the same position in the list. Then 
    we check if the two numbers are identical using the '==' operator. If they are not identical, then increment
    a count for the differences by 1
    """
    dif = 0 #count for the differences
    for i in range(len(x1)): #iterate through the whole of the lists
        if x1[i]==x2[i]: #if they are the same
            continue #keep the loop going
        else: #if a difference is detected
            dif+= 1#increment the difference counter by 1
    return dif #return the number of differences 

def select_pixel(x,w,b):
    """
    Computation: 
    This function is used to select the pixel with the most impact on the final calculated score of the image. 

    Input: The image, the weights of the image, the biases of the image
    Output: the pixel number that needs to be flipped to make the biggest change to the computation of that image

    For example:
    >>> x = read_image('image.txt')
    >>> w = read_weights('weights.txt')
    >>> b = read_biases('biases.txt')
    >>> pixel = select_pixel(x, w, b)
    >>> pixel
    238
    >>> x = modified_list(pixel,x)
    >>> pixel = select_pixel(x, w, b)
    >>> pixel
    210

    Specific problems:
    The problem when coding this solution would be the definition of "most impactful change". Switching any pixel
    in the image will generate some form of change when the inferrence() function is ran on the final image. In this 
    function the most impactful change I decided was the smallest and furthest that we could get the number from its original score. 
    This would mean that the pixel flipped would be one with the biggest difference between the original and the pixel score found
    for the pixel. This I would justify as the most impactful change to the inferrence score of the image. 

    Programming techniques:
    To achieve this difference, the function first has to decide what the original number is in order to be able to compare the 
    difference that the flipping of each pixel makes. The use of inferrence() and argmax() were used to find the number of interest. 
    Then each pixel was flipped in sequence, the inferrence was generated and only the inferrence for the number of interest was stored
    in a separate list. This storage was done by using the number of interest as an index number. Then the resulting list of inferrences 
    for the specific number is searched for its minimum value and its index number at that position as this index would denote the pixel
    number that had to be flipped. Finally the index number was returned. 
    """
    num_index = argmax(inference(x,w,b)) #find what number we are looking at
    i = 0 
    score_lst = [] #final list of all probabilites 
    while i < len(x): #while the index is less than the length of your picture
        mod_lst = modified_list(i,x) #flip the pixel
        res = inference(mod_lst,w,b) #find the inference of it
        score_lst.append(res[num_index]) #record the inference of importance(the one that representes the old picture)
        x = modified_list(i,mod_lst) #return the pixel to its original form 
        i += 1 #go to the next pixel
    min_score = min(score_lst) #find the smallest number which shows the greatest change, greatest improbability 
    min_pixel = score_lst.index(min_score) #find the index of it, and this should represent the pixel that you have to flip as we have recorded the pixel number using the index position
    return min_pixel #return the pixel needed for flipping 

def write_image(x,filename):
    """
    Computation:
    This function is used to make a new text file of a new image from a single list of pixels (1 and 0) and create a text file under the name 
    specified under 'filename'

    Input: A list of pixels used to create an image and the name of the new file that has to be created
    Output: A text file with the name specified in 'filename' with the list of pixels (x) displayed in an image/pixel format

    For example:
    >>> x = read_image(‘image.txt’)
    >>> x = modified_list(238,x)
    >>> x = modified_list(210,x)
    >>> write_image(x,‘new_image.txt’)

    Specific problems:
    The problems that are encountered in this function is defining the lines of 28 numbers each line and inserting each line one after another 
    into the new text file. The numbers had to be changed from list format and ',' had to be taken out to form the final picture.

    Programming techniques:
    The blocks of 28 pixels each row was done through slicing the list. Two variables i and j were used as the start and the end of the slicing.
    i and j would always ahve a difference of 28 thus each block that is sliced and inserted would have a row of 28 pixels. The function join()
    was used to join the list together. The lack of specification with what to join leads to the numbers all joining together to form rows of pixels.
    However, before join, list comprehension was used to change each pixel into a string in order for join to work. Then with each slice of the list, 
    they were joined togehter and written into the text file using the write() function along with a newline '\n' to create the stacking of the pixels.

    """
    f = open(filename,"w") #creates a new text file named using the 'filename' variable, in mode 'write'
    i = 0 #the start of the slice
    j = 28 #the end of the slice
    str_lst = [str(pixel) for pixel in x] #chance each 'pixel' to string for each one in list (x)
    while j < len(str_lst): #while the end of the slice hasn't reached the last pixel 
        int_line = "".join(str_lst[i:j]) #slice out 28 pixels and join them
        f.write(int_line + '\n') #insert the joint pixels into the file with a newline character
        j += 28 #increment the end of the slice 28 pixels forward
        i += 28 #increment the start of the slice 28 pixels forward 
    f.close #close the file to avoid any corruption or problems with the file data


def adversarial_image(image_file_name,weights_file_name,biases_file_name):
    """
    Computation:
    The function will take an image of a number, weights and the biases and will find the pixels to flip such that the image 
    of the number is interpreted incorrectly 

    Input: An image txt file, its weights and biases
    Output: 
    - An adversarial image as a text file
    - Whether the first pixel flip was sufficient 
    - The number of pixels that were flipped
    - The changing of the number from x to y 
    - Which pixels were flipped

    For example:
    >>> x2 =  adversarial_image('image.txt','weights.txt','biases.txt')
    >>> print(x2)
    An adversairal image is found! Total of 2 pixels were flipped.
    The number was changed from 4 to 9 by flipping pixels 238,210

    Specific problems:
    The problems that were encountered were that the first pixel flip was not enough to change the image so that the inferrence function 
    would see the image incorrectly. The select pixel chosen was enough to lower the score but not enough to make it lower than any other different 
    number probability.

    Programming techniques:
    In this function, firstly the correct number is found through the inferrence() function. The most impactful pixel was then found using the select pixel function.
    The pixel that was found was then stored in a list for use later on. Then a check was done to see if the pixel that was selected was able to fufil the goal 
    of displaying an incorrect prediction using an if statement to see if the max of the inferrence was stil at the index of the actual number. If the pixel flip 
    was not enough, a while loop was used to keep finding new pixels of most impact and flipping them until the prediction was incorrect. Finally when the prediction 
    is incorrect the function creates a text file of the new adversarial image using the write_image() function and the difference of the two images is calculated using 
    the compute_difference() to find the amound of pixels flipped. Then the pixel numbers and the comparison of the original number and the adversarial are displayed. 

    """
    x = read_image(image_file_name) #get image in list format
    w = read_weights(weights_file_name) #get weights
    b = read_biases(biases_file_name) #get biases
    ori_image = read_image(image_file_name) #store a separate image of the original before manipulation 
    pixel_count = [] #create a list to store the pixels that are changed

    #distinguish image
    score_lst = inference(x,w,b) #find the list of scores 
    min_score = max(score_lst) #find the smallest number which shows the greatest change, greatest improbability 
    number_found= score_lst.index(min_score) #find the index of it, and this should represent the pixel that you have to flip as we have recorded the pixel number using the index position

    #find pixel
    max_impact_px = select_pixel(x,w,b) #find the maximum impact pixel 
    pixel_count.append(max_impact_px) #record this pixel number
    mod_lst= modified_list(max_impact_px,x) #flip the pixel at the location of the pixel number
    inf_lst = inference(mod_lst,w,b) # calculate a new inferrence

    #flipping more than 1 pixel 
    if max(inf_lst) == inf_lst[number_found]: #Check if change is enough, if not, then find the next pixel 
        while max(inf_lst) == inf_lst[number_found]: #while the number still reads as the correct number
            max_impact_px = select_pixel(mod_lst, w, b) #find new pixel 
            pixel_count.append(max_impact_px) #record the number onto the pixel list
            mod_lst = modified_list(max_impact_px,x) #change the original image
            inf_lst = inference(mod_lst,w,b) #find the inferrence of the new image 
    
    # #final message and text image generation, just change the return statement
    here = os.path.dirname(os.path.abspath(__file__))
    image_file = os.path.join(here, 'new_image.txt')
    write_image(mod_lst,image_file) #create a new adversarial image in the form of a text file
    dif_pix = compute_difference(ori_image,mod_lst) #find the difference between the original and the adversarial 
    new_num = argmax(inf_lst) #find what the new number reads as 
    pix_flipped = ",".join(map(str,pixel_count)) #find the pixels that were flipped, map is used as the numbers are int and join does not work on integers 
    
#return the information in an f string 
    return (f'An adversairal image is found! Total of {dif_pix} pixels were flipped.\nThe number was changed from {number_found} to {new_num} by flipping pixels {pix_flipped}')


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    image_file = os.path.join(here, 'another_image.txt')
    weight_file = os.path.join(here, 'weights.txt')
    bias_file = os.path.join(here, 'biases.txt')
    res = adversarial_image(image_file, weight_file, bias_file)
    print(res)









