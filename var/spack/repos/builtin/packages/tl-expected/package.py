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
#     spack install tl-expected
#
# You can edit this file again by typing:
#
#     spack edit tl-expected
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class TlExpected(CMakePackage):
    """
    Single header implementation of std::expected with functional-style
    extensions.
    """

    homepage = "https://tl.tartanllama.xyz/en/latest"
    url      = "https://github.com/TartanLlama/expected/archive/refs/tags/v1.0.0.tar.gz"
    git      = "https://github.com/TartanLlama/expected"

    version('master', branch='master')
    version('1.0.0', sha256='8f5124085a124113e75e3890b4e923e3a4de5b26a973b891b3deb40e19c03cee')
    version('0.3',   sha256='18103ac213b3a7e5740bee754c9a5f96a4cee0ead1f2f7670775efc467b56ac3')
    version('0.2',   sha256='ca6be2df1eee0c7832612f275e7ccda415e13ada0464bcafc446fd505ca80660')

    def cmake_args(self):
        args = [
            self.define('EXPECTED_BUILD_PACKAGE', False),
            self.define('EXPECTED_BUILD_TESTS', False),
        ]
        return args
