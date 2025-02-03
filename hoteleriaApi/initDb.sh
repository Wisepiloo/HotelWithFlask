if ! [ -x "$(command -v mysql)" ]; then
  echo "Debe instalar mysql"
  exit 1
fi

read -p "Ingrese el usuario de mysql: " user
read -sp "Ingrese la contraseña de mysql: " pass
echo ""

mysql --user=$user --password=$pass <hoteles.sql
