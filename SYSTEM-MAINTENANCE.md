# System Maintenance Steps for Endeavouros

1. Update system:
    - `sudo pacman -Syu`
    - in each aur package in this directory
        - `git remote update` (check for any updates)
        - `git pull` (if necessary)
        - `makepkg -sirc` (if necessary)
    - if nvidia, docker, or linux kernel is updated, try running the
      test pytorch container, to ensure we still have gpu in docker.
      ```
      cd pytorch-gpu-test
      docker compose up --build
      ```
1. Manage `*.pacnew` and `*.pacsave` files: https://wiki.archlinux.org/title/pacman/Pacnew_and_Pacsave
1. clean up docker
    - `df -h` (see if `/var` is filling up)
    - `docker system df`
    - `docker container prune`
    - `docker image prune` (maybe with `--all` flag)
    - `docker rmi $(docker images -q abc-def:*)` filter and delete images by tag:label
    - `docker builder prune`
    - optional: `docker system prune` This actually leaves the named volumes
      and tagged images, so presumably it cleans up the overlays.

Note: If `/var` fills up, things may start to fail. Case in point, `lightdm`,
presumably because it can't write its logs.

If lightdm fails, we can't get into the system...
1. Boot into a live-usb
1. arch-chroot into the dead system (therefore by-passing lightdm and whatever disk issues at startup)
1. Manually clear some stuff out of the docker.
    1. Usually the overlay2 directory is the culprit
    1. `cd /var/lib/docker/overlay2`
    1. `du -ah --max-depth=1 | sort -h` Find the biggest overlay directories
    1. `rm -r` a few of them
1. system should be able to boot normally after restart
1. Best to do a `docker system prune` after this action. We don't know who/what owns the overlays we deleted...

# via AppImage

VIA software used to remap the custom keyboard, needs +x permissions.

When first run, installed some udev rule, probably to give it the right permissions to access the keyboard.

