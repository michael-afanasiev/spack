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
#     spack install xxhash-cmake
#
# You can edit this file again by typing:
#
#     spack edit xxhash-cmake
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class XxhashCmake(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://github.com/Cyan4973/xxHash"
    url      = "https://github.com/Cyan4973/xxHash/archive/v0.6.5.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    root_cmakelists_dir = "cmake_unofficial"
    version('0.8.0', sha256='7054c3ebd169c97b64a92d7b994ab63c70dd53a06974f1f630ab782c28db0f4f')

    variant("shared", default=True, description="Build shared library.")
    variant("xxhsum", default=True, description="Build xxhsum command line binary.")

    def cmake_args(self):
        print(self.spec)
        args = [
            self.define('BUILD_SHARED_LIBS', '+shared' in self.spec),
            self.define('XXHASH_BUILD_XXHSUM', '+xxhsum' in self.spec)
        ]
        return args
