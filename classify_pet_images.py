import os
from classifier import classifier

def classify_images(image_paths, model_names):
    results = {}
    for model_name in model_names:
        results[model_name] = {}
        for image_path in image_paths:
            # Classify each image with the given model
            label = classifier(image_path, model_name)
            # Store results in dictionary
            results[model_name][os.path.basename(image_path)] = label
    return results

# List of images to classify
image_paths = [
    'pet_images/Basenji_00963.jpg', 'pet_images/Basenji_00974.jpg',
    'pet_images/Basset_hound_01034.jpg', 'pet_images/Beagle_01125.jpg',
    'pet_images/Beagle_01141.jpg', 'pet_images/Beagle_01170.jpg',
    'pet_images/Boston_terrier_02259.jpg', 'pet_images/Boston_terrier_02285.jpg',
    'pet_images/Boston_terrier_02303.jpg', 'pet_images/Boxer_02426.jpg',
    'pet_images/Cocker_spaniel_03750.jpg', 'pet_images/Collie_03797.jpg',
    'pet_images/Dalmatian_04017.jpg', 'pet_images/Dalmatian_04037.jpg',
    'pet_images/Dalmatian_04068.jpg', 'pet_images/German_shepherd_dog_04890.jpg',
    'pet_images/German_shepherd_dog_04931.jpg', 'pet_images/German_shorthaired_pointer_04986.jpg',
    'pet_images/Golden_retriever_05182.jpg', 'pet_images/Golden_retriever_05195.jpg',
    'pet_images/Golden_retriever_05223.jpg', 'pet_images/Golden_retriever_05257.jpg',
    'pet_images/Great_dane_05320.jpg', 'pet_images/Great_pyrenees_05367.jpg',
    'pet_images/Great_pyrenees_05435.jpg', 'pet_images/Miniature_schnauzer_06884.jpg',
    'pet_images/Poodle_07927.jpg', 'pet_images/Poodle_07956.jpg',
    'pet_images/Rabbit_002.jpg', 'pet_images/Saint_bernard_08010.jpg',
    'pet_images/Saint_bernard_08036.jpg', 'pet_images/cat_01.jpg',
    'pet_images/cat_02.jpg', 'pet_images/cat_07.jpg', 'pet_images/fox_squirrel_01.jpg',
    'pet_images/gecko_02.jpg', 'pet_images/gecko_80.jpg', 'pet_images/great_horned_owl_02.jpg',
    'pet_images/polar_bear_04.jpg'
]

model_names = ['resnet', 'alexnet', 'vgg']

# Classify images
results = classify_images(image_paths, model_names)

# Print results for inspection
for model_name in results:
    print(f"Results for model: {model_name}")
    for image_name, label in results[model_name].items():
        print(f"{image_name}: {label}")
