# Minnesota Tech Network (MTN) QA Training Project Readme
This project uses the Project IDX IDE, which is located [here](https://idx.dev/).

The technologies involved with this project are [Python](https://www.python.org/), [SQLite w/ Python](https://www.geeksforgeeks.org/python-sqlite/), and [Selenium](https://www.selenium.dev/).

The skills developed in this project are:
1. Using Git & GitHub
2. Writing Python Code
3. Writing SQL (and working with a relational database)
4. Writing Selenium Code
5. Application of core QA Concepts like Test Cases
6. Extract, Transform, Load (ETL) Concepts

# Quickstart
1. This project has been configured to automatically start the Python Virtual Environment (venv) if you load it in Project IDX. If it doesn't start (or you are running this elsewhere) use `source .venv/bin/activate` to activate it.
2. Read `learning-plan/README.md` to learn things.
3. Call `python main.py` to execute the code. It is currently configured to demonstrate Extract, Transform, and Load (ETL) between two databases.
4. Use `database.py` as a starting place to learn how to use Python + SQL. Creates `database.db` files that act as databases.
5. Use `test.py` to write tests for the databases (or Python code). Call the tests using `python test.py`.
6. The `selenium-ide-qa-training.side` file is a small set of tests you can load into the Selenium IDE to be able to learn some of the IDE's functionality. Keep in mind that some tests will be far easier to create in the IDE, and some will be far easier to write via Python code (see `learn_selenium.py`).

# Requirements.txt
Defines the Python packages used in this repository. If you need to add a new package, you can do a `pip install` of the package and then use `pip freeze > requirements.txt` to save the dependency. The repo also uses `venv` to create a virtual environment using `requirements.txt`.

While Project IDX does create a virtualized environment for projects, I found that this approach helped generalize this repository so that it could be run in more environments.