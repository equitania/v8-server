#!/bin/bash
##############################################################################
#
#    Shell Script for Odoo, Open Source Management Solution
#    Copyright (C) 2014-now Equitania Software GmbH(<http://www.equitania.de>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

mybasepath="/home/odoo/git"
echo "Base-path: "$mybasepath

# github repositories
myreppath=$mybasepath"/myodoo-server"
if [ -d $myreppath ]; then
  cd $myreppath
  git checkout develop
  git pull git@bitbucket.org:equitania-ondemand/myodoo-server.git
  echo "Pull lastest branch "$myreppath
else
  cd $mybasepath
  git clone -b develop git@bitbucket.org:equitania-ondemand/myodoo-server.git
  echo "Clone lastest branch "$myreppath
fi

myreppath=$mybasepath"/odoo-addons"
if [ -d $myreppath ]; then
  cd $myreppath
  git checkout develop
  git pull git@github.com:equitania/odoo-addons.git
  echo "Pull lastest branch "$myreppath
else
  cd $mybasepath
  git clone -b develop git@github.com:equitania/odoo-addons.git
  echo "Clone lastest branch "$myreppath
fi

# bitbucket repositories

myreppath=$mybasepath"/odoo-datev"
if [ -d $myreppath ]; then
  cd $myreppath
  git checkout develop
  git pull git@bitbucket.org:equitania-ondemand/odoo-datev.git
  echo "Pull lastest branch "$myreppath
else
  cd $mybasepath
  git clone -b develop git@bitbucket.org:equitania-ondemand/odoo-datev.git
  echo "Clone lastest branch "$myreppath
fi

myreppath=$mybasepath"/odoo-hr"
if [ -d $myreppath ]; then
  cd $myreppath
  git checkout develop
  git pull git@bitbucket.org:equitania-ondemand/odoo-hr.git
  echo "Pull lastest branch "$myreppath
else
  cd $mybasepath
  git clone -b develop git@bitbucket.org:equitania-ondemand/odoo-hr.git
  echo "Clone lastest branch "$myreppath
fi

myreppath=$mybasepath"/odoo-mrp"
if [ -d $myreppath ]; then
  cd $myreppath
  git checkout develop
  git pull git@bitbucket.org:equitania-ondemand/odoo-mrp.git
  echo "Pull lastest branch "$myreppath
else
  cd $mybasepath
  git clone -b develop git@bitbucket.org:equitania-ondemand/odoo-mrp.git
  echo "Clone lastest branch "$myreppath
fi

myreppath=$mybasepath"/odoo-scripts"
if [ -d $myreppath ]; then
  cd $myreppath
  git checkout develop
  git pull git@bitbucket.org:equitania-ondemand/odoo-scripts.git
  echo "Pull lastest branch "$myreppath
else
  cd $mybasepath
  git clone -b develop git@bitbucket.org:equitania-ondemand/odoo-scripts.git
  echo "Clone lastest branch "$myreppath
fi

myreppath=$mybasepath"/odoo-stock"
if [ -d $myreppath ]; then
  cd $myreppath
  git checkout develop
  git pull git@bitbucket.org:equitania-ondemand/odoo-stock.git
  echo "Pull lastest branch "$myreppath
else
  cd $mybasepath
  git clone -b develop git@bitbucket.org:equitania-ondemand/odoo-stock.git
  echo "Clone lastest branch "$myreppath
fi

myreppath=$mybasepath"/odoo-system"
if [ -d $myreppath ]; then
  cd $myreppath
  git checkout develop
  git pull git@bitbucket.org:equitania-ondemand/odoo-system.git
  echo "Pull lastest branch "$myreppath
else
  cd $mybasepath
  git clone -b develop git@bitbucket.org:equitania-ondemand/odoo-system.git
  echo "Clone lastest branch "$myreppath
fi

myreppath=$mybasepath"/odoo-tools"
if [ -d $myreppath ]; then
  cd $myreppath
  git checkout develop
  git pull git@bitbucket.org:equitania-ondemand/odoo-tools.git
  echo "Pull lastest branch "$myreppath
else
  cd $mybasepath
  git clone -b develop git@bitbucket.org:equitania-ondemand/odoo-tools.git
  echo "Clone lastest branch "$myreppath
fi

myreppath=$mybasepath"/odoo-trading"
if [ -d $myreppath ]; then
  cd $myreppath
  git checkout develop
  git pull git@bitbucket.org:equitania-ondemand/odoo-trading.git
  echo "Pull lastest branch "$myreppath
else
  cd $mybasepath
  git clone -b develop git@bitbucket.org:equitania-ondemand/odoo-trading.git
  echo "Clone lastest branch "$myreppath
fi

myreppath=$mybasepath"/odoo-tutorials"
if [ -d $myreppath ]; then
  cd $myreppath
  git checkout develop
  git pull git@bitbucket.org:equitania-ondemand/odoo-tutorials.git
  echo "Pull lastest branch "$myreppath
