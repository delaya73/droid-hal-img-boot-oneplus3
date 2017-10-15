%define device oneplus3

%define mkbootimg_cmd mkbootimg --ramdisk %{initrd}  --kernel %{kernel} --base 0x80000000 --pagesize 4096 --cmdline "androidboot.hardware=qcom user_debug=31 msm_rtb.filter=0x237 ehci-hcd.park=3 lpm_levels.sleep_disabled=1 cma=32M@0-0xffffffff" --output

%define root_part_label userdata
%define factory_part_label system

%define display_brightness_path /sys/class/leds/lcd-backlight/brightness
%define display_brightness 16

%include initrd/droid-hal-device-img-boot.inc
