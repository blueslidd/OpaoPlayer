[app]
title = OpaoPlayer
package.name = opaoplayer
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,mp3
version = 0.1
requirements = python3,kivy==2.1.0
orientation = portrait
fullscreen = 1
android.presplash_color = #000000
android.permissions = INTERNET,MODIFY_AUDIO_SETTINGS,WAKE_LOCK
android.api = 27
android.minapi = 21
android.ndk = 19b
android.sdk = 27
android.accept_sdk_license = True
android.arch = armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 0
