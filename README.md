# Social experiment using Muse™ Brain Computer Interface
### UOIT (ON, Canada) & UTN (SFE, Argentina)

**This version works only in Linux. Windows release available soon**

This is an application to run experiments on subjects using the Muse BCI Headband and collect all the EEG data in a CSV file.

## Prerequisites

1. Make sure that you have **VLC Media Player** installed on your computer. You can download it from [the official VLC website](https://www.videolan.org/vlc/index.html).
2. You have to have installed the **Muse Developers' Tools** installed on your computer. You can get them at the [Muse website](http://developer.choosemuse.com/research-tools/getting-started)
3. You must have your **Muse device paired via bluetooth** with your computer.


## Run

1. Before running the experiment, you have to start sending the OSC data to your machine. In order to do that, open a terminal and execute the following: `muse-io --device <Muse MAC Address> --osc-timestamp --osc  osc.udp://localhost:5000`. Be sure to place your Muse Mac Address where it says so, for example, *00:06:66:78:45:25*
2. Uncompress the `.tar.gz` file whereever you want.
3. Inside `dist` you will find an executable, double click it to start the experiment. 
4. After running the experiment, you will find all data collected in a file placed at `experiments/`
