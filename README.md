# Fake GitHub Contributions Using Python

Ever wanted to have fun and impress your friends with a sky-high GitHub commit history? 🏆 Look no further! This Python script randomly generates fake contributions, making you look like a coding wizard with just a few lines of code. Perfect for those days when you're scrolling through TikTok but still want to seem productive. Create your very own commit carnival and watch those green squares pile up! 🎢

### Prerequisites

Make sure Python is installed on your machine.

Clone this repository and navigate into it:

### Usage

Make sure to replace `YOUR-USERNAME` and `YOUR-REPO` with your actual GitHub username and repository name, the copy past in your CMD:

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPO.git
cd YOUR-REPO
```


Adjust the start_date, end_date, and repo_path variables in the Python script according to your needs. the copy past in your CMD:


```bash
python
import os
import subprocess
from datetime import datetime, timedelta

start_date = datetime(2023, 7, 25)
end_date = datetime(2023, 7, 25)
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
```









