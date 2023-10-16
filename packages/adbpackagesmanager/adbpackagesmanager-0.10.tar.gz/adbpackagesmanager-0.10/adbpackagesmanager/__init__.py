import os
import re
import sys
from touchtouch import touch
from usefuladb import AdbCommands
from a_pandas_ex_apply_ignore_exceptions import pd_add_apply_ignore_exceptions
import pandas as pd
from windows_filepath import make_filepath_windows_comp

pd_add_apply_ignore_exceptions()


class CopyFile:
    def __init__(self, s, fu, p):
        self.fu = fu
        self.p = p
        self.s = s

    def __call__(self, outputfolder, **kwargs):
        return self.fu(self.s, self.p, outputfolder, **kwargs)

    def __str__(self):
        return f"/data/data/{self.p}"

    def __repr__(self):
        return self.__str__()


class CopyApkFile:
    def __init__(self, s, fu, p):
        self.fu = fu
        self.p = p
        self.of = re.sub(r"[\\/]+", r"\\", self.p.strip(r" \\/"))
        self.s = s

    def __call__(self, outputfolder, **kwargs):
        outputfile = os.path.join(outputfolder.strip(r" \\/"), self.of)
        try:
            return self.fu(self.s, self.p, outputfile, **kwargs)
        except Exception as e:
            sys.stderr.write(f"{e}")
            return pd.NA

    def __str__(self):
        return f"{self.of}"

    def __repr__(self):
        return self.__str__()


