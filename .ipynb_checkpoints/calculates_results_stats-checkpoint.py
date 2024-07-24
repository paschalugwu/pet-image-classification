#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#                                                                             
# PROGRAMMER: Paschal Ugwu
# DATE CREATED: 24/07/2024
# REVISED DATE: 24/07/2024
# PURPOSE: Create a function calculates_results_stats that calculates the 
#          statistics of the results of the program run using the classifier's 
#          model architecture to classify the images. This function uses the 
#          results in the results dictionary to calculate these statistics 
#          and then stores them in a dictionary (results_stats_dic) that is 
#          returned by this function. This allows the user to determine the 
#          'best' model for classifying the images. The statistics include 
#          both counts and percentages.

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
    # Initialize the dictionary for storing statistics
    results_stats_dic = {}

    # Initialize counters for various statistics
    results_stats_dic['n_dogs_img'] = 0
    results_stats_dic['n_match'] = 0
    results_stats_dic['n_correct_dogs'] = 0
    results_stats_dic['n_correct_notdogs'] = 0
    results_stats_dic['n_correct_breed'] = 0       

    # Process each entry in results_dic to calculate statistics
    for key in results_dic:
        # Count the number of correct matches between pet and classifier labels
        if results_dic[key][2] == 1:
            results_stats_dic['n_match'] += 1

        # Count the number of correctly classified dog breeds
        if results_dic[key][3] == 1 and results_dic[key][2] == 1:
            results_stats_dic['n_correct_breed'] += 1
        
        # Count the number of dog images
        if results_dic[key][3] == 1:
            results_stats_dic['n_dogs_img'] += 1
            
            # Count the number of correctly classified dog images
            if results_dic[key][4] == 1:
                results_stats_dic['n_correct_dogs'] += 1
        else:
            # Count the number of correctly classified non-dog images
            if results_dic[key][4] == 0:
                results_stats_dic['n_correct_notdogs'] += 1

    # Total number of images
    results_stats_dic['n_images'] = len(results_dic)

    # Number of non-dog images
    results_stats_dic['n_notdogs_img'] = results_stats_dic['n_images'] - results_stats_dic['n_dogs_img']

    # Percentage of correctly matched images
    results_stats_dic['pct_match'] = (results_stats_dic['n_match'] / 
                                      results_stats_dic['n_images']) * 100.0

    # Percentage of correctly classified dog images
    results_stats_dic['pct_correct_dogs'] = (results_stats_dic['n_correct_dogs'] / 
                                             results_stats_dic['n_dogs_img']) * 100.0

    # Percentage of correctly classified dog breeds
    results_stats_dic['pct_correct_breed'] = (results_stats_dic['n_correct_breed'] / 
                                              results_stats_dic['n_dogs_img']) * 100.0

    # Percentage of correctly classified non-dog images
    if results_stats_dic['n_notdogs_img'] > 0:
        results_stats_dic['pct_correct_notdogs'] = (results_stats_dic['n_correct_notdogs'] /
                                                    results_stats_dic['n_notdogs_img']) * 100.0
    else:
        results_stats_dic['pct_correct_notdogs'] = 0.0
        
    return results_stats_dic
