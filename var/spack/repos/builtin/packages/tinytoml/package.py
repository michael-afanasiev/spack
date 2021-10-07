# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install tinytoml
#
# You can edit this file again by typing:
#
#     spack edit tinytoml
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Tinytoml(Package):
    """A header only C++11 library for parsing TOML."""

    homepage = "https://github.com/mayah/tinytoml"
    url      = "https://github.com/mayah/tinytoml/archive/refs/tags/v0.4.tar.gz"

    version('0.4', sha256='bd5e330dcddceba26a2794f543071e0ef2a62ea52afb322d23674c36060e0afa')

    phases  = ["install"]

    def install(self, spec, prefix):
        mkdir(prefix.include)
        install('include/toml/toml.h', '{0}/toml.h'.format(prefix.include))
