[33mtag v1.0[m
Tagger: amanoj319319319 <a.manoj16@gmail.com>
Date:   Sun May 31 22:37:01 2020 +0530

tag for add 2 files

[33mcommit a6d7ff5913db5eeee9eb65b7fb884ad703f9f566[m[33m ([m[1;36mHEAD -> [m[1;32mmaster[m[33m, [m[1;33mtag: v1.0[m[33m, [m[1;31morigin/master[m[33m)[m
Author: amanoj319319319 <a.manoj16@gmail.com>
Date:   Sun May 31 13:04:42 2020 +0530

    conftest added

[1mdiff --git a/.idea/workspace.xml b/.idea/workspace.xml[m
[1mindex 28a386b..0ce2e39 100644[m
[1m--- a/.idea/workspace.xml[m
[1m+++ b/.idea/workspace.xml[m
[36m@@ -3,6 +3,7 @@[m
   <component name="ChangeListManager">[m
     <list default="true" id="90606ea7-9d25-4549-84ee-5c0d8aa3cfc1" name="Default Changelist" comment="">[m
       <change beforePath="$PROJECT_DIR$/.idea/workspace.xml" beforeDir="false" afterPath="$PROJECT_DIR$/.idea/workspace.xml" afterDir="false" />[m
[32m+[m[32m      <change beforePath="$PROJECT_DIR$/PyTest_2/test_file_12.py" beforeDir="false" afterPath="$PROJECT_DIR$/PyTest_2/test_file_12.py" afterDir="false" />[m
     </list>[m
     <option name="SHOW_DIALOG" value="false" />[m
     <option name="HIGHLIGHT_CONFLICTS" value="true" />[m
[1mdiff --git a/PyTest_2/__pycache__/test_file_12.cpython-37-pytest-5.3.5.pyc b/PyTest_2/__pycache__/test_file_12.cpython-37-pytest-5.3.5.pyc[m
[1mnew file mode 100644[m
[1mindex 0000000..046b594[m
Binary files /dev/null and b/PyTest_2/__pycache__/test_file_12.cpython-37-pytest-5.3.5.pyc differ
[1mdiff --git a/PyTest_2/__pycache__/test_file_13.cpython-37-pytest-5.3.5.pyc b/PyTest_2/__pycache__/test_file_13.cpython-37-pytest-5.3.5.pyc[m
[1mnew file mode 100644[m
[1mindex 0000000..85e6d4a[m
Binary files /dev/null and b/PyTest_2/__pycache__/test_file_13.cpython-37-pytest-5.3.5.pyc differ
[1mdiff --git a/PyTest_2/test_file_12.py b/PyTest_2/test_file_12.py[m
[1mindex 5630f8e..3a87a7b 100644[m
[1m--- a/PyTest_2/test_file_12.py[m
[1m+++ b/PyTest_2/test_file_12.py[m
[36m@@ -1,4 +1,3 @@[m
[31m-'''[m
 import unittest[m
 from selenium import webdriver[m
 import time[m
[36m@@ -32,7 +31,6 @@[m [mclass LoginTest(unittest.TestCase):[m
 if __name__ == "__main__":[m
      unittest.main()[m
 [m
[31m-'''[m
 [m
 [m
 [m
[1mdiff --git a/PyTest_5_Conftest_11/__init__.py b/PyTest_5_Conftest_11/__init__.py[m
[1mnew file mode 100644[m
[1mindex 0000000..e69de29[m
[1mdiff --git a/PyTest_5_Conftest_11/__pycache__/__init__.cpython-37.pyc b/PyTest_5_Conftest_11/__pycache__/__init__.cpython-37.pyc[m
[1mnew file mode 100644[m
[1mindex 0000000..f4d63d3[m
Binary files /dev/null and b/PyTest_5_Conftest_11/__pycache__/__init__.cpython-37.pyc differ
[1mdiff --git a/PyTest_5_Conftest_11/__pycache__/conftest.cpython-37-pytest-5.4.2.pyc b/PyTest_5_Conftest_11/__pycache__/conftest.cpython-37-pytest-5.4.2.pyc[m
[1mnew file mode 100644[m
[1mindex 0000000..1248511[m
Binary files /dev/null and b/PyTest_5_Conftest_11/__pycache__/conftest.cpython-37-pytest-5.4.2.pyc differ
[1mdiff --git a/PyTest_5_Conftest_11/__pycache__/test_file_51.cpython-37-pytest-5.4.2.pyc b/PyTest_5_Conftest_11/__pycache__/test_file_51.cpython-37-pytest-5.4.2.pyc[m
[1mnew file mode 100644[m
[1mindex 0000000..0cb7b81[m
Binary files /dev/null and b/PyTest_5_Conftest_11/__pycache__/test_file_51.cpython-37-pytest-5.4.2.pyc differ
[1mdiff --git a/PyTest_5_Conftest_11/conftest.py b/PyTest_5_Conftest_11/conftest.py[m
[1mnew file mode 100644[m
[1mindex 0000000..4300383[m
[1m--- /dev/null[m
[1m+++ b/PyTest_5_Conftest_11/conftest.py[m
[36m@@ -0,0 +1,13 @@[m
[32m+[m[32m#working very fine[m
[32m+[m[32m#we can run our automated test cases against different browsers[m
[32m+[m[32mimport pytest[m
[32m+[m[32m@pytest.fixture(params=["chrome", "firefox"],scope="class")[m
[32m+[m[32mdef driver_init(request):[m
[32m+[m[32m    from selenium import webdriver[m
[32m+[m[32m    if request.param == "chrome":[m
[32m+[m[32m        web_driver = webdriver.Chrome()[m
[32m+[m[32m    if request.param == "firefox":[m
[32m+[m[32m        web_driver = webdriver.Firefox()[m
[32m+[m[32m    request.cls.driver = web_driver[m
[32m+[m[32m    yield[m
[32m+[m[32m    web_driver.close()[m
\ No newline at end of file[m
[1mdiff --git a/PyTest_5_Conftest_11/test_file_51.py b/PyTest_5_Conftest_11/test_file_51.py[m
[1mnew file mode 100644[m
[1mindex 0000000..d514e42[m
[1m--- /dev/null[m
[1m+++ b/PyTest_5_Conftest_11/test_file_51.py[m
[36m@@ -0,0 +1,21 @@[m
[32m+[m[32mimport pytest[m
[32m+[m[32mfrom selenium import webdriver[m
[32m+[m[32mfrom selenium.webdriver.common.by import By[m
[32m+[m[32mfrom selenium.webdriver.support.ui import WebDriverWait[m
[32m+[m[32mfrom selenium.webdriver.support import expected_conditions as EC[m
[32m+[m[32mimport time[m
[32m+[m
[32m+[m[32m@pytest.mark.usefixtures("driver_init")[m
[32m+[m[32mclass TestExampleOne:[m
[32m+[m[32m    def test_method_1(self):[m
[32m+[m[32m        self.driver.get("https://learn.letskodeit.com")[m
[32m+[m[32m        print ("Title of the page is:-",self.driver.title)[m
[32m+[m
[32m+[m
[32m+[m[32m    def test_method_2(self):[m
[32m+[m[32m        self.driver.get("https://learn.letskodeit.com/p/practice")[m
[32m+[m[32m        print ("Title of the page is:-",self.driver.title)[m
[32m+[m[32m        ele=self.driver.find_element_by_id("name").send_keys("Manoj")[m
[32m+[m[32m        time.sleep(5)[m
[32m+[m
[32m+[m
[1mdiff --git a/geckodriver.log b/geckodriver.log[m
[1mnew file mode 100644[m
[1mindex 0000000..4dd45ab[m
[1m--- /dev/null[m
[1m+++ b/geckodriver.log[m
[36m@@ -0,0 +1,29 @@[m
[32m+[m[32m1590909729900	mozrunner::runner	INFO	Running command: "C:\\Program Files\\Mozilla Firefox\\firefox.exe" "-marionette" "-foreground" "-no-remote" "-profile" "C:\\Users\\Manoj\\AppData\\Local\\Temp\\rust_mozprofile.2lfunxCPfilj"[m
[32m+[m[32m1590909734293	addons.webextension.doh-rollout@mozilla.org	WARN	Loading extension 'doh-rollout@mozilla.org': Reading manifest: Invalid extension permission: networkStatus[m
[32m+[m[32m1590909736854	addons.webextension.screenshots@mozilla.org	WARN	Loading extension 'screenshots@mozilla.org': Reading manifest: Invalid extension permission: mozillaAddons[m
[32m+[m[32m1590909736854	addons.webextension.screenshots@mozilla.org	WARN	Loading extension 'screenshots@mozilla.org': Reading manifest: Invalid extension permission: telemetry[m
[32m+[m[32m1590909736854	addons.webextension.screenshots@mozilla.org	WARN	Loading extension 'screenshots@mozilla.org': Reading manifest: Invalid extension permission: resource://pdf.js/[m
[32m+[m[32m1590909736854	addons.webextension.screenshots@mozilla.org	WARN	Loading extension 'screenshots@mozilla.org': Reading manifest: Invalid extension permission: about:reader*[m
[32m+[m[32mJavaScript error: resource://gre/modules/XULStore.jsm, line 66: Error: Can't find profile directory.[m
[32m+[m
[32m+[m[32m###!!! [Child][RunMessage] Error: Channel closing: too late to send/recv, messages will be lost[m
[32m+[m
[32m+[m[32m1590909749652	Marionette	INFO	Listening on port 60822[m
[32m+[m[32m1590909751838	Marionette	WARN	TLS certificate errors will be ignored for this session[m
[32m+[m[32m1590909770525	Marionette	INFO	Stopped listening on port 60822[m
[32m+[m
[32m+[m[32m###!!! [Child][RunMessage] Error: Channel closing: too late to send/recv, messages will be lost[m
[32m+[m
[32m+[m[32m1590909898890	mozrunner::runner	INFO	Running command: "C:\\Program Files\\Mozilla Firefox\\firefox.exe" "-marionette" "-foreground" "-no-remote" "-profile" "C:\\Users\\Manoj\\AppData\\Local\\Temp\\rust_mozprofile.VwmwRx6zVP1U"[m
[32m+[m[32m1590909899693	addons.webextension.doh-rollout@mozilla.org	WARN	Loading extension 'doh-rollout@mozilla.org': Reading manifest: Invalid extension permission: networkStatus[m
[32m+[m[32m1590909902121	addons.webextension.screenshots@mozilla.org	WARN	Loading extension 'screenshots@mozilla.org': Reading manifest: Invalid extension permission: mozillaAddons[m
[32m+[m[32m1590909902122	addons.webextension.screenshots@mozilla.org	WARN	Loading extension 'screenshots@mozilla.org': Reading manifest: Invalid extension permission: telemetry[m
[32m+[m[32m1590909902122	addons.webextension.screenshots@mozilla.org	WARN	Loading extension 'screenshots@mozilla.org': Reading manifest: Invalid extension permission: resource://pdf.js/[m
[32m+[m[32m1590909902122	addons.webextension.screenshots@mozilla.org	WARN	Loading extension 'screenshots@mozilla.org': Reading manifest: Invalid extension permission: about:reader*[m
[32m+[m[32mJavaScript error: resource://gre/modules/XULStore.jsm, line 66: Error: Can't find profile directory.[m
[32m+[m[32m1590909906323	Marionette	INFO	Listening on port 61103[m
[32m+[m[32m1590909906564	Marionette	WARN	TLS certificate errors will be ignored for this session[m
[32m+[m[32m1590909926603	Marionette	INFO	Stopped listening on port 61103[m
[32m+[m
[32m+[m[32m###!!! [Child][RunMessage] Error: Channel closing: too late to send/recv, messages will be lost[m
[32m+[m
