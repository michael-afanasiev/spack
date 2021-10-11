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
#     spack install advobfuscator-git
#
# You can edit this file again by typing:
#
#     spack edit advobfuscator-git
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class AdvobfuscatorGit(Package):
    """ADVobfuscator demonstates how to use C++11/14 language to generate, at
    compile time, obfuscated code without using any external tool and without
    modifying the compiler."""

    homepage = "https://github.com/andrivet/ADVobfuscator.git"
    url      = "https://github.com/andrivet/ADVobfuscator.git"

    version("master", git="https://github.com/andrivet/ADVobfuscator", branch="master")
    phases  = ["install"]

    def install(self, spec, prefix):
        mkdir(prefix.include)
        mkdir('{0}/ADVobfuscator'.format(prefix.include))
        install('Lib/*', '{0}/ADVobfuscator'.format(prefix.include))
