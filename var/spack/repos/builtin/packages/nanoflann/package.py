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

    version('1.4.2', sha256='97fce650eb644a359a767af526cab9ba31842e53790a7279887e1ae2fffe7319')
    version('1.4.1', sha256='4e66edac66cef76460ae5b22c92806b999b16e05bb5b3b3ce2ada320d0bfa7a9')
    version('1.4.0', sha256='9ce09aa7c049e28ca4e2fbeffafc8e09aca98a52624578798c8ebb723ad974bb')
    version('1.3.2', sha256='e100b5fc8d72e9426a80312d852a62c05ddefd23f17cbb22ccd8b458b11d0bea')
    version('1.3.1', sha256='b1b1ac9bf6c3bac284014b326480388ad469bdeca78bd27a34ba2ae1da1a03ff')
    version('1.3.0', sha256='e0efc289422bc4cbaf8811d2f2c3c080ad09ac6d68a2b70134f3595d5da010cb')
    version('1.2.3', sha256='5ef4dfb23872379fe9eb306aabd19c9df4cae852b72a923af01aea5e8d7a59c3')
    version('1.2.2', sha256='368ae77eaaddc6115c2cc9e144f80f6c25e77c6a13826a5950075b00d7eb1ca3')
    version('1.2.1', sha256='8345e46bced5836cbd7584473e656db737bd0f0e22f419b7a7ba86d65cf144f9')
    version('1.2.0', sha256='43c56cc16f578e67304ae819e7e3e5bde7a89bdc2e01236dcd42696755079eca')

    def patch(self):
        filter_file('-mtune=native', '', 'CMakeLists.txt')

    def cmake_args(self):
        args = ['-DBUILD_SHARED_LIBS=ON']
        return args
