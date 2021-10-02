# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
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
#     spack install tinyxml2
#
# You can edit this file again by typing:
#
#     spack edit tinyxml2
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Tinyxml2(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/leethomason/tinyxml2"
    url      = "https://github.com/leethomason/tinyxml2/archive/refs/tags/9.0.0.zip"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('9.0.0', sha256='6904137f290b0836792fd182c0d463cb66da085856b0e5803089b40bf379fdcf')
    version('8.1.0', sha256='a64b64720cadaa053cf0bc2d8be99de2c3a0e7a7ddeaceafdef8e6b694f9e495')
    version('8.0.0', sha256='ad17d277b23b32edfded29890201adeb946b33be80094c3f804688038be3a5bd')
    version('7.1.0', sha256='accdcfc004959309e6344fedeee8fe08a9f44785bde263f85a6143b286737eb0')
    version('7.0.1', sha256='323b1f8bd3c849f853f4f7b804c620a7309d588b1880e90c52da4b79395d664c')
    version('7.0.0', sha256='92ca4d56dd09ca0914080b5467891d9017b0a61b8b0ad6d9a49e43435ccc4a6f')
    version('6.2.0', sha256='11e7cb172744fa6e8ab3cf9e16aab180115ce780e7df345c3afce1dea0b244d4')
    version('6.0.0', sha256='407f8bc7c06aec4786999869aef509d85ba8d6cb62f1c8e35447fd2adc1b0b18')
    version('5.0.1', sha256='f74379e9c3942f539f2236cf0e57edd11f8da684dc3000ded77304c18b1dad1d')
    version('5.0.0', sha256='c61ee259cd712dac3ccf71a3154e8d77277256a9bc53114d625f3db8f8bb5968')

    def cmake_args(self):
        args = [self.define('BUILD_SHARED_LIBS', '+shared' in self.spec)]
        return args
