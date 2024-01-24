Développement local
===================

macOS / Linux
#############

.. toctree::

  cloner
  venv
  envvars
  local_exec_no_docker
  local_exec_with_docker
  lint
  test
  bdd
  admin

Windows
#######

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1`
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`