#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/check_images.py
#
# PROGRAMMER: Paschal Ugwu
# DATE CREATED: 24/07/2024
# REVISED DATE: 24/07/2024
# PURPOSE: Classifies pet images using a pretrained CNN model, compares these
#          classifications to the true identity of the pets in the images, and
#          summarizes how well the CNN performed on the image classification task.
#          The true identity of the pet (or object) in the image is indicated by
#          the filename of the image. The program extracts the pet image label
#          from the filename, classifies the images using the pretrained CNN model,
#          and compares the classifier results with the true labels to evaluate
#          the model's performance.
#
# Use argparse Expected Call with <> indicating expected user input:
#      python check_images.py --dir <directory with images> --arch <model>
#             --dogfile <file that contains dognames>
#   Example call:
#    python check_images_solution.py --dir pet_images/ --arch vgg --dogfile dognames.txt
##

# Imports python modules
from time import time, sleep

# Imports print functions that check the lab
from print_functions_for_lab_checks import *

# Imports functions created for this program
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

# Main program function defined below
def main():
    """
    The main function orchestrates the image classification workflow:
    1. It measures the program runtime.
    2. Retrieves command line inputs using argparse.
    3. Extracts pet labels from image filenames.
    4. Classifies images using a chosen CNN model.
    5. Adjusts the results for cases where images are dogs.
    6. Calculates statistics on the classification results.
    7. Prints a summary of the classification results.

    Args:
        None
    Returns:
        None
    """
    # Measures total program runtime by collecting start time
    start_time = time()
    
    # Retrieves command line arguments
    in_arg = get_input_args()

    # Check the command line arguments
    check_command_line_arguments(in_arg)

    # Creates the results dictionary
    results = get_pet_labels(in_arg.dir)

    # Check pet image labels in the results dictionary
    check_creating_pet_image_labels(results)

    # Classifies the images and adds these results to the results dictionary
    classify_images(in_arg.dir, results, in_arg.arch)

    # Check the results of classification
    check_classifying_images(results)    

    # Adjust the results dictionary for cases where the image is a dog
    adjust_results4_isadog(results, in_arg.dogfile)

    # Check the adjusted results
    check_classifying_labels_as_dogs(results)

    # Calculate the results statistics
    results_stats = calculates_results_stats(results)

    # Check the calculated results statistics
    check_calculating_results(results, results_stats)

    # Print the results
    print_results(results, results_stats, in_arg.arch, True, True)
    
    # Measure total program runtime by collecting end time
    end_time = time()
    
    # Compute and print total runtime in hh:mm:ss format
    tot_time = end_time - start_time
    print("\n** Total Elapsed Runtime:",
          str(int((tot_time/3600)))+":"+str(int((tot_time%3600)/60))+":"
          +str(int((tot_time%3600)%60)) )
    

# Call to main function to run the program
if __name__ == "__main__":
    main()
