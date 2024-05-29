from torchvision.models import alexnet
from torchvision.models import vgg11
from torchvision.models import googlenet
from torchvision.models import resnet18
from torch import nn

def get_pretrained_model(model_name: str, num_classes: int, pretrained: bool=True):
    if model_name == "alexnet":
        if pretrained:
            model = alexnet(pretrained=True)
            model.classifier[6] = nn.Linear(in_features=4096, out_features=num_classes)
            return model
        else:
            model = alexnet()
            model.classifier[6] = nn.Linear(in_features=4096, out_features=num_classes)
            return model
    elif model_name == "vgg11":
        if pretrained:
            model = vgg11(pretrained=True)
            model.classifier[6] = nn.Linear(in_features=4096, out_features=num_classes)
            return model
        else:
            model = vgg11()
            model.classifier[6] = nn.Linear(in_features=4096, out_features=num_classes)
            return model
    elif model_name == "googlenet":
        if pretrained:
            model = googlenet(pretrained=True)
            model.fc = nn.Linear(in_features=1024, out_features=num_classes)
            return model
        else:
            model = googlenet()
            model.aux1.fc2 = nn.Linear(in_features=1024, out_features=num_classes)
            model.aux2.fc2 = nn.Linear(in_features=1024, out_features=num_classes)
            model.fc = nn.Linear(in_features=1024, out_features=num_classes)
            return model
    else:
        if pretrained:
            model = resnet18(pretrained=True)
            model.fc = nn.Linear(in_features=512, out_features=num_classes)
            return model
        else:
            model = resnet18()
            model.fc = nn.Linear(in_features=512, out_features=num_classes)
            return model


if __name__ == "__main__":
    model_name = ["alexnet", "vgg11", "googlenet", "resnet18"]
    for model in model_name:
        fin_model = get_pretrained_model(model, num_classes=20, pretrained=False)
        print(fin_model)
