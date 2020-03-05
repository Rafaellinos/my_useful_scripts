# !/urs/bin/env bash

. /home/rafael/odoo/odoo13/odoo13_env/bin/activate --python=python3 venv

/home/rafael/odoo/odoo13/odoo/odoo-bin --addons-path='~/odoo/odoo13/odoo/addons, ~/odoo/odoo13/odoo/custom-addons, ~/Documents/lliege_work/lliege_documentos' -r'odoo13' -w'odoo'
