if ! command -v pyenv &> /dev/null
then
    curl https://pyenv.run | bash
    export PATH="$HOME/.pyenv/bin:$PATH"
    eval "$(pyenv init --path)"
    eval "$(pyenv virtualenv-init -)"
fi

if [ "$(pyenv version | grep -c "3.9.9")" -eq 0 ]; then
    pyenv install -s 3.9.9
    pyenv global 3.9.9
fi