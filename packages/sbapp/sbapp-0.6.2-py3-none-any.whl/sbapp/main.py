__debug_build__ = False
__disable_shaders__ = False
__version__ = "0.6.2"
__variant__ = "beta"

import sys
import argparse
parser = argparse.ArgumentParser(description="Reticulum Network Stack Daemon")
parser.add_argument("-v", "--verbose", action='store_true', default=False, help="increase logging verbosity")
parser.add_argument("--version", action="version", version="sideband {version}".format(version=__version__))
args = parser.parse_args()
sys.argv = [sys.argv[0]]

import RNS
import LXMF
import time
import os
import plyer
import base64
import threading
import RNS.vendor.umsgpack as msgpack

from kivy.logger import Logger, LOG_LEVELS
if __debug_build__ or args.verbose:
    Logger.setLevel(LOG_LEVELS["debug"])
else:
    Logger.setLevel(LOG_LEVELS["error"])

if RNS.vendor.platformutils.get_platform() != "android":
    local = os.path.dirname(__file__)
    sys.path.append(local)

from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.core.clipboard import Clipboard
from kivy.base import EventLoop
from kivy.clock import Clock
from kivy.lang.builder import Builder
from kivy.effects.scroll import ScrollEffect
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import FadeTransition, NoTransition

if RNS.vendor.platformutils.get_platform() == "android":
    from sideband.core import SidebandCore

    from ui.layouts import root_layout
    from ui.conversations import Conversations, MsgSync, NewConv
    from ui.announces import Announces
    from ui.messages import Messages, ts_format
    from ui.helpers import ContentNavigationDrawer, DrawerList, IconListItem

    from jnius import cast
    from jnius import autoclass
    from android import mActivity
    from android.permissions import request_permissions, check_permission

    from kivymd.utils.set_bars_colors import set_bars_colors
    android_api_version = autoclass('android.os.Build$VERSION').SDK_INT

else:
    from .sideband.core import SidebandCore

    from .ui.layouts import root_layout
    from .ui.conversations import Conversations, MsgSync, NewConv
    from .ui.announces import Announces
    from .ui.messages import Messages, ts_format
    from .ui.helpers import ContentNavigationDrawer, DrawerList, IconListItem

    from kivy.config import Config
    Config.set('input', 'mouse', 'mouse,disable_multitouch')

from kivy.metrics import dp, sp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.color_definitions import colors

dark_theme_text_color = "ddd"

if RNS.vendor.platformutils.get_platform() == "android":
    from jnius import autoclass
    from android.runnable import run_on_ui_thread

