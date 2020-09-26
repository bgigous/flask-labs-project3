## Instructions

### Getting Started

To get started with this lab:

- Mac or Linux
  ```bash
  python3 -m venv env
  . env/bin/activate
  pip install -r requirements.txt
  export FLASK_APP=todolist.py
  # optional
  export FLASK_ENV=development
  # optional
  export FLASK_DEBUG=1
  # run the app
  flask run
  ```

- Windows
  ```powershell
  python3 -m venv env
  env\Scripts\activate.bat
  pip install -r requirements.txt
  set FLASK_APP=app.py
  # optional
  set FLASK_ENV=development
  # optional
  set FLASK_DEBUG=1
  # run the app
  flask run
  ```

[//]: # (To add some 'play' data you can run)
[//]: #     (pip install -r test-requirements.txt)
[//]: #     (flask fill-db)

