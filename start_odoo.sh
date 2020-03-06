# !/urs/bin/env bash



. /home/$(whoami)/odoo/odoo13/odoo13_env/bin/activate --python=python3 venv


if [[ $1 != "" ]]; then
	/home/$(whoami)/odoo/odoo13/odoo/odoo-bin --addons-path='/home/lliege/odoo/odoo13/odoo/addons,/home/lliege/odoo/odoo13/odoo/odoo/addons, /home/lliege/Projects/odoo_13_modules, /home/lliege/Projects/lliege_login_redirect,/home/lliege/Projects' -r'odoo13' -w'odoo' -d $1
else
	/home/$(whoami)/odoo/odoo13/odoo/odoo-bin --addons-path='/home/lliege/odoo/odoo13/odoo/addons,/home/lliege/odoo/odoo13/odoo/odoo/addons, /home/lliege/Projects/odoo_13_modules, /home/lliege/Projects/lliege_login_redirect,/home/lliege/Projects' -r'odoo13' -w'odoo'
fi

