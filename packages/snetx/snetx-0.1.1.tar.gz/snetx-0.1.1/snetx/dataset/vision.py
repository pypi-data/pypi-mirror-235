import os
import torch
import torchvision

from snetx import utils

def mnist_dataset(data_dir, batch_size, test_batch_size, transforms=None):
    if transforms == None:
        transform_train = torchvision.transforms.Compose([
            torchvision.transforms.RandomAffine(degrees=30, translate=(0.15, 0.15), scale=(0.85, 1.11)),
            torchvision.transforms.ToTensor(),
            torchvision.transforms.Normalize(0.1307, 0.3081),
        ])

        transform_test = torchvision.transforms.Compose([
            torchvision.transforms.ToTensor(),
            torchvision.transforms.Normalize(0.1307, 0.3081),
        ])
    else:
        transform_train, transform_test = transforms
        
    train_data_loader = torch.utils.data.DataLoader(
        dataset=torchvision.datasets.MNIST(
            root=os.path.join(data_dir, 'MNIST'),
            train=True,
            transform=transform_train,
            download=True
        ),
        batch_size=batch_size,
        shuffle=True,
        num_workers=4,
        drop_last=True,
        pin_memory=True
    )
    test_data_loader = torch.utils.data.DataLoader(
        dataset=torchvision.datasets.MNIST(
            root=os.path.join(data_dir, 'MNIST'),
            train=False,
            transform=transform_test,
            download=True
        ),
        batch_size=test_batch_size,
        shuffle=False,
        num_workers=4,
        drop_last=False,
        pin_memory=True
    )
    return train_data_loader, test_data_loader

def Fmnist_dataset(data_dir, batch_size, test_batch_size, transforms=None):
    if transforms == None:
        transform_train = torchvision.transforms.Compose([
            torchvision.transforms.ToTensor(),
            torchvision.transforms.Normalize(0.2860, 0.3530),
        ])
        transform_test = torchvision.transforms.Compose([
            torchvision.transforms.ToTensor(),
            torchvision.transforms.Normalize(0.2860, 0.3530),
        ])
    else:
        transform_train, transform_test = transforms
        
    train_data_loader = torch.utils.data.DataLoader(
        dataset=torchvision.datasets.FashionMNIST(
            root=os.path.join(data_dir, 'FashionMNIST'),
            train=True,
            transform=transform_train,
            download=True
        ),
        batch_size=batch_size,
        shuffle=True,
        num_workers=4,
        drop_last=True,
        pin_memory=True
    )
    test_data_loader = torch.utils.data.DataLoader(
        dataset=torchvision.datasets.FashionMNIST(
            root=os.path.join(data_dir, 'FashionMNIST'),
            train=False,
            transform=transform_test,
            download=True
        ),
        batch_size=test_batch_size,
        shuffle=False,
        num_workers=4,
        drop_last=False,
        pin_memory=True
    )
    return train_data_loader, test_data_loader

def cifar10_dataset(data_dir, batch_size, test_size, transforms=None):
    if transforms == None:
        transform_train = torchvision.transforms.Compose([
            torchvision.transforms.RandomCrop(32, padding=4),
            torchvision.transforms.RandomHorizontalFlip(),
            torchvision.transforms.ToTensor(),
            utils.Cutout(1, 16),
            torchvision.transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010)),
        ])

        transform_test = torchvision.transforms.Compose([
            torchvision.transforms.ToTensor(),
            torchvision.transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010)),
        ])
    else:
        transform_train, transform_test = transforms
        
    train_data_loader = torch.utils.data.DataLoader(
        dataset=torchvision.datasets.CIFAR10(
            root=os.path.join(data_dir, 'CIFAR10'),
            train=True,
            transform=transform_train,
            download=True
        ),
        batch_size=batch_size,
        shuffle=True,
        num_workers=2,
        drop_last=True,
        pin_memory=True
    )
    test_data_loader = torch.utils.data.DataLoader(
        dataset=torchvision.datasets.CIFAR10(
            root=os.path.join(data_dir, 'CIFAR10'),
            train=False,
            transform=transform_test,
            download=True
        ),
        batch_size=test_size,
        shuffle=False,
        num_workers=2,
        drop_last=False,
        pin_memory=True
    )
    return train_data_loader, test_data_loader

def cifar100_dataset(data_dir, batch_size, test_batch_size, transforms=None):
    if transforms == None:
        normalize = torchvision.transforms.Normalize(
            mean=[0.507, 0.487, 0.441],
            std=[0.267, 0.256, 0.276],
        )
        transform_train = torchvision.transforms.Compose([
            torchvision.transforms.RandomCrop(32, padding=4),
            torchvision.transforms.RandomHorizontalFlip(0.5),
            torchvision.transforms.ToTensor(),
            normalize
        ])
        
        transform_test = torchvision.transforms.Compose([
        #     transforms.RandomCrop(32, padding=4),
        #     transforms.RandomHorizontalFlip(0.5),
            torchvision.transforms.ToTensor(),
            normalize
        ])
    else:
        transform_train, transform_test = transforms
    
    train_data_loader = torch.utils.data.DataLoader(
        dataset=torchvision.datasets.CIFAR100(
            root=os.path.join(data_dir, 'CIFAR100'),
            train=True,
            transform=transform_train,
            download=True
        ),
        batch_size=batch_size,
        shuffle=False,
        num_workers=2,
        drop_last=False,
        pin_memory=True
    )
    
    test_data_loader = torch.utils.data.DataLoader(
        dataset=torchvision.datasets.CIFAR100(
            root=os.path.join(data_dir, 'CIFAR100'),
            train=False,
            transform=transform_test,
            download=True
        ),
        batch_size=test_batch_size,
        shuffle=False,
        num_workers=2,
        drop_last=False,
        pin_memory=True
    )
    return train_data_loader, test_data_loader