import setuptools
import os
import re

name="uun-guardman"
name_=name.replace('-', '_')

# version from exported binary
pkg_path = os.path.abspath(os.path.dirname(__file__))
with open(f"{pkg_path}/bin/{name}", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

setuptools.setup(
    name=name,
    version=version,
    author="(UUN) - Tomáš Faikl, Marek Beránek",
    author_email="",
    description="Display status of remote uuApp on a colorful LED strip.",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires='>=3.6',
    install_requires=[
        "uun-iot>=0.10.0",
        "uun-iot-libledstrip >= 0.2.4" 
    ],
    extras_require={
        # uun-iot-libledstrip >= 0.2
        "neopixel": [
            "uun-iot-libledstrip[neopixel] >= 0.2.4",
        ],
        "dev": [
            "uun-iot-libledstrip[dev] >= 0.2.4",
        ]
    },
    scripts=[
        "bin/" + name,
        "bin/" + name + "-install",
        "bin/" + name + "-setup"
    ],
    package_data={
        name_: ["data/*"]
    }
)
