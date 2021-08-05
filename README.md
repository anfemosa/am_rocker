# am_rocker
Extensions to development

===============
AM Rocker
===============

This adds extensions for `tfoote/rocker <https://github.com/tfoote/rocker>`_.

Extensions
^^^^^^^^^^

Devenv
:::::

This mounts paths as docker volumes.
The path used inside the container is the same as the path outside the container.
Multiple paths may be passed.
The last path must be terminated with two slashes -- before the image name.

::

    rocker --oyr-mount ~/.vimrc ~/.bashrc -- ubuntu:18.04