else
  cd $mybasepath
  git clone -b develop git@bitbucket.org:equitania-ondemand/odoo-tutorials.git
  echo "Clone lastest branch "$myreppath
fi

myreppath=$mybasepath"/odoo-website"
if [ -d $myreppath ]; then
  cd $myreppath
  git checkout develop
  git pull git@bitbucket.org:equitania-ondemand/odoo-website.git
  echo "Pull lastest branch "$myreppath
else
  cd $mybasepath
  git clone -b develop git@bitbucket.org:equitania-ondemand/odoo-website.git
  echo "Clone lastest branch "$myreppath
fi

# customer repositories

myreppath=$mybasepath"/odoo-easydisplay"
if [ -d $myreppath ]; then
  cd $myreppath
  git checkout develop
  git pull git@bitbucket.org:equitania-ondemand/odoo-easydisplay.git
  echo "Pull lastest branch "$myreppath
else
  cd $mybasepath
  git clone -b develop git@bitbucket.org:equitania-ondemand/odoo-easydisplay.git
  echo "Clone lastest branch "$myreppath
fi

myreppath=$mybasepath"/odoo-futuretv"
if [ -d $myreppath ]; then
  cd $myreppath
  git checkout develop
  git pull git@bitbucket.org:equitania-ondemand/odoo-futuretv.git
  echo "Pull lastest branch "$myreppath
else
  cd $mybasepath
  git clone -b develop git@bitbucket.org:equitania-ondemand/odoo-futuretv.git
  echo "Clone lastest branch "$myreppath
fi

myreppath=$mybasepath"/odoo-ibf"
if [ -d $myreppath ]; then
  cd $myreppath
  git checkout develop
  git pull git@bitbucket.org:equitania-ondemand/odoo-ibf.git
  echo "Pull lastest branch "$myreppath
else
  cd $mybasepath
  git clone -b develop git@bitbucket.org:equitania-ondemand/odoo-ibf.git
  echo "Clone lastest branch "$myreppath
fi

myreppath=$mybasepath"/odoo-illingen"
if [ -d $myreppath ]; then
  cd $myreppath
  git checkout develop
  git pull git@bitbucket.org:equitania-ondemand/odoo-illingen.git
  echo "Pull lastest branch "$myreppath
else
  cd $mybasepath
  git clone -b develop git@bitbucket.org:equitania-ondemand/odoo-illingen.git
  echo "Clone lastest branch "$myreppath
fi

myreppath=$mybasepath"/odoo-jeremias"
if [ -d $myreppath ]; then
  cd $myreppath
  git checkout develop
  git pull git@bitbucket.org:equitania-ondemand/odoo-jeremias.git
  echo "Pull lastest branch "$myreppath
else
  cd $mybasepath
  git clone -b develop git@bitbucket.org:equitania-ondemand/odoo-jeremias.git
  echo "Clone lastest branch "$myreppath
fi

myreppath=$mybasepath"/odoo-myodoo"
if [ -d $myreppath ]; then
  cd $myreppath
  git checkout develop
  git pull git@bitbucket.org:equitania-ondemand/odoo-myodoo.git
  echo "Pull lastest branch "$myreppath
else
  cd $mybasepath
  git clone -b develop git@bitbucket.org:equitania-ondemand/odoo-myodoo.git
  echo "Clone lastest branch "$myreppath
fi

myreppath=$mybasepath"/odoo-sanicus"
if [ -d $myreppath ]; then
  cd $myreppath
  git checkout develop
  git pull git@bitbucket.org:equitania-ondemand/odoo-sanicus.git
  echo "Pull lastest branch "$myreppath
else
  cd $mybasepath
  git clone -b develop git@bitbucket.org:equitania-ondemand/odoo-sanicus.git
  echo "Clone lastest branch "$myreppath
fi

myreppath=$mybasepath"/odoo-schauspiel"
if [ -d $myreppath ]; then
  cd $myreppath
  git checkout develop
  git pull git@bitbucket.org:equitania-ondemand/odoo-schauspiel.git
  echo "Pull lastest branch "$myreppath
else
  cd $mybasepath
  git clone -b develop git@bitbucket.org:equitania-ondemand/odoo-schauspiel.git
  echo "Clone lastest branch "$myreppath
fi

myreppath=$mybasepath"/odoo-segelkoje"
if [ -d $myreppath ]; then
  cd $myreppath
  git checkout develop
  git pull git@bitbucket.org:equitania-ondemand/odoo-segelkoje.git
  echo "Pull lastest branch "$myreppath
else
  cd $mybasepath
  git clone -b develop git@bitbucket.org:equitania-ondemand/odoo-segelkoje.git
  echo "Clone lastest branch "$myreppath
fi

echo "Finished!"
