# Quorum Test

Quorum Test is a small project running over Python and Django

## Prerequisites
If Python and Django aren't already configured, you can follow those first steps
```bash
sudo apt install python-is-python3
sudo apt install python3-pip

python -m pip install Django
```

## Setup
When Python and Django are already configured
```bash
mkdir ~/projects_quorum
cd ~/projects_quorum/

git clone git@github.com:mbrunocesar/quorum_test.git
# You can replace the cloning process with unzipping the zip version at ~/projects_quorum/
```


## Usage
First we start the Django server at port 8000
```bash
cd ~/projects_quorum/quorum_test
python manage.py runserver
```

## Usage
Then we just need to access the endpoints, there are both the JSON version and html based one
```curl
for JSON
curl http://localhost:8000/legislators/json
curl http://localhost:8000/bills/json

for HTML
curl http://localhost:8000/legislators
curl http://localhost:8000/bills
```

## License

[MIT](https://choosealicense.com/licenses/mit/)