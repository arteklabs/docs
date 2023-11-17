Docs
====

About
-----

The section shows the project's documentation component.

Layout & Architecture
---------------------

The docs component has the following layout:

.. code-block::

   ├── docs
   │   └── sphinx
   │       ├── _static           Styling and images
   │       ├── links             Constants for URLs
   │       ├── static/img/src    Diagrams
   │       ├── src               Documentation
   │       ├── conf.py           Sphinx server config
   │       ├── index.rst         Converts to index.html
   │       └── Makefile          Sphinx task runner
   ├── src                       (imported by sphinx)
   ├── tests                     (imported by sphinx)
   ├── README.md                 (imported by sphinx)
   ├── CHANGELOG.md              (imported by sphinx)
   └── LICENSE.md                (imported by sphinx)

Getting Started
---------------

If the docs infrastructure hasn't been deployed yet, deploy it with:

.. code:: shell

   $ inv docs --step deploy

Having made your changes to the docs, test the build with:

.. code:: shell

   $ inv docs --step build

Validate your changes:

.. code:: shell

   $ inv docs --step preview

Having validated the pages, publish the build to cloudfront:

.. code:: shell

   $ inv docs --step publish

Shutdown the preview container:

.. code:: shell

   $ inv docs --step stop-preview

Literature
----------

* `AWS Cloud Front Docs <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/GettingStarted.SimpleDistribution.html#GettingStartedSignup>`_
* `AWS Construct CloudFront To S3 <https://github.com/awslabs/aws-solutions-constructs/tree/main/source/patterns/%40aws-solutions-constructs/aws-cloudfront-s3>`_
