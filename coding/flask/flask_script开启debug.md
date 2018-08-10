manage.py
```python
from flask.ext.script import Manager, Server

app = Flask(__name__)
manager = Manager(app)
manager.add_command("runserver", Server(use_debugger=True))


if __name__ == "__main__":
    manager.run()
```
terminal
```bash
python manage.py runserver
```

