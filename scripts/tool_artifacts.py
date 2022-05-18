import traceback

from scripts.artifacts.accounts_ce import get_accounts_ce
from scripts.artifacts.accounts_ce_authtokens import get_accounts_ce_authtokens
from scripts.artifacts.appicons import get_appicons
from scripts.artifacts.battery_usage_v4 import get_battery_usage_v4
from scripts.artifacts.bluetoothConnections import get_bluetoothConnections
from scripts.artifacts.build import get_build
from scripts.artifacts.burner import get_burner
from scripts.artifacts.calllog import get_calllog
from scripts.artifacts.chrome import get_chrome
from scripts.artifacts.chromeBookmarks import get_chromeBookmarks
from scripts.artifacts.chromeCookies import get_chromeCookies
from scripts.artifacts.chromeOfflinePages import get_chromeOfflinePages
from scripts.artifacts.chromeTopSites import get_chromeTopSites
from scripts.artifacts.contacts import get_contacts
from scripts.artifacts.discreteNative import get_discreteNative
from scripts.artifacts.gmail import get_gmailActive
from scripts.artifacts.googleKeepNotes import get_googleKeepNotes
from scripts.artifacts.messages import get_messages
from scripts.artifacts.googlePhotos import get_googlePhotos
from scripts.artifacts.googlePlaySearches import get_googlePlaySearches
from scripts.artifacts.googleQuickSearchbox import get_quicksearch
from scripts.artifacts.googleQuickSearchboxRecent import get_quicksearch_recent
from scripts.artifacts.googleTasks import get_googleTasks
from scripts.artifacts.last_boot_time import get_last_boot_time
from scripts.artifacts.packageGplinks import get_packageGplinks
from scripts.artifacts.permissions import get_permissions
from scripts.artifacts.powerOffReset import get_powerOffReset
from scripts.artifacts.recentactivity import get_recentactivity
from scripts.artifacts.shutdown_checkpoints import get_shutdown_checkpoints
from scripts.artifacts.siminfo import get_siminfo
from scripts.artifacts.teams import get_teams
from scripts.artifacts.usagestatsVersion import get_usagestatsVersion
from scripts.artifacts.userDict import get_userDict
from scripts.artifacts.Whatsapp import get_Whatsapp
from scripts.artifacts.wifiHotspot import get_wifiHotspot

from scripts.funcs import *

tosearch = {
    'build':('Device Info', '*/system/build.prop'),
    'accounts_ce': ('Accounts_ce', '*/data/system_ce/*/accounts_ce.db'),
    'accounts_ce_authtokens':('Accounts_ce', '*/data/system_ce/*/accounts_ce.db'),
    'appicons':('Installed Apps', '*/data/com.google.android.apps.nexuslauncher/databases/app_icons.db*'),
    'battery_usage_v4':('Settings Services', '**/com.google.android.settings.intelligence/databases/battery-usage-db-v4*'),
    'bluetoothConnections':('Bluetooth Connections', '*/data/misc/bluedroid/bt_config.conf'),
    'calllog': ('Call Logs', '*/data/com.android.providers.contacts/databases/calllog.db'),
    'chrome':('Chromium', '*/data/data/*/app_chrome/Default/History*'),
    'chromeBookmarks':('Chromium', '*/data/data/*/app_chrome/Default/Bookmarks*'),
    'chromeCookies':('Chromium', '*/data/data/*/app_chrome/Default/Cookies*'),
    'chromeOfflinePages':('Chromium', '*/data/data/*/app_chrome/Default/Offline Pages/metadata/OfflinePages.db*'),
    'chromeTopSites':('Chromium', '*/data/data/*/app_chrome/Default/Top Sites*'),
    'contacts':('Contacts', '**/com.android.providers.contacts/databases/contact*'),
    'discreteNative':('Privacy Dashboard',('*/data/system/appops/discrete/*')),
    'gmailActive':('Gmail', '**/com.google.android.gm/shared_prefs/Gmail.xml'),
    'googleKeepNotes':('Google Keep', "**/data/com.google.android.keep/databases/keep.db"),
    'messages': ('Messages', ('**/com.google.android.apps.messaging/databases/bugle_db*')),
    'googlePhotos':('Google Photos', ('*/data/data/com.google.android.apps.photos/databases/gphotos0.db*','*/data/data/com.google.android.apps.photos/databases/disk_cache*','*/data/data/com.google.android.apps.photos/cache/glide_cache/*','*/data/data/com.google.android.apps.photos/databases/local_trash.db*','*/data/data/com.google.android.apps.photos/files/trash_files/*')),
    'googlePlaySearches':('Google Play', '*/data/data/com.android.vending/databases/suggestions.db*'),
    'googleTasks':('Google Tasks', '*/com.google.android.apps.tasks/files/tasks-*/data.db'),
    'last_boot_time': ('Power Events', '**/data/misc/bootstat/last_boot_time_utc'),
    'packageGplinks': ('Installed Apps', '*/system/packages.list'),
    'powerOffReset': ('Power Events', ('*/data/log/power_off_reset_reason.txt','*/data/log/power_off_reset_reason_backup.txt')),
    'quicksearch':('Google Now & QuickSearch', '*/com.google.android.googlequicksearchbox/app_session/*.binarypb'),
    'quicksearch_recent':('Google Now & QuickSearch', '*/com.google.android.googlequicksearchbox/files/recently/*'),
    'recentactivity':('Recent Activity', '*/data/system_ce/*'),
    'permissions':('Permissions', '*/system/packages.xml'),
    'shutdown_checkpoints':('Power Events', '**/data/system/shutdown-checkpoints/*'),
    'siminfo':('Device Info', '*/user_de/*/com.android.providers.telephony/databases/telephony.db'),
    'teams':('Teams', '*/com.microsoft.teams/databases/SkypeTeams.db*'),
    'usagestatsVersion':('Usage Stats', '*/system/usagestats/*/version'),
    'userDict':('User Dictionary', '**/com.android.providers.userdictionary/databases/user_dict.db*'),
    'Whatsapp':('Whatsapp', ('*/com.whatsapp/databases/*.db*','**/com.whatsapp/shared_prefs/com.whatsapp_preferences_light.xml')),
    'wifiHotspot':('WiFi Profiles', '**/misc/wifi/softap.conf'),
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
