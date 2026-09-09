import torch
import torch.nn as nn

class MlpPolicy(nn.Module):
    """ Neural Network for SAC for MlpPolicy type"""
    def __init__(self, input_dim, hidden_dim, activation: str, output_dim):
        super(MlpPolicy, self).__init__()
        self.activation = nn.ModuleDict({
            'relu': nn.ReLU(),
            'tanh': nn.Tanh()
        })

        if hidden_dim == None or len(hidden_dim) == 0:  # if no hidden layers specified by the user
            raise ValueError("hidden_dim cannot be None or empty")
        
        self.input_layer = nn.Sequential(
            nn.Linear(in_features=input_dim, out_features=hidden_dim[0]),
            self.activation,  # Note: BatchNorm and Dropout are avoided in RL (no overfitting and replay buffer)
        )
        
        for i in range(1, len(hidden_dim)-1):
            self.layers = nn.ModuleList(nn.Sequential(
                nn.Linear(in_features= hidden_dim[i], out_features= hidden_dim[i+1]),
                self.activation,
            ))

        self.output_layer = nn.Sequential(
            nn.Linear(in_features=hidden_dim[-1], out_features=output_dim),
            self.activation,  # Note: BatchNorm and Dropout are avoided in RL (no overfitting and replay buffer)
        )

    def forward(self, x):
        return self.output_layer(self.layers(self.input_layer(x)))
    
