import traceback

from scripts.artifacts.accounts_ce import get_accounts_ce
from scripts.artifacts.accounts_ce_authtokens import get_accounts_ce_authtokens
from scripts.artifacts.appicons import get_appicons
from scripts.artifacts.battery_usage_v4 import get_battery_usage_v4
from scripts.artifacts.bluetoothConnections import get_bluetoothConnections
from scripts.artifacts.build import get_build
from scripts.artifacts.burner import get_burner
from scripts.artifacts.cachelocation import get_cachelocation
from scripts.artifacts.calllog import get_calllog
from scripts.artifacts.calllogs import get_calllogs
from scripts.artifacts.chrome import get_chrome
from scripts.artifacts.chromeAutofill import get_chromeAutofill
from scripts.artifacts.chromeBookmarks import get_chromeBookmarks
from scripts.artifacts.chromeCookies import get_chromeCookies
from scripts.artifacts.chromeLoginData import get_chromeLoginData
from scripts.artifacts.chromeMediaHistory import get_chromeMediaHistory
from scripts.artifacts.chromeNetworkActionPredictor import get_chromeNetworkActionPredictor
from scripts.artifacts.chromeOfflinePages import get_chromeOfflinePages
from scripts.artifacts.chromeTopSites import get_chromeTopSites
from scripts.artifacts.clipBoard import get_clipBoard
from scripts.artifacts.contacts import get_contacts
from scripts.artifacts.discreteNative import get_discreteNative
from scripts.artifacts.DocList import get_DocList
from scripts.artifacts.emulatedSmeta import get_emulatedSmeta
from scripts.artifacts.gboard import get_gboardCache
from scripts.artifacts.gmail import get_gmailActive
from scripts.artifacts.googleCallScreen import get_googleCallScreen
from scripts.artifacts.googleChat import get_googleChat
from scripts.artifacts.googleDuo import get_googleDuo
from scripts.artifacts.googleFitGMS import get_googleFitGMS
from scripts.artifacts.googleKeepNotes import get_googleKeepNotes
from scripts.artifacts.messages import get_messages
from scripts.artifacts.googlePhotos import get_googlePhotos
from scripts.artifacts.googlemaplocation import get_googlemaplocation
from scripts.artifacts.googlemapaudio import get_googlemapaudio
from scripts.artifacts.googleNowPlaying import get_googleNowPlaying
from scripts.artifacts.googlePlaySearches import get_googlePlaySearches
from scripts.artifacts.googleQuickSearchbox import get_quicksearch
from scripts.artifacts.googleQuickSearchboxRecent import get_quicksearch_recent
from scripts.artifacts.googleTasks import get_googleTasks
from scripts.artifacts.last_boot_time import get_last_boot_time
from scripts.artifacts.pSettings import get_pSettings
from scripts.artifacts.packageGplinks import get_packageGplinks
from scripts.artifacts.permissions import get_permissions
from scripts.artifacts.playgroundVault import get_playgroundVault
from scripts.artifacts.powerOffReset import get_powerOffReset
from scripts.artifacts.recentactivity import get_recentactivity
from scripts.artifacts.lgRCS import get_lgRCS
from scripts.artifacts.Oruxmaps import get_Oruxmaps
from scripts.artifacts.roles import get_roles
from scripts.artifacts.shareit import get_shareit
from scripts.artifacts.shutdown_checkpoints import get_shutdown_checkpoints
from scripts.artifacts.siminfo import get_siminfo
from scripts.artifacts.skype import get_skype
from scripts.artifacts.smyfilesRecents import get_smyfilesRecents
from scripts.artifacts.smyFiles import get_smyFiles
from scripts.artifacts.smyfilesStored import get_smyfilesStored
from scripts.artifacts.snapchat import get_snapchat
from scripts.artifacts.teams import get_teams
from scripts.artifacts.usageapps import get_usageapps
from scripts.artifacts.usagestatsVersion import get_usagestatsVersion
from scripts.artifacts.userDict import get_userDict
from scripts.artifacts.vlcMedia import get_vlcMedia
from scripts.artifacts.vlcThumbs import get_vlcThumbs
from scripts.artifacts.walStrings import get_walStrings
from scripts.artifacts.wellbeing import get_wellbeing
from scripts.artifacts.wellbeingURLs import get_wellbeingURLs
from scripts.artifacts.wellbeingaccount import get_wellbeingaccount
from scripts.artifacts.Whatsapp import get_Whatsapp
from scripts.artifacts.wifiConfigstore import get_wifiConfigstore
from scripts.artifacts.wifiHotspot import get_wifiHotspot
from scripts.artifacts.wifiProfiles import get_wifiProfiles

