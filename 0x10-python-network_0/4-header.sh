#!/bin/bash
# This script sends a GET request to the URL passed as the first argument with a custom header and displays the body of the response
curl -sH "X-School-User-Id: 98" "$1"
