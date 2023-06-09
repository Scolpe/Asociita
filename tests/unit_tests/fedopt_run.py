from tests.unit_tests.components.settings.settings_test import unit_test_settings
from components.orchestrator.fedopt_orchestrator import unit_test_fedoptorchestrator
from components.orchestrator.fedopt_orchestrator import unit_test_fedoptorchestrator_warchiver

def test_suite():
    # Test 1: Generic Setting Class Object Initialization
    test_settings = unit_test_settings()
    # Test 2: Generic Orchestrator Class Object Initialization
    test_genorch = unit_test_fedoptorchestrator()
    print("The simulation of FedOpt orchestrator training and managing nodes was passed successfully.")

def test_suite2():
    # Test 2: Generic Orchestrator Class Object Initialization
    test_genorch = unit_test_fedoptorchestrator_warchiver()
    print("The simulation of generic orchestrator training and managing nodes was passed successfully.")

if __name__ == "__main__":
    test_suite()
    test_suite2()