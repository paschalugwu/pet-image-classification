#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images_hints.py

# PROGRAMMER: Paschal Ugwu
# DATE CREATED: 24/07/2024
# REVISED DATE: 24/07/2024
# PURPOSE: This is a *hints* file to help guide students in creating the 
#          function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function 
#             and as in_arg.dir for function call within main. 
#            -The results dictionary as results_dic within classify_images 
#             function and results for the function call within main.
#            -The CNN model architecture as model within classify_images function
#             and in_arg.arch for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison 
#           of the pet and classifier labels as the item at index 2 of the list.
#

# Imports classifier function for using CNN to classify images 
from classifier import classifier 

def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with classifier function, compares pet labels to 
    the classifier labels, and adds the classifier label and the comparison of 
    the labels to the results dictionary using the extend function. Be sure to
    format the classifier labels so that they will match your pet image labels.
    The format will include putting the classifier labels in all lower case 
    letters and strip the leading and trailing whitespace characters from them.
    For example, the Classifier function returns = 'Maltese dog, Maltese terrier, Maltese' 
    so the classifier label = 'maltese dog, maltese terrier, maltese'.
    Recall that dog names from the classifier function can be a string of dog 
    names separated by commas when a particular breed of dog has multiple dog 
    names associated with that breed. For example, you will find pet images of
    a 'dalmatian'(pet label) and it will match to the classifier label 
    'dalmatian, coach dog, carriage dog' if the classifier function correctly 
    classified the pet images of dalmatians.
    
    Parameters: 
      images_dir (str): The (full) path to the folder of images that are to be
                        classified by the classifier function
      results_dic (dict): Results Dictionary with 'key' as image filename and 'value'
                          as a List. Where the list will contain the following items: 
                          index 0 = pet image label (string)
                          NEW - index 1 = classifier label (string)
                          NEW - index 2 = 1/0 (int)  where 1 = match between pet image
                          and classifer labels and 0 = no match between labels
      model (str): Indicates which CNN model architecture will be used by the 
                   classifier function to classify the pet images,
                   values must be either: 'resnet', 'alexnet', 'vgg'
                   
    Returns:
      None - results_dic is mutable data type so no return needed.         
    """
    
    # Process all files in the results_dic - use images_dir to give fullpath
    # that indicates the folder and the filename (key) to be used in the 
    # classifier function
    for key in results_dic:
       
        # 3a. Run classifier function to classify the images
        # inputs: path + filename  and  model, returns model_label 
        model_label = classifier(images_dir + key, model)

        # 3b. Process the model_label to convert all characters to lowercase
        # and remove leading and trailing whitespace characters
        model_label = model_label.lower().strip()

        # Define truth as pet image label
        truth = results_dic[key][0]

        # 3c. Use extend list function to add the classifier label (model_label) 
        # and the value of 1 if there's a match between pet image label and the
        # classifier label, otherwise 0
        if truth in model_label:
            results_dic[key].extend([model_label, 1])
        else:
            results_dic[key].extend([model_label, 0])
