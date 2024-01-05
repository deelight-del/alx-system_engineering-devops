#!/bin/bash
# curl to send a request and receive the content-length
curl -s -w "%{size_download}\n" -o /dev/null ${1}
