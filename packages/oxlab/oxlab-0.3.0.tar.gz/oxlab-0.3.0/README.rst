Introduction
============

The ``oxlab`` package provides tools for Google Colab and Jupyter
notebooks.

Sometimes you want to be able to use or distribute private GitHub repos
in Jupyter notebooks that people may run on their local systems or in
Google Colab. This project provides a simple way to accomplish that
goal.

Imagine you have an example notebook called ``oxlab_demo.ipynb`` and you
want to have it reference a private GitHub repo for your project.

You can take the following steps:

#. Generate an SSH deploy key for your project via something like:

   .. code:: shell

      ssh-keygen -t ecdsa -f /tmp/example_deploy_key_id_ecdsa

#. Upload the public key (which is saved at
   ``/tmp/example_deploy_key_id_ecdsa.pub`` if you used the above
   command) to GitHub as discussed in the `instructions on deploy
   keys <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/managing-deploy-keys#deploy-keys>`__.
#. Create a cell in your notebook like the following where you replace
   ``$YOUR_PRIVATE_KEY`` with your ssh deploy key generated in step 1
   (e.g., the contents of ``/tmp/example_deploy_key_id_ecdsa``), replace
   ``$OWNER`` with the owner of your GitHub repo (e.g., ``emin63``) and
   ``$REPO`` with your repo (e.g., ``oxlab``):

   ::

      # @title Pull in our private github repo
      SSH_DEPLOY_KEY = $YOUR_PRIVATE_KEY
      !pip install oxlab
      from oxlab import github
      oxlab.add_github_repo($OWNER, $REPO, SSH_DEPLOY_KEY)

#. Then the rest of your notebook will be able to do something like
   ``import $REPO`` and reference your private GitHub code.

See the `oxlab_demo.ipynb
notebook <https://github.com/emin63/oxlab/blob/main/oxlab_demo.ipynb>`__
for an example.
