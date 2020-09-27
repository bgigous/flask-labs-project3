# Fake And Paginate

So while Samir was travelling back from his family's home, he ran into *yet another* Flask developer at the airport, Naomi (yes, he took a plane because Fredo means that much to him). In fact, she was in the plane seat next to him. Naomi grew up in Australia and has been a developer for a while. On the side, she's an avid skydiver.

It was that she really struggled with keeping track of what she needed to do for her projects, and on top of that traveled a lot and could never keep her paper todolists organized. So, she made a website in Flask for todolists that she could access anywhere! Samir was the first person who would listen to her blabber on an on about something that put everyone around them to sleep. Good news, because it was an overnight flight. Naturally, they exchanged contact info.

Sometimes, Naomi has such a long todolist that she gets annoyed having to scroll so far down a page just to find one todo. Samir couldn't help as he was busy with his blog, but he knew just who to go to... Enter you. You've just learned about **faking data and pagination**, and know just the thing to do. Once you can paginate the todolist, Naomi will be able to

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

