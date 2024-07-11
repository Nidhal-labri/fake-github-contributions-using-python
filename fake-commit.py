import os
import subprocess
from datetime import datetime, timedelta

start_date = datetime(2023, 7, 25)
end_date = datetime(2024, 7, 25)
repo_path = '/path/to/your/repo'
commit_message = 'Automated commit'
file_to_modify = 'README.md'

os.chdir(repo_path)

def make_commit(commit_date):
    with open(file_to_modify, 'a') as f:
        f.write(f'Commit on {commit_date}\n')
    
    subprocess.run(['git', 'add', file_to_modify])
    subprocess.run(['git', 'commit', '-m', commit_message, '--date', commit_date.isoformat()])

current_date = start_date
while current_date <= end_date:
    make_commit(current_date)
    current_date += timedelta(days=1)

subprocess.run(['git', 'push'])
