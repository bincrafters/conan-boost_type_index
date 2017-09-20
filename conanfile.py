from conans import ConanFile


class BoostType_IndexConan(ConanFile):
    name = "Boost.Type_Index"
    version = "1.65.1"
    url = "https://github.com/bincrafters/conan-boost-type_index"
    description = "Please visit http://www.boost.org/doc/libs/1_65_1/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    requires =  "Boost.Level5Group/1.65.1@bincrafters/testing"
   
    def package_id(self):
        self.info.header_only()
        
    #This library is part of one or more cyclic dependency groups within Boost.
    
    #All members of cyclic dependency groups must be built under single package per group for Conan.
    
    #The combination is performed in the package(s) listed in the requires field.
    
    #This package enables simple consumption of this library while abstracting away the cyclic dependency issues. 