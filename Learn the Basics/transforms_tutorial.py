"""
`学习基础知识 <intro.html>`_ ||
`快速开始 <quickstart_tutorial.html>`_ ||
`张量 <tensorqs_tutorial.html>`_ ||
`数据集和数据加载器 <data_tutorial.html>`_ ||
`变换  <transforms_tutorial.html>`_ ||
`创建模型 <buildmodel_tutorial.html>`_ ||
**自动求导** ||
`优化 <optimization_tutorial.html>`_ ||
`保存和加载模型 <saveloadrun_tutorial.html>`_

变换
===================

数据并不总是以训练机器学习算法所需的最终处理形式出现。我们使用**转换**来对数据进行一些对数据进行一些处理，使其适合训练。

所有的TorchVision数据集都有两个参数 -``transform`` 来修改特征，``target_transform`` to 来修改标签，这让它们接受包含转换逻辑的可调用文件。
`torchvision.transforms <https://pytorch.org/vision/stable/transforms.html>`_ 模块提供了几个常用的转换模块。

FashionMNIST的特征是PIL图像格式，而标签是整数。
为了训练，我们需要将特征作为归一化的张量，将标签作为one-hot编码的张量。
为了进行这些转换，我们使用 ``ToTensor`` 和 ``Lambda``.
"""

import torch
from torchvision import datasets
from torchvision.transforms import ToTensor, Lambda

ds = datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=ToTensor(),
    target_transform=Lambda(lambda y: torch.zeros(10, dtype=torch.float).scatter_(0, torch.tensor(y), value=1))
)

#################################################
# ToTensor()
# -------------------------------
#
# `ToTensor <https://pytorch.org/vision/stable/transforms.html#torchvision.transforms.ToTensor>`_
# 将PIL图像或NumPy的 ``ndarray`` 转换为 ``FloatTensor`` 。
# 图像的像素强度值在[0., 1.]范围内。
#

##############################################
# Lambda转换
# -------------------------------
#
# Lambda变换应用任何用户定义的lambda函数。这里，我们定义了一个函数把整数变成了一个one-hot编码的张量。
# 首先创建了一个大小为10的零张量（我们的数据集中的标签数量），并调用
# `scatter_ <https://pytorch.org/docs/stable/generated/torch.Tensor.scatter_.html>`_ which assigns a
# 在标签 ``y`` 给出的索引上分配一个 ``value=1`` 。

target_transform = Lambda(lambda y: torch.zeros(
    10, dtype=torch.float).scatter_(dim=0, index=torch.tensor(y), value=1))

######################################################################
# --------------
#

#################################################################
# 进一步学习
# ~~~~~~~~~~~~~~~~~
# - `torchvision.transforms API <https://pytorch.org/vision/stable/transforms.html>`_