from scripts.funcs import *

tosearch = {
    'build':('Device Info', '*/vendor/build.prop'),
    'accounts_ce': ('Accounts_ce', '*/data/system_ce/*/accounts_ce.db'),
    'accounts_ce_authtokens':('Accounts_ce', '*/data/system_ce/*/accounts_ce.db'),
    'appicons':('Installed Apps', '*/data/com.google.android.apps.nexuslauncher/databases/app_icons.db*'),
    'battery_usage_v4':('Settings Services', '**/com.google.android.settings.intelligence/databases/battery-usage-db-v4*'),
    'bluetoothConnections':('Bluetooth Connections', '*/data/misc/bluedroid/bt_config.conf'),
    'cachelocation': ('GEO Location', ('**/com.google.android.location/files/cache.cell/cache.cell', '**/com.google.android.location/files/cache.wifi/cache.wifi')),
    'calllog': ('Call Logs', '*/data/com.android.providers.contacts/databases/calllog.db'),
    'calllogs':('Call Logs', ('**/com.android.providers.contacts/databases/contact*', '**/com.sec.android.provider.logsprovider/databases/logs.db*')),
    'chrome':('Chromium', ('*/data/data/*/app_chrome/Default/History*', '*/data/data/*/app_sbrowser/Default/History*', '*/data/data/*/app_opera/History*')),
    'chromeAutofill':('Chromium', ('*/data/data/*/app_chrome/Default/Web Data*', '*/data/data/*/app_sbrowser/Default/Web Data*', '*/data/data/*/app_opera/Web Data*')),
    'chromeBookmarks':('Chromium', ('*/data/data/*/app_chrome/Default/Bookmarks*', '*/data/data/*/app_sbrowser/Default/Bookmarks*', '*/data/data/*/app_opera/Bookmarks*')),
    'chromeCookies':('Chromium', ('*/data/data/*/app_chrome/Default/Cookies*', '*/data/data/*/app_sbrowser/Default/Cookies*', '*/data/data/*/app_opera/Cookies*')),
    'chromeLoginData':('Chromium', ('*/data/data/*/app_chrome/Default/Login Data*', '*/data/data/*/app_sbrowser/Default/Login Data*', '*/data/data/*/app_opera/Login Data*')),
    'chromeMediaHistory':('Chromium', ('*/data/data/*/app_chrome/Default/Media History*','*/data/data/*/app_sbrowser/Default/Media History*', '*/data/data/*/app_opera/Media History*')),
    'chromeNetworkActionPredictor':('Chromium', ('*/data/data/*/app_Chrome/Default/Network Action Predictor*','*/data/data/*/app_sbrowser/Default/Network Action Predictor*', '*/data/data/*/app_opera/Network Action Predicator*')),
    'chromeOfflinePages':('Chromium', ('*/data/data/*/app_chrome/Default/Offline Pages/metadata/OfflinePages.db*', '*/data/data/*/app_sbrowser/Default/Offline Pages/metadata/OfflinePages.db*')),
    'chromeTopSites':('Chromium', ('*/data/data/*/app_chrome/Default/Top Sites*', '*/data/data/*/app_sbrowser/Default/Top Sites*', '*/data/*/app_opera/Top Sites*')),
    'clipBoard':('Clipboard', '*/data/*clipboard/*/*'),
    'contacts':('Contacts', ('**/com.android.providers.contacts/databases/contact*', '**/com.sec.android.provider.logsprovider/databases/logs.db*')),
    'discreteNative':('Privacy Dashboard',('*/data/system/appops/discrete/*')),
    'DocList':('Google Drive', '*/data/data/com.google.android.apps.docs/databases/DocList.db*'),
    'emulatedSmeta':('Emulated Storage Metadata', '*/data/data/com.google.android.providers.media.module/databases/external.db*'),
    'gboardCache':('Gboard Keyboard', '**/com.google.android.inputmethod.latin/databases/trainingcache*.db'),
    'gmailActive':('Gmail', '**/com.google.android.gm/shared_prefs/Gmail.xml'),
    'googleCallScreen':('Google Call Screen', ('**/com.google.android.dialer/databases/callscreen_transcripts*','**/com.google.android.dialer/files/callscreenrecordings/*.*')),
    'googleChat':('Google Chat', ('**/com.google.android.gm/databases/user_accounts/*/dynamite*.db','**/com.google.android.apps.dynamite/databases/dynamite*.db')),
    'googleDuo':('Google Duo', ('**/com.google.android.apps.tachyon/databases/tachyon.db*','**/com.google.android.apps.tachyon/files/media/*.*')),
    'googleFitGMS': ('Google Fit (GMS)', ('*/data/data/com.google.android.gms/databases/fitness.db.*')),
    'googleKeepNotes':('Google Keep', "**/data/com.google.android.keep/databases/keep.db"),
    'googlemaplocation': ('GEO Location', ('**/com.google.android.apps.maps/databases/da_destination_history*')),
    'googlemapaudio': ('Google Maps Voice Guidance', '**/data/data/com.google.android.apps.maps/app_tts-cache/*_*'),
    'messages': ('Messages', ('**/com.google.android.apps.messaging/databases/bugle_db*')),
    'googleNowPlaying':('Now Playing', ('*/data/data/com.google.intelligence.sense/db/history_db*','*/data/data/com.google.android.as/databases/history_db*')),
    'googlePhotos':('Google Photos', ('*/data/data/com.google.android.apps.photos/databases/gphotos0.db*','*/data/data/com.google.android.apps.photos/databases/disk_cache*','*/data/data/com.google.android.apps.photos/cache/glide_cache/*','*/data/data/com.google.android.apps.photos/databases/local_trash.db*','*/data/data/com.google.android.apps.photos/files/trash_files/*')),
    'googlePlaySearches':('Google Play', '*/data/data/com.android.vending/databases/suggestions.db*'),
    'googleTasks':('Google Tasks', '*/com.google.android.apps.tasks/files/tasks-*/data.db'),
    'last_boot_time': ('Power Events', '**/data/misc/bootstat/last_boot_time_utc'),
    'pSettings':('Device Info', '*/data/data/com.google.android.gsf/databases/googlesettings.db*'),
    'packageGplinks': ('Installed Apps', '*/system/packages.list'),
    'powerOffReset': ('Power Events', ('*/data/log/power_off_reset_reason.txt','*/data/log/power_off_reset_reason_backup.txt')),
    'quicksearch':('Google Now & QuickSearch', '*/com.google.android.googlequicksearchbox/app_session/*.binarypb'),
    'quicksearch_recent':('Google Now & QuickSearch', '*/com.google.android.googlequicksearchbox/files/recently/*'),
    'recentactivity':('Recent Activity', '*/data/system_ce/*'),
    'lgRCS':('RCS Chats', '*/mmssms.db*'),
    'Oruxmaps':('GEO Location', '**/oruxmaps/tracklogs/oruxmapstracks.db*'),
    'permissions':('Permissions', '*/system/packages.xml'),
    'playgroundVault':('Encrypting Media Apps',('*/playground.develop.applocker/shared_prefs/crypto.KEY_256.xml','*/applocker/vault/*')),
    'roles':('App Roles',('*/system/users/*/roles.xml','*/misc_de/*/apexdata/com.android.permission/roles.xml')),
    'shareit':('File Transfer', '*/com.lenovo.anyshare.gps/databases/history.db*'),
    'shutdown_checkpoints':('Power Events', '**/data/system/shutdown-checkpoints/*'),
    'siminfo':('Device Info', '*/user_de/*/com.android.providers.telephony/databases/telephony.db'),
    'skype': ('Skype', '**/com.skype.raider/databases/live*'),
    'smyfilesRecents':('Media Metadata', '*/com.sec.android.app.myfiles/databases/myfiles.db'),
    'smyFiles':('Media Metadata', '**/com.sec.android.app.myfiles/databases/MyFiles*.db*'),
    'smyfilesStored':('Media Metadata', '**/com.sec.android.app.myfiles/databases/FileCache.db'),
    'snapchat': ('Snapchat', ('**/data/com.snapchat.android/databases/*.db', '**/data/com.snapchat.android/shared_prefs/*.xml')),
    'teams':('Teams', '*/com.microsoft.teams/databases/SkypeTeams.db*'),
    'usageapps': ('App Interaction', '**/com.google.android.as/databases/reflection_gel_events.db*'),
    'usagestatsVersion':('Usage Stats', '*/system/usagestats/*/version'),
    'userDict':('User Dictionary', '**/com.android.providers.userdictionary/databases/user_dict.db*'),
    'vlcMedia': ('VLC', '*vlc_media.db*'),
    'vlcThumbs': ('VLC', '*/org.videolan.vlc/files/medialib/*.jpg'),
    'walStrings':('SQLite Journaling', ('**/*-wal', '**/*-journal')),
    'wellbeing': ('Wellbeing', '**/com.google.android.apps.wellbeing/databases/app_usage*'),
    'wellbeingURLs': ('Wellbeing', '**/com.google.android.apps.wellbeing/databases/app_usage*'), # Get app_usage & app_usage-wal
    'wellbeingaccount': ('Wellbeing', '**/com.google.android.apps.wellbeing/files/AccountData.pb'),
    'Whatsapp':('Whatsapp', ('*/com.whatsapp/databases/*.db*','**/com.whatsapp/shared_prefs/com.whatsapp_preferences_light.xml')),
    'wifiConfigstore':('WiFi Profiles', ('**/misc/wifi/WifiConfigStore.xml', '**/misc**/apexdata/com.android.wifi/WifiConfigStore.xml')),
    'wifiHotspot':('WiFi Profiles', ('**/misc/wifi/softap.conf', '**/misc**/apexdata/com.android.wifi/WifiConfigStoreSoftAp.xml')),
    'wifiProfiles':('WiFi Profiles', ('**/misc/wifi/WifiConfigStore.xml', '**/misc**/apexdata/com.android.wifi/WifiConfigStore.xml')),
    }

slash = '\\' if is_platform_windows() else '/'

def process_artifact(files_found, artifact_func, artifact_name, seeker, report_folder_base, wrap_text):
    logfunc('{} [{}] artifact executing'.format(artifact_name, artifact_func))
    report_folder = os.path.join(report_folder_base, artifact_name) + slash
    try:
        if os.path.isdir(report_folder):
            pass
        else:
            os.makedirs(report_folder)
    except Exception as ex:
        logfunc('Error creating {} report directory at path {}'.format(artifact_name, report_folder))
        logfunc('Reading {} artifact failed!'.format(artifact_name))
        logfunc('Error was {}'.format(str(ex)))
        return
    try:
        method = globals()['get_' + artifact_func]
        method(files_found, report_folder, seeker, wrap_text)
    except Exception as ex:
        logfunc('Reading {} artifact had errors!'.format(artifact_name))
        logfunc('Error was {}'.format(str(ex)))
        logfunc('Exception Traceback: {}'.format(traceback.format_exc()))
        return

    logfunc('{} [{}] artifact completed'.format(artifact_name, artifact_func))
