# Pasta
Pastebin but with Github Gist from your terminal. Paste your logs directly to Github Gist and share the link with others.

### Dependency
  * python3

alias it
```
 alias pasta=/path-to-pasta/pasta.sh
```

pipe into Pasta
```
  echo "Hello World " | pasta

  >> Your pasta is available at: https://gist.github.com/8a3d739ccdc32a11b7434fcbeeaf6e25

```
options
```

Pastebin with Github Gists.

optional arguments:
  -h, --help            show this help message and exit
  -r, --read            Read from specific gist
  -u URL, --url URL     Specific to read from
  -n NAME, --name NAME  Name for gist
  -s, --secret          Make the gist private
  -d DESC, --desc DESC  Description of gist
```

### Why?

```
Why not?
```

Contributions
  * You should include a link to a Pasta recipe with your Pull Request :)
    Format: ```" commit message (recipe link) "```
  * If you see something missing just submit a PR
