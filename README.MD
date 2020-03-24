# Setup
Once installation is complete and server is listening, the app can be found at `localhost:{port}`.

## Automatic Installation & Startup (recommended)

### Develpment
 `$ ./dev`
### Production
`$ ./prod`

## Manual Installation
`$ python -m pip install -r requirements.txt`

## Manual Startup
`$ python manage.py runserver {port}`

## Adding Dependencies
Additional dependencies can be added with 

`$ pip freeze > requirements.txt`

This should ideally be done in a fresh virtual environment to avoid including extraneous dependencies. As of Python3.3, [venv](https://docs.python.org/3/tutorial/venv.html) has been included in the standard library, and can be used for managing virtual environments. However, due to it's relative simplicity, [Anaconda](https://www.anaconda.com/distribution/) will be used to explain the process, below:

Create a new environment using 

`$ conda create -n my_new_environment`

Optionally, you can specify the Python version by including `python={version}`.

Your new environment can be accessed via 

`$ conda activate my_new_environment`

After activating the new environment, install all relevant dependencies and run a new pip freeze. 

The new environment can be deactivated with 

`$ conda deactivate`

Dependencies can also be added manually by editing `requirements.txt`, but this is not recommended.
