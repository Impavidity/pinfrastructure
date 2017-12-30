# TODO: https://discuss.pytorch.org/t/regularization-in-torch/2577
# TODO: https://discuss.pytorch.org/t/how-does-one-implement-weight-regularization-l1-or-l2-manually-without-optimum/7951
# TODO: https://gist.github.com/rtqichen/b22a9c6bfc4f36e605a7b3ac1ab4122f
# TODO: http://pytorch.org/docs/master/nn.html#torch.nn.utils.weight_norm

class optimizer:
    def __init__(self, parameter, config):
        self.optim = None
        raise NotImplementedError
        # The user must rewrite init part to define the optimizer
    def zero_grad(self):
        self.optim.zero_grad()

    def step(self):
        self.optim.step()

    def schedule(self):
        pass


