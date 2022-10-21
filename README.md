# GPU Checker


# Run
```
python main.py
```


## Server
Edit *server_example.json*.
```
{
  "server1":
  {
    "host": "123.456.789.012",
    "user": "user_name1",
    "password": "1234567890",
    "port": 22
  },
  "server2":
  {
    "host": "345.678.901.234",
    "user": "user_name2",
    "password": "9876543210",
    "port": 23
  }
}
```
# GPU Checker


# Run
```
python main.py
```


## Server
Edit *server_example.json*.
```
{
  "server1":
  {
    "host": "123.456.789.012",
    "user": "user_name1",
    "password": "1234567890",
    "port": 22
  },
  "server2":
  {
    "host": "345.678.901.234",
    "user": "user_name2",
    "password": "9876543210",
    "port": 23
  }
}
```

## Result
```
server1
nvidia-smi
Fri Oct 21 10:42:36 2022       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 465.19.01    Driver Version: 465.19.01    CUDA Version: 11.3     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  NVIDIA RTX A5000    On   | 00000000:3B:00.0 Off |                  Off |
| 57%   81C    P2   214W / 230W |  16854MiB / 24256MiB |     94%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
|   1  NVIDIA GeForce ...  On   | 00000000:5E:00.0 Off |                  N/A |
| 53%   85C    P2   209W / 250W |   5853MiB / 11019MiB |     99%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
|   2  NVIDIA RTX A5000    On   | 00000000:B1:00.0 Off |                  Off |
| 51%   76C    P2   220W / 230W |  22652MiB / 24256MiB |    100%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
|   3  NVIDIA RTX A5000    On   | 00000000:D9:00.0 Off |                  Off |
| 47%   73C    P2   224W / 230W |  22798MiB / 24256MiB |    100%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

server2
nvidia-smi
Fri Oct 21 10:42:39 2022       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 495.46       Driver Version: 495.46       CUDA Version: 11.5     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  NVIDIA GeForce ...  Off  | 00000000:1A:00.0 Off |                  N/A |
| 94%   83C    P2   344W / 350W |   4183MiB / 24268MiB |     97%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
|   1  NVIDIA GeForce ...  Off  | 00000000:68:00.0 Off |                  N/A |
|100%   80C    P2   345W / 350W |  19383MiB / 24260MiB |    100%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
```