class PackageManager:
    def __init__(self, adb=None, adb_path=None, serial_number=None, **kwargs):
        r"""
        Initializes a PackageManager instance for managing Android packages on a device.

        Args:
            adb (AdbCommands, optional): An existing AdbCommands instance. If not provided,
                a new instance will be created using the specified adb_path and serial_number.
            adb_path (str, optional): The path to the adb executable (e.g., 'C:\Android\android-sdk\platform-tools\adb.exe').
            serial_number (str, optional): The serial number of the Android device or emulator to target.
            **kwargs: Additional keyword arguments to pass to AdbCommands.

        Example:
            from adbpackagesmanager import PackageManager

            adbpath = r"C:\Android\android-sdk\platform-tools\adb.exe"
            serial_number = "127.0.0.1:5555"
            addpkg = PackageManager(adb_path=adbpath, serial_number=serial_number)
            df=addpkg.get_packages_df(ps=True)

            df.loc[(df.aa_3rd_party) &(df.aa_package=='com.ytheekshana.deviceinfo')].aa_copy_data_to_hdd.iloc[0]('c:\\deviceinfo_data')
            df.loc[(df.aa_3rd_party) &(df.aa_package=='com.ytheekshana.deviceinfo')].aa_copy_apk_to_hdd.iloc[0]('c:\\deviceinfo_apk')
            print(df[:5].to_string())

            # print(df[:5].to_string())
            #                                                                                 aa_path                                            aa_package aa_installer  aa_uid  aa_3rd_party  aa_system                                              aa_copy_data_to_hdd                                                                   aa_copy_apk_to_hdd
            # 0  /vendor/overlay/DisplayCutoutEmulationCorner/DisplayCutoutEmulationCornerOverlay.apk  com.android.internal.display.cutout.emulation.corner         <NA>   10002         False       True  /data/data/com.android.internal.display.cutout.emulation.corner  vendor\overlay\DisplayCutoutEmulationCorner\DisplayCutoutEmulationCornerOverlay.apk
            # 1  /vendor/overlay/DisplayCutoutEmulationDouble/DisplayCutoutEmulationDoubleOverlay.apk  com.android.internal.display.cutout.emulation.double         <NA>   10001         False       True  /data/data/com.android.internal.display.cutout.emulation.double  vendor\overlay\DisplayCutoutEmulationDouble\DisplayCutoutEmulationDoubleOverlay.apk
            # 2                       /data/downloads/com.location.provider/com.location.provider.apk                                 com.location.provider         <NA>   10044         False       True                                 /data/data/com.location.provider                       data\downloads\com.location.provider\com.location.provider.apk
            # 3                              /system/priv-app/TelephonyProvider/TelephonyProvider.apk                       com.android.providers.telephony         <NA>    1001         False       True                       /data/data/com.android.providers.telephony                              system\priv-app\TelephonyProvider\TelephonyProvider.apk
            # 4                                /system/priv-app/CalendarProvider/CalendarProvider.apk                        com.android.providers.calendar         <NA>   10013         False       True                        /data/data/com.android.providers.calendar                                system\priv-app\CalendarProvider\CalendarProvider.apk


        """
        if not adb:
            self.adb = AdbCommands(adb_path, serial_number, **kwargs)
        else:
            self.adb = adb

    def get_packages_df(self, **kwargs):
        r"""
        Retrieves a DataFrame containing information about installed Android packages on the device.

        Args:
            **kwargs: Additional keyword arguments to customize package listing.

        Returns:
            pandas.DataFrame: A DataFrame with package information, including package path, package name, installer,
                UID, whether it's a third-party app, and whether it's a system app. It also provides methods for
                copying the app's data and APK to the local file system.

        Example:
            df = PackageManager.get_packages_df(ps=True)
            # Retrieve and manipulate package information using the DataFrame.

        Note:
            To access package-specific actions like copying data or APK, you can use the provided methods in the DataFrame.
        """
        kwargs.update({"print_stdout": False})
        df = (
            pd.DataFrame(
                [
                    x.decode("utf-8")
                    for x in self.adb.sh_pm_list_packages_f_i_u(**kwargs)[0]
                ]
            )[0]
            .str.extractall(
                r"^package:/(?P<aa_package>.*?)\s+installer=(?P<aa_installer>.*?)\s+uid:(?P<aa_uid>.*)"
            )
            .reset_index(drop=True)
        )
        df = pd.concat(
            [
                df.aa_package.str.rsplit("=", n=1, expand=True).rename(
                    columns={0: "aa_path", 1: "aa_package"}
                ),
                df[["aa_installer", "aa_uid"]],
            ],
            axis=1,
        )

        df.aa_uid = df.aa_uid.astype("Int64")
        df.loc[df.aa_installer == "null", "aa_installer"] = pd.NA

        df["aa_3rd_party"] = False
        df.loc[
            df.aa_package.isin(
                [
                    re.sub(
                        "^package:", "", x.decode("utf-8", "backslashreplace").strip()
                    )
                    for x in self.adb.sh_pm_list_packages_3(**kwargs)[0]
                ]
            ),
            "aa_3rd_party",
        ] = True
        df["aa_system"] = False
        df.loc[
            df.aa_package.isin(
                [
                    re.sub(
                        "^package:", "", x.decode("utf-8", "backslashreplace").strip()
                    )
                    for x in self.adb.sh_pm_list_packages_s(**kwargs)[0]
                ]
            ),
            "aa_system",
        ] = True

        df.aa_path = "/" + df.aa_path
        df["aa_copy_data_to_hdd"] = df.aa_package.ds_apply_ignore(
            pd.NA, lambda q: CopyFile(self.adb, copy_package_data_to_hdd, q)
        )

        df["aa_copy_apk_to_hdd"] = df.aa_path.ds_apply_ignore(
            pd.NA, lambda q: CopyApkFile(self.adb, copy_apk_to_hdd, q)
        )
        return df


def copy_package_data_to_hdd(s, package, outputfolder, **kwargs):
    kwargs.update({"su": True})
    rdf = s.manage_files(f"/data/data/{package}", **kwargs)
    kwargs.update({"su": True, "print_stdout": False})
    resultdict = {}
    for k, v in rdf.files.items():
        if not v["is_file"]:
            continue
        try:
            p = os.path.join(outputfolder, v["path"].strip("/").replace("/", os.sep))
            touch(p)

            with open(p, mode="wb") as f:
                f.write(v["cat_file"](**kwargs))
            resultdict[v["path"]] = p
            sys.stderr.write(f'\r{v["path"]} -> {p}')
        except Exception as e:
            sys.stderr.write(f"{e}")
    return resultdict


def copy_apk_to_hdd(s, p, savepath, **kwargs):
    kwargs.update({"su": True, "print_stdout": False})
    try:
        touch(savepath)
    except Exception:
        savepath = make_filepath_windows_comp(
            filepath=savepath,
            fillvalue="_",
            reduce_fillvalue=False,
            remove_backslash_and_col=False,
            spaceforbidden=False,
            other_to_replace=(),
            slash_to_backslash=True,
        )
        touch(savepath)

    with open(savepath, mode="wb") as f:
        f.write(s.sh_cat_get_file(p, **kwargs))
    return savepath
