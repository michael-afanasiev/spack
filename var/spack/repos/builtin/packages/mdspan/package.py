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
#     spack install mdspan
#
# You can edit this file again by typing:
#
#     spack edit mdspan
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Mdspan(CMakePackage):
    """Kokkos reference implementation of the C++23 mdspan proposal."""

    homepage = "https://github.com/kokkos/mdspan"
    url      = "https://github.com/kokkos/mdspan/archive/refs/tags/mdspan-0.1.0.tar.gz"
    git      = "https://github.com/kokkos/mdspan"

    version("stable", branch="stable")
    version('0.1.0', sha256='24c1e4be4870436c6c5e80d38870721b0b6252185b8288d00d8f3491dfba754b')

