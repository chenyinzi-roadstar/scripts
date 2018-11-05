from conans import ConanFile, CMake


class GeneralConan(ConanFile):
    # TODO fill the name
    name = ""
    version = "1.0.0"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Visualizer here>"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    generators = "cmake","cmake_paths","cmake_find_package"
    # exports_sources = "*"

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=".")
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        # Build include folder
        self.copy("*", dst="include", src="include")

        # Build lib folder
        self.copy("*", dst="lib", src="lib")
    def package_info(self):
        self.cpp_info.libs = []

    def imports(self):
        # self.copy("*", dst="/opt/xxx", src=".", excludes=["*.tgz"])
        pass

