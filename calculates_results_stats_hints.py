#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats_hints.py
#                                                                             
# PROGRAMMER: Paschal Ugwu
# DATE CREATED: 24/07/2024
# REVISED DATE: 24/07/2024
# PURPOSE: This script contains a function `calculates_results_stats` that
#          calculates various statistics from the results of a pet image
#          classification program. These statistics help evaluate the 
#          performance of different model architectures in classifying 
#          images as either dog or non-dog, and in correctly identifying 
#          dog breeds.

def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using the classifier's 
    model architecture to classify pet images. The function returns a dictionary 
    containing counts and percentages of various statistics.
    
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List:
                    idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifier labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet image 'is-NOT-a' dog
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
                            
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                         a percentage or a count) where the key is the statistic's 
                         name (starting with 'pct' for percentage or 'n' for count)
                         and the value is the statistic's value.
    """        
    # Initialize results_stats_dic dictionary
    results_stats_dic = dict()
    
    # Initialize counters
    results_stats_dic['n_dogs_img'] = 0
    results_stats_dic['n_match'] = 0
    results_stats_dic['n_correct_dogs'] = 0
    results_stats_dic['n_correct_notdogs'] = 0
    results_stats_dic['n_correct_breed'] = 0       
    
    # Process each item in results_dic
    for key in results_dic:
        # Count matches between pet image label and classifier label
        if results_dic[key][2] == 1:
            results_stats_dic['n_match'] += 1

        # Count correct dog breed classifications
        if results_dic[key][3] == 1 and results_dic[key][2] == 1:
            results_stats_dic['n_correct_breed'] += 1
        
        # Count number of dog images
        if results_dic[key][3] == 1:
            results_stats_dic['n_dogs_img'] += 1
            
            # Count correct dog classifications
            if results_dic[key][4] == 1:
                results_stats_dic['n_correct_dogs'] += 1
        else:
            # Count correct non-dog classifications
            if results_dic[key][4] == 0:
                results_stats_dic['n_correct_notdogs'] += 1

    # Calculate statistics
    results_stats_dic['n_images'] = len(results_dic)
    results_stats_dic['n_notdogs_img'] = (results_stats_dic['n_images'] - 
                                          results_stats_dic['n_dogs_img']) 
    results_stats_dic['pct_match'] = (results_stats_dic['n_match'] / 
                                      results_stats_dic['n_images']) * 100.0
    results_stats_dic['pct_correct_dogs'] = (results_stats_dic['n_correct_dogs'] / 
                                             results_stats_dic['n_dogs_img']) * 100.0
    results_stats_dic['pct_correct_breed'] = (results_stats_dic['n_correct_breed'] / 
                                              results_stats_dic['n_dogs_img']) * 100.0
    
    # Handle case with no non-dog images
    if results_stats_dic['n_notdogs_img'] > 0:
        results_stats_dic['pct_correct_notdogs'] = (results_stats_dic['n_correct_notdogs'] /
                                                    results_stats_dic['n_notdogs_img']) * 100.0
    else:
        results_stats_dic['pct_correct_notdogs'] = 0.0
        
    return results_stats_dic
