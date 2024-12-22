# Message Spammer
This is a software that will can spam messages for you really fast.

It is written in Python by Green11_KD.

This is still in BETA. Expect some bugs and stuff not working.

# System / Hardware Requirements
Please review your computer's specifications before downloading the software.

### Minimum System / Hardware Requirements

- Operating System:
  - Windows 11 Home or Pro, version 22H2 (32-bit)
- CPU:
  - Dual-core Processors
- RAM / Memory:
  - At least 3GB
- Storage:
  - At least 5MB of available space on the hard drive
- Software Needed:
  - Python version 3.11

### Recommended System / Hardware Requirements

- Operating System:
  - Windows 11 Home or Pro (64-bit), version 22H2 or later
- CPU:
  - Dual-core Processors (Intel Core i3 8th generation or higher or AMD Ryzen 3 or higher)
- RAM / Memory:
  - 8GB
- Storage:
  - SSD Hard Drive with at least 15GB of available space
- Software Needed:
  - Python version 3.13 or later

 # How to Install

 To download the software, you need the latest Python installed in your computer.

 If you don't have Python in your computer, you can download it from the Microsoft Store from here: https://apps.microsoft.com/detail/9pnrbtzxmb4z?hl=en-us&gl=US

 ## Installation Process

 1. Download the latest release from the [release page](https://github.com/Green11-KD/Message-Spammer/releases).
 2. Once you're done, open it and read all the guidelines. (It's not long)
    ![Licensing Image](https://github.com/user-attachments/assets/6c5f6811-4d6c-4ee7-ae03-0be8d74c0077)
 3. Make sure you check "Create Start Menu Folder" so that it shows as an app.
    ![Check Start Menu Folder](https://github.com/user-attachments/assets/a3f45df8-e121-4c86-983e-4b0a1314ce3a)
 4. Press next and the installer will download all the files needed for the software and the 3 packages needed for Python too. (The 3 packages will not be properly installed if you don't have Python installed first.
 5. Once it's done, launch the app, and we are good to go!

## Is it a virus?

Some anti-virus software flaggs the installer as a virus or trojan, but don't worry, the file is 100% safe.

The installer is made with [InstallForge](https://installforge.net/), which is common for an installer made with InstallForge to be flagged as trojan by many anti-virus software such as McAfee and VirusTotal.

These anti-virus software might flag this file as virus:
- CrowdStrike Falcon
- Cynet
- Gridinsoft
- McAfee
- SentinelOne

If any other virus flags the file as virus, please report it in the [issues page](https://github.com/Green11-KD/Message-Spammer/issues).

## What does this installer do?

What this installer does is, it downloads all the required files and the 3 python packages that is used for this program.

The 3 Python packages that will be installed are:
- pyautogui
- keyboard
- pyperclip

### File Tree Diagram

This is how all the files will be installed, and what they do.

All the files will be stored in C:\Program Files (x86)\Green11_KD\Message Spammer

```
└─Message Spammer
    │  launcher.bat -- Launches message_spammer.py
    │  message_spammer.py -- The main program
    │  Uninstall Message Spammer.dat -- Uninstaller Data File
    │  Uninstall Message Spammer.exe -- This will uninstall the software
    │  Uninstall Message Spammer_lang.ifl -- Uninstaller Data File
    │
    ├─installation
    │      README.md -- README file
    │      setup.bat -- This file will be used by the installer to configure Python, and install the 3 packages.
    │
    └─logo
            logo.bmp -- Logo
            logo.ico -- Logo
            logo.png -- Logo
```

# How to Use

Before you use:

**Make sure you get the person's permission before spamming them!!**

1. Run the program by pressing the windows key and type "Message Spammer"
  ![image](https://github.com/user-attachments/assets/36e7daa7-6812-4c7a-bc78-b93eeea57e03)
2. The app will ask you the message you want to send. Type in your message and press enter.
   ![image](https://github.com/user-attachments/assets/8dec8ea8-a55d-4dfe-9df6-e0565166b48f)
3. The app will now ask you how many times you want to send the message. Type a number and press enter.
   ![image](https://github.com/user-attachments/assets/4031f8b5-d401-4c46-9c6a-fa07a521e6b9)
4. The app will show you the message you're sending and the amount of messages. Press enter again to confirm or press Ctrl + C to cancel.
   ![image](https://github.com/user-attachments/assets/22a76674-6b62-45a3-9570-b18a1a78dce6)
5. The app will start preparing, and when you get this screen, you are ready to go!
   ![image](https://github.com/user-attachments/assets/be02a1a3-5e2d-417a-868d-2b147a43c924)
6. Open the chat that you want to send, click on the place to type, and press F6 to start! (Make sure you have the person's permission to spam)
   ![image](https://github.com/user-attachments/assets/ef908606-1425-40dc-9f41-85133e3d0a1d)
7. If you want to stop it, you can do that by pressing F6 again. But when the program sends enough message, it will stop by itself.
8. When you're done, press enter again to exit the program.

# Not working?

Find the solution to your problem here!

If you can't find it or it doesn't work, please report it in the [issues page](https://github.com/Green11-KD/Message-Spammer/issues).

### Python not Installed

![image](https://github.com/user-attachments/assets/9b2e1d18-9e7b-4c13-8631-1ac48096511d)

This error means that you do not have Python installed in your computer.
To resolve it, please download the latest Python from the Microsoft Store from here: https://apps.microsoft.com/detail/9pnrbtzxmb4z?hl=en-us&gl=US
Then run the installer again to correctly configure Python.

### Not all packages are not installed

![image](https://github.com/user-attachments/assets/b97bdd02-3a40-4cee-9b0d-fc78547c3584)

This error means that you do not have all 3 python packages installed in your computer.

These 3 packages are:
- pyautogui
- keyboard
- pyperclip

To resolve it, please run the installer again to install the packages.
