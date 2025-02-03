if ! [ -x "$(command -v python3)" ]; then
  echo "Debe instalar python3"
  exit 1
fi

python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
pip install -r requirements.txt
