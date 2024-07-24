#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: Paschal Ugwu
# DATE CREATED: 24/07/2024
# REVISED DATE: 24/07/2024
# PURPOSE: This file contains the adjust_results4_isadog function that adjusts 
#          the results dictionary to indicate whether or not the pet image label 
#          is of a dog, and whether or not the classifier image label is of a dog.
#          This function helps to identify the classification performance in 
#          distinguishing dog images from non-dog images. The dog labels for both 
#          pet images and classifier functions are sourced from a text file.
#
##
# FUNCTION: adjust_results4_isadog
#          Adjusts the results dictionary to determine if classifier correctly 
#          classified images 'as a dog' or 'not a dog' especially when not a match. 
#          Demonstrates if model architecture correctly classifies dog images even 
#          if it gets dog breed wrong (not a match).
#          
#          Parameters:
#            results_dic - Dictionary with 'key' as image filename and 'value' as a 
#                          List. The list will contain the following items: 
#                          index 0 = pet image label (string)
#                          index 1 = classifier label (string)
#                          index 2 = 1/0 (int)  where 1 = match between pet image
#                                    and classifier labels and 0 = no match between labels
#                          index 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
#                                    0 = pet Image 'is-NOT-a' dog. 
#                          index 4 = 1/0 (int)  where 1 = Classifier classifies image 
#                                    'as-a' dog and 0 = Classifier classifies image  
#                                    'as-NOT-a' dog.
#            dogfile - A text file that contains names of all dogs from the classifier
#                      function and dog names from the pet image files. This file has 
#                      one dog name per line; dog names are all in lowercase with 
#                      spaces separating the distinct words of the dog name. Dog names
#                      from the classifier function can be a string of dog names separated
#                      by commas when a particular breed of dog has multiple dog names 
#                      associated with that breed (ex. maltese dog, maltese terrier, 
#                      maltese).
#
#          Returns:
#            None - results_dic is mutable data type so no return is needed.
#          
##

def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if classifier correctly 
    classified images 'as a dog' or 'not a dog' especially when not a match. 
    Demonstrates if model architecture correctly classifies dog images even if
    it gets dog breed wrong (not a match).
    
    Parameters:
      results_dic (dict): Dictionary with key as image filename and value as a 
                          list. The list contains:
                          index 0 = pet image label (string)
                          index 1 = classifier label (string)
                          index 2 = 1/0 (int)  where 1 = match between pet image
                                     and classifier labels and 0 = no match between labels
                          index 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                                     0 = pet image 'is-NOT-a' dog. 
                          index 4 = 1/0 (int)  where 1 = Classifier classifies image 
                                     'as-a' dog and 0 = Classifier classifies image  
                                     'as-NOT-a' dog.
     dogfile (str): A text file that contains names of all dogs from the classifier
                    function and dog names from the pet image files. This file has 
                    one dog name per line; dog names are all in lowercase with 
                    spaces separating the distinct words of the dog name. Dog names
                    from the classifier function can be a string of dog names separated
                    by commas when a particular breed of dog has multiple dog names 
                    associated with that breed (e.g., maltese dog, maltese terrier, 
                    maltese).
                    
    Returns:
        None - results_dic is a mutable data type so no return is needed.
    """           
    # Creates a dictionary to hold dog names for quick lookup
    dognames_dic = dict()

    # Reads in dog names from the dogfile and stores them in the dictionary
    with open(dogfile, "r") as infile:
        # Processes each line in the file
        for line in infile:
            # Removes newline character and any leading/trailing whitespace
            line = line.strip()
            # Adds the dog name to dognames_dic if it doesn't already exist
            if line not in dognames_dic:
                dognames_dic[line] = 1

    # Iterate through the results dictionary to update the 'is-a-dog' status
    for key in results_dic:
        # Check if the pet image label is a dog
        pet_label_is_dog = 1 if results_dic[key][0] in dognames_dic else 0
        # Check if the classifier label is a dog
        classifier_label_is_dog = 1 if results_dic[key][1] in dognames_dic else 0
        
        # Extend the list in results_dic with the results
        results_dic[key].extend([pet_label_is_dog, classifier_label_is_dog])
