DevOps
======



Branch Tagging
--------------

Tagging a branch bookmarks a branch commit. 

:Tag a branch:

   .. code:: shell

      git tag -a {tag} -m "{message}"

:List tags:

   .. code:: shell

   git tag --sort=-creatordate
   git show {tag}
   git tag -l "v1.*"

:Delete local tag:

   .. code:: shell

      git tag -d {tag} {tag}

:Delete local tag:

   .. code:: shell

      git push --delete origin {tag} {tag}

:Push tag:

   .. code:: shell

      git push {origin} {tag}
      git push --tags

:Checkout from a specific tag:

   .. code:: shell

      git checkout -b {branch} {tag}

:Tag an existing commit:

   .. code:: shell

      git tag {tag} {commit-checksum}
