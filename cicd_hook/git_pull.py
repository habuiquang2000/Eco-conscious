import subprocess
cwd = 'D:/__Code/___My_Project/_University/2024/Eco-conscious/templates/NCKH-2024'
# command = 'git pull'
# command = 'git fetch'
command = 'git restore .'
process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, cwd=cwd)
output, unused_err = process.communicate()
print(output)