# NOTE: This script is now deprecated! (2018-07-01)

Sony released "[Digital Paper App for mobile](https://itunes.apple.com/jp/app/digital-paper-app-for-mobile/id1384897785)", their official app for transmitting PDF files between DPT-RP1 (and DPT-CP1) and iOS devices. I strongly recommend using it.

# dptrp1-uploader-for-iOS
Python script for uploading PDF file to DPT-RP1 from iOS devices. It is a Pythonista wrapper for the package [dpt-rp1-py](https://github.com/janten/dpt-rp1-py), focusing only the function to upload files. It runs as the extension of Pythonista on iOS.

## Installation

Using `pip` in [StaSh](https://github.com/ywangd/stash),

```shell
$ pip install httpsig
$ pip install pbkdf2
$ pip install pycrypto
```

Next, install [urllib3](https://github.com/shazow/urllib3) and [dptrp1](https://github.com/janten/dpt-rp1-py) from the latest source code.

```shell
$ cd ~/Documents
$ git clone git://github.com/shazow/urllib3.git
$ cp urllib3/urllib3 site-packages/urllib3
```

```shell
$ git clone https://github.com/janten/dpt-rp1-py.git
$ cp dpt-rp1-py/dptrp1 site-packages/dptrp1
```


Clone the script,

```shell
$ git clone https://github.com/ki-chi/dptrp1-uploader-for-iOS.git
```

set `uploadpdf.py` on "Share Extension Shortcuts" on Pythonista, and reboot the device.

## Usage

Connect iOS devices and DPT-RP1 with LAN (or connect DPT-RP1 with iOS's Wi-Fi tethering network) and choose "Run Pythonista Script" in iOS's "Open In..." functions on any apps. Then, Pythonista runs the script and send the PDF to your iOS device. It requires pairing if you run it at the first time.

<img src="http://ki-chi.jp/wp-content/uploads/IMG_7225.png" width="320">

## Notes

* The connection through the Wi-Fi tethering network is really slow.
* While you open a PDF file in Safari, you should choose "More..." on the top of the view. Do not choose "Open In..." shortcut in the bottom. The latter sends only URL of the file.
* DPT-RP1 has poor responses to do pairing. So try several times if errors occur.
* If a document has same filename already exists in DPT-RP1, your uploading will be failed.
