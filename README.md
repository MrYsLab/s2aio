A work in progress

More detailed documentation is on the way, but if you would like to try it out, here are some initial guidelines.

To install s2aio, first install python 3.5 (it must be 3.5!) on your computer. 

From a command window type:

pip install s2aio

(for linux type: sudo pip3 install s2aio)

All libraries needed by the program will be installed on your computer.

To start the program, type s2aio in the command window. This will start the s2aio server, and open Scratch with the
English version of s2aio programming blocks. 

To start Scratch with a different language set, specify the language as a command line parameter. For example:

s2aio -l 5

This will start Scratch with French blocks.

The Arduino COM port will be auto detected. Just make sure that you have Standard Firmata or FirmataPlus uploaded
to your Arduino. Firmata Plus can be found [here](https://github.com/MrYsLab/pymata-aio/tree/master/FirmataPlus).

Installation instructions for FirmataPlus are [here](https://github.com/MrYsLab/pymata-aio/wiki/Uploading-FirmataPlus-to-Arduino)


Here are the command line arguments available for s2aio:

usage: __main__.py [-h] [-c CLIENT] [-l LANGUAGE] [-p COMPORT]

optional arguments:

  -h, --help   show this help message and exit
  
  -c CLIENT    default = scratch [scratch | snap | no_client]
  
  -l LANGUAGE  1=English(default) 2=Chinese(zh-CN) 3=Chinese(zh-TW) 4=Dutch(NL) 5=French(FR) 6=German(DE) 7=Greek(GR) 8=Korean(KO) 9=Italian(IT) 10=Portuguese(PT) 11=Spanish(ES)
               
  -p COMPORT   Arduino COM port - e.g. /dev/ttyACMO or COM3


If you select Snap! as the client with the "-c snap" option,  the web page will open automatically, but you need to manually import the blocks.

The snap block files can be found at:

For Linux - /usr/local/lib/python3.5/dist-packages/s2aio/Snap!Files

For Windows - C:\Users\YOUR USER NAME\AppData\Local\Programs\Python\Python35\Lib\site-packages\s2aio\Snap!Files