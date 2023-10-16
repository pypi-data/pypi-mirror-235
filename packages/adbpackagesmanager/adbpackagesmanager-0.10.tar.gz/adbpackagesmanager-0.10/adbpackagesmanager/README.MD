# Manages Android packages on a device through DataFrames 

## Tested against Windows / Python 3.11 / Anaconda

## pip install adbpackagesmanager

```python

class PackageManager(builtins.object)
 |  PackageManager(adb=None, adb_path=None, serial_number=None, **kwargs)
 |  
 |  Methods defined here:
 |  
 |  __init__(self, adb=None, adb_path=None, serial_number=None, **kwargs)
 |      Initializes a PackageManager instance for managing Android packages on a device.
 |      
 |      Args:
 |          adb (AdbCommands, optional): An existing AdbCommands instance. If not provided,
 |              a new instance will be created using the specified adb_path and serial_number.
 |          adb_path (str, optional): The path to the adb executable (e.g., 'C:\Android\android-sdk\platform-tools\adb.exe').
 |          serial_number (str, optional): The serial number of the Android device or emulator to target.
 |          **kwargs: Additional keyword arguments to pass to AdbCommands.
 |      
 |      Example:
 |          from adbpackagesmanager import PackageManager
 |      
 |          adbpath = r"C:\Android\android-sdk\platform-tools\adb.exe"
 |          serial_number = "127.0.0.1:5555"
 |          addpkg = PackageManager(adb_path=adbpath, serial_number=serial_number)
 |          df=addpkg.get_packages_df(ps=True)
 |      
 |          df.loc[(df.aa_3rd_party) &(df.aa_package=='com.ytheekshana.deviceinfo')].aa_copy_data_to_hdd.iloc[0]('c:\\deviceinfo_data')
 |          df.loc[(df.aa_3rd_party) &(df.aa_package=='com.ytheekshana.deviceinfo')].aa_copy_apk_to_hdd.iloc[0]('c:\\deviceinfo_apk')
 |          print(df[:5].to_string())
 |      
 |          # print(df[:5].to_string())
 |          #                                                                                 aa_path                                            aa_package aa_installer  aa_uid  aa_3rd_party  aa_system                                              aa_copy_data_to_hdd                                                                   aa_copy_apk_to_hdd
 |          # 0  /vendor/overlay/DisplayCutoutEmulationCorner/DisplayCutoutEmulationCornerOverlay.apk  com.android.internal.display.cutout.emulation.corner         <NA>   10002         False       True  /data/data/com.android.internal.display.cutout.emulation.corner  vendor\overlay\DisplayCutoutEmulationCorner\DisplayCutoutEmulationCornerOverlay.apk
 |          # 1  /vendor/overlay/DisplayCutoutEmulationDouble/DisplayCutoutEmulationDoubleOverlay.apk  com.android.internal.display.cutout.emulation.double         <NA>   10001         False       True  /data/data/com.android.internal.display.cutout.emulation.double  vendor\overlay\DisplayCutoutEmulationDouble\DisplayCutoutEmulationDoubleOverlay.apk
 |          # 2                       /data/downloads/com.location.provider/com.location.provider.apk                                 com.location.provider         <NA>   10044         False       True                                 /data/data/com.location.provider                       data\downloads\com.location.provider\com.location.provider.apk
 |          # 3                              /system/priv-app/TelephonyProvider/TelephonyProvider.apk                       com.android.providers.telephony         <NA>    1001         False       True                       /data/data/com.android.providers.telephony                              system\priv-app\TelephonyProvider\TelephonyProvider.apk
 |          # 4                                /system/priv-app/CalendarProvider/CalendarProvider.apk                        com.android.providers.calendar         <NA>   10013         False       True                        /data/data/com.android.providers.calendar                                system\priv-app\CalendarProvider\CalendarProvider.apk
 |  
 |  get_packages_df(self, **kwargs)
 |      Retrieves a DataFrame containing information about installed Android packages on the device.
 |      
 |      Args:
 |          **kwargs: Additional keyword arguments to customize package listing.
 |      
 |      Returns:
 |          pandas.DataFrame: A DataFrame with package information, including package path, package name, installer,
 |              UID, whether it's a third-party app, and whether it's a system app. It also provides methods for
 |              copying the app's data and APK to the local file system.
 |      
 |      Example:
 |          df = PackageManager.get_packages_df(ps=True)
 |          # Retrieve and manipulate package information using the DataFrame.
 |      
 |      Note:
 |          To access package-specific actions like copying data or APK, you can use the provided methods in the DataFrame.

```