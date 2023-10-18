

Shell completion
================

pglift comes with completion scripts for your favorite shell. You can activate
completion for ``bash``, ``zsh`` or ``fish``.

Bash
----

.. code-block:: shell

  $ source <(pglift --completion=bash)

  # To load completions for each session, execute once:
  $ pglift --completion=bash | sudo tee /etc/bash_completion.d/pglift

Zsh
---

.. code-block:: shell

  $ pglift --completion=zsh > "${fpath[1]}/pglift"

Fish
----

.. code-block:: shell

  $ pglift --completion=fish | source

  # To load completions for each session, execute once:
  $ pglift --completion=fish > ~/.config/fish/completions/pglift.fish
