### Test out Celery (with Flask)

To run, install RabbitMQ and start in background. `run.sh` checks for
port 5672.

The script will install the current package so all you should need to do is:

```sh
mkdir robnagler
cd robnagler
git clone https://github.com/robnagler/rncelery
cd rncelery
bash run.sh
```

There are two logs saved from runs with Python 2.7.10 in a Pyenv on Fedora 21:

* [celery-3.1.23.log](https://github.com/robnagler/rncelery/blob/master/celery-3.1.23.log)* [celery-4rc3.log](https://github.com/robnagler/rncelery/blob/master/celery-4rc3.log)

#### License

License: http://www.apache.org/licenses/LICENSE-2.0.html

Copyright (c) 2016 RadiaSoft LLC.  All Rights Reserved.
