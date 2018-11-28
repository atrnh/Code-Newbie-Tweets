# Code Newbie Rewind

This is a fork of @aligg's [Code Newbie
Tweets](https://github.com/aligg/Code-Newbie-Tweets). For more information about
the motivations behind this project, go to the original repo.

This is a fork where I revert most changes and file more bugs so there's more
stuff to do for this open source workshop at Hackbright Academy.

Also it uses Reddit instead of Twitter.

Also it has some setup scripts.

## How to contribute

- Follow the instructions in [Installing for
  development](#Installing-for-development)
- Find an issue (or open a new one)
- Read the wiki
- ???
- Profit

## Installing for development

### Dependencies

- Python 3
- PostgreSQL
- A Reddit API key

### How to install

#### Install project dependencies

In a virtual environment, run

```
pip install --upgrade pip
pip install -r requirements.txt
```

#### Run setup script

```
python setup.py
```

This script will

- Create a directory called `secret` with an empty `__init__.py` file inside
- Make a `keys.py` file in the `secret` directory

and remind you to populate `keys.py` with your Reddit API credentials.

#### Configuration

If you'd like to alter default behavior, set the following variables in your
environment:

`NEWBIE_TWEETS_DB_URI`
  Override `DEFAULT_DB_URI` in `server.py`

`NEWBIE_TWEETS_LISTEN_HOST`
  Override `DEFAULT_LISTEN_HOST` in `server.py`

`NEWBIE_TWEETS_LISTEN_PORT`
  Override the `DEFAULT_LISTEN_PORT` in `server.py`


