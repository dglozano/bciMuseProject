# Social experiment using Muse™ Brain Computer Interface
### UOIT (ON, Canada) & UTN (SFE, Argentina)

Before running the experiment, run the following command to start receiving the headband's data using the OSC protocol

```
muse-io --device 00:06:66:78:45:25 --osc-timestamp --osc  osc.udp://localhost:5000
```

There will be a server running on a thread listening to that port while doing the experiment.

All the data recored will be saved in a CSV file located in `/experiments`