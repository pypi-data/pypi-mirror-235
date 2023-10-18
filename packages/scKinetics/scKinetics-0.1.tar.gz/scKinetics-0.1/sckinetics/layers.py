import torch
import anndata
import collections
import numpy as np
import torch.nn as nn
from tqdm import tqdm
import pytorch_lightning as pl
from typing import Iterable
from pytorch_lightning.callbacks import ProgressBarBase
import torch.nn.functional as F

class EpochProgressBar(ProgressBarBase):

    def __init__(self):
        super().__init__()
        self.bar = None

    def on_train_start(self, trainer, pl_module):
        self.bar = tqdm(
            desc='Epoch',
            leave=False,
            dynamic_ncols=True,
            total=trainer.max_epochs,
        )

    def on_train_epoch_end(self, *args, **kwargs):
        self.bar.update(1)

class UnS_Dataset(torch.utils.data.Dataset):
    def __init__(self,
                 Mu: np.ndarray = None,
                 Ms: np.ndarray = None,
                 u_v: np.ndarray = None,
                 s_v: np.ndarray = None,
                 ):

        self.u = Mu
        self.s = Ms
        self.u_v = u_v
        self.s_v = s_v

    def __len__(self):
        return self.u.shape[0]

    def __getitem__(self, index):
        u = torch.from_numpy(self.u[index]).float()
        s = torch.from_numpy(self.s[index]).float()
        u_v = torch.from_numpy(self.u_v[index]).float()
        s_v = torch.from_numpy(self.s_v[index]).float()

        return u, s, u_v, s_v


class AutoEncoder(pl.LightningModule):
    def __init__(self,
                 n_genes: int,
                 latent_dim: int,
                 hidden_dim: int = None,
                 activation_fn: nn.Module = nn.ReLU,
                 variational: bool = False,
                 gamma: float = 10):

        super().__init__()
        self.variational = variational


        self.encoder = nn.Sequential(
            SandwichFc(in_features=2*n_genes, out_features=hidden_dim, activation=activation_fn, scale=gamma**0.5),
            SandwichFc(in_features=hidden_dim, out_features=hidden_dim, activation=activation_fn),
            SandwichFc(in_features=hidden_dim, out_features=hidden_dim, activation=activation_fn),
        )

        if variational:
            self.mu_nn = nn.Sequential(
                SandwichFc(in_features=hidden_dim, out_features=latent_dim, activation=activation_fn),
            )
            self.log_var_nn = nn.Sequential(
                SandwichFc(in_features=hidden_dim, out_features=latent_dim, activation=activation_fn),
            )

        else:
            self.encoder_final_layer = nn.Sequential(
                SandwichFc(in_features=hidden_dim, out_features=latent_dim, activation=activation_fn),
            )

        self.decoder = nn.Sequential(
            SandwichFc(in_features=latent_dim, out_features=hidden_dim, activation=activation_fn,),
            SandwichFc(in_features=hidden_dim, out_features=hidden_dim, activation=activation_fn,),
            SandwichFc(in_features=hidden_dim, out_features=hidden_dim, activation=activation_fn,)
        )

        self.alpha_decoder = nn.Sequential(
            SandwichFc(in_features=hidden_dim, out_features=latent_dim, activation=nn.ReLU, scale=gamma**0.5),
        )

        self.beta_decoder = nn.Sequential(
            SandwichFc(in_features=hidden_dim, out_features=latent_dim, activation=nn.ReLU, scale=gamma**0.5),
        )

        self.gamma_decoder = nn.Sequential(
            SandwichFc(in_features=hidden_dim, out_features=latent_dim, activation=nn.ReLU, scale=gamma**0.5),
        )

    def forward(self, x, x_cat):
        pass

    def reparameterize(self, mu, log_var):
        std = torch.exp(log_var * 0.5)
        eps = torch.randn_like(std)

        return mu + eps * std

    def encode(self, x):

        if self.variational:
            x = self.encoder(x)
            mu = self.mu_nn(x)
            log_var = self.log_var_nn(x)
            return mu, log_var, self.reparameterize(mu, log_var)
        else:
            x = self.encoder(x)
            if self.inject_covariates:
                x = torch.concat([x], dim=1)
            return self.encoder_final_layer(x)

    def decode(self, x):
        x = self.decoder(x)

        return F.relu(self.alpha_decoder(x)), F.relu(self.beta_decoder(x)), F.relu(self.gamma_decoder(x))

"""
Codes below are modified from https://github.com/acfr/LBDN/blob/main/layer.py, the orginal artical about LBDNN is
"Direct Parameterization of Lipschitz-Bounded Deep Networks" at https://arxiv.org/abs/2301.11526
"""


def cayley(W):
    """
    Cayley transformation
    :param W: input matrix
    :return: Cayley transformed matrix
    """
    if len(W.shape) == 2:
        return cayley(W[None])[0]
    _, cout, cin = W.shape
    if cin > cout:
        return cayley(W.transpose(1, 2)).transpose(1, 2)
    U, V = W[:, :cin], W[:, cin:]
    I = torch.eye(cin, dtype=W.dtype, device=W.device)[None, :, :]
    A = U - U.conj().transpose(1, 2) + V.conj().transpose(1, 2) @ V
    iIpA = torch.inverse(I + A)
    return torch.cat((iIpA @ (I - A), -2 * V @ iIpA), axis=1)

class SandwichFc(nn.Linear):
    def __init__(self, in_features, out_features, bias=True, scale=1.0, activation=None):
        """
        The implementation of
        :param in_features: number of input features
        :param out_features: number of output features
        :param bias: use bias or not
        :param scale: used to control the upper bound of Lipschitz coefficient
        :param activation: activation function used in the layer,
               the slope of the activation function should always less or equal than 1
        """
        super().__init__(in_features+out_features, out_features, bias)
        self.alpha = nn.Parameter(torch.ones(1, dtype=torch.float32, requires_grad=True))
        self.alpha.data = self.weight.norm()
        self.scale = scale
        self.psi = nn.Parameter(torch.zeros(out_features, dtype=torch.float32, requires_grad=True))
        self.Q = None
        self.activation = activation

    def forward(self, x):
        fout, _ = self.weight.shape
        if self.training or self.Q is None:
            self.Q = cayley(self.alpha * self.weight / self.weight.norm())
        Q = self.Q if self.training else self.Q.detach()
        x = F.linear(self.scale * x, Q[:, fout:]) # B*h
        if self.psi is not None:
            x = x * torch.exp(-self.psi) * (2 ** 0.5) # sqrt(2) \Psi^{-1} B * h
        if self.bias is not None:
            x += self.bias
        x = self.activation(x) * torch.exp(self.psi) # \Psi z
        x = 2 ** 0.5 * F.linear(x, Q[:, :fout].T) # sqrt(2) A^top \Psi z
        return x