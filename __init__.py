import os

from . import sdk
from . import util

sdkModulePath = os.path.join(os.path.dirname(__file__), "modules")
sdkInstalledModules = [
    __import__("sdkFrame.modules.{}".format(os.path.basename(x)))
    for x in os.listdir(sdkModulePath)
    if os.path.isdir(os.path.join(sdkModulePath, x)) and x.startswith("m_")
]

print(sdkInstalledModules)
# elements = ["a", "b", "c"]
# dependencies = {"a": ["b", "c"], "c": ["b"], "b": []}

# try:
#     sorted_elements = util.topological_sort(elements, dependencies)
#     print(sorted_elements)
# except ValueError as e:
#     print(e)
#     exit(1)
