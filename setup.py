# setup.py
#
# Copyright 2008 Rafael Menezes Barreto <rmb3@cin.ufpe.br,
# rafaelbarreto87@gmail.com>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License version 2
# as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.


from distutils.core import Extension
from distutils.core import setup


_package_description = ''' Interval Arithmetic package

This package provides types and functions for Maximum Accuracy Interval
Arithmetic.

'''.split("\n")


if __name__ == "__main__":
    setup(
        name="pyrdmia",
        version="0.1.0",
        description=_package_description[0],
        long_description="\n".join(_package_description[2:-1]),
        author="Aline Brum Loreto, Alice Fonseca Finger, Lucas Mendes Tortelli, Dirceu Maraschin Jr.",
        author_email="aline.loreto@gmail.com, aliceffinger@gmail.com,lmtortelli@inf.ufpel.edu.br,dirceu_maraschin@hotmail.com",
        license="GPL",
        platforms=[
            "Windows",
            "Linux"
        ],
        packages=[
            "pyrdmia",
            "pyrdmia.core",
            "pyrdmia.utils",
            "pyrdmia.support"
        ],
        package_dir={
            "pyrdmia" : "src"
        },
        install_requires = [
                          'numpy >= 1.13.0',
                          'enum34',
                          ],

    )
