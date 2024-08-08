# NuggyNet Beta Channel
The beta channel for NuggyNet. View main release [here](https://www.github.com/NuggyNet/NuggyNet)

## building?
Run this:
`pip install pyinstaller PyQt5 PyQtWebEngine`

use Pyinstaller with the following cmd (make sure it's in the PATH system environment variable, replace <folder location> with folder location)
`pyinstaller --noconfirm --onefile --console --icon "<folder location>\NuggyNetBeta\icon.ico;." --add-data "<folder location>\NuggyNetBeta\icon.ico;." --add-data "<folder location>\NuggyNetBeta\Beta.py;." -add--data "<folder location>\NuggyNetBeta\Beta.py"`

If you don't have PyInstaller in PATH, use this command instead (replace <username> with username>):
`C:\Users\<username>\AppData\Roaming\Python\Python312\Scripts\pyinstaller.exe --noconfirm --onefile --console --icon "<folder location>\NuggyNetBeta\icon.ico;." --add-data "<folder location>NuggyNetBeta\Homepage.html;." --add-data "<folder location>\NuggyNetBeta\icon.ico;." --add-data "<folder location>\NuggyNetBeta\Beta.py;." --add-data "<folder location>\NuggyNetBeta\Beta.py"`

### Planned features
- [ ] Tabs
- [ ] First Launch screen
- [ ] Accounts
- [ ] System-level interactions

[Main NuggyNet Repo](https://www.github.com/NuggyNet/NuggyNet) | [My website](https://awethebird.neocities.org) | [YouTube channel](https://www.youtube.com/@NuggyNet)
