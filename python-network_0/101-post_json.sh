#!/bin/bash
# display methods
curl -s -X POST $1 -d @"$2" "Content-Type: application/json"