class SidebandApp(MDApp):
    STARTING = 0x00
    ACTIVE   = 0x01
    PAUSED   = 0x02
    STOPPING = 0x03

    PKGNAME  = "io.unsigned.sideband"

    SERVICE_TIMEOUT = 30

    EINK_BG_STR = "1,0,0,1"
    EINK_BG_ARR = [1,0,0,1]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Sideband"
        self.app_state = SidebandApp.STARTING
        self.android_service = None
        self.app_dir = plyer.storagepath.get_application_dir()
        self.shaders_disabled = __disable_shaders__

        if RNS.vendor.platformutils.get_platform() == "android":
            self.sideband = SidebandCore(self, is_client=True, android_app_dir=self.app_dir, verbose=__debug_build__)
        else:
            self.sideband = SidebandCore(self, is_client=False, verbose=(args.verbose or __debug_build__))

        self.set_ui_theme()

        self.conversations_view = None
        self.sync_dialog = None
        self.settings_ready = False
        self.connectivity_ready = False
        self.hardware_ready = False
        self.repository_ready = False
        self.hardware_rnode_ready = False
        self.hardware_modem_ready = False
        self.hardware_serial_ready = False

        self.final_load_completed = False
        self.service_last_available = 0

        Window.softinput_mode = "below_target"
        self.icon = self.sideband.asset_dir+"/icon.png"
        self.notification_icon = self.sideband.asset_dir+"/notification_icon.png"

        self.connectivity_updater = None


    #################################################
    # Application Startup                           #
    #################################################

    def update_loading_text(self):
        if self.sideband:
            loadingstate = self.sideband.getstate("init.loadingstate")
            if loadingstate:
                self.root.ids.connecting_status.text = loadingstate

    def update_init_status(self, dt):
        self.update_loading_text()
        if not RNS.vendor.platformutils.is_android() or self.sideband.service_available():
            self.service_last_available = time.time()
            self.start_final()
            self.loading_updater.cancel()

    def start_core(self, dt):
        self.loading_updater = Clock.schedule_interval(self.update_init_status, 0.1)

        self.check_permissions()
        self.check_bluetooth_permissions()
        self.start_service()
        
        Clock.schedule_interval(self.jobs, 1.5)

        def dismiss_splash(dt):
            from android import loadingscreen
            loadingscreen.hide_loading_screen()

        if RNS.vendor.platformutils.get_platform() == "android":
            Clock.schedule_once(dismiss_splash, 0)

        self.set_bars_colors()

        self.sideband.setstate("app.loaded", True)
        self.sideband.setstate("app.running", True)
        self.sideband.setstate("app.foreground", True)
        
    def start_service(self):
        if RNS.vendor.platformutils.is_android():
            RNS.log("Running on Android API level "+str(android_api_version))

        RNS.log("Launching platform-specific service for RNS and LXMF")
        if RNS.vendor.platformutils.get_platform() == "android":
            self.android_service = autoclass('io.unsigned.sideband.ServiceSidebandservice')
            mActivity = autoclass('org.kivy.android.PythonActivity').mActivity
            argument = self.app_dir
            self.android_service.start(mActivity, argument)

    def start_final(self):
        # Start local core instance
        self.sideband.start()

        # Pre-load announce stream widgets
        self.update_loading_text()
        self.init_announces_view()
        self.announces_view.update()

        # Wait a little extra for user to react to permissions prompt
        # if RNS.vendor.platformutils.get_platform() == "android":
        #     if self.sideband.first_run:
        #         time.sleep(6)

        if self.sideband.first_run:
            self.guide_action()
            def fp(delta_time):
                self.request_permissions()
            Clock.schedule_once(fp, 3)
        else:
            self.open_conversations()

        self.app_state = SidebandApp.ACTIVE
        self.loading_updater.cancel()
        self.final_load_completed = True

        def check_errors(dt):
            if self.sideband.getpersistent("startup.errors.rnode") != None:
                description = self.sideband.getpersistent("startup.errors.rnode")["description"]
                self.sideband.setpersistent("startup.errors.rnode", None)
                yes_button = MDRectangleFlatButton(
                    text="OK",
                    font_size=dp(18),
                )
                self.hw_error_dialog = MDDialog(
                    title="Hardware Error",
                    text="When starting a connected RNode, Reticulum reported the following error:\n\n[i]"+description+"[/i]",
                    buttons=[ yes_button ],
                    # elevation=0,
                )
                def dl_yes(s):
                    self.hw_error_dialog.dismiss()
                yes_button.bind(on_release=dl_yes)
                self.hw_error_dialog.open()

        Clock.schedule_once(check_errors, 1.5)


    #################################################
    # General helpers                               #
    #################################################

    def set_ui_theme(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.widget_style = "android"
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.accent_palette = "Orange"

        if self.sideband.config["dark_ui"]:
            self.theme_cls.theme_style = "Dark"
        else:
            self.theme_cls.theme_style = "Light"

        self.update_ui_colors()

    def update_ui_colors(self):
        if self.sideband.config["dark_ui"]:
            self.color_reject = colors["DeepOrange"]["900"]
            self.color_accept = colors["LightGreen"]["700"]
        else:
            self.color_reject = colors["DeepOrange"]["800"]
            self.color_accept = colors["LightGreen"]["700"]
        
        self.apply_eink_mods()

    def update_ui_theme(self):
        if self.sideband.config["dark_ui"]:
            self.theme_cls.theme_style = "Dark"
        else:
            self.theme_cls.theme_style = "Light"
            self.apply_eink_mods()

        self.update_ui_colors()

    def apply_eink_mods(self):
        if self.sideband.config["eink_mode"]:
            if self.root != None:
                self.root.md_bg_color = self.theme_cls.bg_light

        else:
            if self.root != None:
                self.root.md_bg_color = self.theme_cls.bg_darkest

    def set_bars_colors(self):
        if RNS.vendor.platformutils.get_platform() == "android":
            set_bars_colors(
                self.theme_cls.primary_color,  # status bar color
                [0,0,0,0],  # navigation bar color
                "Light",                       # icons color of status bar
            )

    def close_any_action(self, sender=None):
        self.open_conversations(direction="right")

    def share_text(self, text):
        if RNS.vendor.platformutils.get_platform() == "android":
            Intent = autoclass('android.content.Intent')
            JString = autoclass('java.lang.String')

            shareIntent = Intent()
            shareIntent.setAction(Intent.ACTION_SEND)
            shareIntent.setType("text/plain")
            shareIntent.putExtra(Intent.EXTRA_TEXT, JString(text))

            mActivity.startActivity(shareIntent)

    def share_image(self, image, filename):
        if RNS.vendor.platformutils.get_platform() == "android":
            save_path = self.sideband.exports_dir
            file_path = save_path+"/"+filename

            try:
                if not os.path.isdir(save_path):
                    RNS.log("Creating directory: "+str(save_path))
                    os.makedirs(save_path)

                Intent = autoclass("android.content.Intent")
                Uri = autoclass("android.net.Uri")
                File = autoclass("java.io.File")
                FileProvider = autoclass("androidx.core.content.FileProvider")

                image.save(file_path)
                i_file = File(file_path)
                image_uri = FileProvider.getUriForFile(mActivity, "io.unsigned.sideband.provider", i_file)

                shareIntent = Intent()
                shareIntent.setAction(Intent.ACTION_SEND)
                shareIntent.setType("image/png")
                shareIntent.putExtra(Intent.EXTRA_STREAM, cast('android.os.Parcelable', image_uri))
                mActivity.startActivity(shareIntent)

            except Exception as e:
                ok_button = MDRectangleFlatButton(text="OK",font_size=dp(18))
                dialog = MDDialog(
                    title="Export Error",
                    text="The QR-code could not be exported and shared:\n\n"+str(e),
                    buttons=[ ok_button ],
                )
                def dl_ok(s):
                    dialog.dismiss()
                
                ok_button.bind(on_release=dl_ok)
                dialog.open()

    def on_pause(self):
        if self.sideband:
            if self.sideband.getstate("flag.focusfix_pause"):
                self.sideband.setstate("flag.focusfix_pause", False)
                return True
            else:
                RNS.log("App pausing...", RNS.LOG_DEBUG)
                self.sideband.setstate("app.running", True)
                self.sideband.setstate("app.foreground", False)
                self.app_state = SidebandApp.PAUSED
                self.sideband.should_persist_data()
                if self.conversations_view != None:
                    self.root.ids.conversations_scrollview.effect_cls = ScrollEffect
                    self.root.ids.conversations_scrollview.scroll = 1

                RNS.log("App paused", RNS.LOG_DEBUG)
                return True
        else:
            return True

    def on_resume(self):
        if self.sideband:
            if self.sideband.getstate("flag.focusfix_resume"):
                self.sideband.setstate("flag.focusfix_resume", False)
                return True
            else:
                RNS.log("App resuming...", RNS.LOG_DEBUG)
                self.sideband.setstate("app.running", True)
                self.sideband.setstate("app.foreground", True)
                self.sideband.setstate("wants.clear_notifications", True)
                self.app_state = SidebandApp.ACTIVE
                if self.conversations_view != None:
                    self.root.ids.conversations_scrollview.effect_cls = ScrollEffect
                    self.root.ids.conversations_scrollview.scroll = 1
                    
                else:
                    RNS.log("Conversations view did not exist", RNS.LOG_DEBUG)

                RNS.log("App resumed", RNS.LOG_DEBUG)

    def on_stop(self):
        RNS.log("App stopping...", RNS.LOG_DEBUG)
        self.sideband.setstate("app.running", False)
        self.sideband.setstate("app.foreground", False)
        self.app_state = SidebandApp.STOPPING
        RNS.log("App stopped", RNS.LOG_DEBUG)

    def is_in_foreground(self):
        if self.app_state == SidebandApp.ACTIVE:
            return True
        else:
            return False

    def check_bluetooth_permissions(self):
        if RNS.vendor.platformutils.get_platform() == "android":
            mActivity = autoclass('org.kivy.android.PythonActivity').mActivity
            Context = autoclass('android.content.Context')
            
            if android_api_version > 30:
                bt_permission_name = "android.permission.BLUETOOTH_CONNECT"
            else:
                bt_permission_name = "android.permission.BLUETOOTH"

            if check_permission(bt_permission_name):
                RNS.log("Have bluetooth connect permissions", RNS.LOG_DEBUG)
                self.sideband.setpersistent("permissions.bluetooth", True)
            else:
                RNS.log("Do not have bluetooth connect permissions")
                self.sideband.setpersistent("permissions.bluetooth", False)
        else:
            self.sideband.setpersistent("permissions.bluetooth", True)

    def check_permissions(self):
        if RNS.vendor.platformutils.get_platform() == "android":
            mActivity = autoclass('org.kivy.android.PythonActivity').mActivity
            Context = autoclass('android.content.Context')
            NotificationManager = autoclass('android.app.NotificationManager')
            notification_service = cast(NotificationManager, mActivity.getSystemService(Context.NOTIFICATION_SERVICE))

            if notification_service.areNotificationsEnabled():
                self.sideband.setpersistent("permissions.notifications", True)
            else:
                if check_permission("android.permission.POST_NOTIFICATIONS"):
                    RNS.log("Have notification permissions", RNS.LOG_DEBUG)
                    self.sideband.setpersistent("permissions.notifications", True)
                else:
                    RNS.log("Do not have notification permissions")
                    self.sideband.setpersistent("permissions.notifications", False)
        else:
            self.sideband.setpersistent("permissions.notifications", True)

    def request_permissions(self):
        self.request_notifications_permission()

    def request_notifications_permission(self):
        if RNS.vendor.platformutils.get_platform() == "android":
            if not check_permission("android.permission.POST_NOTIFICATIONS"):
                RNS.log("Requesting notification permission", RNS.LOG_DEBUG)
                request_permissions(["android.permission.POST_NOTIFICATIONS"])
            
        self.check_permissions()

    def check_storage_permission(self):
        storage_permissions_ok = False
        if android_api_version < 30:
            if check_permission("android.permission.WRITE_EXTERNAL_STORAGE"):
                storage_permissions_ok = True
            else:
                self.request_storage_permission()

        else:
            Environment = autoclass('android.os.Environment')

            if Environment.isExternalStorageManager():
                storage_permissions_ok = True
            else:
                ok_button = MDRectangleFlatButton(text="OK",font_size=dp(18))
                dialog = MDDialog(
                    title="Storage Permission",
                    text="Sideband needs permission to write to external storage to export, share and print paper messages.\n\nOn this Android version, the Manage All Files permission is needed, since normal external storage permission is no longer supported.\n\nSideband will only ever read and write to files in the \"Sideband\" folder of your external storage, and does not read any other data from your system.",
                    buttons=[ ok_button ],
                )
                def dl_ok(s):
                    dialog.dismiss()
                    self.request_storage_permission()
                
                ok_button.bind(on_release=dl_ok)
                dialog.open()

        return storage_permissions_ok

    def request_storage_permission(self):
        if RNS.vendor.platformutils.get_platform() == "android":
            if android_api_version < 30:
                if not check_permission("android.permission.WRITE_EXTERNAL_STORAGE"):
                    RNS.log("Requesting storage write permission", RNS.LOG_DEBUG)
                    request_permissions(["android.permission.WRITE_EXTERNAL_STORAGE"])
                
                if not check_permission("android.permission.READ_EXTERNAL_STORAGE"):
                    RNS.log("Requesting storage read permission", RNS.LOG_DEBUG)
                    request_permissions(["android.permission.READ_EXTERNAL_STORAGE"])
            else:
                Intent = autoclass('android.content.Intent')
                Settings = autoclass('android.provider.Settings')
                pIntent = Intent()
                pIntent.setAction(Settings.ACTION_MANAGE_ALL_FILES_ACCESS_PERMISSION)
                mActivity.startActivity(pIntent)

    def request_bluetooth_permissions(self):
        if RNS.vendor.platformutils.get_platform() == "android":
            if not check_permission("android.permission.BLUETOOTH_CONNECT"):
                RNS.log("Requesting bluetooth permission", RNS.LOG_DEBUG)
                request_permissions(["android.permission.BLUETOOTH_CONNECT"])

        self.check_bluetooth_permissions()

    def on_new_intent(self, intent):
        RNS.log("Received intent", RNS.LOG_DEBUG)
        intent_action = intent.getAction()
        action = None
        data = None

        if intent_action == "android.intent.action.WEB_SEARCH":
            SearchManager = autoclass('android.app.SearchManager')
            data = intent.getStringExtra(SearchManager.QUERY)
            
            if data.lower().startswith(LXMF.LXMessage.URI_SCHEMA):
                action = "lxm_uri"

        if intent_action == "android.intent.action.VIEW":
            data = intent.getData().toString()
            if data.lower().startswith(LXMF.LXMessage.URI_SCHEMA):
                action = "lxm_uri"

        if action != None:
            self.handle_action(action, data)

    def handle_action(self, action, data):
        if action == "lxm_uri":
            self.ingest_lxm_uri(data)

    def ingest_lxm_uri(self, lxm_uri):
        RNS.log("Ingesting LXMF paper message from URI: "+str(lxm_uri), RNS.LOG_DEBUG)
        self.sideband.lxm_ingest_uri(lxm_uri)
        
    def build(self):
        FONT_PATH = self.sideband.asset_dir+"/fonts"
        if RNS.vendor.platformutils.is_darwin():
            self.icon = self.sideband.asset_dir+"/icon_macos_formed.png"
        else:
            self.icon = self.sideband.asset_dir+"/icon.png"

        self.announces_view = None

        if RNS.vendor.platformutils.is_android():
            ActivityInfo = autoclass('android.content.pm.ActivityInfo')
            activity = autoclass('org.kivy.android.PythonActivity').mActivity
            activity.setRequestedOrientation(ActivityInfo.SCREEN_ORIENTATION_UNSPECIFIED)

            from android import activity as a_activity
            a_activity.bind(on_new_intent=self.on_new_intent)

        if self.sideband.config["eink_mode"] == True:
            screen = Builder.load_string(root_layout.replace("app.theme_cls.bg_darkest", "app.theme_cls.bg_light"))
        else:
            screen = Builder.load_string(root_layout)

        return screen

    def jobs(self, delta_time):
        if self.final_load_completed:
            if RNS.vendor.platformutils.is_android() and not self.sideband.service_available():
                if time.time() - self.service_last_available > SidebandApp.SERVICE_TIMEOUT:
                    if self.app_state == SidebandApp.ACTIVE:
                        info_text = "The Reticulum and LXMF service seem to have disappeared, and Sideband is no longer connected. This should not happen, and probably indicates a bug in the background service. Please restart Sideband to regain connectivity."
                        ok_button = MDRectangleFlatButton(text="OK",font_size=dp(18))
                        dialog = MDDialog(
                            title="Error",
                            text=info_text,
                            buttons=[ ok_button ],
                            # elevation=0,
                        )
                        def dl_ok(s):
                            dialog.dismiss()
                            self.quit_action(s)
                        
                        ok_button.bind(on_release=dl_ok)
                        self.final_load_completed = False
                        dialog.open()

                    else:
                        self.quit_action(s)

            else:
                self.service_last_available = time.time()


        if self.root.ids.screen_manager.current == "messages_screen":
            self.messages_view.update()

            if not self.root.ids.messages_scrollview.dest_known:
                self.message_area_detect()

        elif self.root.ids.screen_manager.current == "conversations_screen":
            if self.sideband.getstate("app.flags.unread_conversations", allow_cache=True):
                if self.conversations_view != None:
                    self.conversations_view.update()

            if self.sideband.getstate("app.flags.lxmf_sync_dialog_open", allow_cache=True) and self.sync_dialog != None:
                self.sync_dialog.ids.sync_progress.value = self.sideband.get_sync_progress()*100
                self.sync_dialog.ids.sync_status.text = self.sideband.get_sync_status()

                state = self.sideband.message_router.propagation_transfer_state
                if state > LXMF.LXMRouter.PR_IDLE and state < LXMF.LXMRouter.PR_COMPLETE:
                    self.widget_hide(self.sync_dialog.stop_button, False)
                else:
                    self.widget_hide(self.sync_dialog.stop_button, True)

        elif self.root.ids.screen_manager.current == "announces_screen":
            if self.sideband.getstate("app.flags.new_announces", allow_cache=True):
                if self.announces_view != None:
                    self.announces_view.update()

        if self.sideband.getstate("app.flags.new_conversations", allow_cache=True):
            if self.conversations_view != None:
                self.conversations_view.update()

        if self.sideband.getstate("wants.viewupdate.conversations", allow_cache=True):
            if self.conversations_view != None:
                self.conversations_view.update()

        if self.sideband.getstate("lxm_uri_ingest.result", allow_cache=True):
            info_text = self.sideband.getstate("lxm_uri_ingest.result", allow_cache=True)
            self.sideband.setstate("lxm_uri_ingest.result", False)
            ok_button = MDRectangleFlatButton(text="OK",font_size=dp(18))
            dialog = MDDialog(
                title="Message Scan",
                text=info_text,
                buttons=[ ok_button ],
                # elevation=0,
            )
            def dl_ok(s):
                dialog.dismiss()
            
            ok_button.bind(on_release=dl_ok)
            dialog.open()

        if self.sideband.getstate("hardware_operation.error", allow_cache=True):
            info_text = self.sideband.getstate("hardware_operation.error", allow_cache=True)
            self.sideband.setstate("hardware_operation.error", False)
            ok_button = MDRectangleFlatButton(text="OK",font_size=dp(18))
            dialog = MDDialog(
                title="Error",
                text=info_text,
                buttons=[ ok_button ],
                # elevation=0,
            )
            def dl_ok(s):
                dialog.dismiss()
            
            ok_button.bind(on_release=dl_ok)
            dialog.open()

    def on_start(self):
        self.last_exit_event = time.time()
        self.root.ids.screen_manager.transition.duration = 0.25
        self.root.ids.screen_manager.transition.bind(on_complete=self.screen_transition_complete)

        EventLoop.window.bind(on_keyboard=self.keyboard_event)
        EventLoop.window.bind(on_key_down=self.keydown_event)
        
        # This incredibly hacky hack circumvents a bug in SDL2
        # that prevents focus from being correctly released from
        # the software keyboard on Android. Without this the back
        # button/gesture does not work after the soft-keyboard has
        # appeared for the first time.
        if RNS.vendor.platformutils.is_android():
            BIND_CLASSES = ["kivymd.uix.textfield.textfield.MDTextField",]
            
            for e in self.root.ids:
                te = self.root.ids[e]
                ts = str(te).split(" ")[0].replace("<", "")

                if ts in BIND_CLASSES:
                    te.bind(focus=self.android_focus_fix)

        self.root.ids.screen_manager.app = self
        self.root.ids.app_version_info.text = "Sideband v"+__version__+" "+__variant__
        self.root.ids.nav_scrollview.effect_cls = ScrollEffect
        Clock.schedule_once(self.start_core, 3.5)
    
    # Part of the focus hack fix
    def android_focus_fix(self, sender, val):
        if not val:
            @run_on_ui_thread
            def fix_back_button():
                self.sideband.setstate("flag.focusfix_pause", True)
                self.sideband.setstate("flag.focusfix_resume", True)
                activity = autoclass('org.kivy.android.PythonActivity').mActivity
                activity.onWindowFocusChanged(False)
                activity.onWindowFocusChanged(True)

            fix_back_button()

    def keydown_event(self, instance, keyboard, keycode, text, modifiers):
        if len(modifiers) > 0 and modifiers[0] == 'ctrl' and (text == "q"):
            self.quit_action(self)
        if len(modifiers) > 0 and modifiers[0] == 'ctrl' and (text == "w"):
            if self.root.ids.screen_manager.current == "conversations_screen":
                self.quit_action(self)
            else:
                self.open_conversations()
        if len(modifiers) > 0 and modifiers[0] == 'ctrl' and (text == "s" or text == "d"):
            if self.root.ids.screen_manager.current == "messages_screen":
                self.message_send_action()
        if len(modifiers) > 0 and modifiers[0] == 'ctrl' and (text == "l"):
            self.announces_action(self)
        if len(modifiers) > 0 and modifiers[0] == 'ctrl' and (text == "r"):
            self.conversations_action(self)
        if len(modifiers) > 0 and modifiers[0] == 'ctrl' and (text == "g"):
            self.guide_action(self)
        if len(modifiers) > 0 and modifiers[0] == 'ctrl' and (text == "n"):
            if self.root.ids.screen_manager.current == "conversations_screen":
                if not hasattr(self, "dialog_open") or not self.dialog_open:
                    self.new_conversation_action(self)
            
    def keyboard_event(self, window, key, *largs):
        # Handle escape/back
        if key == 27:
            if self.root.ids.screen_manager.current == "conversations_screen":
                if time.time() - self.last_exit_event < 2:
                    self.quit_action(self)
                else:
                    self.last_exit_event = time.time()

            else:
                if self.root.ids.screen_manager.current == "hardware_rnode_screen":
                    self.close_sub_hardware_action()
                elif self.root.ids.screen_manager.current == "hardware_modem_screen":
                    self.close_sub_hardware_action()
                elif self.root.ids.screen_manager.current == "hardware_serial_screen":
                    self.close_sub_hardware_action()
                else:
                    self.open_conversations(direction="right")

            return True

    def widget_hide(self, w, hide=True):
        if hasattr(w, "saved_attrs"):
            if not hide:
                w.height, w.size_hint_y, w.opacity, w.disabled = w.saved_attrs
                del w.saved_attrs
        elif hide:
            w.saved_attrs = w.height, w.size_hint_y, w.opacity, w.disabled
            w.height, w.size_hint_y, w.opacity, w.disabled = 0, None, 0, True

    def quit_action(self, sender):
        self.root.ids.nav_drawer.set_state("closed")
        self.sideband.should_persist_data()

        self.root.ids.screen_manager.transition = NoTransition()
        self.root.ids.screen_manager.current = "exit_screen"
        self.sideband.setstate("app.displaying", self.root.ids.screen_manager.current)

        self.sideband.setstate("app.running", False)
        self.sideband.setstate("app.foreground", False)

        def final_exit(dt):
            RNS.log("Stopping service...")
            self.sideband.setstate("wants.service_stop", True)
            while self.sideband.service_available():
                time.sleep(0.2)
            RNS.log("Service stopped")

            if RNS.vendor.platformutils.is_android():
                RNS.log("Finishing activity")
                activity = autoclass('org.kivy.android.PythonActivity').mActivity
                activity.finishAndRemoveTask()
            else:
                RNS.exit()
                MDApp.get_running_app().stop()
                Window.close()

        Clock.schedule_once(final_exit, 0.85)

    def announce_now_action(self, sender=None):
        self.sideband.lxmf_announce()

        yes_button = MDRectangleFlatButton(text="OK",font_size=dp(18))

        dialog = MDDialog(
            title="Announce Sent",
            text="Your LXMF address has been announced on all available interfaces",
            buttons=[ yes_button ],
            # elevation=0,
        )
        def dl_yes(s):
            dialog.dismiss()
        
        yes_button.bind(on_release=dl_yes)
        dialog.open()


    #################################################
    # Screens                                       #
    #################################################

    ### Messages (conversation) screen
    ######################################
    def conversation_from_announce_action(self, context_dest):
        if self.sideband.has_conversation(context_dest):
            pass
        else:
            self.sideband.create_conversation(context_dest)
            self.sideband.setstate("app.flags.new_conversations", True)

        self.open_conversation(context_dest)

    def conversation_action(self, sender):
        def cb(dt):
            self.open_conversation(sender.sb_uid)
        def cbu(dt):
            self.conversations_view.update()
        Clock.schedule_once(cb, 0.15)
        Clock.schedule_once(cbu, 0.15+0.25)

    def open_conversation(self, context_dest):
        self.outbound_mode_paper = False
        if self.sideband.config["propagation_by_default"]:
            self.outbound_mode_propagation = True
        else:
            self.outbound_mode_propagation = False

        self.root.ids.screen_manager.transition.direction = "left"
        self.messages_view = Messages(self, context_dest)

        self.root.ids.messages_scrollview.effect_cls = ScrollEffect
        for child in self.root.ids.messages_scrollview.children:
            self.root.ids.messages_scrollview.remove_widget(child)

        list_widget = self.messages_view.get_widget()

        self.root.ids.messages_scrollview.add_widget(list_widget)
        self.root.ids.messages_scrollview.scroll_y = 0.0

        self.root.ids.messages_toolbar.title = self.sideband.peer_display_name(context_dest)
        self.root.ids.messages_scrollview.active_conversation = context_dest
        self.sideband.setstate("app.active_conversation", context_dest)

        self.root.ids.nokeys_text.text = ""
        self.message_area_detect()
        self.update_message_widgets()
        self.root.ids.message_text.disabled = False


        self.root.ids.screen_manager.current = "messages_screen"
        self.sideband.setstate("app.displaying", self.root.ids.screen_manager.current)
    
        self.sideband.read_conversation(context_dest)
        self.sideband.setstate("app.flags.unread_conversations", True)

        def scb(dt):
            self.root.ids.messages_scrollview.scroll_y = 0.0
        Clock.schedule_once(scb, 0.33)

    def close_messages_action(self, sender=None):
        self.open_conversations(direction="right")

    def message_send_action(self, sender=None):
        if self.root.ids.message_text.text == "":
            return

        def cb(dt):
            self.message_send_dispatch(sender)
        Clock.schedule_once(cb, 0.20)

    def message_send_dispatch(self, sender=None):
        self.root.ids.message_send_button.disabled = True
        if self.root.ids.screen_manager.current == "messages_screen":
            if self.outbound_mode_propagation and self.sideband.message_router.get_outbound_propagation_node() == None:
                self.messages_view.send_error_dialog = MDDialog(
                    title="Error",
                    text="Propagated delivery was requested, but no active LXMF propagation nodes were found. Cannot send message.\n\nWait for a Propagation Node to announce on the network, or manually specify one in the settings.",
                    buttons=[
                        MDRectangleFlatButton(
                            text="OK",
                            font_size=dp(18),
                            on_release=self.messages_view.close_send_error_dialog
                        )
                    ],
                    # elevation=0,
                )
                self.messages_view.send_error_dialog.open()

            else:
                msg_content = self.root.ids.message_text.text
                context_dest = self.root.ids.messages_scrollview.active_conversation
                if self.outbound_mode_paper:
                    if self.sideband.paper_message(msg_content, context_dest):
                        self.root.ids.message_text.text = ""
                        self.root.ids.messages_scrollview.scroll_y = 0
                        self.jobs(0)
                
                elif self.sideband.send_message(msg_content, context_dest, self.outbound_mode_propagation):
                    self.root.ids.message_text.text = ""
                    self.root.ids.messages_scrollview.scroll_y = 0
                    self.jobs(0)

                else:
                    self.messages_view.send_error_dialog = MDDialog(
                        title="Error",
                        text="Could not send the message",
                        buttons=[
                            MDRectangleFlatButton(
                                text="OK",
                                font_size=dp(18),
                                on_release=self.messages_view.close_send_error_dialog
                            )
                        ],
                        # elevation=0,
                    )
                    self.messages_view.send_error_dialog.open()
        
        def cb(dt):
            self.root.ids.message_send_button.disabled = False
        Clock.schedule_once(cb, 0.5)

    def message_propagation_action(self, sender):
        if self.outbound_mode_paper:
            self.outbound_mode_paper = False
            self.outbound_mode_propagation = False
        else:
            if self.outbound_mode_propagation:
                self.outbound_mode_paper = True
                self.outbound_mode_propagation = False
            else:
                self.outbound_mode_propagation = True
                self.outbound_mode_paper = False

        self.update_message_widgets()

    def update_message_widgets(self):
        toolbar_items = self.root.ids.messages_toolbar.ids.right_actions.children
        mode_item = toolbar_items[1]

        if self.outbound_mode_paper:
            mode_item.icon = "qrcode"
            self.root.ids.message_text.hint_text = "Paper message"
        else:
            if not self.outbound_mode_propagation:
                mode_item.icon = "lan-connect"
                self.root.ids.message_text.hint_text = "Message for direct delivery"
            else:
                mode_item.icon = "upload-network"
                self.root.ids.message_text.hint_text = "Message for propagation"
                # self.root.ids.message_text.hint_text = "Write message for delivery via propagation nodes"
    
    def key_query_action(self, sender):
        context_dest = self.root.ids.messages_scrollview.active_conversation
        if self.sideband.request_key(context_dest):
            keys_str = "Public key information for "+RNS.prettyhexrep(context_dest)+" was requested from the network. Waiting for request to be answered."
            self.root.ids.nokeys_text.text = keys_str
        else:
            keys_str = "Could not send request. Check your connectivity and addresses."
            self.root.ids.nokeys_text.text = keys_str

    def message_area_detect(self):
        context_dest = self.root.ids.messages_scrollview.active_conversation
        if self.sideband.is_known(context_dest):
            self.root.ids.messages_scrollview.dest_known = True
            self.widget_hide(self.root.ids.message_input_part, False)
            self.widget_hide(self.root.ids.no_keys_part, True)
        else:
            self.root.ids.messages_scrollview.dest_known = False
            if self.root.ids.nokeys_text.text == "":
                keys_str = "The crytographic keys for the destination address are unknown at this time. You can wait for an announce to arrive, or query the network for the necessary keys."
                self.root.ids.nokeys_text.text = keys_str
            self.widget_hide(self.root.ids.message_input_part, True)
            self.widget_hide(self.root.ids.no_keys_part, False)


    ### Conversations screen
    ######################################       
    def conversations_action(self, sender=None):
        self.open_conversations()

    def open_conversations(self, direction="left"):
        self.root.ids.screen_manager.transition.direction = direction
        self.root.ids.nav_drawer.set_state("closed")
        
        if not self.conversations_view:
            self.conversations_view = Conversations(self)

            for child in self.root.ids.conversations_scrollview.children:
                self.root.ids.conversations_scrollview.remove_widget(child)

            self.root.ids.conversations_scrollview.effect_cls = ScrollEffect
            self.root.ids.conversations_scrollview.add_widget(self.conversations_view.get_widget())

        self.root.ids.screen_manager.current = "conversations_screen"
        self.root.ids.messages_scrollview.active_conversation = None

        def cb(dt):
            self.sideband.setstate("app.displaying", self.root.ids.screen_manager.current)
            self.sideband.setstate("wants.clear_notifications", True)
        Clock.schedule_once(cb, 0.10)

    def get_connectivity_text(self):
        connectivity_status = ""
        if RNS.vendor.platformutils.get_platform() == "android":
            connectivity_status = self.sideband.getstate("service.connectivity_status")

        else:
            if self.sideband.reticulum.is_connected_to_shared_instance:
                connectivity_status = "Sideband is connected via a shared Reticulum instance running on this system. Use the rnstatus utility to obtain full connectivity info."
            else:
                connectivity_status = "Sideband is currently running a standalone or master Reticulum instance on this system. Use the rnstatus utility to obtain full connectivity info."

        return connectivity_status
    
    def connectivity_status(self, sender):
        hs = dp(22)

        yes_button = MDRectangleFlatButton(text="OK",font_size=dp(18))
        dialog = MDDialog(
            title="Connectivity Status",
            text=self.get_connectivity_text(),
            buttons=[ yes_button ],
            # elevation=0,
        )
        def cs_updater(dt):
            dialog.text = self.get_connectivity_text()
        def dl_yes(s):
            self.connectivity_updater.cancel()
            dialog.dismiss()
            if self.connectivity_updater != None:
                self.connectivity_updater.cancel()

        yes_button.bind(on_release=dl_yes)
        dialog.open()

        if self.connectivity_updater != None:
            self.connectivity_updater.cancel()

        self.connectivity_updater = Clock.schedule_interval(cs_updater, 2.0)

    def ingest_lxm_action(self, sender):
        def cb(dt):
            self.open_ingest_lxm_dialog(sender)
        Clock.schedule_once(cb, 0.15)

    def open_ingest_lxm_dialog(self, sender=None):
        try:
            cancel_button = MDRectangleFlatButton(text="Cancel",font_size=dp(18))
            ingest_button = MDRectangleFlatButton(text="Read LXM",font_size=dp(18), theme_text_color="Custom", line_color=self.color_accept, text_color=self.color_accept)
            
            dialog = MDDialog(
                title="Ingest Paper Message",
                text="You can read LXMF paper messages into this program by scanning a QR-code containing the message with your device camera or QR-scanner app, and then opening the resulting link in Sideband.\n\nAlternatively, you can copy an [b]lxm://[/b] link from any source to your clipboard, and ingest it using the [i]Read LXM[/i] button below.",
                buttons=[ ingest_button, cancel_button ],
            )
            def dl_yes(s):
                try:
                    lxm_uri = Clipboard.paste()
                    if not lxm_uri.lower().startswith(LXMF.LXMessage.URI_SCHEMA+"://"):
                        lxm_uri = LXMF.LXMessage.URI_SCHEMA+"://"+lxm_uri

                    self.ingest_lxm_uri(lxm_uri)
                    dialog.dismiss()

                except Exception as e:
                    response = "Error ingesting message from URI: "+str(e)
                    RNS.log(response, RNS.LOG_ERROR)
                    self.sideband.setstate("lxm_uri_ingest.result", response)
                    dialog.dismiss()

            def dl_no(s):
                dialog.dismiss()

            def dl_ds(s):
                self.dialog_open = False

            ingest_button.bind(on_release=dl_yes)
            cancel_button.bind(on_release=dl_no)

            dialog.bind(on_dismiss=dl_ds)
            dialog.open()
            self.dialog_open = True

        except Exception as e:
            RNS.log("Error while creating ingest LXM dialog: "+str(e), RNS.LOG_ERROR)

    def lxmf_sync_action(self, sender):
        def cb(dt):
            self.lxmf_sync_request(sender)
        Clock.schedule_once(cb, 0.15)

    def lxmf_sync_request(self, sender):
        if self.sideband.message_router.get_outbound_propagation_node() == None:
            yes_button = MDRectangleFlatButton(text="OK",font_size=dp(18))

            dialog = MDDialog(
                title="Can't Sync",
                text="No active LXMF propagation nodes were found. Cannot fetch messages. Wait for a Propagation Node to announce on the network, or manually specify one in the settings.",
                buttons=[ yes_button ],
                # elevation=0,
            )
            def dl_yes(s):
                dialog.dismiss()
            
            yes_button.bind(on_release=dl_yes)
            dialog.open()
        else:
            if self.sideband.config["lxmf_sync_limit"]:
                sl = self.sideband.config["lxmf_sync_max"]
            else:
                sl = None

            self.sideband.setpersistent("lxmf.lastsync", time.time())
            self.sideband.setpersistent("lxmf.syncretrying", False)
            self.sideband.request_lxmf_sync(limit=sl)

            close_button = MDRectangleFlatButton(text="Close",font_size=dp(18))
            stop_button = MDRectangleFlatButton(text="Stop",font_size=dp(18), theme_text_color="Custom", line_color=self.color_reject, text_color=self.color_reject)
            dialog_content = MsgSync()
            dialog = MDDialog(
                title="LXMF Sync via "+RNS.prettyhexrep(self.sideband.message_router.get_outbound_propagation_node()),
                type="custom",
                content_cls=dialog_content,
                buttons=[ stop_button, close_button ],
                # elevation=0,
            )
            dialog.d_content = dialog_content
            def dl_close(s):                
                self.sideband.setstate("app.flags.lxmf_sync_dialog_open", False)
                dialog.dismiss()
                # self.sideband.cancel_lxmf_sync()

            def dl_stop(s):                
                # self.sideband.setstate("app.flags.lxmf_sync_dialog_open", False)
                # dialog.dismiss()
                self.sideband.cancel_lxmf_sync()
                def cb(dt):
                    self.widget_hide(self.sync_dialog.stop_button, True)
                Clock.schedule_once(cb, 0.25)

            close_button.bind(on_release=dl_close)
            stop_button.bind(on_release=dl_stop)
            self.sideband.setstate("app.flags.lxmf_sync_dialog_open", True)
            self.sync_dialog = dialog_content
            self.sync_dialog.stop_button = stop_button
            dialog.open()
            dialog_content.ids.sync_progress.value = self.sideband.get_sync_progress()*100
            dialog_content.ids.sync_status.text = self.sideband.get_sync_status()

    def new_conversation_action(self, sender=None):
        def cb(dt):
            self.new_conversation_request(sender)
        Clock.schedule_once(cb, 0.15)

    def new_conversation_request(self, sender=None):
        try:
            cancel_button = MDRectangleFlatButton(text="Cancel",font_size=dp(18))
            create_button = MDRectangleFlatButton(text="Create",font_size=dp(18), theme_text_color="Custom", line_color=self.color_accept, text_color=self.color_accept)
            
            dialog_content = NewConv()
            dialog = MDDialog(
                title="New Conversation",
                type="custom",
                content_cls=dialog_content,
                buttons=[ create_button, cancel_button ],
                # elevation=0,
            )
            dialog.d_content = dialog_content
            def dl_yes(s):
                new_result = False
                try:
                    n_address = dialog.d_content.ids["n_address_field"].text
                    n_name = dialog.d_content.ids["n_name_field"].text
                    n_trusted = dialog.d_content.ids["n_trusted"].active
                    new_result = self.sideband.new_conversation(n_address, n_name, n_trusted)

                except Exception as e:
                    RNS.log("Error while creating conversation: "+str(e), RNS.LOG_ERROR)

                if new_result:
                    dialog.d_content.ids["n_address_field"].error = False
                    dialog.dismiss()
                    if self.conversations_view != None:
                        self.conversations_view.update()
                else:
                    dialog.d_content.ids["n_address_field"].error = True
                    # dialog.d_content.ids["n_error_field"].text = "Could not create conversation. Check your input."

            def dl_no(s):
                dialog.dismiss()

            def dl_ds(s):
                self.dialog_open = False

            create_button.bind(on_release=dl_yes)
            cancel_button.bind(on_release=dl_no)

            dialog.bind(on_dismiss=dl_ds)
            dialog.open()
            self.dialog_open = True

        except Exception as e:
            RNS.log("Error while creating new conversation dialog: "+str(e), RNS.LOG_ERROR)

    ### Information/version screen
    ######################################
    def information_action(self, sender=None):
        def link_exec(sender=None, event=None):
            import webbrowser
            webbrowser.open("https://unsigned.io/donate")

        self.root.ids.information_scrollview.effect_cls = ScrollEffect
        self.root.ids.information_logo.icon = self.sideband.asset_dir+"/rns_256.png"

        info = "This is Sideband v"+__version__+" "+__variant__+", on RNS v"+RNS.__version__+" and LXMF v"+LXMF.__version__+".\n\nHumbly build using the following open components:\n\n - [b]Reticulum[/b] (MIT License)\n - [b]LXMF[/b] (MIT License)\n - [b]KivyMD[/b] (MIT License)\n - [b]Kivy[/b] (MIT License)\n - [b]Python[/b] (PSF License)"+"\n\nGo to [u][ref=link]https://unsigned.io/donate[/ref][/u] to support the project.\n\nThe Sideband app is Copyright (c) 2022 Mark Qvist / unsigned.io\n\nPermission is granted to freely share and distribute binary copies of Sideband v"+__version__+" "+__variant__+", so long as no payment or compensation is charged for said distribution or sharing.\n\nIf you were charged or paid anything for this copy of Sideband, please report it to [b]license@unsigned.io[/b].\n\nTHIS IS EXPERIMENTAL SOFTWARE - USE AT YOUR OWN RISK AND RESPONSIBILITY"
        self.root.ids.information_info.text = info
        self.root.ids.information_info.bind(on_ref_press=link_exec)
        self.root.ids.screen_manager.transition.direction = "left"
        self.root.ids.screen_manager.current = "information_screen"
        self.root.ids.nav_drawer.set_state("closed")
        self.sideband.setstate("app.displaying", self.root.ids.screen_manager.current)

    def close_information_action(self, sender=None):
        self.open_conversations(direction="right")


    ### Settings screen
    ######################################
    def settings_action(self, sender=None):
        self.settings_init()
        self.root.ids.screen_manager.transition.direction = "left"
        self.root.ids.nav_drawer.set_state("closed")
        if self.sideband.active_propagation_node != None:
            self.root.ids.settings_propagation_node_address.text = RNS.hexrep(self.sideband.active_propagation_node, delimit=False)
        self.root.ids.screen_manager.current = "settings_screen"
        self.sideband.setstate("app.displaying", self.root.ids.screen_manager.current)

    def settings_init(self, sender=None):
        if not self.settings_ready:
            self.root.ids.settings_scrollview.effect_cls = ScrollEffect

            def save_disp_name(sender=None, event=None):
                if not sender.focus:
                    in_name = self.root.ids.settings_display_name.text
                    if in_name == "":
                        new_name = "Anonymous Peer"
                    else:
                        new_name = in_name

                    self.sideband.config["display_name"] = new_name
                    self.sideband.save_configuration()

            def save_prop_addr(sender=None, event=None):
                if not sender.focus:
                    in_addr = self.root.ids.settings_propagation_node_address.text

                    new_addr = None
                    if in_addr == "":
                        new_addr = None
                        self.root.ids.settings_propagation_node_address.error = False
                    else:
                        if len(in_addr) != RNS.Reticulum.TRUNCATED_HASHLENGTH//8*2:
                            new_addr = None
                        else:
                            try:
                                new_addr = bytes.fromhex(in_addr)
                            except Exception as e:
                                new_addr = None

                        if new_addr == None:
                            self.root.ids.settings_propagation_node_address.error = True
                        else:
                            self.root.ids.settings_propagation_node_address.error = False


                    self.sideband.config["lxmf_propagation_node"] = new_addr
                    self.sideband.set_active_propagation_node(self.sideband.config["lxmf_propagation_node"])

            def save_dark_ui(sender=None, event=None):
                self.sideband.config["dark_ui"] = self.root.ids.settings_dark_ui.active
                self.sideband.save_configuration()
                self.update_ui_theme()

            def save_eink_mode(sender=None, event=None):
                self.sideband.config["eink_mode"] = self.root.ids.settings_eink_mode.active
                self.sideband.save_configuration()
                self.update_ui_theme()

            def save_notifications_on(sender=None, event=None):
                self.sideband.config["notifications_on"] = self.root.ids.settings_notifications_on.active
                self.sideband.save_configuration()

            def save_start_announce(sender=None, event=None):
                self.sideband.config["start_announce"] = self.root.ids.settings_start_announce.active
                self.sideband.save_configuration()

            def save_lxmf_delivery_by_default(sender=None, event=None):
                self.sideband.config["propagation_by_default"] = self.root.ids.settings_lxmf_delivery_by_default.active
                self.sideband.save_configuration()

            def save_lxmf_ignore_unknown(sender=None, event=None):
                self.sideband.config["lxmf_ignore_unknown"] = self.root.ids.settings_lxmf_ignore_unknown.active
                self.sideband.save_configuration()

            def save_lxmf_sync_limit(sender=None, event=None):
                self.sideband.config["lxmf_sync_limit"] = self.root.ids.settings_lxmf_sync_limit.active
                self.sideband.save_configuration()

            def save_debug(sender=None, event=None):
                self.sideband.config["debug"] = self.root.ids.settings_debug.active
                self.sideband.save_configuration()

            def save_print_command(sender=None, event=None):
                if not sender.focus:
                    in_cmd = self.root.ids.settings_print_command.text
                    if in_cmd == "":
                        new_cmd = "lp"
                    else:
                        new_cmd = in_cmd

                    self.sideband.config["print_command"] = new_cmd.strip()
                    self.root.ids.settings_print_command.text = self.sideband.config["print_command"]
                    self.sideband.save_configuration()

            def save_lxmf_periodic_sync(sender=None, event=None, save=True):
                if self.root.ids.settings_lxmf_periodic_sync.active:
                    self.widget_hide(self.root.ids.lxmf_syncslider_container, False)
                else:
                    self.widget_hide(self.root.ids.lxmf_syncslider_container, True)

                if save:
                    self.sideband.config["lxmf_periodic_sync"] = self.root.ids.settings_lxmf_periodic_sync.active
                    self.sideband.save_configuration()

            def sync_interval_change(sender=None, event=None, save=True):
                interval = (self.root.ids.settings_lxmf_sync_interval.value//300)*300
                interval_text = RNS.prettytime(interval)
                pre = self.root.ids.settings_lxmf_sync_periodic.text
                self.root.ids.settings_lxmf_sync_periodic.text = "Auto sync every "+interval_text
                if save:
                    self.sideband.config["lxmf_sync_interval"] = interval
                    self.sideband.save_configuration()

            self.root.ids.settings_lxmf_address.text = RNS.hexrep(self.sideband.lxmf_destination.hash, delimit=False)
            self.root.ids.settings_identity_hash.text = RNS.hexrep(self.sideband.lxmf_destination.identity.hash, delimit=False)

            self.root.ids.settings_display_name.text = self.sideband.config["display_name"]
            self.root.ids.settings_display_name.bind(focus=save_disp_name)

            if RNS.vendor.platformutils.is_android():
                self.widget_hide(self.root.ids.settings_print_command, True)
            else:
                self.root.ids.settings_print_command.text = self.sideband.config["print_command"]
                self.root.ids.settings_print_command.bind(focus=save_print_command)

            if self.sideband.config["lxmf_propagation_node"] == None:
                prop_node_addr = ""
            else:
                prop_node_addr = RNS.hexrep(self.sideband.config["lxmf_propagation_node"], delimit=False)

            self.root.ids.settings_propagation_node_address.text = prop_node_addr
            self.root.ids.settings_propagation_node_address.bind(focus=save_prop_addr)

            if not RNS.vendor.platformutils.is_android() or android_api_version >= 26:
                self.root.ids.settings_notifications_on.active = self.sideband.config["notifications_on"]
                self.root.ids.settings_notifications_on.bind(active=save_notifications_on)
            else:
                self.root.ids.settings_notifications_on.active = False
                self.root.ids.settings_notifications_on.disabled = True

            self.root.ids.settings_dark_ui.active = self.sideband.config["dark_ui"]
            self.root.ids.settings_dark_ui.bind(active=save_dark_ui)

            self.root.ids.settings_eink_mode.active = self.sideband.config["eink_mode"]
            self.root.ids.settings_eink_mode.bind(active=save_eink_mode)

            self.root.ids.settings_start_announce.active = self.sideband.config["start_announce"]
            self.root.ids.settings_start_announce.bind(active=save_start_announce)

            self.root.ids.settings_lxmf_delivery_by_default.active = self.sideband.config["propagation_by_default"]
            self.root.ids.settings_lxmf_delivery_by_default.bind(active=save_lxmf_delivery_by_default)

            self.root.ids.settings_lxmf_ignore_unknown.active = self.sideband.config["lxmf_ignore_unknown"]
            self.root.ids.settings_lxmf_ignore_unknown.bind(active=save_lxmf_ignore_unknown)

            self.root.ids.settings_lxmf_periodic_sync.active = self.sideband.config["lxmf_periodic_sync"]
            self.root.ids.settings_lxmf_periodic_sync.bind(active=save_lxmf_periodic_sync)
            save_lxmf_periodic_sync(save=False)

            def sync_interval_change_cb(sender=None, event=None):
                sync_interval_change(sender=sender, event=event, save=False)
            self.root.ids.settings_lxmf_sync_interval.bind(value=sync_interval_change_cb)
            self.root.ids.settings_lxmf_sync_interval.bind(on_touch_up=sync_interval_change)
            self.root.ids.settings_lxmf_sync_interval.value = self.sideband.config["lxmf_sync_interval"]
            sync_interval_change(save=False)

            if self.sideband.config["lxmf_sync_limit"] == None or self.sideband.config["lxmf_sync_limit"] == False:
                sync_limit = False
            else:
                sync_limit = True

            self.root.ids.settings_lxmf_sync_limit.active = sync_limit
            self.root.ids.settings_lxmf_sync_limit.bind(active=save_lxmf_sync_limit)

            self.root.ids.settings_debug.active = self.sideband.config["debug"]
            self.root.ids.settings_debug.bind(active=save_debug)

            self.settings_ready = True

    def close_settings_action(self, sender=None):
        self.open_conversations(direction="right")


    ### Connectivity screen
    ######################################
    def connectivity_action(self, sender=None):
        self.root.ids.screen_manager.transition.direction = "left"
        self.root.ids.nav_drawer.set_state("closed")
        self.connectivity_init()
        self.root.ids.screen_manager.current = "connectivity_screen"
        self.sideband.setstate("app.displaying", self.root.ids.screen_manager.current)

    def connectivity_init(self, sender=None):
        if not self.connectivity_ready:
            self.root.ids.connectivity_scrollview.effect_cls = ScrollEffect
            def con_hide_settings():
                self.widget_hide(self.root.ids.connectivity_use_local)
                self.widget_hide(self.root.ids.connectivity_local_groupid)
                self.widget_hide(self.root.ids.connectivity_local_ifac_netname)
                self.widget_hide(self.root.ids.connectivity_local_ifac_passphrase)
                self.widget_hide(self.root.ids.connectivity_use_tcp)
                self.widget_hide(self.root.ids.connectivity_tcp_host)
                self.widget_hide(self.root.ids.connectivity_tcp_port)
                self.widget_hide(self.root.ids.connectivity_tcp_ifac_netname)
                self.widget_hide(self.root.ids.connectivity_tcp_ifac_passphrase)
                self.widget_hide(self.root.ids.connectivity_use_i2p)
                self.widget_hide(self.root.ids.connectivity_i2p_b32)
                self.widget_hide(self.root.ids.connectivity_i2p_ifac_netname)
                self.widget_hide(self.root.ids.connectivity_i2p_ifac_passphrase)
                self.widget_hide(self.root.ids.connectivity_tcp_label)
                self.widget_hide(self.root.ids.connectivity_local_label)
                self.widget_hide(self.root.ids.connectivity_i2p_label)
                self.widget_hide(self.root.ids.connectivity_rnode_label)
                self.widget_hide(self.root.ids.connectivity_rnode_ifac_netname)
                self.widget_hide(self.root.ids.connectivity_rnode_ifac_passphrase)
                self.widget_hide(self.root.ids.connectivity_use_rnode)
                self.widget_hide(self.root.ids.connectivity_modem_label)
                self.widget_hide(self.root.ids.connectivity_use_modem)
                self.widget_hide(self.root.ids.connectivity_modem_fields)
                # self.widget_hide(self.root.ids.connectivity_bluetooth_label)
                # self.widget_hide(self.root.ids.connectivity_use_bluetooth)
                # self.widget_hide(self.root.ids.connectivity_bluetooth_fields)
                self.widget_hide(self.root.ids.connectivity_transport_label)
                self.widget_hide(self.root.ids.connectivity_enable_transport)
                self.widget_hide(self.root.ids.connectivity_serial_label)
                self.widget_hide(self.root.ids.connectivity_use_serial)
                self.widget_hide(self.root.ids.connectivity_serial_fields)
                
                self.widget_hide(self.root.ids.connectivity_shared_access)
                self.widget_hide(self.root.ids.connectivity_shared_access_label)
                self.widget_hide(self.root.ids.connectivity_shared_access_fields)
                self.widget_hide(self.root.ids.connectivity_transport_label)
                self.widget_hide(self.root.ids.connectivity_enable_transport)
                self.widget_hide(self.root.ids.connectivity_transport_info)
                self.widget_hide(self.root.ids.connectivity_transport_fields)

            def con_collapse_local(collapse=True):
                # self.widget_hide(self.root.ids.connectivity_local_fields, collapse)
                pass
                
            def con_collapse_tcp(collapse=True):
                # self.widget_hide(self.root.ids.connectivity_tcp_fields, collapse)
                pass
                
            def con_collapse_i2p(collapse=True):
                # self.widget_hide(self.root.ids.connectivity_i2p_fields, collapse)
                pass
                
            def con_collapse_bluetooth(collapse=True):
                # self.widget_hide(self.root.ids.connectivity_bluetooth_fields, collapse)
                pass
                
            def con_collapse_rnode(collapse=True):
                # self.widget_hide(self.root.ids.connectivity_rnode_fields, collapse)
                pass
                
            def con_collapse_modem(collapse=True):
                # self.widget_hide(self.root.ids.connectivity_modem_fields, collapse)
                pass
                
            def con_collapse_serial(collapse=True):
                # self.widget_hide(self.root.ids.connectivity_serial_fields, collapse)
                pass
                
            def con_collapse_transport(collapse=True):
                # self.widget_hide(self.root.ids.connectivity_transport_fields, collapse)
                pass
                
            def save_connectivity(sender=None, event=None):
                self.sideband.config["connect_transport"] = self.root.ids.connectivity_enable_transport.active
                self.sideband.config["connect_local"] = self.root.ids.connectivity_use_local.active
                self.sideband.config["connect_local_groupid"] = self.root.ids.connectivity_local_groupid.text
                self.sideband.config["connect_local_ifac_netname"] = self.root.ids.connectivity_local_ifac_netname.text
                self.sideband.config["connect_local_ifac_passphrase"] = self.root.ids.connectivity_local_ifac_passphrase.text
                self.sideband.config["connect_tcp"] = self.root.ids.connectivity_use_tcp.active
                self.sideband.config["connect_tcp_host"] = self.root.ids.connectivity_tcp_host.text
                self.sideband.config["connect_tcp_port"] = self.root.ids.connectivity_tcp_port.text
                self.sideband.config["connect_tcp_ifac_netname"] = self.root.ids.connectivity_tcp_ifac_netname.text
                self.sideband.config["connect_tcp_ifac_passphrase"] = self.root.ids.connectivity_tcp_ifac_passphrase.text
                self.sideband.config["connect_i2p"] = self.root.ids.connectivity_use_i2p.active
                self.sideband.config["connect_i2p_b32"] = self.root.ids.connectivity_i2p_b32.text
                self.sideband.config["connect_i2p_ifac_netname"] = self.root.ids.connectivity_i2p_ifac_netname.text
                self.sideband.config["connect_i2p_ifac_passphrase"] = self.root.ids.connectivity_i2p_ifac_passphrase.text
                self.sideband.config["connect_rnode"] = self.root.ids.connectivity_use_rnode.active
                self.sideband.config["connect_rnode_ifac_netname"] = self.root.ids.connectivity_rnode_ifac_netname.text
                self.sideband.config["connect_rnode_ifac_passphrase"] = self.root.ids.connectivity_rnode_ifac_passphrase.text

                self.sideband.config["connect_serial"] = self.root.ids.connectivity_use_serial.active
                self.sideband.config["connect_serial_ifac_netname"] = self.root.ids.connectivity_serial_ifac_netname.text
                self.sideband.config["connect_serial_ifac_passphrase"] = self.root.ids.connectivity_serial_ifac_passphrase.text

                self.sideband.config["connect_modem"] = self.root.ids.connectivity_use_modem.active
                self.sideband.config["connect_modem_ifac_netname"] = self.root.ids.connectivity_modem_ifac_netname.text
                self.sideband.config["connect_modem_ifac_passphrase"] = self.root.ids.connectivity_modem_ifac_passphrase.text

                self.sideband.config["connect_ifmode_local"] = self.root.ids.connectivity_local_ifmode.text.lower()
                self.sideband.config["connect_ifmode_tcp"] = self.root.ids.connectivity_tcp_ifmode.text.lower()
                self.sideband.config["connect_ifmode_i2p"] = self.root.ids.connectivity_i2p_ifmode.text.lower()
                self.sideband.config["connect_ifmode_rnode"] = self.root.ids.connectivity_rnode_ifmode.text.lower()
                self.sideband.config["connect_ifmode_modem"] = self.root.ids.connectivity_modem_ifmode.text.lower()
                self.sideband.config["connect_ifmode_serial"] = self.root.ids.connectivity_serial_ifmode.text.lower()

                con_collapse_local(collapse=not self.root.ids.connectivity_use_local.active)
                con_collapse_tcp(collapse=not self.root.ids.connectivity_use_tcp.active)
                con_collapse_i2p(collapse=not self.root.ids.connectivity_use_i2p.active)
                con_collapse_rnode(collapse=not self.root.ids.connectivity_use_rnode.active)
                con_collapse_modem(collapse=not self.root.ids.connectivity_use_modem.active)
                con_collapse_serial(collapse=not self.root.ids.connectivity_use_serial.active)
                con_collapse_transport(collapse=not self.sideband.config["connect_transport"])

                # con_collapse_bluetooth(collapse=not self.root.ids.connectivity_use_bluetooth.active)

                self.sideband.save_configuration()

                if sender == self.root.ids.connectivity_enable_transport:
                    if sender.active:
                        def cb(dt):
                            yes_button = MDRectangleFlatButton(text="Understood",font_size=dp(18), theme_text_color="Custom", line_color=self.color_reject, text_color=self.color_reject)
                            dialog = MDDialog(
                                title="Warning!",
                                text="You have enabled [i]Reticulum Transport[/i] for this device.\n\nFor normal operation, and for most users, this is [b]not[/b] necessary, and might even degrade your network performance.\n\nWhen Transport is enabled, your device will route traffic between all connected interfaces and for all reachable devices on the network.\n\nThis should only be done if you intend to keep your device in a fixed position and for it to remain available continously.\n\nIf this is not the case, or you don't understand any of this, turn off Transport.",
                                buttons=[ yes_button ],
                                # elevation=0,
                            )
                            def dl_yes(s):
                                dialog.dismiss()
                            yes_button.bind(on_release=dl_yes)
                            dialog.open()
                        Clock.schedule_once(cb, 0.65)

            def serial_connectivity_save(sender=None, event=None):
                if sender.active:
                    self.root.ids.connectivity_use_rnode.unbind(active=serial_connectivity_save)
                    self.root.ids.connectivity_use_modem.unbind(active=serial_connectivity_save)
                    self.root.ids.connectivity_use_serial.unbind(active=serial_connectivity_save)
                    self.root.ids.connectivity_use_rnode.active = False
                    self.root.ids.connectivity_use_modem.active = False
                    self.root.ids.connectivity_use_serial.active = False
                    sender.active = True
                    self.root.ids.connectivity_use_rnode.bind(active=serial_connectivity_save)
                    self.root.ids.connectivity_use_modem.bind(active=serial_connectivity_save)
                    self.root.ids.connectivity_use_serial.bind(active=serial_connectivity_save)
                save_connectivity(sender, event)

            def focus_save(sender=None, event=None):
                if not sender.focus:
                    save_connectivity(sender, event)

            def ifmode_validate(sender=None, event=None):
                if not sender.focus:
                    all_valid = True
                    iftypes = ["local", "tcp", "i2p", "rnode", "modem", "serial"]
                    for iftype in iftypes:
                        element = self.root.ids["connectivity_"+iftype+"_ifmode"]
                        modes = ["full", "gateway", "access point", "roaming", "boundary"]
                        value = element.text.lower()
                        if value in ["", "f"] or value.startswith("fu"):
                            value = "full"
                        elif value in ["g", "gw"] or value.startswith("ga"):
                            value = "gateway"
                        elif value in ["a", "ap", "a p", "accesspoint", "access point", "ac", "acc", "acce", "acces"] or value.startswith("access"):
                            value = "access point"
                        elif value in ["r"] or value.startswith("ro"):
                            value = "roaming"
                        elif value in ["b", "edge"] or value.startswith("bo"):
                            value = "boundary"
                        else:
                            value = "full"

                        if value in modes:
                            element.text = value.capitalize()
                            element.error = False
                        else:
                            element.error = True
                            all_valid = False

                    if all_valid:
                        save_connectivity(sender, event)

            if RNS.vendor.platformutils.get_platform() == "android":
                if not self.sideband.getpersistent("service.is_controlling_connectivity"):
                    info =  "Sideband is connected via a shared Reticulum instance running on this system.\n\n"
                    info += "To configure connectivity, edit the relevant configuration file for the instance."
                    self.root.ids.connectivity_info.text = info
                    con_hide_settings()

                else:
                    info =  "By default, Sideband will try to discover and connect to any available Reticulum networks via active WiFi and/or Ethernet interfaces. If any Reticulum Transport Instances are found, Sideband will use these to connect to wider Reticulum networks. You can disable this behaviour if you don't want it.\n\n"
                    info += "You can also connect to a network via a remote or local Reticulum instance using TCP or I2P. [b]Please Note![/b] Connecting via I2P requires that you already have I2P running on your device, and that the SAM API is enabled.\n\n"
                    info += "For changes to connectivity to take effect, you must shut down and restart Sideband.\n"
                    self.root.ids.connectivity_info.text = info

                    self.root.ids.connectivity_use_local.active = self.sideband.config["connect_local"]
                    con_collapse_local(collapse=not self.root.ids.connectivity_use_local.active)
                    self.root.ids.connectivity_local_groupid.text = self.sideband.config["connect_local_groupid"]
                    self.root.ids.connectivity_local_ifac_netname.text = self.sideband.config["connect_local_ifac_netname"]
                    self.root.ids.connectivity_local_ifac_passphrase.text = self.sideband.config["connect_local_ifac_passphrase"]

                    self.root.ids.connectivity_use_tcp.active = self.sideband.config["connect_tcp"]
                    con_collapse_tcp(collapse=not self.root.ids.connectivity_use_tcp.active)
                    self.root.ids.connectivity_tcp_host.text = self.sideband.config["connect_tcp_host"]
                    self.root.ids.connectivity_tcp_port.text = self.sideband.config["connect_tcp_port"]
                    self.root.ids.connectivity_tcp_ifac_netname.text = self.sideband.config["connect_tcp_ifac_netname"]
                    self.root.ids.connectivity_tcp_ifac_passphrase.text = self.sideband.config["connect_tcp_ifac_passphrase"]

                    self.root.ids.connectivity_use_i2p.active = self.sideband.config["connect_i2p"]
                    con_collapse_i2p(collapse=not self.root.ids.connectivity_use_i2p.active)
                    self.root.ids.connectivity_i2p_b32.text = self.sideband.config["connect_i2p_b32"]
                    self.root.ids.connectivity_i2p_ifac_netname.text = self.sideband.config["connect_i2p_ifac_netname"]
                    self.root.ids.connectivity_i2p_ifac_passphrase.text = self.sideband.config["connect_i2p_ifac_passphrase"]

                    self.root.ids.connectivity_use_rnode.active = self.sideband.config["connect_rnode"]
                    con_collapse_rnode(collapse=not self.root.ids.connectivity_use_rnode.active)
                    self.root.ids.connectivity_rnode_ifac_netname.text = self.sideband.config["connect_rnode_ifac_netname"]
                    self.root.ids.connectivity_rnode_ifac_passphrase.text = self.sideband.config["connect_rnode_ifac_passphrase"]

                    # self.root.ids.connectivity_use_bluetooth.active = False
                    # con_collapse_bluetooth(collapse=not self.root.ids.connectivity_use_bluetooth.active)

                    self.root.ids.connectivity_use_modem.active = self.sideband.config["connect_modem"]
                    con_collapse_modem(collapse=not self.root.ids.connectivity_use_modem.active)
                    self.root.ids.connectivity_modem_ifac_netname.text = self.sideband.config["connect_modem_ifac_netname"]
                    self.root.ids.connectivity_modem_ifac_passphrase.text = self.sideband.config["connect_modem_ifac_passphrase"]

                    self.root.ids.connectivity_use_serial.active = self.sideband.config["connect_serial"]
                    con_collapse_serial(collapse=not self.root.ids.connectivity_use_serial.active)
                    self.root.ids.connectivity_serial_ifac_netname.text = self.sideband.config["connect_serial_ifac_netname"]
                    self.root.ids.connectivity_serial_ifac_passphrase.text = self.sideband.config["connect_serial_ifac_passphrase"]

                    self.root.ids.connectivity_enable_transport.active = self.sideband.config["connect_transport"]
                    con_collapse_transport(collapse=not self.sideband.config["connect_transport"])
                    self.root.ids.connectivity_enable_transport.bind(active=save_connectivity)
                    self.root.ids.connectivity_local_ifmode.text = self.sideband.config["connect_ifmode_local"].capitalize()
                    self.root.ids.connectivity_tcp_ifmode.text = self.sideband.config["connect_ifmode_tcp"].capitalize()
                    self.root.ids.connectivity_i2p_ifmode.text = self.sideband.config["connect_ifmode_i2p"].capitalize()
                    self.root.ids.connectivity_rnode_ifmode.text = self.sideband.config["connect_ifmode_rnode"].capitalize()
                    self.root.ids.connectivity_modem_ifmode.text = self.sideband.config["connect_ifmode_modem"].capitalize()
                    self.root.ids.connectivity_serial_ifmode.text = self.sideband.config["connect_ifmode_serial"].capitalize()

                    self.root.ids.connectivity_use_local.bind(active=save_connectivity)
                    self.root.ids.connectivity_local_groupid.bind(focus=focus_save)
                    self.root.ids.connectivity_local_ifac_netname.bind(focus=focus_save)
                    self.root.ids.connectivity_local_ifac_passphrase.bind(focus=focus_save)

                    self.root.ids.connectivity_use_tcp.bind(active=save_connectivity)
                    self.root.ids.connectivity_tcp_host.bind(focus=focus_save)
                    self.root.ids.connectivity_tcp_port.bind(focus=focus_save)
                    self.root.ids.connectivity_tcp_ifac_netname.bind(focus=focus_save)
                    self.root.ids.connectivity_tcp_ifac_passphrase.bind(focus=focus_save)
                    
                    self.root.ids.connectivity_use_i2p.bind(active=save_connectivity)
                    self.root.ids.connectivity_i2p_b32.bind(focus=focus_save)
                    self.root.ids.connectivity_i2p_ifac_netname.bind(focus=focus_save)
                    self.root.ids.connectivity_i2p_ifac_passphrase.bind(focus=focus_save)
                    
                    self.root.ids.connectivity_use_rnode.bind(active=serial_connectivity_save)
                    self.root.ids.connectivity_rnode_ifac_netname.bind(focus=focus_save)
                    self.root.ids.connectivity_rnode_ifac_passphrase.bind(focus=focus_save)

                    self.root.ids.connectivity_use_modem.bind(active=serial_connectivity_save)
                    self.root.ids.connectivity_modem_ifac_netname.bind(focus=focus_save)
                    self.root.ids.connectivity_modem_ifac_passphrase.bind(focus=focus_save)

                    self.root.ids.connectivity_use_serial.bind(active=serial_connectivity_save)
                    self.root.ids.connectivity_serial_ifac_netname.bind(focus=focus_save)
                    self.root.ids.connectivity_serial_ifac_passphrase.bind(focus=focus_save)

                    self.root.ids.connectivity_local_ifmode.bind(focus=ifmode_validate)
                    self.root.ids.connectivity_tcp_ifmode.bind(focus=ifmode_validate)
                    self.root.ids.connectivity_i2p_ifmode.bind(focus=ifmode_validate)
                    self.root.ids.connectivity_rnode_ifmode.bind(focus=ifmode_validate)
                    self.root.ids.connectivity_modem_ifmode.bind(focus=ifmode_validate)
                    self.root.ids.connectivity_serial_ifmode.bind(focus=ifmode_validate)

                    # self.root.ids.connectivity_use_bluetooth.bind(active=save_connectivity)

            else:
                info = ""

                if self.sideband.reticulum.is_connected_to_shared_instance:
                    info =  "Sideband is connected via a shared Reticulum instance running on this system.\n\n"
                    info += "To get connectivity status, use the rnstatus utility.\n\n"
                    info += "To configure connectivity, edit the configuration file located at:\n\n"
                    info += str(RNS.Reticulum.configpath)
                else:
                    info =  "Sideband is currently running a standalone or master Reticulum instance on this system.\n\n"
                    info += "To get connectivity status, use the rnstatus utility.\n\n"
                    info += "To configure connectivity, edit the configuration file located at:\n\n"
                    info += str(RNS.Reticulum.configpath)

                self.root.ids.connectivity_info.text = info

                con_hide_settings()

        self.connectivity_ready = True

    def close_connectivity_action(self, sender=None):
        self.open_conversations(direction="right")
    
    def rpc_copy_action(self, sender=None):
        c_yes_button = MDRectangleFlatButton(text="Yes",font_size=dp(18), theme_text_color="Custom", line_color=self.color_reject, text_color=self.color_reject)
        c_no_button = MDRectangleFlatButton(text="No, go back",font_size=dp(18))
        c_dialog = MDDialog(text="[b]Caution![/b]\n\nA configuration line containing your Reticulum RPC key will be copied to the system clipboard.\n\nWhile the key can only be used by other programs running locally on this system, it is still recommended to take care in not exposing it to unwanted programs.\n\nAre you sure that you wish to proceed?", buttons=[ c_no_button, c_yes_button ])
        def c_dl_no(s):
            c_dialog.dismiss()
        def c_dl_yes(s):
            c_dialog.dismiss()
            yes_button = MDRectangleFlatButton(text="OK")
            dialog = MDDialog(text="The RPC configuration was copied to the system clipboard. Paste in into the [b][reticulum][/b] section of the relevant Reticulum configuration file to allow access to this instance.", buttons=[ yes_button ])
            def dl_yes(s):
                dialog.dismiss()
            yes_button.bind(on_release=dl_yes)

            rpc_string = "rpc_key = "+RNS.hexrep(self.sideband.reticulum.rpc_key, delimit=False)
            Clipboard.copy(rpc_string)
            dialog.open()
        
        c_yes_button.bind(on_release=c_dl_yes)
        c_no_button.bind(on_release=c_dl_no)

        c_dialog.open()

    ### Repository screen
    ######################################
    def repository_action(self, sender=None, direction="left"):
        self.repository_init()
        self.root.ids.screen_manager.transition.direction = direction
        self.root.ids.screen_manager.current = "repository_screen"
        self.root.ids.nav_drawer.set_state("closed")
        if not RNS.vendor.platformutils.is_android():
            self.widget_hide(self.root.ids.repository_enable_button)
            self.widget_hide(self.root.ids.repository_disable_button)
            self.widget_hide(self.root.ids.repository_download_button)
            self.root.ids.repository_info.text = "\nThe [b]Repository Webserver[/b] feature is currently only available on mobile devices."


        self.sideband.setstate("app.displaying", self.root.ids.screen_manager.current)

    def repository_update_info(self, sender=None):
        info =  "Sideband includes a small repository of useful software and guides related to the Sideband and Reticulum ecosystem. You can start this repository to allow other people on your local network to download software and information directly from this device, without needing an Internet connection.\n\n"
        info += "If you want to share the Sideband application itself via the repository server, you must first download it into the local repository, using the \"Update Content\" button below.\n\n"
        info += "To make the repository available on your local network, simply start it below, and it will become browsable on a local IP address for anyone connected to the same WiFi or wired network.\n\n"
        if self.sideband.webshare_server != None:
            if RNS.vendor.platformutils.is_android():                    
                def getIP():
                    adrs = []
                    try:
                        from jnius import autoclass
                        import ipaddress
                        mActivity = autoclass('org.kivy.android.PythonActivity').mActivity
                        SystemProperties = autoclass('android.os.SystemProperties')
                        Context = autoclass('android.content.Context')
                        connectivity_manager = mActivity.getSystemService(Context.CONNECTIVITY_SERVICE)
                        ns = connectivity_manager.getAllNetworks()
                        if not ns == None and len(ns) > 0:
                            for n in ns:
                                lps = connectivity_manager.getLinkProperties(n)
                                las = lps.getLinkAddresses()
                                for la in las:
                                    ina = la.getAddress()
                                    ha = ina.getHostAddress()
                                    if not ina.isLinkLocalAddress():
                                        adrs.append(ha)

                    except Exception as e:
                        RNS.log("Error while getting repository IP address: "+str(e), RNS.LOG_ERROR)
                        return None

                    return adrs

                ips = getIP()
                if ips == None or len(ips) == 0:
                    info += "The repository server is running, but the local device IP address could not be determined.\n\nYou can access the repository by pointing a browser to: http://DEVICE_IP:4444/"
                else:
                    ipstr = ""
                    for ip in ips:
                        ipstr += "http://"+str(ip)+":4444/\n"
                    ms = "" if len(ips) == 1 else "es"
                    info += "The repository server is running at the following address"+ms+":\n"+ipstr

            self.root.ids.repository_enable_button.disabled = True
            self.root.ids.repository_disable_button.disabled = False

        else:
            self.root.ids.repository_enable_button.disabled = False
            self.root.ids.repository_disable_button.disabled = True

        info += "\n"
        self.root.ids.repository_info.text = info

    def repository_start_action(self, sender=None):
        self.sideband.start_webshare()
        Clock.schedule_once(self.repository_update_info, 1.0)

    def repository_stop_action(self, sender=None):
        self.sideband.stop_webshare() 
        Clock.schedule_once(self.repository_update_info, 0.75)

    def repository_download_action(self, sender=None):
        def update_job(sender=None):
            try:
                import requests

                # Get release info
                apk_version = None
                apk_url = None
                pkgname = None
                try:
                    release_url = "https://api.github.com/repos/markqvist/sideband/releases"
                    with requests.get(release_url) as response:
                        releases = response.json()
                        release = releases[0]
                        assets = release["assets"]
                        for asset in assets:
                            if asset["name"].lower().endswith(".apk"):
                                apk_url = asset["browser_download_url"]
                                pkgname = asset["name"]
                                apk_version = release["tag_name"]
                                RNS.log(f"Found version {apk_version} artefact {pkgname} at {apk_url}")
                except Exception as e:
                    self.root.ids.repository_update.text = f"Downloading release info failed with the error:\n"+str(e)
                    return

                self.root.ids.repository_update.text = "Downloading: "+str(apk_url)
                with requests.get(apk_url, stream=True) as response:
                    with open("./dl_tmp", "wb") as tmp_file:
                        cs = 32*1024
                        tds = 0
                        for chunk in response.iter_content(chunk_size=cs):
                            tmp_file.write(chunk)
                            tds += cs
                            self.root.ids.repository_update.text = "Downloaded "+RNS.prettysize(tds)+" of "+str(pkgname)

                    os.rename("./dl_tmp", f"./share/pkg/{pkgname}")
                    self.root.ids.repository_update.text = f"Added {pkgname} to the repository!"
            except Exception as e:
                self.root.ids.repository_update.text = f"Downloading contents failed with the error:\n"+str(e)

        self.root.ids.repository_update.text = "Starting package download..."
        def start_update_job(sender=None):
            threading.Thread(target=update_job, daemon=True).start()
        Clock.schedule_once(start_update_job, 0.5)

    def repository_init(self, sender=None):
        if not self.repository_ready:
            self.root.ids.hardware_scrollview.effect_cls = ScrollEffect
                                
            self.repository_update_info()

        self.root.ids.repository_update.text = ""
        self.repository_ready = True

    def close_repository_action(self, sender=None):
        self.open_conversations(direction="right")

    ### Hardware screen
    ######################################
    def hardware_action(self, sender=None, direction="left"):
        self.hardware_init()
        self.root.ids.screen_manager.transition.direction = direction
        self.root.ids.screen_manager.current = "hardware_screen"
        self.root.ids.nav_drawer.set_state("closed")
        self.sideband.setstate("app.displaying", self.root.ids.screen_manager.current)

    def close_sub_hardware_action(self, sender=None):
        self.hardware_action(direction="right")
    
    def hardware_init(self, sender=None):
        if not self.hardware_ready:
            self.root.ids.hardware_scrollview.effect_cls = ScrollEffect

            def con_hide_settings():
                self.widget_hide(self.root.ids.hardware_rnode_button)
                self.widget_hide(self.root.ids.hardware_modem_button)
                self.widget_hide(self.root.ids.hardware_serial_button)

            def con_collapse_local(collapse=True):
                self.widget_hide(self.root.ids.connectivity_local_fields, collapse)
                                
            def save_connectivity(sender=None, event=None):
                # self.sideband.config["connect_local"] = self.root.ids.connectivity_use_local.active
                con_collapse_local(collapse=not self.root.ids.connectivity_use_local.active)
                self.sideband.save_configuration()

            if RNS.vendor.platformutils.get_platform() == "android":
                if not self.sideband.getpersistent("service.is_controlling_connectivity"):
                    info =  "Sideband is connected via a shared Reticulum instance running on this system.\n\n"
                    info += "To configure hardware parameters, edit the relevant configuration file for the instance."
                    self.root.ids.hardware_info.text = info
                    con_hide_settings()

                else:
                    info =  "When using external hardware for communicating, you may configure various parameters, such as channel settings, modulation schemes, interface speeds and access parameters. You can set up these parameters per device type, and Sideband will apply the configuration when opening a device of that type.\n\n"
                    info += "Hardware configurations can also be exported or imported as [i]config motes[/i], which are self-contained plaintext strings that are easy to share with others. When importing a config mote, Sideband will automatically set all relevant parameters as specified within it.\n\n"
                    info += "For changes to hardware parameters to take effect, you must shut down and restart Sideband.\n"
                    self.root.ids.hardware_info.text = info

            else:
                info = ""

                if self.sideband.reticulum.is_connected_to_shared_instance:
                    info =  "Sideband is connected via a shared Reticulum instance running on this system.\n\n"
                    info += "To configure hardware parameters, edit the configuration file located at:\n\n"
                    info += str(RNS.Reticulum.configpath)
                else:
                    info =  "Sideband is currently running a standalone or master Reticulum instance on this system.\n\n"
                    info += "To configure hardware parameters, edit the configuration file located at:\n\n"
                    info += str(RNS.Reticulum.configpath)

                self.root.ids.hardware_info.text = info

                con_hide_settings()

        self.hardware_ready = True

    def close_hardware_action(self, sender=None):
        self.open_conversations(direction="right")

    ## RNode hardware screen
    def hardware_rnode_action(self, sender=None):
        self.hardware_rnode_init()
        self.root.ids.screen_manager.transition.direction = "left"
        self.root.ids.screen_manager.current = "hardware_rnode_screen"
        self.root.ids.nav_drawer.set_state("closed")
        self.sideband.setstate("app.displaying", self.root.ids.screen_manager.current)

    def hardware_rnode_save(self):
        try:
            self.sideband.config["hw_rnode_frequency"] = int(float(self.root.ids.hardware_rnode_frequency.text)*1000000)
        except:
            pass

        try:
            self.sideband.config["hw_rnode_bandwidth"] = int(float(self.root.ids.hardware_rnode_bandwidth.text)*1000)
        except:
            pass

        try:
            self.sideband.config["hw_rnode_tx_power"] = int(self.root.ids.hardware_rnode_txpower.text)
        except:
            pass

        try:
            self.sideband.config["hw_rnode_spreading_factor"] = int(self.root.ids.hardware_rnode_spreadingfactor.text)
        except:
            pass
        
        try:
            self.sideband.config["hw_rnode_coding_rate"] = int(self.root.ids.hardware_rnode_codingrate.text)
        except:
            pass
        
        try:
            self.sideband.config["hw_rnode_atl_short"] = float(self.root.ids.hardware_rnode_atl_short.text)
        except:
            self.sideband.config["hw_rnode_atl_short"] = None

        try:
            self.sideband.config["hw_rnode_atl_long"] = float(self.root.ids.hardware_rnode_atl_long.text)
        except:
            self.sideband.config["hw_rnode_atl_long"] = None
        
        if self.root.ids.hardware_rnode_beaconinterval.text == "":
            self.sideband.config["hw_rnode_beaconinterval"] = None
        else:
            self.sideband.config["hw_rnode_beaconinterval"] = int(self.root.ids.hardware_rnode_beaconinterval.text)

        if self.root.ids.hardware_rnode_beacondata.text == "":
            self.sideband.config["hw_rnode_beacondata"] = None
        else:
            self.sideband.config["hw_rnode_beacondata"] = self.root.ids.hardware_rnode_beacondata.text

        if self.root.ids.hardware_rnode_bt_device.text == "":
            self.sideband.config["hw_rnode_bt_device"] = None
        else:
            self.sideband.config["hw_rnode_bt_device"] = self.root.ids.hardware_rnode_bt_device.text

        self.sideband.save_configuration()

    def hardware_rnode_bt_on_action(self, sender=None):
        self.root.ids.hardware_rnode_bt_pair_button.disabled = True
        self.root.ids.hardware_rnode_bt_on_button.disabled = True
        self.root.ids.hardware_rnode_bt_off_button.disabled = True
        def re_enable():
            time.sleep(2)
            while self.sideband.getstate("executing.bt_on"):
                time.sleep(1)
            self.root.ids.hardware_rnode_bt_off_button.disabled = False
            self.root.ids.hardware_rnode_bt_pair_button.disabled = False
            self.root.ids.hardware_rnode_bt_on_button.disabled = False
        threading.Thread(target=re_enable, daemon=True).start()
        self.sideband.setstate("wants.bt_on", True)

    def hardware_rnode_bt_off_action(self, sender=None):
        self.root.ids.hardware_rnode_bt_pair_button.disabled = True
        self.root.ids.hardware_rnode_bt_on_button.disabled = True
        self.root.ids.hardware_rnode_bt_off_button.disabled = True
        def re_enable():
            time.sleep(2)
            while self.sideband.getstate("executing.bt_off"):
                time.sleep(1)
            self.root.ids.hardware_rnode_bt_off_button.disabled = False
            self.root.ids.hardware_rnode_bt_pair_button.disabled = False
            self.root.ids.hardware_rnode_bt_on_button.disabled = False
        threading.Thread(target=re_enable, daemon=True).start()
        self.sideband.setstate("wants.bt_off", True)

    def hardware_rnode_bt_pair_action(self, sender=None):
        self.root.ids.hardware_rnode_bt_pair_button.disabled = True
        self.root.ids.hardware_rnode_bt_on_button.disabled = True
        self.root.ids.hardware_rnode_bt_off_button.disabled = True
        def re_enable():
            time.sleep(2)
            while self.sideband.getstate("executing.bt_pair"):
                time.sleep(1)
            self.root.ids.hardware_rnode_bt_off_button.disabled = False
            self.root.ids.hardware_rnode_bt_pair_button.disabled = False
            self.root.ids.hardware_rnode_bt_on_button.disabled = False
        threading.Thread(target=re_enable, daemon=True).start()
        self.sideband.setstate("wants.bt_pair", True)

    def hardware_rnode_bt_toggle_action(self, sender=None, event=None):
        if sender.active:
            self.sideband.config["hw_rnode_bluetooth"] = True
            self.request_bluetooth_permissions()
        else:
            self.sideband.config["hw_rnode_bluetooth"] = False

        self.sideband.save_configuration()

    
    def hardware_rnode_framebuffer_toggle_action(self, sender=None, event=None):
        if sender.active:
            self.sideband.config["hw_rnode_enable_framebuffer"] = True
        else:
            self.sideband.config["hw_rnode_enable_framebuffer"] = False

        self.sideband.save_configuration()

    
    def hardware_rnode_init(self, sender=None):
        if not self.hardware_rnode_ready:
            self.root.ids.hardware_rnode_scrollview.effect_cls = ScrollEffect
            def save_connectivity(sender=None, event=None):
                if self.hardware_rnode_validate():
                    self.hardware_rnode_save()

            def focus_save(sender=None, event=None):
                if sender != None:
                    if not sender.focus:
                        save_connectivity(sender=sender)

            if self.sideband.config["hw_rnode_frequency"] != None:
                t_freq = str(self.sideband.config["hw_rnode_frequency"]/1000000.0)
            else:
                t_freq = ""
            if self.sideband.config["hw_rnode_bandwidth"] != None:
                t_bw = str(self.sideband.config["hw_rnode_bandwidth"]/1000.0)
            else:
                t_bw = str(62.5)
            if self.sideband.config["hw_rnode_tx_power"] != None:
                t_p = str(self.sideband.config["hw_rnode_tx_power"])
            else:
                t_p = str(0)
            if self.sideband.config["hw_rnode_spreading_factor"] != None:
                t_sf = str(self.sideband.config["hw_rnode_spreading_factor"])
            else:
                t_sf = str(8)
            if self.sideband.config["hw_rnode_coding_rate"] != None:
                t_cr = str(self.sideband.config["hw_rnode_coding_rate"])
            else:
                t_cr = str(6)
            if self.sideband.config["hw_rnode_beaconinterval"] != None:
                t_bi = str(self.sideband.config["hw_rnode_beaconinterval"])
            else:
                t_bi = ""
            if self.sideband.config["hw_rnode_beacondata"] != None:
                t_bd = str(self.sideband.config["hw_rnode_beacondata"])
            else:
                t_bd = ""
            if self.sideband.config["hw_rnode_bt_device"] != None:
                t_btd = str(self.sideband.config["hw_rnode_bt_device"])
            else:
                t_btd = ""
            if self.sideband.config["hw_rnode_atl_short"] != None:
                t_ats = str(self.sideband.config["hw_rnode_atl_short"])
            else:
                t_ats = ""
            if self.sideband.config["hw_rnode_atl_long"] != None:
                t_atl = str(self.sideband.config["hw_rnode_atl_long"])
            else:
                t_atl = ""

            self.root.ids.hardware_rnode_bluetooth.active = self.sideband.config["hw_rnode_bluetooth"]
            self.root.ids.hardware_rnode_framebuffer.active = self.sideband.config["hw_rnode_enable_framebuffer"]
            self.root.ids.hardware_rnode_frequency.text = t_freq
            self.root.ids.hardware_rnode_bandwidth.text = t_bw
            self.root.ids.hardware_rnode_txpower.text = t_p
            self.root.ids.hardware_rnode_spreadingfactor.text = t_sf
            self.root.ids.hardware_rnode_codingrate.text = t_cr
            self.root.ids.hardware_rnode_beaconinterval.text = t_bi
            self.root.ids.hardware_rnode_beacondata.text = t_bd
            self.root.ids.hardware_rnode_bt_device.text = t_btd
            self.root.ids.hardware_rnode_atl_short.text = t_ats
            self.root.ids.hardware_rnode_atl_long.text = t_atl
            self.root.ids.hardware_rnode_frequency.bind(focus=focus_save)
            self.root.ids.hardware_rnode_bandwidth.bind(focus=focus_save)
            self.root.ids.hardware_rnode_txpower.bind(focus=focus_save)
            self.root.ids.hardware_rnode_spreadingfactor.bind(focus=focus_save)
            self.root.ids.hardware_rnode_codingrate.bind(focus=focus_save)
            self.root.ids.hardware_rnode_beaconinterval.bind(focus=focus_save)
            self.root.ids.hardware_rnode_beacondata.bind(focus=focus_save)
            self.root.ids.hardware_rnode_bt_device.bind(focus=focus_save)
            self.root.ids.hardware_rnode_frequency.bind(on_text_validate=save_connectivity)
            self.root.ids.hardware_rnode_bandwidth.bind(on_text_validate=save_connectivity)
            self.root.ids.hardware_rnode_txpower.bind(on_text_validate=save_connectivity)
            self.root.ids.hardware_rnode_spreadingfactor.bind(on_text_validate=save_connectivity)
            self.root.ids.hardware_rnode_codingrate.bind(on_text_validate=save_connectivity)
            self.root.ids.hardware_rnode_beaconinterval.bind(on_text_validate=save_connectivity)
            self.root.ids.hardware_rnode_beacondata.bind(on_text_validate=save_connectivity)
            self.root.ids.hardware_rnode_atl_short.bind(on_text_validate=save_connectivity)
            self.root.ids.hardware_rnode_atl_long.bind(on_text_validate=save_connectivity)
            self.root.ids.hardware_rnode_bluetooth.bind(active=self.hardware_rnode_bt_toggle_action)
            self.root.ids.hardware_rnode_framebuffer.bind(active=self.hardware_rnode_framebuffer_toggle_action)


    def hardware_rnode_validate(self, sender=None):
        valid = True        
        try:
            val = float(self.root.ids.hardware_rnode_frequency.text)
            if not val > 0:
                raise ValueError("Invalid frequency")
            self.root.ids.hardware_rnode_frequency.error = False
            self.root.ids.hardware_rnode_frequency.text = str(val)
        except:
            self.root.ids.hardware_rnode_frequency.error = True
            valid = False
        
        try:
            valid_vals = [7.8, 10.4, 15.6, 20.8, 31.25, 41.7, 62.5, 125, 250, 500]
            val = float(self.root.ids.hardware_rnode_bandwidth.text)
            if not val in valid_vals:
                raise ValueError("Invalid bandwidth")
            self.root.ids.hardware_rnode_bandwidth.error = False
            self.root.ids.hardware_rnode_bandwidth.text = str(val)
        except:
            self.root.ids.hardware_rnode_bandwidth.error = True
            valid = False
        
        try:
            val = int(self.root.ids.hardware_rnode_txpower.text)
            if not val >= 0:
                raise ValueError("Invalid TX power")
            self.root.ids.hardware_rnode_txpower.error = False
            self.root.ids.hardware_rnode_txpower.text = str(val)
        except:
            self.root.ids.hardware_rnode_txpower.error = True
            valid = False
        
        try:
            val = int(self.root.ids.hardware_rnode_spreadingfactor.text)
            if val < 7 or val > 12:
                raise ValueError("Invalid sf")
            self.root.ids.hardware_rnode_spreadingfactor.error = False
            self.root.ids.hardware_rnode_spreadingfactor.text = str(val)
        except:
            self.root.ids.hardware_rnode_spreadingfactor.error = True
            valid = False
        
        try:
            val = int(self.root.ids.hardware_rnode_codingrate.text)
            if val < 5 or val > 8:
                raise ValueError("Invalid cr")
            self.root.ids.hardware_rnode_codingrate.error = False
            self.root.ids.hardware_rnode_codingrate.text = str(val)
        except:
            self.root.ids.hardware_rnode_codingrate.error = True
            valid = False
        
        try:
            if self.root.ids.hardware_rnode_beaconinterval.text != "":
                val = int(self.root.ids.hardware_rnode_beaconinterval.text)
                if val < 10:
                    raise ValueError("Invalid bi")
                self.root.ids.hardware_rnode_beaconinterval.text = str(val)

            self.root.ids.hardware_rnode_beaconinterval.error = False
        except:
            self.root.ids.hardware_rnode_beaconinterval.text = ""
            valid = False
        
        return valid

    def hardware_rnode_import(self, sender=None):
        mote = None
        try:
            mote = Clipboard.paste()
        except Exception as e:
            yes_button = MDRectangleFlatButton(text="OK",font_size=dp(18))
            dialog = MDDialog(
                title="Import Failed",
                text="Could not read data from your clipboard, please check your system permissions.",
                buttons=[ yes_button ],
                # elevation=0,
            )
            def dl_yes(s):
                dialog.dismiss()
            yes_button.bind(on_release=dl_yes)
            dialog.open()

        try:
            config = msgpack.unpackb(base64.b32decode(mote))
            self.root.ids.hardware_rnode_frequency.text        = str(config["f"]/1000000.0)
            self.root.ids.hardware_rnode_bandwidth.text        = str(config["b"]/1000.0)
            self.root.ids.hardware_rnode_txpower.text          = str(config["t"])
            self.root.ids.hardware_rnode_spreadingfactor.text  = str(config["s"])
            self.root.ids.hardware_rnode_codingrate.text       = str(config["c"])
            
            if "n" in config and config["n"] != None:
                ifn = str(config["n"])
            else:
                ifn = ""
            if "p" in config and config["p"] != None:
                ifp = str(config["p"])
            else:
                ifp = ""

            self.root.ids.connectivity_rnode_ifac_netname.text    = ifn
            self.sideband.config["connect_rnode_ifac_netname"]             = ifn
            self.root.ids.connectivity_rnode_ifac_passphrase.text = ifp
            self.sideband.config["connect_rnode_ifac_passphrase"]          = ifp

            if config["i"] != None:
                ti = str(config["i"])
            else:
                ti = ""
            self.root.ids.hardware_rnode_beaconinterval.text  = ti
            if config["d"] != None:
                td = str(config["d"])
            else:
                td = ""
            self.root.ids.hardware_rnode_beacondata.text      = td

            if self.hardware_rnode_validate():
                self.hardware_rnode_save()
                yes_button = MDRectangleFlatButton(text="OK",font_size=dp(18))
                dialog = MDDialog(
                    title="Configuration Imported",
                    text="The config mote was imported and saved as your active configuration.",
                    buttons=[ yes_button ],
                    # elevation=0,
                )
                def dl_yes(s):
                    dialog.dismiss()
                yes_button.bind(on_release=dl_yes)
                dialog.open()
            else:
                raise ValueError("Invalid mote")

        except Exception as e:
            yes_button = MDRectangleFlatButton(text="OK",font_size=dp(18))
            dialog = MDDialog(
                title="Import Failed",
                text="The read data did not contain a valid config mote. If any data was decoded, you may try to correct it by editing the relevant fields. The reported error was:\n\n"+str(e),
                buttons=[ yes_button ],
                # elevation=0,
            )
            def dl_yes(s):
                dialog.dismiss()
            yes_button.bind(on_release=dl_yes)
            dialog.open()

    def hardware_rnode_export(self, sender=None):
        mote = None
        try:
            mote = base64.b32encode(msgpack.packb({
                "f": self.sideband.config["hw_rnode_frequency"],
                "b": self.sideband.config["hw_rnode_bandwidth"],
                "t": self.sideband.config["hw_rnode_tx_power"],
                "s": self.sideband.config["hw_rnode_spreading_factor"],
                "c": self.sideband.config["hw_rnode_coding_rate"],
                "i": self.sideband.config["hw_rnode_beaconinterval"],
                "d": self.sideband.config["hw_rnode_beacondata"],
                "n": self.sideband.config["connect_rnode_ifac_netname"],
                "p": self.sideband.config["connect_rnode_ifac_passphrase"],
            }))
        except Exception as e:
            pass

        if mote != None:
            Clipboard.copy(mote)
            yes_button = MDRectangleFlatButton(text="OK",font_size=dp(18))
            dialog = MDDialog(
                title="Configuration Exported",
                text="The config mote was created and copied to your clipboard.",
                buttons=[ yes_button ],
                # elevation=0,
            )
            def dl_yes(s):
                dialog.dismiss()
            yes_button.bind(on_release=dl_yes)
            dialog.open()
        else:
            yes_button = MDRectangleFlatButton(text="OK",font_size=dp(18))
            dialog = MDDialog(
                title="Export Failed",
                text="The config mote could not be created, please check your settings.",
                buttons=[ yes_button ],
                # elevation=0,
            )
            def dl_yes(s):
                dialog.dismiss()
            yes_button.bind(on_release=dl_yes)
            dialog.open()
    
    ## Modem hardware screen
    def hardware_modem_action(self, sender=None):
        self.hardware_modem_init()
        self.root.ids.screen_manager.transition.direction = "left"
        self.root.ids.screen_manager.current = "hardware_modem_screen"
        self.root.ids.nav_drawer.set_state("closed")
        self.sideband.setstate("app.displaying", self.root.ids.screen_manager.current)

    def hardware_modem_init(self, sender=None):
        if not self.hardware_modem_ready:
            self.root.ids.hardware_modem_scrollview.effect_cls = ScrollEffect
            def save_connectivity(sender=None, event=None):
                if self.hardware_modem_validate():
                    self.hardware_modem_save()

            def focus_save(sender=None, event=None):
                if sender != None:
                    if not sender.focus:
                        save_connectivity(sender=sender)

            if self.sideband.config["hw_modem_baudrate"] != None:
                t_b = str(self.sideband.config["hw_modem_baudrate"])
            else:
                t_b = ""

            if self.sideband.config["hw_modem_databits"] != None:
                t_db = str(self.sideband.config["hw_modem_databits"])
            else:
                t_db = ""

            if self.sideband.config["hw_modem_parity"] != None:
                t_p = str(self.sideband.config["hw_modem_parity"])
            else:
                t_p = ""
            
            if self.sideband.config["hw_modem_stopbits"] != None:
                t_sb = str(self.sideband.config["hw_modem_stopbits"])
            else:
                t_sb = ""
            
            if self.sideband.config["hw_modem_preamble"] != None:
                t_pa = str(self.sideband.config["hw_modem_preamble"])
            else:
                t_pa = ""
            
            if self.sideband.config["hw_modem_tail"] != None:
                t_t = str(self.sideband.config["hw_modem_tail"])
            else:
                t_t = ""
            
            if self.sideband.config["hw_modem_persistence"] != None:
                t_ps = str(self.sideband.config["hw_modem_persistence"])
            else:
                t_ps = ""

            if self.sideband.config["hw_modem_slottime"] != None:
                t_st = str(self.sideband.config["hw_modem_slottime"])
            else:
                t_st = ""

            if self.sideband.config["hw_modem_beaconinterval"] != None:
                t_bi = str(self.sideband.config["hw_modem_beaconinterval"])
            else:
                t_bi = ""
            if self.sideband.config["hw_modem_beacondata"] != None:
                t_bd = str(self.sideband.config["hw_modem_beacondata"])
            else:
                t_bd = ""
            
            self.root.ids.hardware_modem_baudrate.text = t_b
            self.root.ids.hardware_modem_databits.text = t_db
            self.root.ids.hardware_modem_parity.text = t_p
            self.root.ids.hardware_modem_stopbits.text = t_sb
            self.root.ids.hardware_modem_beaconinterval.text = t_bi
            self.root.ids.hardware_modem_beacondata.text = t_bd
            self.root.ids.hardware_modem_preamble.text = t_pa
            self.root.ids.hardware_modem_tail.text = t_t
            self.root.ids.hardware_modem_persistence.text = t_ps
            self.root.ids.hardware_modem_slottime.text = t_st
            
            self.root.ids.hardware_modem_baudrate.bind(focus=focus_save)
            self.root.ids.hardware_modem_databits.bind(focus=focus_save)
            self.root.ids.hardware_modem_parity.bind(focus=focus_save)
            self.root.ids.hardware_modem_stopbits.bind(focus=focus_save)
            self.root.ids.hardware_modem_beaconinterval.bind(focus=focus_save)
            self.root.ids.hardware_modem_beacondata.bind(focus=focus_save)
            self.root.ids.hardware_modem_preamble.bind(focus=focus_save)
            self.root.ids.hardware_modem_tail.bind(focus=focus_save)
            self.root.ids.hardware_modem_persistence.bind(focus=focus_save)
            self.root.ids.hardware_modem_slottime.bind(focus=focus_save)
            
            self.root.ids.hardware_modem_baudrate.bind(on_text_validate=save_connectivity)
            self.root.ids.hardware_modem_databits.bind(on_text_validate=save_connectivity)
            self.root.ids.hardware_modem_parity.bind(on_text_validate=save_connectivity)
            self.root.ids.hardware_modem_stopbits.bind(on_text_validate=save_connectivity)
            self.root.ids.hardware_modem_beaconinterval.bind(on_text_validate=save_connectivity)
            self.root.ids.hardware_modem_beacondata.bind(on_text_validate=save_connectivity)
            self.root.ids.hardware_modem_preamble.bind(on_text_validate=save_connectivity)
            self.root.ids.hardware_modem_tail.bind(on_text_validate=save_connectivity)
            self.root.ids.hardware_modem_persistence.bind(on_text_validate=save_connectivity)
            self.root.ids.hardware_modem_slottime.bind(on_text_validate=save_connectivity)
    
    def hardware_modem_save(self):
        self.sideband.config["hw_modem_baudrate"] = int(self.root.ids.hardware_modem_baudrate.text)
        self.sideband.config["hw_modem_databits"] = int(self.root.ids.hardware_modem_databits.text)
        self.sideband.config["hw_modem_parity"] = self.root.ids.hardware_modem_parity.text
        self.sideband.config["hw_modem_stopbits"] = int(self.root.ids.hardware_modem_stopbits.text)
        self.sideband.config["hw_modem_preamble"] = int(self.root.ids.hardware_modem_preamble.text)
        self.sideband.config["hw_modem_tail"] = int(self.root.ids.hardware_modem_tail.text)
        self.sideband.config["hw_modem_persistence"] = int(self.root.ids.hardware_modem_persistence.text)
        self.sideband.config["hw_modem_slottime"] = int(self.root.ids.hardware_modem_slottime.text)

        if self.root.ids.hardware_modem_beaconinterval.text == "":
            self.sideband.config["hw_modem_beaconinterval"] = None
        else:
            self.sideband.config["hw_modem_beaconinterval"] = int(self.root.ids.hardware_modem_beaconinterval.text)

        if self.root.ids.hardware_modem_beacondata.text == "":
            self.sideband.config["hw_modem_beacondata"] = None
        else:
            self.sideband.config["hw_modem_beacondata"] = self.root.ids.hardware_modem_beacondata.text

        self.sideband.save_configuration()

    def hardware_modem_validate(self, sender=None):
        valid = True        
        try:
            val = int(self.root.ids.hardware_modem_baudrate.text)
            if not val > 0:
                raise ValueError("Invalid baudrate")
            self.root.ids.hardware_modem_baudrate.error = False
            self.root.ids.hardware_modem_baudrate.text = str(val)
        except:
            self.root.ids.hardware_modem_baudrate.error = True
            valid = False
        
        try:
            val = int(self.root.ids.hardware_modem_databits.text)
            if not val > 0:
                raise ValueError("Invalid databits")
            self.root.ids.hardware_modem_databits.error = False
            self.root.ids.hardware_modem_databits.text = str(val)
        except:
            self.root.ids.hardware_modem_databits.error = True
            valid = False
        
        try:
            val = int(self.root.ids.hardware_modem_stopbits.text)
            if not val > 0:
                raise ValueError("Invalid stopbits")
            self.root.ids.hardware_modem_stopbits.error = False
            self.root.ids.hardware_modem_stopbits.text = str(val)
        except:
            self.root.ids.hardware_modem_stopbits.error = True
            valid = False
        
        try:
            val = int(self.root.ids.hardware_modem_preamble.text)
            if not (val >= 0 and val <= 1000):
                raise ValueError("Invalid preamble")
            self.root.ids.hardware_modem_preamble.error = False
            self.root.ids.hardware_modem_preamble.text = str(val)
        except:
            self.root.ids.hardware_modem_preamble.error = True
            valid = False
        
        try:
            val = int(self.root.ids.hardware_modem_tail.text)
            if not (val > 0 and val <= 500):
                raise ValueError("Invalid tail")
            self.root.ids.hardware_modem_tail.error = False
            self.root.ids.hardware_modem_tail.text = str(val)
        except:
            self.root.ids.hardware_modem_tail.error = True
            valid = False
        
        try:
            val = int(self.root.ids.hardware_modem_slottime.text)
            if not (val > 0 and val <= 500):
                raise ValueError("Invalid slottime")
            self.root.ids.hardware_modem_slottime.error = False
            self.root.ids.hardware_modem_slottime.text = str(val)
        except:
            self.root.ids.hardware_modem_slottime.error = True
            valid = False
        
        try:
            val = int(self.root.ids.hardware_modem_persistence.text)
            if not (val > 0 and val <= 255):
                raise ValueError("Invalid persistence")
            self.root.ids.hardware_modem_persistence.error = False
            self.root.ids.hardware_modem_persistence.text = str(val)
        except:
            self.root.ids.hardware_modem_persistence.error = True
            valid = False
        
        try:
            val = self.root.ids.hardware_modem_parity.text
            nval = val.lower()
            if nval in ["e", "ev", "eve", "even"]:
                val = "even"
            if nval in ["o", "od", "odd"]:
                val = "odd"
            if nval in ["n", "no", "non", "none", "not", "null", "off"]:
                val = "none"
            if not val in ["even", "odd", "none"]:
                raise ValueError("Invalid parity")
            self.root.ids.hardware_modem_parity.error = False
            self.root.ids.hardware_modem_parity.text = str(val)
        except:
            self.root.ids.hardware_modem_parity.error = True
            valid = False

        try:
            if self.root.ids.hardware_modem_beaconinterval.text != "":
                val = int(self.root.ids.hardware_modem_beaconinterval.text)
                if val < 10:
                    raise ValueError("Invalid bi")
                self.root.ids.hardware_modem_beaconinterval.text = str(val)

            self.root.ids.hardware_modem_beaconinterval.error = False
        except:
            self.root.ids.hardware_modem_beaconinterval.text = ""
            valid = False

        return valid
    
    ## Serial hardware screen
    def hardware_serial_action(self, sender=None):
        self.hardware_serial_init()
        self.root.ids.screen_manager.transition.direction = "left"
        self.root.ids.screen_manager.current = "hardware_serial_screen"
        self.root.ids.nav_drawer.set_state("closed")
        self.sideband.setstate("app.displaying", self.root.ids.screen_manager.current)

    def hardware_serial_init(self, sender=None):
        if not self.hardware_serial_ready:
            self.root.ids.hardware_serial_scrollview.effect_cls = ScrollEffect
            def save_connectivity(sender=None, event=None):
                if self.hardware_serial_validate():
                    self.hardware_serial_save()

            def focus_save(sender=None, event=None):
                if sender != None:
                    if not sender.focus:
                        save_connectivity(sender=sender)

            if self.sideband.config["hw_serial_baudrate"] != None:
                t_b = str(self.sideband.config["hw_serial_baudrate"])
            else:
                t_b = ""

            if self.sideband.config["hw_serial_databits"] != None:
                t_db = str(self.sideband.config["hw_serial_databits"])
            else:
                t_db = ""

            if self.sideband.config["hw_serial_parity"] != None:
                t_p = str(self.sideband.config["hw_serial_parity"])
            else:
                t_p = ""
            
            if self.sideband.config["hw_serial_stopbits"] != None:
                t_sb = str(self.sideband.config["hw_serial_stopbits"])
            else:
                t_sb = ""
            
            self.root.ids.hardware_serial_baudrate.text = t_b
            self.root.ids.hardware_serial_databits.text = t_db
            self.root.ids.hardware_serial_parity.text = t_p
            self.root.ids.hardware_serial_stopbits.text = t_sb
            
            self.root.ids.hardware_serial_baudrate.bind(focus=focus_save)
            self.root.ids.hardware_serial_databits.bind(focus=focus_save)
            self.root.ids.hardware_serial_parity.bind(focus=focus_save)
            self.root.ids.hardware_serial_stopbits.bind(focus=focus_save)
            
            self.root.ids.hardware_serial_baudrate.bind(on_text_validate=save_connectivity)
            self.root.ids.hardware_serial_databits.bind(on_text_validate=save_connectivity)
            self.root.ids.hardware_serial_parity.bind(on_text_validate=save_connectivity)
            self.root.ids.hardware_serial_stopbits.bind(on_text_validate=save_connectivity)

    def hardware_serial_validate(self, sender=None):
        valid = True        
        try:
            val = int(self.root.ids.hardware_serial_baudrate.text)
            if not val > 0:
                raise ValueError("Invalid baudrate")
            self.root.ids.hardware_serial_baudrate.error = False
            self.root.ids.hardware_serial_baudrate.text = str(val)
        except:
            self.root.ids.hardware_serial_baudrate.error = True
            valid = False
        
        try:
            val = int(self.root.ids.hardware_serial_databits.text)
            if not val > 0:
                raise ValueError("Invalid databits")
            self.root.ids.hardware_serial_databits.error = False
            self.root.ids.hardware_serial_databits.text = str(val)
        except:
            self.root.ids.hardware_serial_databits.error = True
            valid = False
        
        try:
            val = int(self.root.ids.hardware_serial_stopbits.text)
            if not val > 0:
                raise ValueError("Invalid stopbits")
            self.root.ids.hardware_serial_stopbits.error = False
            self.root.ids.hardware_serial_stopbits.text = str(val)
        except:
            self.root.ids.hardware_serial_stopbits.error = True
            valid = False
        
        try:
            val = self.root.ids.hardware_serial_parity.text
            nval = val.lower()
            if nval in ["e", "ev", "eve", "even"]:
                val = "even"
            if nval in ["o", "od", "odd"]:
                val = "odd"
            if nval in ["n", "no", "non", "none", "not", "null", "off"]:
                val = "none"
            if not val in ["even", "odd", "none"]:
                raise ValueError("Invalid parity")
            self.root.ids.hardware_serial_parity.error = False
            self.root.ids.hardware_serial_parity.text = str(val)
        except:
            self.root.ids.hardware_serial_parity.error = True
            valid = False

        return valid

    def hardware_serial_save(self):
        self.sideband.config["hw_serial_baudrate"] = int(self.root.ids.hardware_serial_baudrate.text)
        self.sideband.config["hw_serial_databits"] = int(self.root.ids.hardware_serial_databits.text)
        self.sideband.config["hw_serial_parity"] = self.root.ids.hardware_serial_parity.text
        self.sideband.config["hw_serial_stopbits"] = int(self.root.ids.hardware_serial_stopbits.text)

        self.sideband.save_configuration()

    ### Announce Stream screen
    ######################################
    def init_announces_view(self, sender=None):
        if not self.announces_view:
            self.announces_view = Announces(self)
            self.sideband.setstate("app.flags.new_announces", True)

            for child in self.root.ids.announces_scrollview.children:
                self.root.ids.announces_scrollview.remove_widget(child)

            self.root.ids.announces_scrollview.effect_cls = ScrollEffect
            self.root.ids.announces_scrollview.add_widget(self.announces_view.get_widget())

    def announces_action(self, sender=None):
        self.root.ids.screen_manager.transition.direction = "left"
        self.root.ids.nav_drawer.set_state("closed")
        
        if self.sideband.getstate("app.flags.new_announces"):
            self.init_announces_view()
            self.announces_view.update()

        self.root.ids.screen_manager.current = "announces_screen"
        self.sideband.setstate("app.displaying", self.root.ids.screen_manager.current)

    def close_announces_action(self, sender=None):
        self.open_conversations(direction="right")

    def announce_filter_action(self, sender=None):
        pass

    def screen_transition_complete(self, sender):
        if self.root.ids.screen_manager.current == "announces_screen":
            pass
        if self.root.ids.screen_manager.current == "conversations_screen":
            pass

    ### Keys screen
    ######################################
    def keys_action(self, sender=None):
        # def link_exec(sender=None, event=None):
        #     import webbrowser
        #     webbrowser.open("https://unsigned.io/sideband")
        # self.root.ids.keys_info.bind(on_ref_press=link_exec)

        self.root.ids.keys_scrollview.effect_cls = ScrollEffect
        info = "Your primary encryption keys are stored in a Reticulum Identity within the Sideband app. If you want to backup this Identity for later use on this or another device, you can export it as a plain text blob, with the key data encoded in Base32 format. This will allow you to restore your address in Sideband or other LXMF clients at a later point.\n\n[b]Warning![/b] Anyone that gets access to the key data will be able to control your LXMF address, impersonate you, and read your messages. In is [b]extremely important[/b] that you keep the Identity data secure if you export it.\n\nBefore displaying or exporting your Identity data, make sure that no machine or person in your vicinity is able to see, copy or record your device screen or similar."

        if not RNS.vendor.platformutils.get_platform() == "android":
            self.widget_hide(self.root.ids.keys_share)

        self.root.ids.keys_info.text = info
        self.root.ids.screen_manager.transition.direction = "left"
        self.root.ids.screen_manager.current = "keys_screen"
        self.root.ids.nav_drawer.set_state("closed")
        self.sideband.setstate("app.displaying", self.root.ids.screen_manager.current)

    def close_keys_action(self, sender=None):
        self.open_conversations(direction="right")

    def identity_display_action(self, sender=None):
        yes_button = MDRectangleFlatButton(text="OK",font_size=dp(18))

        dialog = MDDialog(
            text="Your Identity key, in base32 format is as follows:\n\n[b]"+str(base64.b32encode(self.sideband.identity.get_private_key()).decode("utf-8"))+"[/b]",
            buttons=[ yes_button ],
            # elevation=0,
        )
        def dl_yes(s):
            dialog.dismiss()
        
        yes_button.bind(on_release=dl_yes)
        dialog.open()

    def identity_copy_action(self, sender=None):
        c_yes_button = MDRectangleFlatButton(text="Yes",font_size=dp(18), theme_text_color="Custom", line_color=self.color_reject, text_color=self.color_reject)
        c_no_button = MDRectangleFlatButton(text="No, go back",font_size=dp(18))
        c_dialog = MDDialog(text="[b]Caution![/b]\n\nYour Identity key will be copied to the system clipboard. Take extreme care that no untrusted app steals your key by reading the clipboard data. Clear the system clipboard immediately after pasting your key where you need it.\n\nAre you sure that you wish to proceed?", buttons=[ c_no_button, c_yes_button ])
        def c_dl_no(s):
            c_dialog.dismiss()
        def c_dl_yes(s):
            c_dialog.dismiss()
            yes_button = MDRectangleFlatButton(text="OK")
            dialog = MDDialog(text="Your Identity key was copied to the system clipboard", buttons=[ yes_button ])
            def dl_yes(s):
                dialog.dismiss()
            yes_button.bind(on_release=dl_yes)

            Clipboard.copy(str(base64.b32encode(self.sideband.identity.get_private_key()).decode("utf-8")))
            dialog.open()
        
        c_yes_button.bind(on_release=c_dl_yes)
        c_no_button.bind(on_release=c_dl_no)

        c_dialog.open()

    def identity_share_action(self, sender=None):
        if RNS.vendor.platformutils.get_platform() == "android":
            self.share_text(str(base64.b32encode(self.sideband.identity.get_private_key()).decode("utf-8")))

    def identity_restore_action(self, sender=None):
        c_yes_button = MDRectangleFlatButton(text="Yes",font_size=dp(18), theme_text_color="Custom", line_color=self.color_reject, text_color=self.color_reject)
        c_no_button = MDRectangleFlatButton(text="No, go back",font_size=dp(18))
        c_dialog = MDDialog(text="[b]Caution![/b]\n\nYou are about to import a new Identity key into Sideband. The currently active key will be irreversibly destroyed, and you will loose your LXMF address if you have not already backed up your current Identity key.\n\nAre you sure that you wish to import the key?", buttons=[ c_no_button, c_yes_button ])
        def c_dl_no(s):
            c_dialog.dismiss()
        def c_dl_yes(s):
            c_dialog.dismiss()
            b32_text = self.root.ids.key_restore_text.text
        
            try:
                key_bytes = base64.b32decode(b32_text)
                new_id = RNS.Identity.from_bytes(key_bytes)

                if new_id != None:
                    new_id.to_file(self.sideband.identity_path)

                yes_button = MDRectangleFlatButton(text="OK",font_size=dp(18))
                dialog = MDDialog(text="[b]The provided Identity key data was imported[/b]\n\nThe app will now exit. Please restart Sideband to use the new Identity.", buttons=[ yes_button ])
                def dl_yes(s):
                    dialog.dismiss()
                    self.quit_action(sender=self)
                yes_button.bind(on_release=dl_yes)
                dialog.open()

            except Exception as e:
                yes_button = MDRectangleFlatButton(text="OK",font_size=dp(18))
                dialog = MDDialog(text="[b]The provided Identity key data was not valid[/b]\n\nThe error reported by Reticulum was:\n\n[i]"+str(e)+"[/i]\n\nNo Identity was imported into Sideband.", buttons=[ yes_button ])
                def dl_yes(s):
                    dialog.dismiss()
                yes_button.bind(on_release=dl_yes)
                dialog.open()
            
        
        c_yes_button.bind(on_release=c_dl_yes)
        c_no_button.bind(on_release=c_dl_no)

        c_dialog.open()


    ### Guide screen
    ######################################
    def close_guide_action(self, sender=None):
        self.open_conversations(direction="right")
    
    def guide_action(self, sender=None):
        def link_exec(sender=None, event=None):
            import webbrowser
            webbrowser.open("https://unsigned.io/donate")

        guide_text1 = """
[size=18dp][b]Introduction[/b][/size][size=5dp]\n \n[/size]Welcome to [i]Sideband[/i], an LXMF client for Android, Linux and macOS. With Sideband, you can communicate with other people or LXMF-compatible systems over Reticulum networks using LoRa, Packet Radio, WiFi, I2P, or anything else Reticulum supports.

This short guide will give you a basic introduction to the concepts that underpin Sideband and LXMF (which is the protocol that Sideband uses to communicate). If you are not already familiar with LXMF and Reticulum, it is probably a good idea to read this guide, since Sideband is very different from other messaging apps."""
        guide_text2 = """
[size=18dp][b]Communication Without Subjection[/b][/size][size=5dp]\n \n[/size]Sideband is completely free, permission-less, anonymous and infrastructure-less. Sideband uses the peer-to-peer and distributed messaging system LXMF. There is no sign-up, no service providers, no "end-user license agreements", no data theft and no surveillance. You own the system.

This also means that Sideband operates differently than what you might be used to. It does not need a connection to a server on the Internet to function, and you do not have an account anywhere."""
        
        guide_text3 = """
[size=18dp][b]Operating Principles[/b][/size][size=5dp]\n \n[/size]When Sideband is started on your device for the first time, it randomly generates a set of cryptographic keys. These keys are then used to create an LXMF address for your use. Any other endpoint in [i]any[/i] Reticulum network will be able to send data to this address, as long as there is [i]some sort of physical connection[/i] between your device and the remote endpoint. You can also move around to other Reticulum networks with this address, even ones that were never connected to the network the address was created on, or that didn't exist when the address was created. The address is yours to keep and control for as long (or short) a time you need it, and you can always delete it and create a new one."""
        
        guide_text4 = """
[size=18dp][b]Becoming Reachable[/b][/size][size=5dp]\n \n[/size]To establish reachability for any Reticulum address on a network, an [i]announce[/i] must be sent. Sideband does not do this automatically by default, but can be configured to do so every time the program starts. To send an announce manually, press the [i]Announce[/i] button in the [i]Conversations[/i] section of the program. When you send an announce, you make your LXMF address reachable for real-time messaging to the entire network you are connected to. Even in very large networks, you can expect global reachability for your address to be established in under a minute.

If you don't move to other places in the network, and keep connected through the same hubs or gateways, it is generally not necessary to send an announce more often than once every week. If you change your entry point to the network, you may want to send an announce, or you may just want to stay quiet."""

        guide_text5 = """
[size=18dp][b]Relax & Disconnect[/b][/size][size=5dp]\n \n[/size]If you are not connected to the network, it is still possible for other people to message you, as long as one or more [i]Propagation Nodes[/i] exist on the network. These nodes pick up and hold encrypted in-transit messages for offline users. Messages are always encrypted before leaving the originators device, and nobody else than the intended recipient can decrypt messages in transit.

The Propagation Nodes also distribute copies of messages between each other, such that even the failure of almost every node in the network will still allow users to sync their waiting messages. If all Propagation Nodes disappear or are destroyed, users can still communicate directly. Reticulum and LXMF will degrade gracefully all the way down to single users communicating directly via long-range data radios. Anyone can start up new propagation nodes and integrate them into existing networks without permission or coordination. Even a small and cheap device like a Rasperry Pi can handle messages for millions of users. LXMF networks are designed to be quite resilient, as long as there are people using them."""

        guide_text6 = """
[size=18dp][b]Packets Find A Way[/b][/size][size=5dp]\n \n[/size]Connections in Reticulum networks can be wired or wireless, span many intermediary hops, run over fast links or ultra-low bandwidth radio, tunnel over the Invisible Internet (I2P), private networks, satellite connections, serial lines or anything else that Reticulum can carry data over. In most cases it will not be possible to know what path data takes in a Reticulum network, and no transmitted packets carries any identifying characteristics, apart from a destination address. There is no source addresses in Reticulum. As long as you do not reveal any connecting details between your person and your LXMF address, you can remain anonymous. Sending messages to others does not reveal [i]your[/i] address to anyone else than the intended recipient."""

        guide_text7 = """
[size=18dp][b]Be Yourself, Be Unknown, Stay Free[/b][/size][size=5dp]\n \n[/size]Even with the above characteristics in mind, you [b]must remember[/b] that LXMF and Reticulum is not a technology that can guarantee anonymising connections that are already de-anonymised! If you use Sideband to connect to TCP Reticulum hubs over the clear Internet, from a network that can be tied to your personal identity, an adversary may learn that you are generating LXMF traffic. If you want to avoid this, it is recommended to use I2P to connect to Reticulum hubs on the Internet. Or only connecting from within pure Reticulum networks, that take one or more hops to reach connections that span the Internet. This is a complex topic, with many more nuances than can be covered here. You are encouraged to ask on the various Reticulum discussion forums if you are in doubt.

If you use Reticulum and LXMF on hardware that does not carry any identifiers tied to you, it is possible to establish a completely free and anonymous communication system with Reticulum and LXMF clients."""
        
        guide_text8 = """
[size=18dp][b]Keyboard Shortcuts[/b][/size][size=5dp]\n \n[/size] - Ctrl+Q or Ctrl-W Shut down Sideband
 - Ctrl-D or Ctrl-S Send message
 - Ctrl-R Show Conversations
 - Ctrl-L Show Announce Stream
 - Ctrl-N New conversation
 - Ctrl-G Show guide"""
        
        guide_text9 = """
[size=18dp][b]Sow Seeds Of Freedom[/b][/size][size=5dp]\n \n[/size]It took me more than seven years to design and built the entire ecosystem of software and hardware that makes this possible. If this project is valuable to you, please go to [u][ref=link]https://unsigned.io/donate[/ref][/u] to support the project with a donation. Every donation directly makes the entire Reticulum project possible.

Thank you very much for using Free Communications Systems.
"""
        info1 = guide_text1
        info2 = guide_text2
        info3 = guide_text3
        info4 = guide_text4
        info5 = guide_text5
        info6 = guide_text6
        info7 = guide_text7
        info8 = guide_text8
        info9 = guide_text9

        if self.theme_cls.theme_style == "Dark":
            info1 = "[color=#"+dark_theme_text_color+"]"+info1+"[/color]"
            info2 = "[color=#"+dark_theme_text_color+"]"+info2+"[/color]"
            info3 = "[color=#"+dark_theme_text_color+"]"+info3+"[/color]"
            info4 = "[color=#"+dark_theme_text_color+"]"+info4+"[/color]"
            info5 = "[color=#"+dark_theme_text_color+"]"+info5+"[/color]"
            info6 = "[color=#"+dark_theme_text_color+"]"+info6+"[/color]"
            info7 = "[color=#"+dark_theme_text_color+"]"+info7+"[/color]"
            info8 = "[color=#"+dark_theme_text_color+"]"+info8+"[/color]"
            info9 = "[color=#"+dark_theme_text_color+"]"+info9+"[/color]"
        self.root.ids.guide_info1.text = info1
        self.root.ids.guide_info2.text = info2
        self.root.ids.guide_info3.text = info3
        self.root.ids.guide_info4.text = info4
        self.root.ids.guide_info5.text = info5
        self.root.ids.guide_info6.text = info6
        self.root.ids.guide_info7.text = info7
        self.root.ids.guide_info8.text = info8
        self.root.ids.guide_info9.text = info9
        self.root.ids.guide_info9.bind(on_ref_press=link_exec)
        self.root.ids.guide_scrollview.effect_cls = ScrollEffect
        self.root.ids.screen_manager.transition.direction = "left"
        self.root.ids.screen_manager.current = "guide_screen"
        self.root.ids.nav_drawer.set_state("closed")
        self.sideband.setstate("app.displaying", self.root.ids.screen_manager.current)


    #################################################
    # Unimplemented Screens                         #
    #################################################

    def map_action(self, sender=None):
        def link_exec(sender=None, event=None):
            import webbrowser
            webbrowser.open("https://unsigned.io/donate")

        self.root.ids.map_scrollview.effect_cls = ScrollEffect
        info = "The [b]Local Area[/b] feature is not yet implemented in Sideband.\n\nWant it faster? Go to [u][ref=link]https://unsigned.io/donate[/ref][/u] to support the project."
        if self.theme_cls.theme_style == "Dark":
            info = "[color=#"+dark_theme_text_color+"]"+info+"[/color]"
        self.root.ids.map_info.text = info
        self.root.ids.map_info.bind(on_ref_press=link_exec)
        self.root.ids.screen_manager.transition.direction = "left"
        self.root.ids.screen_manager.current = "map_screen"
        self.root.ids.nav_drawer.set_state("closed")
        self.sideband.setstate("app.displaying", self.root.ids.screen_manager.current)

    def broadcasts_action(self, sender=None):
        def link_exec(sender=None, event=None):
            import webbrowser
            webbrowser.open("https://unsigned.io/donate")

        self.root.ids.broadcasts_scrollview.effect_cls = ScrollEffect
        info = "The [b]Local Broadcasts[/b] feature will allow you to send and listen for local broadcast transmissions on connected radio, LoRa and WiFi interfaces.\n\n[b]Local Broadcasts[/b] makes it easy to establish public information exchange with anyone in direct radio range, or even with large areas far away using the [i]Remote Broadcast Repeater[/i] feature.\n\nThese features are not yet implemented in Sideband.\n\nWant it faster? Go to [u][ref=link]https://unsigned.io/donate[/ref][/u] to support the project."
        if self.theme_cls.theme_style == "Dark":
            info = "[color=#"+dark_theme_text_color+"]"+info+"[/color]"
        self.root.ids.broadcasts_info.text = info
        self.root.ids.broadcasts_info.bind(on_ref_press=link_exec)
        self.root.ids.screen_manager.transition.direction = "left"
        self.root.ids.screen_manager.current = "broadcasts_screen"
        self.root.ids.nav_drawer.set_state("closed")
        self.sideband.setstate("app.displaying", self.root.ids.screen_manager.current)

    

def run():
    SidebandApp().run()

if __name__ == "__main__":
    run()
