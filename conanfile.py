from os.path import join,exists
from os import listdir,rmdir,chdir
from conans import ConanFile
import shutil

class HRIDriverConan(ConanFile):
    name = "hridriver"
    version = "1.1"
    license = "MIT"

    # No exports necessary

    def source(self):
        src_folder = '%s/hri-safe-remote-control-system' % self.conanfile_directory
        if not exists(src_folder):
            self.run("git clone https://github.com/humanisticrobotics/hri-safe-remote-control-system.git")

    def build(self):
        makefile_folder = join(self.conanfile_directory,'hri-safe-remote-control-system/drivers/C')
        chdir(makefile_folder)
        self.run('make')
        chdir(self.conanfile_directory)

    def package(self):
        makefile_folder = 'hri-safe-remote-control-system/drivers/C'
        print (join(makefile_folder,'include'))
        self.copy("*.h", dst="include", src=join(makefile_folder,'include'))
        self.copy("*.so", dst="lib", src=join(makefile_folder,'lib'))

    def package_info(self):
        self.cpp_info.libs = ["hridriver"]
