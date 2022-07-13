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
#importing files 
import os 


# Part 1 (due Week 6)
def linear(x, w, b): # 1 Mark
    """
    Computation: 
    This function computes the euqation of f(x) using a list of inputs (x), 
    a list of weights (w) and a bias (b) 

    Input: A list of inputs (x), a list of weights (w) and a bias (b).
    Output: A single number corresponding to the value of f(x) in Equation 1.

    >>> x = [1.0, 3.5]
    >>> w = [3.8, 1.5]
    >>> b = -1.7
    >>> round(linear(x, w, b),6) #linear(x, w, b)
    7.35

    Specific problems:
    The problems faced in this is the addition of two numbers that are in the same index
    but at different lists. After the addition of the numbers, a bias must be added to the resulting
    sum. A for loop was used to iterate through the items of the list.

    Programming techniques:
    This problem was tackled using a for loop as the i could act as the index to iterate through 
    both lists and add the numbers. The additions were then stored in a variable called carry which 
    could then be added to the bias later on. 


    """
    carry = 0 #storage variable
    for i in range(len(w)): #i = index to iterate through both lists
        carry = x[i]*w[i] + carry #times the numbers of index 0 / index 1 and store them in carry
    summation = carry + b #after iteration has finished, add the bias 
    return summation #return the output of f(x)
    pass



def linear_layer(x, w, b): # 1 Mark
    """
    Computation:
    This function calculates the final step of layer 3 to the output using the input from 
    layer 2

    Input: A list of inputs (x), a table of weights (w) and a list of 
           biases (b).
    Output: A list of numbers corresponding to the values of f(x) in
            Equation 2.
    
    >>> x = [1.0, 3.5]
    >>> w = [[3.8, 1.5], [-1.2, 1.1]]
    >>> b = [-1.7, 2.5]
    >>> y = linear_layer(x, w, b)
    >>> [round(y_i,6) for y_i in y] #linear_layer(x, w, b)
    [7.35, 5.15]

    Specific problems:
    The linear layer function has the addition of a two dimensional list which needs to be 
    iterated through separately, requiring the use of loops to compute two different outputs 
    from the two different biases and weight lists.

    Programming techniques:
    In this function a nested for loop is used. The first loop is used to iterate through the 
    weight lists while the secondary i2 index is used to select the elements insdie the 
    individual lists. The same concept as the previous function linear is used where the numbers are
    times and loaded into a variable called carry before a bias is added to it. However in this
    code, a separate list is needed to contain both the outputs. Therefore the use of 
    list.append() is used to store each individual output in a list one after another when they 
    have been computed by the loop.

    """
    linear_layer_x_list = [] #list to contain final x values 
    carry = 0 #storage variable
    for i in range(len(x)): #iterates over the lists in weights, number in x and number in bias
        for i2 in range(len(w[i])): #used to target an individual value within the secondary list
            carry = carry + x[i2]*w[i][i2] #computation of weight times the x values
        summation = carry + b[i] #bias is added to equation to form final output
        linear_layer_x_list.append(summation) #final output is then appended to the list of final x values
        summation = 0 #clear variable for further iterations
        carry = 0 #clear variable for further iterations
    return linear_layer_x_list #return list of x outputs 
    pass

def inner_layer(x, w, b): # 1 Mark
    """
    Computation:
    The program inner layer computes the outputs of layer two using the inputs of layer one with the function f(x). The computation of 
    this problem is exactly the same as the linear layer function and are both interchangable 

    Input: A list of inputs (x), a table of weights (w) and a 
           list of biases (b).
    Output: A list of numbers corresponding to the values of f(x) in 
            Equation 4.

    >>> x = [1, 0]
    >>> w = [[2.1, -3.1], [-0.7, 4.1]]
    >>> b = [-1.1, 4.2]
    >>> y = inner_layer(x, w, b)
    >>> [round(y_i,6) for y_i in y] #inner_layer(x, w, b)
    [1.0, 3.5]
    >>> x = [0, 1]
    >>> y = inner_layer(x, w, b)
    >>> [round(y_i,6) for y_i in y] #inner_layer(x, w, b)
    [0.0, 8.3]

    Specific problems:
    The inner layer function has the addition of a two dimensional list which needs to be 
    iterated through separately, requiring the use of loops to compute two different outputs 
    from the two different biases and weight lists.


    Programming techniques:
    In this function a nested for loop is used. The first loop is used to iterate through the 
    weight lists while the secondary i2 index is used to select the elements insdie the 
    individual lists. The same concept as the previous function linear is used where the numbers are
    times and loaded into a variable called carry before a bias is added to it. However in this
    code, a separate list is needed to contain both the outputs. Therefore the use of 
    list.append() is used to store each individual output in a list one after another when they 
    have been computed by the loop.



    """
    inner_layer_x_list = [] #list to store the inner layer output x variables 
    carry = 0 #Storage variable
    for i in range(len(w)):# for loop to iterate through the lists of weight, bias and x value inputs
        for i2 in range(len(w[i])):# loop to deal with the multi-dimensional lists 
            carry = carry + x[i2]*w[i][i2] #used to store the multiplication of the martrix 
        summation = max(carry + b[i],0) #addition of the bias with the extra conditon of max, where if the funciton is negative, it replaces it with 0 
        inner_layer_x_list.append(float(summation)) #store the final output in the list using append
        summation = 0 #clear variable for next iteration 
        carry = 0 #clear variable for next iteration 
    return inner_layer_x_list #return the outputs 
    pass


