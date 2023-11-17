Dependencies
============

About
-----

The section lists the DMA CLI dependencies and shows how to manage these with ``poetry``.

Requirements
------------

* :doc:`installation`

Project Dependencies
--------------------

Below is the list of the project's python and system dependencies.

:Development Dependencies:

   * ``PACKAGE`` The project requires the python package ``PACKAGE`` to ....


:Python Package Management Dependencies:

   * ``poetry`` The project requires the `poetry <https://python-poetry.org/docs/>`_ CLI app to manage the python package dependencies, building, publishing and tracking.

:Task-Runner Dependencies:

   * ``invoke`` The project requires the python package ``invoke`` to run the invoke task runner.

:Documentation Dependencies:

   * ``sphinx`` The project requires the python package ``sphinx`` to build the static webpages from the project's ``rst`` docs files and the project's python modules ``docstrings``.
   * ``furo`` The project requires the python package ``furo`` to style the static webpages of the project's docs.

:Python Security Dependencies:

   * ``bandit`` The project requires the python package ``bandit`` to audit the security of the python dependencies.

:Linting And Formatting Dependencies:

   * ``black`` The project requires the python package ``black`` to format the source code according to ``pep8``.
   * ``isort`` The project requires the python package ``isort`` to structure the module imports.

:Solution Quality Dependencies:

   * ``radon`` The project requires the python package ``radon`` to analyse metrics like complexity, etc.

Managing The Project Dependencies
---------------------------------

The DMA CLI project uses `poetry <https://python-poetry.org/docs/>`_ as a dependencies manager. ``poetry.lock`` lists all our dependencies and our dependencies' dependencies, meaning it's possible to version these.

.. figure:: ../../../static/img/poetry.png
   :width: 80%
   :align: center

   Poetry Flow

list
~~~~

:List current poetry virtual environments:

   Doesn't require the environment to be activated

   .. code:: shell

      $ poetry env list
      dmacli-zj9n41Gh-py3.8 (Activated)

      $ poetry env list --full-path
      /{PATH}/.cache/pypoetry/virtualenvs/dmacli-zj9n41Gh-py3.8 (Activated)

:List current poetry virtual environment properties:

   Doesn't require the environment to be activated

   .. code:: shell

      $ poetry env info

:List dependencies:

   .. code:: shell

      poetry show --tree

create
~~~~~~

:Create new python virtual environment:

   Poetry handles virtual environments in child processes. Why? Child processes inherit their parent processes environments but do not share them, meaning any modification to the environment will not be persisted/affect the parent process' environment (`read more <https://python-poetry.org/docs/basic-usage/#activating-the-virtual-environment>`_)

   The virtual environments can either be persisted `in your project <https://python-poetry.org/docs/configuration/#virtualenvsin-project>`_ or outside of your project, `anywhere in your system <https://python-poetry.org/docs/configuration/#cache-dir>`_

   Create a nested shell on the current project dir:

   .. code:: shell

      $ poetry shell
      Creating virtualenv dmacli-zj9n41Gh-py3.8 in /home/dipm/.cache/pypoetry/virtualenvs
      Spawning shell within /home/dipm/.cache/pypoetry/virtualenvs/dmacli-zj9n41Gh-py3.8
      . /home/dipm/.cache/pypoetry/virtualenvs/dmacli-zj9n41Gh-py3.8/bin/activate
      $ (dmacli-py3.8) python --version
      Python 3.8.10
      $ (dmacli-py3.8) exit
      exit

activate
~~~~~~~~

:Activate the virtual environment:

   Activate the virtual environment in your poetry shell process:

   .. code:: shell

      $ source $PATH/bin/activate
      $ poetry env list
      dmacli-zj9n41Gh-py3.8 (Activated)
      $ poetry env info --path
      /home/dipm/.cache/pypoetry/virtualenvs/dmacli-zj9n41Gh-py3.8
      $ source $(poetry env info --path)/bin/activate
      $ (dmacli-py3.8)

exit
~~~~

:Exit virtual environment:

   Leave the shell:

   .. code:: shell

      $ (dmacli-py3.8) exit
      exit

   Don't leave the shell, but exit the environment:

   .. code:: shell

      $ (dmacli-py3.8) deactivate
      $ exit
      exit

info
~~~~

:Collect current environment info:

   .. code:: shell

      (dmacli-py3.8) poetry env info
      Virtualenv
      Python:         3.8.10
      Implementation: CPython
      Path:           /{PATH}/.cache/pypoetry/virtualenvs/dmacli-zj9n41Gh-py3.8
      Executable:     /{PATH}/.cache/pypoetry/virtualenvs/dmacli-zj9n41Gh-py3.8/ bin/python
      Valid:          True

      System
      Platform:   linux
      OS:         posix
      Python:     3.8.10
      Path:       /usr
      Executable: /usr/bin/python3.8

version
~~~~~~~

:Check for latest dependencies versions:

   .. code:: shell

      poetry show --latest

install
~~~~~~~

:Install the project's python dependencies:

   Poetry installs dependencies asynchronously (unlike pip) meaning it runs faster.

   .. code:: shell

      poetry install

   .. warning::

      Extra dependencies are declared as:

      .. code:: text

         [tool.poetry.extras]
         mysql = ["mysqlclient"]
         pgsql = ["psycopg2"]

      And are installed as:

      .. code:: shell

         poetry install -E mysql -E pgsql

add
~~~

:Add production dependency:

   Add to ``[tool.poetry.dependencies]``

   .. code:: shell

      poetry add $PACKAGE

:Add development dependency:

   Add to ``[tool.poetry.group.dev.dependencies]``

   .. code:: shell

      poetry add -group dev $PACKAGE

run
~~~

:Run python app in poetry environment:

   It is possible to run python apps within virtual environments without having to have them activated (like spinning a docker image).

   .. code:: shell

      poetry run python app.py
      poetry run pytest
      poetry run black

remove
~~~~~~

:Remove poetry environment:

   .. code:: shell

      poetry env remove /full/path/to/python python3.7 3.7 test-O3eWbxRl-py3.7
      poetry env remove --all

:Remove poetry dependencies:

   .. code:: shell

      $ poetry env list
      dmacli-zj9n41Gh-py3.8 (Activated)

      poetry remove dmacli-zj9n41Gh-py3.8

.. note::

   It is possible to manage dependencies of an environment simply by being in the environment's project directory, that by virtue of ``pyproject.toml`` which ``poetry`` looks out for whenever called.
