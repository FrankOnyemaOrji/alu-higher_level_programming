#!/bin/bash
#curl size
curl -sI $1 | grep Content-Length | tail -c 4