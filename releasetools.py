# Copyright (C) 2012 The Android Open Source Project
# Copyright (C) 2014 The CyanogenMod Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""Custom OTA commands for trlte devices"""

def FullOTA_InstallEnd(info):
  info.script.AppendExtra('mount("ext4", "EMMC", "/dev/block/platform/msm_sdcc.1/by-name/system", "/system", "");')
  info.script.AppendExtra('mount("vfat", "EMMC", "/dev/block/platform/msm_sdcc.1/by-name/apnhlos", "/firmware", "");')
  info.script.AppendExtra('run_program("/sbin/sh", "-c", "busybox mkdir -p /system/vendor/firmware/keymaster");')
  info.script.AppendExtra('run_program("/sbin/sh", "-c", "busybox cp /firmware/image/keymaste.mdt /system/vendor/firmware/keymaster/keymaster.mdt");')
  info.script.AppendExtra('run_program("/sbin/sh", "-c", "busybox cp /firmware/image/keymaste.b00 /system/vendor/firmware/keymaster/keymaster.b00");')
  info.script.AppendExtra('run_program("/sbin/sh", "-c", "busybox cp /firmware/image/keymaste.b01 /system/vendor/firmware/keymaster/keymaster.b01");')
  info.script.AppendExtra('run_program("/sbin/sh", "-c", "busybox cp /firmware/image/keymaste.b02 /system/vendor/firmware/keymaster/keymaster.b02");')
  info.script.AppendExtra('run_program("/sbin/sh", "-c", "busybox cp /firmware/image/keymaste.b03 /system/vendor/firmware/keymaster/keymaster.b03");')
  info.script.AppendExtra('set_metadata_recursive("/system/vendor/firmware/keymaster", "uid", 1000, "gid", 1000, "fmode", 0644, "dmode", 0777);')
  info.script.AppendExtra('unmount("/firmware");')
  info.script.AppendExtra('unmount("/system");')