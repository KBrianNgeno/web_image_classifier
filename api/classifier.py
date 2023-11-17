import base64
import torch
import io, decimal
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

def base64_to_PILImage(base64string):
    base64bytes = base64.b64decode(base64string)
    bytesObj = io.BytesIO(base64bytes)
    img = Image.open(bytesObj)
    return img
    

# def classify(img, weights, model, preprocess):
def classify_image(image):
    # img = Image.open(image)
    weights = ResNet152_Weights.DEFAULT
    model = resnet152(weights=weights)
    model.eval()
    preprocess = weights.transforms()
    # img = Image.open(BytesIO(base64.b64decode(imgstring)))
    batch = preprocess(image).unsqueeze(0)
    prediction = model(batch).squeeze(0).softmax(0)
    class_id = prediction.argmax().item()
    score = prediction[class_id].item()
    category_name = weights.meta["categories"][class_id]
    # print(f"{category_name}: {100 * score:.1f}%")
    result = {'category': category_name,
              'score': "{:.1f}".format(100 * score)}
            #   'score': decimal.Decimal("{:.1f}".format(100 * score))}
    return result

