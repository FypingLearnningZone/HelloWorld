title: fix_virtualbox_Kernel_Driver_Not_Installed
date: 2018/1/1 12:12:12
---
After a fresh VirtualBox installation on Manjaro linux, you may run into this error message "Kernel driver not installed (rc=-1908)

The VirtualBox Linux kernel driver (vboxdrv) is either not loaded or there is a permission problem with /dev/vboxdrv."

Run these commands to fix (First one gives you the precise version of the 2nd.. if you have linux kernel 4.16 then pacman linux416)
uname -r 
sudo pacman -S linux414-virtualbox-host-modules
sudo modprobe vboxdrv

And finally restart virtualbox



> from https://www.youtube.com/watch?v=2_H62iUxVj8

