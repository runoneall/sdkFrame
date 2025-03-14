import os
import sys

from . import sdk
from . import util

sdkModulePath = os.path.join(os.path.dirname(__file__), "modules")
sys.path.append(sdkModulePath)
sdkInstalledModules = [
    os.path.basename(x)
    for x in os.listdir(sdkModulePath)
    if os.path.isdir(os.path.join(sdkModulePath, x)) and x.startswith("m_")
]

sdkModuleDependencies = {}
for module in sdkInstalledModules:
    moduleDependecies = __import__(module).moduleInfo["dependencies"]
    sdkModuleDependencies[module] = moduleDependecies
try:
    sdkInstalledModules = [
        __import__(m)
        for m in util.topological_sort(sdkInstalledModules, sdkModuleDependencies)
    ]
except ValueError as e:
    print(e)
    exit(1)

print(sdkInstalledModules)
