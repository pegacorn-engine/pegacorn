from pegacorn.core.apk.apkinfo import Apkinfo


def proc_apk(filepath):
    apk = Apkinfo(filepath)

    print("APK INFO")
    print("--------")
    print(apk.package_name)
    print(apk.main_activity)

    print("--------")
    print(apk.activity)
    print(apk.receivers)
    print(apk.services)
    print(apk.providers)
