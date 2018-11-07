#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/stable")

class BoostType_IndexConan(base.BoostBaseConan):
    name = "boost_type_index"
    url = "https://github.com/bincrafters/conan-boost_type_index"
    lib_short_names = ["type_index"]
    header_only_libs = ["type_index"]
    b2_requires = [
        "boost_config",
        "boost_container_hash",
        "boost_core",
        "boost_mpl",
        "boost_preprocessor",
        "boost_smart_ptr",
        "boost_static_assert",
        "boost_throw_exception",
        "boost_type_traits"
    ]


