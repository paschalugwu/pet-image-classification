#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND/intropylab-classifying-images/print_functions_for_lab_checks.py
#
# PROGRAMMER: Paschal Ugwu
# DATE CREATED: 24/07/2024
# REVISED DATE: 24/07/2024
# PURPOSE: This set of functions can be used to check your code after programming 
#          each function. The top section of each part of the lab contains
#          the section labeled 'Checking your code'. When directed within this
#          section of the lab one can use these functions to more easily check 
#          your code. See the docstrings below each function for details on how
#          to use the function within your code.
#

def check_command_line_arguments(in_arg):
    """
    For Lab: Classifying Images - 7. Command Line Arguments
    Prints each of the command line arguments passed in as parameter in_arg, 
    assumes you defined all three command line arguments as outlined in 
    '7. Command Line Arguments'.
    
    Parameters:
     in_arg - Data structure that stores the command line arguments object
    
    Returns:
     None - just prints to console  
    """
    if in_arg is None:
        print("* Doesn't Check the Command Line Arguments because 'get_input_args' hasn't been defined.")
    else:
        print("Command Line Arguments:\n     dir =", in_arg.dir, 
              "\n    arch =", in_arg.arch, "\n dogfile =", in_arg.dogfile)

def check_creating_pet_image_labels(results_dic):
    """
    For Lab: Classifying Images - 9/10. Creating Pet Image Labels
    Prints first 10 key-value pairs and ensures there are 40 key-value pairs 
    in the results_dic dictionary. Assumes you defined the results_dic 
    dictionary as outlined in '9/10. Creating Pet Image Labels'.
    
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
                    (index 0 = pet image label (string))
    
    Returns:
     None - just prints to console  
    """
    if results_dic is None:
        print("* Doesn't Check the Results Dictionary because 'get_pet_labels' hasn't been defined.")
    else:
        stop_point = len(results_dic)
        if stop_point > 10:
            stop_point = 10
        print("\nPet Image Label Dictionary has", len(results_dic),
              "key-value pairs.\nBelow are", stop_point, "of them:")
    
        n = 0
        for key in results_dic:
            if n < stop_point:
                print("{:2d} key: {:>30}  label: {:>26}".format(n+1, key,
                      results_dic[key][0]))
                n += 1
            else:
                break

def check_classifying_images(results_dic):
    """
    For Lab: Classifying Images - 11/12. Classifying Images
    Prints Pet Image Label and Classifier Label for ALL Matches followed by ALL 
    NOT matches. Next prints out the total number of images followed by how 
    many were matches and how many were not-matches to check all 40 images are
    processed. Assumes you defined the results_dic dictionary as outlined in 
    '11/12. Classifying Images'.
    
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
                    (index 0 = pet image label (string),
                     index 1 = classifier label (string),
                     index 2 = 1/0 (int) where 1 = match between pet image and 
                     classifier labels and 0 = no match between labels)
    
    Returns:
     None - just prints to console  
    """
    if results_dic is None:
        print("* Doesn't Check the Results Dictionary because 'classify_images' hasn't been defined.")
    elif len(results_dic[next(iter(results_dic))]) < 2:
        print("* Doesn't Check the Results Dictionary because 'classify_images' hasn't been defined.")
    else:
        n_match = 0
        n_notmatch = 0
    
        print("\n     MATCH:")
        for key in results_dic:
            if results_dic[key][2] == 1:
                n_match += 1
                print("\n{:>30}: \nReal: {:>26}   Classifier: {:>30}".format(key, 
                      results_dic[key][0], results_dic[key][1]))

        print("\n NOT A MATCH:")
        for key in results_dic:
            if results_dic[key][2] == 0:
                n_notmatch += 1
                print("\n{:>30}: \nReal: {:>26}   Classifier: {:>30}".format(key,
                      results_dic[key][0], results_dic[key][1]))

        print("\n# Total Images",n_match + n_notmatch, "# Matches:",n_match ,
              "# NOT Matches:",n_notmatch)

