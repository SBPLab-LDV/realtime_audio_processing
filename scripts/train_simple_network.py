import torch
from models.simple_network import SimpleNetwork

if __name__ == "__main__":
    model = SimpleNetwork()
    torch.save(model.state_dict(), 'models/simple_network.pth')
    print("模型已保存為 'models/simple_network.pth'")