scrapingfish
=============

Unix/macOS:

.. code-block:: sh

    export TWINE_PASSWORD=pypi-Rh34nfT...

Unix/macOS:

.. code-block:: sh

    [ -d "./dist/" ] && find ./dist/ -mindepth 1 -delete; python -m build

Windows:

.. code-block:: powershell

    py -m build

Unix/macOS:

.. code-block:: sh

    python3 -m twine upload --username __token__ --repository testpypi dist/*

Windows:

.. code-block:: powershell

    py -m twine upload --username __token__ --repository testpypi dist/*
