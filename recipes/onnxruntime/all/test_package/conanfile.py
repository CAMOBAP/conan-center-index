from conans import ConanFile, CMake, tools
import os


class OnnxRuntimeTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake", "cmake_find_package"

    def source(self):
        tools.download(
            "https://github.com/microsoft/onnxruntime/raw"
            "/master/csharp/testdata/squeezenet.onnx",
            "squeezenet.onnx"
        )

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

        self.copy("squeezenet.onnx")

    def test(self):
        if not tools.cross_building(self.settings):
            bin_path = os.path.join("bin", "test_package")
            self.run(bin_path, run_environment=True)
