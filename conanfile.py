from conans import ConanFile, tools, os

class BoostType_IndexConan(ConanFile):
    name = "Boost.Type_Index"
    version = "1.64.0"
    url = "https://github.com/bincrafters/conan-boost-type_index"
    source_url = "https://github.com/boostorg/type_index"
    description = "Please visit http://www.boost.org/doc/libs/1_64_0/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    requires =  "Boost.Level5Group/1.64.0@bincrafters/testing"
   
    def package_id(self):
        self.info.header_only()
        
    #This library is part of one or more cyclic dependency groups within Boost.
    
    #All members of cyclic dependency groups must be built under single package per group for Conan.
    
    #The combination is performed in the package(s) listed in the requires field.
    
    #This package enables simple consumption of this library while abstracting away the cyclic dependency issues. 