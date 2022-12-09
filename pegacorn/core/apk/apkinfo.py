from androguard.misc import AnalyzeDex, AnalyzeAPK
from androguard.core import androconf


class Apkinfo:
    def __init__(self, filepath):

        if get_file_type(filepath) == "APK":
            self.apk, self.dvm, self.dex = AnalyzeAPK(filepath)
        elif get_file_type(filepath) == "DEX":
            _, _, self.dex = AnalyzeDex(filepath)

    @property
    def package_name(self):
        if self.apk:
            return self.apk.get_package()
        return None

    @property
    def permissions(self):
        if self.apk:
            permissions = self.apk.get_permissions()
            return [p for p in permissions]
        return None

    @property
    def android_apis(self):
        """
        Return all Android native APIs from given APK.
        :return: a set of all Android native APIs MethodAnalysis
        """
        apis = set()

        for external_cls in self.dex.get_external_classes():
            for meth_analysis in external_cls.get_methods():
                if meth_analysis.is_android_api():
                    apis.add(meth_analysis)

        return apis

    @property
    def external_methods(self):
        """
        Return all external methods from given APK.
        :return: a set of all external methods MethodAnalysis
        """
        return {
            meth_analysis
            for meth_analysis in self.dex.get_methods()
            if not meth_analysis.is_external()
        }

    @property
    def strings(self):

        result = set()
        for string_analysis in self.dex.get_strings():
            # for cls_analysis in string_analysis.get_xref_from():
            # class_md, dvm_md = cls_analysis
            # if not exclude_package(class_md.name):
            result.add(string_analysis.get_orig_value())

        return result

    def get_intent_filters(self):
        if self.apk:
            return self.apk.get_intent_filters()
        return None

    @property
    def main_activity(self):
        if self.apk:
            return self.apk.get_main_activity()
        return None

    @property
    def providers(self):
        if self.apk:
            return self.apk.get_providers()
        return None

    @property
    def receivers(self):
        if self.apk:
            return self.apk.get_receivers()
        return None

    @property
    def services(self):
        if self.apk:
            return self.apk.get_services()
        return None

    @property
    def activity(self):
        if self.apk:
            return self.apk.get_activities()
        return None


def get_file_type(filename):
    return androconf.is_android(filename)
