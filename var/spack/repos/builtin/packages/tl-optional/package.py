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
#     spack install tl-optional
#
# You can edit this file again by typing:
#
#     spack edit tl-optional
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class TlOptional(CMakePackage):
    """
    Single header implementation of std::optional with functional-style
    extensions and support for references.
    """

    homepage = "https://tl.tartanllama.xyz/en/latest"
    url      = "https://github.com/TartanLlama/optional/archive/refs/tags/v1.0.0.tar.gz"
    git      = "https://github.com/TartanLlama/optional"

    version('master', branch='master')
    version('1.0.0', sha256='e18941da05bca12a796ebbeacb83993bc0f10e817fa10bb45124a421c2384690')
    version('0.5',   sha256='a801d5ebf505b3152fdf4b792a256e5c2460741a713e816a8d0538c087fe41fb')
    version('0.4',   sha256='411b3a11c334b6744bbc0031d5c8bc1026f6ba7262c5fff5c9ed57879b8d1efb')
    version('0.3',   sha256='12709019dfb0ecee11b3a8cb2f799000aa5f5b1b54bac6b3357467215e359954')
    version('0.2',   sha256='3c7481cd3181ce56ca2dc0cf5576790f255cafca5b266b51b0a98ca6405e0036')
    version('0.1',   sha256='7b95af6ed8a112a05dcc143a5c0e53d78d9ce921213faf3924792d6d58d19820')

    def cmake_args(self):
        args = [
            self.define('OPTIONAL_BUILD_PACKAGE', False),
            self.define('OPTIONAL_BUILD_TESTS', False),
        ]
        return args
