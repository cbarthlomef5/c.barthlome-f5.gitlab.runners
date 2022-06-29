# deployDevOpsEnv.py
# Script to deploy DevOps environment for personal lab
#

# Enable or Disable Debug Logging
debug_logging = 1

#Import Modules
import subprocess, sys, os

# Copy .secrets files
src = '/private/etc/.secrets/'
dst = '/Users/c.barthlome/Documents/Code/F5/DevOpsEnvironment/f5.gitlab.runners/secrets/'
os.system('cp -rf %s %s' % (src, dst))

# Install required Python modules
if(debug_logging == 1) : print('='*50)
if(debug_logging == 1) : print('Installing required Python modules...')

# Set full file path for requirements file
requirementsFilePath = __file__
stringSplit = requirementsFilePath.split('/')
stringEndLen = len(stringSplit[-1])
requirementsFilePath = requirementsFilePath[:-stringEndLen]
requirementsFilePath = requirementsFilePath + "requirements.txt"

# Install Python modules from requirements file
subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirementsFilePath], stdout=subprocess.DEVNULL)

if(debug_logging == 1) : print('Required modules installed!')
if(debug_logging == 1) : print('='*50)

# Import Third Party Modules
from python_on_whales import docker

# Deploy Docker containers
if(debug_logging == 1) : print('='*50)
if(debug_logging == 1) : print('Deploying Docker environment. Please wait...')

# Deploy Docker environment from docker-compose.yml file
docker.compose.build()
docker.compose.up(detach=True)

if(debug_logging == 1) : print('Docker environment deployed!')
if(debug_logging == 1) : print('='*50)
