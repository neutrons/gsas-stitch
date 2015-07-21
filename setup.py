try:
  # Use easy setup to ensure dependencies
  import ez_setup
  ez_setup.use_setuptools()
except ImportError:
  pass

from distutils.core import setup


package_name = "mergegsas"
version      = "0.1.1" # TODO currently hand-synchronized
author       = "Peter F. Peterson"
license      = "The MIT License"
email        = "petersonpf@ornl.gov"
url          = "https://github.com/neutrons/gsas-stitch"
description  = "Script to combine two or more powgen gsas files for use in pdfgetn"

scripts = ["scripts/mergegsas"]
py_modules = []
package_dir = []
packages = []
package_data = {}
data_files = []
extensions_modules=[] # written in C
requires=[]
options={}

if __name__ == "__main__":
    setup(name=package_name,
          version=version,
          description=description,
          author=author,
          author_email=email,
          url=url,
          scripts=scripts,
          py_modules=py_modules,
          ext_modules=extensions_modules,
          packages=packages,
          package_dir=package_dir,
          package_data=package_data,
          data_files=data_files,
          requires=requires,
          **options)