def check_classifying_labels_as_dogs(results_dic):
    """
    For Lab: Classifying Images - 13. Classifying Labels as Dogs
    Prints Pet Image Label, Classifier Label, whether Pet Label is-a-dog (1=Yes,
    0=No), and whether Classifier Label is-a-dog (1=Yes, 0=No) for ALL Matches 
    followed by ALL NOT matches. Next prints out the total number of images 
    followed by how many were matches and how many were not-matches to check 
    all 40 images are processed. Assumes you defined the results_dic dictionary
    as outlined in '13. Classifying Labels as Dogs'.
    
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
                    (index 0 = pet image label (string),
                     index 1 = classifier label (string),
                     index 2 = 1/0 (int) where 1 = match between pet image and 
                     classifier labels and 0 = no match between labels,
                     index 3 = 1/0 (int) where 1 = pet image 'is-a' dog and 
                     0 = pet image 'is-NOT-a' dog, 
                     index 4 = 1/0 (int) where 1 = Classifier classifies image 
                     'as-a' dog and 0 = Classifier classifies image 'as-NOT-a' dog)
    
    Returns:
     None - just prints to console  
    """
    if results_dic is None:
        print("* Doesn't Check the Results Dictionary because 'adjust_results4_isadog' hasn't been defined.")
    elif len(results_dic[next(iter(results_dic))]) < 4:
        print("* Doesn't Check the Results Dictionary because 'adjust_results4_isadog' hasn't been defined.")
    else:
        n_match = 0
        n_notmatch = 0
    
        print("\n     MATCH:")
        for key in results_dic:
            if results_dic[key][2] == 1:
                n_match += 1
                print("\n{:>30}: \nReal: {:>26}   Classifier: {:>30}  \nPetLabelDog: {:1d}  ClassLabelDog: {:1d}".format(key,
                      results_dic[key][0], results_dic[key][1], results_dic[key][3], 
                      results_dic[key][4]))

        print("\n NOT A MATCH:")
        for key in results_dic:
            if results_dic[key][2] == 0:
                n_notmatch += 1
                print("\n{:>30}: \nReal: {:>26}   Classifier: {:>30}  \nPetLabelDog: {:1d}  ClassLabelDog: {:1d}".format(key,
                      results_dic[key][0], results_dic[key][1], results_dic[key][3], 
                      results_dic[key][4]))

        print("\n# Total Images",n_match + n_notmatch, "# Matches:",n_match ,
              "# NOT Matches:",n_notmatch)

def check_calculating_results(results_dic, results_stats_dic):
    """
    For Lab: Classifying Images - 14. Calculating Results
    Prints statistics from the results stats dictionary (created by the 
    calculates_results_stats() function) and the same statistics calculated 
    using the results dictionary. Assumes you defined the results_stats 
    dictionary and the statistics as outlined in '14. Calculating Results'.
    
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
                    (index 0 = pet image label (string),
                     index 1 = classifier label (string),
                     index 2 = 1/0 (int) where 1 = match between pet image and 
                     classifier labels and 0 = no match between labels,
                     index 3 = 1/0 (int) where 1 = pet image 'is-a' dog and 
                     0 = pet image 'is-NOT-a' dog, 
                     index 4 = 1/0 (int) where 1 = Classifier classifies image 
                     'as-a' dog and 0 = Classifier classifies image 'as-NOT-a' dog)
      results_stats_dic - Dictionary that contains the results statistics (either
                          a percentage or a count) where the key is the statistic's 
                          name (starting with 'pct' for percentage or 'n' for count)
                          and the value is the statistic's value
    
    Returns:
     None - just prints to console  
    """
    if results_stats_dic is None:
        print("* Doesn't Check the Results Dictionary because 'calculates_results_stats' hasn't been defined.")
    else:
        print("\n ** Results Statistics from calculates_results_stats() function:")
        print("N Images: ", results_stats_dic['n_images'])
        print("N Dog Images: ", results_stats_dic['n_dogs_img'])
        print("N Not-a-Dog Images: ", results_stats_dic['n_notdogs_img'])
        print("Pct Corr dog: %5.1f" % results_stats_dic['pct_correct_dogs'])
        print("Pct Corr NOTdog: %5.1f" % results_stats_dic['pct_correct_notdogs'])
        print("Pct Corr Breed: %5.1f" % results_stats_dic['pct_correct_breed'])
        print("Pct Match: %5.1f" % results_stats_dic['pct_match'])
    
        n_to_check = len(results_dic)
        if n_to_check > 10:
            n_to_check = 10
    
        print("\n ** Check Statistics - calculated from this function as a check:")
    
        n_images = len(results_dic)
        n_dogs_img = 0
        n_notdogs_img = 0
        n_match = 0
        n_correct_dogs = 0
        n_correct_notdogs = 0
        n_correct_breed = 0
    
        for key in results_dic:
            if results_dic[key][2] == 1:
                n_match += 1
    
            if results_dic[key][3] == 1:
                n_dogs_img += 1
    
                if results_dic[key][4] == 1:
                    n_correct_dogs += 1
    
                if results_dic[key][2] == 1:
                    n_correct_breed += 1
    
            else:
                n_notdogs_img += 1
    
                if results_dic[key][4] == 0:
                    n_correct_notdogs += 1
    
        pct_match = (n_match / n_images) * 100.0
        pct_correct_dogs = (n_correct_dogs / n_dogs_img) * 100.0
        pct_correct_breed = (n_correct_breed / n_dogs_img) * 100.0
        pct_correct_notdogs = (n_correct_notdogs / n_notdogs_img) * 100.0
    
        print("N Images: ", n_images)
        print("N Dog Images: ", n_dogs_img)
        print("N Not-a-Dog Images: ", n_notdogs_img)
        print("Pct Corr dog: %5.1f" % pct_correct_dogs)
        print("Pct Corr NOTdog: %5.1f" % pct_correct_notdogs)
        print("Pct Corr Breed: %5.1f" % pct_correct_breed)
        print("Pct Match: %5.1f" % pct_match)
