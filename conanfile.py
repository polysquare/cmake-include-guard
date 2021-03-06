from conans import ConanFile
from conans.tools import download, unzip
import os

VERSION = "0.1.4"


class CMakeIncludeGuardConan(ConanFile):
    name = "cmake-include-guard"
    version = os.environ.get("CONAN_VERSION_OVERRIDE", VERSION)
    generators = "cmake"
    url = "http://github.com/polysquare/cmake-include-guard"
    licence = "MIT"
    options = {
        "dev": [True, False]
    }
    default_options = "dev=False"

    def requirements(self):
        if self.options.dev:
            self.requires("cmake-module-common/master@smspillaz/cmake-module-common")

    def source(self):
        zip_name = "cmake-include-guard.zip"
        download("https://github.com/polysquare/"
                 "cmake-include-guard/archive/{version}.zip"
                 "".format(version="v" + VERSION),
                 zip_name)
        unzip(zip_name)
        os.unlink(zip_name)

    def package(self):
        self.copy(pattern="*.cmake",
                  dst="cmake/cmake-include-guard",
                  src="cmake-include-guard-" + VERSION,
                  keep_path=True)
