import datasets
from datasets import load_dataset

def load_mnist(settings: dict) -> list[datasets.arrow_dataset.Dataset,
                                       list[list[list[datasets.arrow_dataset.Dataset]]]]:
    """Loads the MNIST dataset, splits it into the number of shards, pre-process selected
    shards (subsets) and returns in a following format:
    list[   
        "Orchestrator Data"[
            Dataset
            ],   
        "Agents Data"[
            "Agent N"[
                "Train Data"[
                Dataset
                ],
                "Test Data"[
                Dataset
                ]
            ]]]
    Where all 'Datasets' are an instances of hugging face container datasets.arrow_dataset.Dataset
    ---------
    Args:
        settings (dict) : A dictionary containing all the dataset settings.
    Returns:
        list[datasets.arrow_dataset.Dataset,
                                       list[list[list[datasets.arrow_dataset.Dataset]]]]"""
    
    # Using the 'test' data as a orchestrator validaiton set.
    orchestrator_data = load_dataset('mnist', split='test')
    # Using the 'train' data as a dataset reserved for agents
    dataset = load_dataset('mnist', split='train')
    
    # List datasets for all nodes.
    nodes_data = []
    
    # Type: Random Uniform (Sharding) -> Same size, random distribution
    if settings['split_type'] == 'random_uniform':
        for shard in range(settings['shards']):
            agent_data = dataset.shard(num_shards=settings['shards'], index=shard)
            # In-shard split between test and train data.
            agent_data = agent_data.train_test_split(test_size=settings["local_test_size"])
            nodes_data.append([agent_data['train'], agent_data['test']])
    
    
    return [orchestrator_data, nodes_data]
            