# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Nanoflann(CMakePackage):
    """a C++ header-only library for Nearest Neighbor (NN) search wih KD-trees.
    """

    homepage = "https://github.com/jlblancoc/nanoflann"
    url      = "https://github.com/jlblancoc/nanoflann/archive/v1.2.3.tar.gz"

    version('1.3.2', sha256='e100b5fc8d72e9426a80312d852a62c05ddefd23f17cbb22ccd8b458b11d0bea')
    version('1.3.0', sha256='e0efc289422bc4cbaf8811d2f2c3c080ad09ac6d68a2b70134f3595d5da010cb')
    version('1.2.3', sha256='5ef4dfb23872379fe9eb306aabd19c9df4cae852b72a923af01aea5e8d7a59c3')

    def patch(self):
        filter_file('-mtune=native', '', 'CMakeLists.txt')

    def cmake_args(self):
        args = ['-DBUILD_SHARED_LIBS=ON']
        return args
