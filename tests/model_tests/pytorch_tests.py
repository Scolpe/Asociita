# A workaround for import error
import sys, os
from pathlib import Path
from collections import OrderedDict
import unittest
import logging
p = Path(__file__).parents[2]
p = os.path.join(p, 'asociita')
sys.path.insert(0, p)

from asociita.models.pytorch.federated_model import FederatedModel
from asociita.datasets.fetch_data import load_data
from asociita.models.pytorch.mnist import MnistNet


class PyTorch_Tests(unittest.TestCase):

    def test_init(self):
        settings_data = {"dataset_name": 'mnist',
                         "split_type": "random_uniform",
                         "shards": 10,
                         "local_test_size": 0.2,}
        settings_node = {
            "optimizer": "RMS",
            "batch_size": 32,
            "learning_rate": 0.1}
        data = load_data(settings=settings_data)
        model = MnistNet()

        self.federated_model = FederatedModel(settings=settings_node,
                                         local_dataset=data,
                                         net=model,
                                         node_name=0)
        print(self.federated_model.trainloader)
        print(self.federated_model.testloader)

        self.assertIsNotNone(self.federated_model)
        self.assertIsNotNone(self.federated_model.trainloader)
        self.assertIsNotNone(self.federated_model.testloader)
        self.assertEqual(0, self.federated_model.node_name)
        print("Initialization tests passed successfully")
    

    def test_get_weights(self):
        weights = self.federated_model.get_weights_list()
        self.assertIs(type(weights), list)
        weights = self.federated_model.get_weights()
        self.assertIs(type(weights), OrderedDict)
        print("Weights has been received successfully")


if __name__ == "__main__":
    test_instance = PyTorch_Tests()
    test_instance.test_init()
    test_instance.test_get_weights()