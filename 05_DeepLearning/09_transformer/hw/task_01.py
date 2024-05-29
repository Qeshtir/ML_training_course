import torch
import torch.nn as nn


class Similarity1(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, encoder_states: torch.Tensor, decoder_state: torch.Tensor):
        # encoder_states.shape = [T, N]
        # decoder_state.shape = [N]
        # YOUR CODE HERE
        return torch.matmul(encoder_states, decoder_state.unsqueeze(1)).squeeze(1)



if __name__ == "__main__":
    # Создание двух тензоров
    tensor1 = torch.randn(3, 2)  # [T, N]
    tensor2 = torch.randn(2)  # [N]
    test = Similarity1
    print(test.forward(test, encoder_states=tensor1, decoder_state=tensor2))