def inference(x, w, b): # 2 Marks
    """
    Computation:
    This function brings together the computation of both inner and linear layer to output the desired x outputs 

    Input: A list of inputs (x), a list of tables of weights (w) and a table
           of biases (b).
    Output: A list of numbers corresponding to output of the ANN.
    
    >>> x = [1, 0]
    >>> w = [[[2.1, -3.1], [-0.7, 4.1]], [[3.8, 1.5], [-1.2, 1.1]]]
    >>> b = [[-1.1, 4.2], [-1.7, 2.5]]
    >>> y = inference(x, w, b)
    >>> [round(y_i,6) for y_i in y] #inference(x, w, b)
    [7.35, 5.15]

    Specific problems:
    The problems that are joining of the functions to compute the desired x outputs through the computation of the linear and inner layer. 
    The x value must be transferred from one function to the other to compute the desired resuting output

    Programming techniques:
    A for loop was used to loop through the various multi dimensional lists, a temp_w and temp_b were used as flexible variables
    to be able to switch to the next list for the secondary input. The x value was then overriden and computed again. Due to the similarity of the 
    functions it is actually easier to use the inner layer function in a for loop which both reduces the amount of coding required 
    while providing the desired accurate output. 
    """
    for i in range(len(w)): #using a for loop where i is an index to iterate through the various lists 
        temp_w = w[i] #temporary variable which is overriden to compute each iteration of the for loop
        temp_b = b[i] #temporary variable which is overriden to compute each iteration of the for loop
        x = inner_layer(x,temp_w,temp_b) #the inner layer is iterated through both times to provide the desired x outputs
    return x #return the desired x output
    pass



def read_weights(file_name): # 1 Mark
    """
    Computation:
    This function is used to open and read a file. After reading it copies the file onto a list where the hashtag(#) is used to denote the splitting
    of the matrixes.

    Input: A string (file_name) that corresponds to the name of the file
           that contains the weights of the ANN.
    Output: A list of tables of numbers corresponding to the weights of
            the ANN.
    
    >>> w_example = read_weights('example_weights.txt')
    >>> w_example
    [[[2.1, -3.1], [-0.7, 4.1]], [[3.8, 1.5], [-1.2, 1.1]]]
    >>> w = read_weights('weights.txt')
    >>> len(w)
    3
    >>> len(w[2])
    10
    >>> len(w[2][0])
    16
    
    Specific problems:
    The specific problem was the # in the looping as the # is usually used to denote a comment and thus had to be recognised as a string first
    before its condition could be completed. The storing into multiple lists was also an issue as multiple for loops with exit conditions 
    have to be created. 

    Programming techniques:
    In this program, I change the order of the delimited (#) from the front to the end of the list while using next(f) to skip over the first
    line of the program. Using the .extend() attribute, I added a # to the end of the list instead to denote the instance of a new list. 
    Whenever a # was reached, the temporary list was inserted into the final list, allowing for the desired splitting of the matrixes. 

    """
    final_list = [] #the final list with the 
    weight_list = [] #list to iterate through
    new_list = [] #storage list before reaching a # and this is emptied into final list 
    stripped_file = 0 #the stripped data from the file 
    list_carry = [] #list container to transfer the lists from one list to another 
    #function to convert the items in the list from string to floating points before being put in the new_list
    def str_to_float(lst):
        for i in range(len(lst)): #iterate through all the items of the list
            lst[i] = float(lst[i]) #change each string into a float variables 
        return lst #return the converted list 
    


    with open(file_name,'r') as f: #use the with open so that we don't have to worry about f.close()
        next(f) #skip the first line
        file_contents = f.read().strip().split() #copy the whole thing out of the file, strip the white space and each element into a list
    file_contents.extend(["#"]) #add an extra # at the end 
    for i in range(len(file_contents)): #i used to iterate through the various lists
        stripped_file = file_contents[i].split(',') #split the contents of string into a list using the ',' as the split location 
        for j in range(len(stripped_file)): #iterate through the new list created by split
            if stripped_file[j] == "#": #if the # is detected
                while new_list: #while the new list still has elements, if [] then it will return False 
                    list_carry = new_list.pop(0)  #take the items out one by one from the left, index 0 instead of the default end of the list in the usual .pop()
                    weight_list.append(list_carry) #add the popped variable into the weight_list
                final_list.insert(len(final_list),weight_list) #Weight list is then inserted into the final list
                weight_list = [] #weight list is then emptied
                break #iterate to the next list 
                
            else:
                stripped_file = str_to_float(stripped_file)  #change the items inside from string to float
                new_list.append(stripped_file) #store inside the stripped file 
                break #iterate to next thing in list

    return final_list #return the split matrixes
  
    pass


