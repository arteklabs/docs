Agile
=====

Remote Branching Policies
-------------------------

Branching Flow
--------------

Branch Semantics
----------------

Format: 

.. code-block:: text

    <type>/#<issueNumber>-<alias>

where ``<type>`` takes ONE and ONLY ONE of the following values:

- ``feat`` or `feature`: (new feature for the user, not a new feature for build script)
- ``fix``: (bug fix for the user, not a fix to a build script)
- ``docs``: (changes to the documentation)
- ``style``: (formatting, missing semi colons, etc; no production code change)
- ``refactor``: (refactoring production code, eg. renaming a variable)
- ``test``: (adding missing tests, refactoring tests; no production code change)
- ``chore``: (updating grunt tasks etc; no production code change)


Commit Semantics
----------------

Format: 

.. code-block:: text

    <type>[(<scope>)]: <subject>

where ``<type>`` takes ONE and ONLY ONE of the following values:

- ``feat`` or `feature`: (new feature for the user, not a new feature for build script)
- ``fix``: (bug fix for the user, not a fix to a build script)
- ``docs``: (changes to the documentation)
- ``style``: (formatting, missing semi colons, etc; no production code change)
- ``refactor``: (refactoring production code, eg. renaming a variable)
- ``test``: (adding missing tests, refactoring tests; no production code change)
- ``chore``: (updating grunt tasks etc; no production code change)

Tagging, Versioning and Changelog
---------------------------------

Format:

.. code-block:: text

    <major>.<minor>.<patch>[-alpha|beta] 


* ``major``: breaking changes with previous versions
* ``minor``: adding feature with backward compatibility
* ``patch``: fix with backward compatibility
* [-``alpha``|``beta``]: alpha or beta release

The release branch is tagged accordingly. The changelog is a scrape of the squashed commits.

License
-------

The license of the project.
