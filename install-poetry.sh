if ! command -v poetry &> /dev/null
then
    curl -sSL https://install.python-poetry.org | python3 -
    export PATH="$HOME/.local/bin:$PATH"
    export PATH="$HOME/.poetry/bin:$PATH"
fi