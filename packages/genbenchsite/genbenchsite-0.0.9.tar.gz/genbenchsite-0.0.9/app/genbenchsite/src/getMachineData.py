import platform
import psutil
import multiprocessing
import datetime

import json


def GetRunMachineMetadata():
    """
    Get the metadata of the machine
    """
    return {
        "machine_os": platform.system(),
        "machine_os_version": platform.release(),
        "machine_os_architecture": platform.architecture(),
        "machine_processor": platform.processor(),
        "machine_processor_count": multiprocessing.cpu_count(),
        "machine_memory": psutil._common.bytes2human(psutil.virtual_memory().total),
        "machine_python_version": platform.python_version(),
        "execution_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }


def SaveMachineDataInJson(outputFile: str):
    with open(outputFile, "w") as file:
        json.dump(GetRunMachineMetadata(), file)
