# PROGRAMMER: Paschal Ugwu
# DATE CREATED: 24/07/2024
# REVISED DATE: 24/07/2024

import ast
from PIL import Image
import torchvision.transforms as transforms
from torch.autograd import Variable
import torchvision.models as models
from torch import __version__

# Load pretrained models
resnet18 = models.resnet18(pretrained=True)
alexnet = models.alexnet(pretrained=True)
vgg16 = models.vgg16(pretrained=True)

# Dictionary to hold models
models = {'resnet': resnet18, 'alexnet': alexnet, 'vgg': vgg16}

# Obtain ImageNet labels
with open('imagenet1000_clsid_to_human.txt') as imagenet_classes_file:
    imagenet_classes_dict = ast.literal_eval(imagenet_classes_file.read())

def classifier(img_path, model_name):
    """
    Classifies an image using a pretrained model.

    Parameters:
    img_path (str): Path to the input image.
    model_name (str): The name of the model to use for classification ('resnet', 'alexnet', 'vgg').

    Returns:
    str: The human-readable class label predicted by the model.
    """

    # Load the image
    img_pil = Image.open(img_path)

    # Define the transformations
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    
    # Preprocess the image
    img_tensor = preprocess(img_pil)
    
    # Add a batch dimension
    img_tensor.unsqueeze_(0)
    
    # Get PyTorch version
    pytorch_ver = __version__.split('.')
    
    # Adjust for PyTorch version differences
    if int(pytorch_ver[0]) > 0 or int(pytorch_ver[1]) >= 4:
        img_tensor.requires_grad_(False)
    else:
        data = Variable(img_tensor, volatile=True)

    # Select the model
    model = models[model_name]

    # Set the model to evaluation mode
    model = model.eval()
    
    # Get the model's output
    if int(pytorch_ver[0]) > 0 or int(pytorch_ver[1]) >= 4:
        output = model(img_tensor)
    else:
        output = model(data)

    # Get the predicted class index
    pred_idx = output.data.numpy().argmax()

    # Return the human-readable class label
    return imagenet_classes_dict[pred_idx]
