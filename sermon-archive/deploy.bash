#!/bin/bash

set -ex

rsync --verbose --copy-links stalfreds-sermons.html sermons.json illuminu@burt.id.au:dave.burt.id.au/