def read_biases(file_name): # 1 Mark
    """
    Computation:
    The function read_biases is used to read into the text file and extract the data. The extracted data is then stored in lists with the 
    hashtag denoting the split between the lists

    Input: A string (file_name), that corresponds to the name of the file
           that contains the biases of the ANN.
    Output: A table of numbers corresponding to the biases of the ANN.
    
    >>> b_example = read_biases('example_biases.txt')
    >>> b_example
    [[-1.1, 4.2], [-1.7, 2.5]]
    >>> b = read_biases('biases.txt')
    >>> len(b)
    3
    >>> len(b[0])
    16
    
    Specific problems:
    The specific problem was the # in the looping as the # is usually used to denote a comment and thus had to be recognised as a string first
    before its condition could be completed. The storing into multiple lists was also an issue as multiple for loops with exit conditions 
    have to be created. 

    Programming techniques:
    In this program, I change the order of the delimited (#) from the front to the end of the list while using next(f) to skip over the first
    line of the program. Using the .extend() attribute, I added a # to the end of the list instead to denote the instance of a new list. 
    Whenever a # was reached, the temporary list was inserted into the final list, allowing for the desired splitting of the matrixes. 

    """
    bias_list = [] #final list 
    new_list = [] #list used to empty into bias_list when the hashtag is reached    
    stripped_file = 0 #Where the read and stripped file is stored
    list_carry = [] #storage list to transfer items 
    def str_to_float(lst): #this function changes the items inside the list into a float from a string 
        for i in range(len(lst)): #uses i to iterate through all items in the list of its length
            lst[i] = float(lst[i]) #change items to float
        return lst #return the list 
    


    with open(file_name,'r') as f: #used so that f.close is not needed  
        next(f) #skip the first line 
        file_contents = f.read().strip().split() #read, strip and split what is read in the file and store it in file contents 
    file_contents.extend(["#"]) #add a hashtag to the end 
    for i in range(len(file_contents)): #iterate through the lists
        stripped_file = file_contents[i].split(',') #split the string into lists wherever there is a "," 
        for j in range(len(stripped_file)): #go through the items in the list created from split 
            if stripped_file[j] == "#":#if a hashtag is found
                while new_list: #while the list has items in it 
                    list_carry = new_list.pop(0)   #take the items out into the carry list
                    bias_list.append(list_carry) #append the carried elements into the final bias list
                break
                
            else:
                stripped_file = str_to_float(stripped_file) #change the items inside the list to float instead of string
                new_list.append(stripped_file) #append the file to new list
                break
            
    return bias_list #return the bias list 

  
    pass


