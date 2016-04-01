# Collection of gimp plugins written for Fishing Cactus

## How to use:

```bash
#find the location of your gimp plugins:
dpkg -L gimp | grep plug-ins
#symlink the desired scripts:
ln -s /path_to_git_repo/gimp-plugins/background-to-border-image.py /path_to_gimp_plugins/plug-ins/
```

## Image manipulation:

* [Convert background image to border-image ( prepare for 9 slice )](https://github.com/FishingCactus/gimp-plugins/blob/master/background-to-border-image.py)
