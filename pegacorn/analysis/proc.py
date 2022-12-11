from pegacorn.core.apk.apkinfo import Apkinfo
from pegacorn.output.json import json_output


def proc_apk(filepath):
    apk = Apkinfo(filepath)

    result = {
        "main_activity": apk.main_activity,
        "package_name": apk.package_name,
        "activity": apk.activity,
        "receiver": apk.receivers,
        "service": apk.services,
        "provider": apk.providers,
    }

    print(result)

    print(json_output(result))