def read_image(file_name): # 1 Mark
    """
    Computation:
    The function here is used to take the image and convert it into a list where each individual number of either 1 or 0 is in a separate 
    index location and is an integer instead of a string. 

    Input: A string (file_name), that corresponds to the name of the file
           that contains the image.
    Output: A list of numbers corresponding to input of the ANN.
    
    >>> x = read_image('image.txt')
    >>> len(x)
    784

    Specific problems:
    The function should be able to read and strip the file of any whitespace, then split the file into a list. The list must be then
    iterated through to change each individual element into an integer for calculations later on.

    Programming techniques:
    After stripping and splitting the items, the different strings are then concatenation using the .join() attribute into a large line of
    text, it is then put throught the list() fucntion to change each individual string into an element into the list. Finally it is then 
    put through the function str_to_int() to iterate through the list and change each element from a string to an integer 
    """
    def str_to_int(lst): #function to change the strings in a list to integers
        for i in range(len(lst)): #use a for loop to iterate through all the elements   
            lst[i] = int(lst[i]) #change each one individually to an integer
        return lst #when all elements have been iterated through, return the list

    with open(file_name,'r') as f: #open the file with open() as f to not make mistakes in closing it
        file_contents = f.read().strip().split() #read, strip and split the image
    str_file_contents = ''.join(file_contents) #concatenate the string
    lst_image = list(str_file_contents)#change it into a list 
    lst_image = str_to_int(lst_image) #change all strings into integer
    return lst_image #return the image in list form
    pass


def argmax(x): # 1 Mark
    """
    Computation:
    This function is used to find the index of the largest value in a list

    Input: A list of numbers (i.e., x) that can represent the scores 
           computed by the ANN.
    Output: A number representing the index of an element with the maximum
            value, the function should return the minimum index.
    
    >>> x = [1.3, -1.52, 3.9, 0.1, 3.9]
    >>> argmax(x)
    2

    Specific problems:
    The function needs to iterate through all elements in the list while comparing the elements within to check which is the largest.
    The largest number's index must be stored and at the end of the code must be outputted. Multiple numbers of the same number is also
    a problem and it must be the first instance of the number that must be recorded. 

    Programming techniques:
    A for loop is used to iterate through the items in the list, if the number is bigger, it is stored in max_num and goes to the next element
    if the next element is bigger, it is stored;else it goes on to the next element in the list. The index of the max number is stored in 
    carry and is then outputted at the end of the for loop. If there is a duplicate later on in the list, it just skips it to the next index.
    """
    carry = 0 #stores the index of the largest number
    max_num = 0 #stores the largest number
    for i in range(len(x)): #iterate through the whole list
        if x[i] > max_num: #if the number in the list is bigger than the max num
            max_num = x[i] #replace the max number with the bigger one
            carry = i #store the index of the bigger number
        else:
            max_num = max_num #otherwise just keep the max number
    return "The image is number " + str(carry)#return the index 
    pass

def predict_number(image_file_name, weights_file_name, biases_file_name): # 1 Mark
    """
    Computation:
    Take the text files of image, weight and biases. Read and put them into lists. Then use the inference function to compute the 
    information using the f(x) function and output a list of x values of the probability each number. Argmax(x) is then used to find which 
    the number through the largest number in the x list of probabilites. The index is the most probable number.

    Input: A string (i.e., image_file_name) that corresponds to the image
           file name, a string (i.e., weights_file_name) that corresponds
           to the weights file name and a string (i.e., biases_file_name)
           that corresponds to the biases file name.
    Output: The number predicted in the image by the ANN.

    >>> i = predict_number('image.txt', 'weights.txt', 'biases.txt')
    >>> print('The image is number ' + str(i))
    The image is number 4

    Specific problems:
    The text files must be converted into lists to be able to be computed by the inference function. Argmax is then used to find the 
    predicted number

    Programming techniques:
    The different lists were stored in variables of their respective names of iamge, weights and bias. They were then put through inference 
    and stored in a variable x. They are put into the function argmax to find the predicted number from the output of x. The number is then
    returned. 
    """
    image = read_image(image_file_name) #read the file of image and put them into a list
    weights = read_weights(weights_file_name)#read the file of weights and put them into the list
    bias = read_biases(biases_file_name) #Read the file of bias and put them into the list 
    x = inference(image,weights,bias) #put the different lists into the inference to get an output of X values that predict the likeliness of each number
    return(argmax(x)) #return the predicted number 

    pass




if __name__ == "__main__":
    #need to set path of weights, biases and source image 
    here = os.path.dirname(os.path.abspath(__file__))
    #setting files for first image 
    image_file = os.path.join(here, 'image.txt')
    weight_file = os.path.join(here, 'weights.txt')
    bias_file = os.path.join(here, 'biases.txt')
    print(predict_number(image_file, weight_file, bias_file)) # should return 4

    #setting files for alternate image 
    image_file = os.path.join(here, 'another_image.txt')
    print(predict_number(image_file, weight_file, bias_file)) #should return 8 