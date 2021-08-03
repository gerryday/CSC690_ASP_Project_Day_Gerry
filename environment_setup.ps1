Remove-Item venv -Recurse -ErrorAction Ignore
python3 -m venv venv
.\venv\Scripts\activate
pip install flask
$env:FLASK_APP = "main"
$env:FLASK_ENV = "development"
flask run