####################################################
Calyx: Bundle-Adjustment via Factor Graphs in Python
####################################################

====================================================
Quick Start
====================================================
Calyx aims to do several things:

# It aims to provide a library and interfaces which 
  make it easy to express optimization problems 
  (specifically bundle-adjustment in this case)

# It includes implementations of numerical
  optimizers (such as Levenberg-Marquardt, nonlinear
  conjugate gradients, etc.) as well as interoperability 
  with Scipy's optimizers.

====================================================
Building and Using Calyx
====================================================
To develop Calyx, you will need tox installed. 
Everything else should happen automagically via the
tox virtual environments. 


# Run the pretty-printers and linters:

  .. code-block:: bash
     
     tox -e 'py35-{pretty-print,lint}'

# Run the quick tests:

  .. code-block:: bash

     tox -e 'py35-quicktest'

# Run the full test suite

  .. code-block:: bash

     tox -e py35-fulltest

     
