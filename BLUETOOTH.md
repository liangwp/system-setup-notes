## Bluetooth Headphones Setup, Endeavouros 2024.07.06

### Bluetooth Driver and System Tools Setup

* Install bluetooth system software [https://wiki.archlinux.org/title/bluetooth](https://wiki.archlinux.org/title/bluetooth)
    ```
    sudo pacman -S bluez bluez-utils
    ```

* Ensure the bluetooth kernel drivers are available. (will see btusb in the list)
  [https://wiki.archlinux.org/title/Kernel_module#Obtaining_information](https://wiki.archlinux.org/title/Kernel_module#Obtaining_information)
    ```
    lsmod | grep btusb
    ```

* Start the bluetooth service, (and maybe enable it)
    ```
    sudo systemctl status bluetooth
    sudo systemctl start bluetooth
    (sudo systemctl enable bluetooth)
    ```

* Use a GUI tool to manage the bluetooth service
    ```
    sudo pacman -S blueman
    ```
* Blueman will show up in the system tray. Use to turn on and off the bluetooth
  adapter, and manage device pairings and connections.

* At this point, the system should be able to detect and pair with the bluetooth
  headphones, but will not be able to connect to it.

### Bluetooth Audio Connection Setup

* (Bluetooth supports many other things besides audio)

* Check if using pipewire or pulseaudio [https://www.reddit.com/r/linux4noobs/comments/n7tf6r/how_to_know_if_i_am_using_pipewire/](https://www.reddit.com/r/linux4noobs/comments/n7tf6r/how_to_know_if_i_am_using_pipewire/)
    ```
    pactl info
    ps -e | grep pipewire
    ```

* Install the audio system for pipewire or pulseaudio (pulseaudio in my case).
  [https://wiki.archlinux.org/title/Bluetooth_headset](https://wiki.archlinux.org/title/Bluetooth_headset)
    ```
    pacman -S pulseaudio-bluetooth
    ```

* At this point, the system should be able to connect to the bluetooth
  headphones.
* The audio mixer manager (awkward as it is) should display the bluetooth device
  as an audio input/output device, and we should be able to switch to it.


