import base64
import torch

from io import BytesIO
from torchvision import transforms
from torchvision.io import read_image
from torchvision.models import resnet152, ResNet152_Weights
from PIL import Image

def prep_model():
    weights = ResNet152_Weights.DEFAULT
    model = resnet152(weights=weights)
    model.eval()
    preprocess = weights.transforms()
    return weights, model, preprocess
    

def classify(imgstring, weights, model, preprocess):
    img = Image.open(BytesIO(base64.b64decode(imgstring)))
    batch = preprocess(img).unsqueeze(0)
    prediction = model(batch).squeeze(0).softmax(0)
    class_id = prediction.argmax().item()
    score = prediction[class_id].item()
    category_name = weights.meta["categories"][class_id]
    # print(f"{category_name}: {100 * score:.1f}%")
    result = {'category': category_name,
              'score': "{:.1f}".format(100 * score)}
    return result

