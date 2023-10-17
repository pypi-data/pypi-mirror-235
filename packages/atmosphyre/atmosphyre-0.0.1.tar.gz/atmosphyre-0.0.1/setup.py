
import setuptools 
  
with open("README.md", "r") as fh: 
    description = fh.read() 
  
setuptools.setup( 
    name="atmosphyre", 
    version="0.0.1", 
    author="Jay Stephan", 
    author_email="Jay.Stephan@stfc.ac.uk", 
    packages=["atmosphyre"], 
    description="A sample test package", 
    long_description=description, 
    long_description_content_type="text/markdown", 
    license='MIT', 
    python_requires='>=3.8', 
    install_requires=['numpy'] 
) 
