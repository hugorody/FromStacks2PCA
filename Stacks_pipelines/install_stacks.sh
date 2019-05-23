#!/usr/bin/sh

stacks_download=`echo "http://catchenlab.life.illinois.edu/stacks/source/stacks-2.4.tar.gz"`

#Download Stacks
wget "$stacks_download"

#Install Stacks
tar xfvz stacks-2.4.tar.gz
cd stacks-2.4/
./configure
make -j 2 #use 2 processors
sudo make install
