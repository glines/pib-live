{ stdenv, makeWrapper, python, pythonPackages }:

stdenv.mkDerivation rec {
  name = "piab_scrape_remotes";

  src = ./scrape_remotes.py;
  unpackCmd = ''
    mkdir src
    cat "$curSrc" > src/scrape_remotes.py
  '';

  buildInputs = [ makeWrapper python ];
  propagatedBuildInputs = with pythonPackages; [ lxml requests ];

  installPhase = ''
    mkdir -p "$out"/bin
    cp -R "$src" "$out"/bin/scrape_remotes.py
    chmod +x "$out"/bin/scrape_remotes.py
    wrapProgram "$out"/bin/scrape_remotes.py \
      --prefix PYTHONPATH : "$PYTHONPATH"
  '';
}
